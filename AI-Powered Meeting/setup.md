# AI-Powered Meeting Insights Setup

## Prerequisites
1. PostgreSQL installed and running
2. Google Gemini API key
3. Python 3.8+

## Setup Steps

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Database Setup:**
   ```sql
   CREATE DATABASE your_database;
   CREATE USER your_username WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE your_database TO your_username;
   ```

3. **Configure Database Connection:**
   - Edit `database.py` line 7
   - Replace the DATABASE_URL with your actual PostgreSQL credentials:
     ```python
     DATABASE_URL = "postgresql://your_username:your_password@localhost:5432/your_database"
     ```

4. **Configure Gemini API:**
   - Edit `llm.py` line 4
   - Replace `"your-gemini-api-key"` with your actual API key
   - Get API key from: https://makersuite.google.com/app/apikey

5. **Run the application:**
   ```bash
   uvicorn main:app --reload --app-dir "projects_2/AI-Powered Meeting"
   ```

6. **Open UI:**
   - Open `UI.html` in your browser
   - Or visit `http://localhost:8000/docs` for API documentation

## Usage

1. **Upload Transcript:** Use the web interface to upload a .txt file
2. **Search:** Search meetings by keyword or participant
3. **View Insights:** Get extracted insights by meeting ID
4. **Analytics:** Run `python analytics.py` to generate visualizations

## API Endpoints

- `POST /upload/` - Upload and process transcript
- `GET /search/keyword?keyword=budget` - Search by keyword
- `GET /search/participant?participant=Alice` - Search by participant
- `GET /insights/{meeting_id}` - Get insights for specific meeting