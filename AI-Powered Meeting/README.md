# 🤖 AI-Powered Meeting Insights

Transform your meeting transcripts into actionable insights using AI-powered analysis.

## ✨ Features

- **📄 Transcript Upload**: Upload meeting transcripts and get instant AI analysis
- **🎯 Smart Extraction**: Automatically extract action items, risks, and decisions
- **🔍 Powerful Search**: Search meetings by keywords or participants
- **💾 Database Storage**: Store and retrieve meeting insights
- **📊 Analytics**: Generate visualizations from meeting data
- **🎨 Modern UI**: Beautiful, responsive web interface

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL (or use SQLite fallback)
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd AI-Powered-Meeting
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload --app-dir "projects_2/AI-Powered Meeting"
   ```

5. **Open the web interface**
   - Open `UI.html` in your browser
   - Or visit `http://localhost:8000/docs` for API documentation

## 🔧 Configuration

### Environment Variables (.env)
```env
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
GEMINI_API_KEY=your_gemini_api_key_here
```

### Database Setup (PostgreSQL)
```sql
CREATE DATABASE your_database;
CREATE USER your_username WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE your_database TO your_username;
```

## 📖 Usage

### 1. Upload Meeting Transcript
- Click "Choose file" and select a .txt transcript
- Click "Analyze Meeting" to process with AI
- View extracted insights instantly

### 2. Search Meetings
- **By Keyword**: Search for specific topics (e.g., "budget", "timeline")
- **By Participant**: Find meetings with specific attendees

### 3. View Insights
- Enter a Meeting ID to view detailed insights
- See categorized action items, risks, and decisions

### 4. Generate Analytics
```bash
python analytics.py
```

## 🏗️ Architecture

```
├── main.py              # FastAPI application
├── database.py          # SQLAlchemy models
├── llm.py              # AI integration (Gemini)
├── analytics.py        # Data visualization
├── UI.html             # Web interface
├── requirements.txt    # Dependencies
└── sample_transcript.txt # Test data
```

## 🔌 API Endpoints

- `POST /upload/` - Upload and analyze transcript
- `GET /search/keyword?keyword=<term>` - Search by keyword
- `GET /search/participant?participant=<name>` - Search by participant
- `GET /insights/{meeting_id}` - Get meeting insights

## 🎨 UI Features

- **Modern Design**: Gradient backgrounds, smooth animations
- **Responsive**: Works on desktop and mobile
- **Interactive**: Real-time feedback and loading states
- **Accessible**: Clean typography and intuitive navigation

## 🛡️ Security

- Environment variables for sensitive data
- Input validation and sanitization
- CORS protection
- SQL injection prevention

## 🔄 Fallback System

When AI API quota is exceeded, the system automatically falls back to:
- Keyword-based text parsing
- Pattern matching for insights
- Graceful error handling

## 📊 Sample Output

```json
{
  "meeting_id": 1,
  "insights": {
    "action_items": [
      "Bob: coordinate with QA team for testing by March 15th",
      "Carol: provide marketing copy for in-app notifications by March 10th"
    ],
    "risks": [
      "payment integration - third-party API might not be stable",
      "database scalability could be an issue if we get more than 10K users"
    ],
    "decisions": [
      "allocate $50K for digital marketing",
      "implement auto-scaling from day one",
      "March 30th launch date non-negotiable"
    ]
  }
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For issues and questions:
- Check the documentation
- Review API endpoints at `/docs`
- Ensure environment variables are set correctly
- Verify database connection

---

**Built with ❤️ using FastAPI, SQLAlchemy, and Google Gemini AI**