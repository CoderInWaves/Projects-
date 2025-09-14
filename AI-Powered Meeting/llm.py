import google.generativeai as genai
import json
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY", "your-api-key-here"))
model = genai.GenerativeModel('gemini-1.5-flash')

def extract_insights(transcript: str):
    prompt = f"""
    Analyze this meeting transcript and extract:
    1. Action items (format: "Person: Task")
    2. Risks/Issues identified
    3. Decisions made
    
    Return as JSON with keys: action_items, risks, decisions
    
    Transcript: {transcript}
    """
    
    try:
        response = model.generate_content(prompt)
        return json.loads(response.text)
    except Exception as e:
        print(f"API Error: {e}")
        # Fallback: improved text parsing
        lines = [line.strip() for line in transcript.split('\n') if line.strip()]
        
        action_keywords = ['will', 'need to', 'should', 'must', 'coordinate', 'provide', 'implement']
        risk_keywords = ['risk', 'issue', 'concern', 'problem', 'challenge', 'delay']
        decision_keywords = ['decided', 'decision', 'agreed', 'approved', 'confirmed']
        
        action_items = [line for line in lines if any(keyword in line.lower() for keyword in action_keywords)]
        risks = [line for line in lines if any(keyword in line.lower() for keyword in risk_keywords)]
        decisions = [line for line in lines if any(keyword in line.lower() for keyword in decision_keywords)]
        
        return {
            "action_items": action_items[:5],
            "risks": risks[:5], 
            "decisions": decisions[:5]
        }