from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from database import create_tables, get_db, Invoice, SessionLocal
from analytics import generate_analytics, generate_summary
import pandas as pd
import io
from datetime import datetime
from sqlalchemy.orm import Session

app = FastAPI(title="Smart Invoice Analytics", description="Invoice & Expense Analytics for SMBs")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup_event():
    try:
        create_tables()
        print("Tables created successfully!")
    except Exception as e:
        print(f"Database connection failed: {e}")

@app.post("/upload/")
async def upload_invoices(file: UploadFile = File(...)):
    if not file.filename.endswith(('.csv', '.xlsx')):
        raise HTTPException(status_code=400, detail="Only CSV and Excel files allowed")
    
    db = None
    try:
        contents = await file.read()
        if file.filename.endswith('.csv'):
            df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        else:
            df = pd.read_excel(io.BytesIO(contents))
        
        # Debug: show columns
        print(f"CSV columns: {list(df.columns)}")
        print(f"First row: {df.iloc[0].to_dict() if not df.empty else 'Empty'}")
        
        # Validate required columns
        required_columns = ['date', 'vendor', 'amount', 'status']
        if not all(col in df.columns for col in required_columns):
            raise HTTPException(status_code=400, detail=f"CSV must have columns: {required_columns}. Found: {list(df.columns)}")
        
        # Get database session
        db = SessionLocal()
        saved_count = 0
        errors = []
        
        for index, row in df.iterrows():
            try:
                invoice = Invoice(
                    date=pd.to_datetime(row['date']),
                    vendor=str(row['vendor']),
                    amount=float(row['amount']),
                    status=str(row['status']).lower()
                )
                db.add(invoice)
                saved_count += 1
            except Exception as row_error:
                errors.append(f"Row {index + 1}: {str(row_error)}")
                print(f"Row error: {row_error}")
        
        db.commit()
        
        message = f"Successfully uploaded {saved_count} invoices"
        if errors:
            message += f". {len(errors)} rows had errors: {errors[:3]}"
        
        return {"message": message}
    
    except Exception as e:
        print(f"Upload error: {str(e)}")
        if db:
            db.rollback()
        raise HTTPException(status_code=400, detail=f"Error processing file: {str(e)}")
    finally:
        if db:
            db.close()

@app.get("/analytics")
async def get_analytics():
    try:
        analytics = generate_analytics()
        return analytics
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating analytics: {str(e)}")

@app.get("/summary")
async def get_summary():
    try:
        summary = generate_summary()
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating summary: {str(e)}")

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    with open("templates/dashboard.html", "r") as f:
        return f.read()

@app.get("/reports", response_class=HTMLResponse)
async def reports():
    with open("templates/reports.html", "r") as f:
        return f.read()

@app.get("/vendors", response_class=HTMLResponse)
async def vendors():
    with open("templates/vendors.html", "r") as f:
        return f.read()

@app.get("/settings", response_class=HTMLResponse)
async def settings():
    with open("templates/settings.html", "r") as f:
        return f.read()

@app.post("/add-invoice/")
async def add_invoice(
    date: str = Form(...),
    vendor: str = Form(...),
    amount: float = Form(...),
    status: str = Form(...)
):
    db = None
    try:
        db = SessionLocal()
        invoice = Invoice(
            date=datetime.strptime(date, "%Y-%m-%d"),
            vendor=vendor,
            amount=amount,
            status=status.lower()
        )
        db.add(invoice)
        db.commit()
        return {"message": "Invoice added successfully"}
    except Exception as e:
        if db:
            db.rollback()
        print(f"Add invoice error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error adding invoice: {str(e)}")
    finally:
        if db:
            db.close()

@app.get("/invoices")
async def get_invoices():
    db = None
    try:
        db = SessionLocal()
        invoices = db.query(Invoice).order_by(Invoice.date.desc()).limit(50).all()
        return [{"id": inv.id, "date": inv.date.strftime("%Y-%m-%d"), "vendor": inv.vendor, "amount": inv.amount, "status": inv.status} for inv in invoices]
    except Exception as e:
        print(f"Get invoices error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching invoices: {str(e)}")
    finally:
        if db:
            db.close()

@app.get("/test")
async def test_endpoint():
    return {"message": "API is working", "status": "ok"}

@app.delete("/invoices/{invoice_id}")
async def delete_invoice(invoice_id: int):
    db = None
    try:
        db = SessionLocal()
        invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
        if not invoice:
            raise HTTPException(status_code=404, detail="Invoice not found")
        db.delete(invoice)
        db.commit()
        return {"message": "Invoice deleted successfully"}
    except Exception as e:
        if db:
            db.rollback()
        raise HTTPException(status_code=400, detail=f"Error deleting invoice: {str(e)}")
    finally:
        if db:
            db.close()

@app.get("/stats")
async def get_stats():
    db = None
    try:
        db = SessionLocal()
        total_invoices = db.query(Invoice).count()
        total_amount = db.query(Invoice).with_entities(Invoice.amount).all()
        total_sum = sum([amount[0] for amount in total_amount]) if total_amount else 0
        
        paid_count = db.query(Invoice).filter(Invoice.status == 'paid').count()
        pending_count = db.query(Invoice).filter(Invoice.status == 'pending').count()
        overdue_count = db.query(Invoice).filter(Invoice.status == 'overdue').count()
        
        return {
            "total_invoices": total_invoices,
            "total_amount": total_sum,
            "paid_count": paid_count,
            "pending_count": pending_count,
            "overdue_count": overdue_count,
            "avg_amount": total_sum / total_invoices if total_invoices > 0 else 0
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching stats: {str(e)}")
    finally:
        if db:
            db.close()

