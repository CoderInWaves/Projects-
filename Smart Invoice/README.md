# 📊 Smart Invoice Analytics

A modern, full-stack SaaS dashboard for Small and Mid-sized Businesses (SMBs) to analyze invoices and expenses with instant insights and AI-powered summaries.

![Smart Invoice Analytics](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

## ✨ Features

### 📈 **Analytics Dashboard**
- Real-time invoice statistics and KPIs
- Interactive charts and visualizations
- Monthly expense trends analysis
- Top vendor spending breakdown

### 🤖 **AI-Powered Insights**
- Natural language financial summaries
- Automated expense pattern detection
- Business health recommendations
- Overdue payment alerts

### 📁 **Data Management**
- CSV/Excel file upload support
- Manual invoice entry with validation
- Bulk data processing
- Search and filter functionality

### 🏢 **Multi-Page Navigation**
- **Dashboard**: Main analytics and data entry
- **Reports**: Comprehensive financial reports
- **Vendors**: Vendor management and analysis
- **Settings**: Configuration and preferences

### 🎨 **Modern UI/UX**
- Responsive design for all devices
- Beautiful gradient themes
- Smooth animations and transitions
- Toast notifications and loading states

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/smart-invoice-analytics.git
cd smart-invoice-analytics
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your database credentials
```

5. **Setup database**
```bash
# Create PostgreSQL database
createdb your_database_name

# The application will automatically create tables on startup
```

6. **Run the application**
```bash
uvicorn main:app --reload
```

7. **Access the dashboard**
Open your browser and navigate to `http://localhost:8000`

## 📋 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
DB_USER=your_db_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
```

### CSV Format

Your invoice CSV files should have these columns:
- `date` - Invoice date (YYYY-MM-DD)
- `vendor` - Vendor/company name
- `amount` - Invoice amount (numeric)
- `status` - Payment status (paid/pending/overdue)

Example:
```csv
date,vendor,amount,status
2024-01-15,Office Supplies Co,1250.00,paid
2024-01-20,Tech Solutions Inc,3500.00,pending
```

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **UI Framework**: Bootstrap 5
- **Charts**: Chart.js
- **Icons**: Font Awesome
- **Data Processing**: Pandas
- **File Handling**: Python-multipart

## 📊 API Endpoints

### Core Endpoints
- `GET /` - Main dashboard
- `POST /upload/` - Upload CSV/Excel files
- `POST /add-invoice/` - Add single invoice
- `GET /invoices` - List all invoices
- `DELETE /invoices/{id}` - Delete invoice

### Analytics Endpoints
- `GET /analytics` - Get analytics data
- `GET /summary` - Get AI summary
- `GET /stats` - Get statistics

### Page Endpoints
- `GET /reports` - Reports page
- `GET /vendors` - Vendors page
- `GET /settings` - Settings page

## 🎯 Use Cases

### Small Businesses
- Track monthly expenses and vendor payments
- Identify spending patterns and cost optimization opportunities
- Monitor cash flow and payment schedules
- Generate reports for accounting and tax purposes

### Freelancers & Consultants
- Manage client invoices and payment tracking
- Analyze income trends and client profitability
- Export data for bookkeeping and tax filing
- Set up payment reminders and follow-ups

### Startups
- Monitor burn rate and expense categories
- Track vendor relationships and spending
- Generate investor reports and financial summaries
- Scale expense management as the business grows

## 🔧 Development

### Project Structure
```
smart-invoice-analytics/
├── main.py              # FastAPI application
├── database.py          # Database models and connection
├── analytics.py         # Analytics and AI logic
├── requirements.txt     # Python dependencies
├── .env.example        # Environment template
├── templates/          # HTML templates
│   ├── dashboard.html
│   ├── reports.html
│   ├── vendors.html
│   └── settings.html
├── static/            # Static assets (if any)
└── sample_invoices.csv # Sample data
```

### Adding New Features

1. **Backend**: Add new endpoints in `main.py`
2. **Database**: Modify models in `database.py`
3. **Analytics**: Extend logic in `analytics.py`
4. **Frontend**: Update HTML templates and JavaScript

### Testing

```bash
# Test database connection
python test_upload.py

# Test API endpoints
curl http://localhost:8000/test
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- Chart.js for beautiful visualizations
- Bootstrap for responsive UI components
- PostgreSQL for reliable data storage

## 📞 Support

If you have any questions or need help, please:
- Open an issue on GitHub
- Check the documentation
- Review the sample data format

---

**Made with ❤️ for small businesses everywhere**