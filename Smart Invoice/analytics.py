import pandas as pd
from sqlalchemy import text
from database import engine, SessionLocal
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime, timedelta
import openai
import os

def generate_analytics():
    """Generate key analytics from invoice data"""
    db = SessionLocal()
    
    try:
        # Get all invoices
        query = text("SELECT * FROM invoices")
        df = pd.read_sql(query, engine)
        
        if df.empty:
            return {
                "message": "No invoice data available",
                "top_vendors": {},
                "status_breakdown": {},
                "monthly_trends": {},
                "total_invoices": 0,
                "total_amount": 0
            }
        
        # Top vendors by spend
        top_vendors = df.groupby('vendor')['amount'].sum().sort_values(ascending=False).head(5)
        
        # Overdue vs paid invoices
        status_counts = df['status'].value_counts()
        
        # Monthly expense trends
        df['date'] = pd.to_datetime(df['date'])
        monthly_trends = df.groupby(df['date'].dt.to_period('M'))['amount'].sum()
        
        # Generate trend chart
        plt.figure(figsize=(10, 6))
        monthly_trends.plot(kind='line', marker='o')
        plt.title('Monthly Expense Trends')
        plt.xlabel('Month')
        plt.ylabel('Amount ($)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save plot to base64
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        chart_base64 = base64.b64encode(img_buffer.getvalue()).decode()
        plt.close()
        
        return {
            "top_vendors": top_vendors.to_dict(),
            "status_breakdown": status_counts.to_dict(),
            "monthly_trends": monthly_trends.to_dict(),
            "trend_chart": f"data:image/png;base64,{chart_base64}",
            "total_invoices": len(df),
            "total_amount": df['amount'].sum()
        }
    
    finally:
        db.close()

def generate_summary():
    """Generate LLM-powered financial summary"""
    db = SessionLocal()
    
    try:
        query = text("SELECT * FROM invoices ORDER BY date DESC LIMIT 100")
        df = pd.read_sql(query, engine)
        
        if df.empty:
            return "No invoice data available for analysis"
        
        # Calculate key metrics
        total_amount = df['amount'].sum()
        avg_amount = df['amount'].mean()
        top_vendor = df.groupby('vendor')['amount'].sum().idxmax()
        overdue_count = len(df[df['status'] == 'overdue'])
        
        # Create summary prompt
        prompt = f"""
        Analyze this financial data and provide insights:
        - Total invoices: {len(df)}
        - Total amount: ${total_amount:,.2f}
        - Average invoice: ${avg_amount:,.2f}
        - Top vendor: {top_vendor}
        - Overdue invoices: {overdue_count}
        
        Provide a brief business summary with actionable insights.
        """
        
        # Simple rule-based summary (replace with OpenAI API if available)
        if overdue_count > len(df) * 0.2:
            summary = f"⚠️ High overdue rate: {overdue_count}/{len(df)} invoices are overdue. Consider improving payment processes."
        elif total_amount > 50000:
            summary = f"💰 Strong spending activity: ${total_amount:,.2f} total. Top vendor {top_vendor} represents significant expense."
        else:
            summary = f"📊 Moderate activity: {len(df)} invoices totaling ${total_amount:,.2f}. {top_vendor} is your largest vendor."
        
        return summary
    
    finally:
        db.close()