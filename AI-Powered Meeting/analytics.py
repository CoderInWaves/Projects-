import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sqlalchemy.orm import Session
from database import get_db, Meeting, Insight
import json
from collections import Counter

def generate_analytics():
    db = next(get_db())
    
    # Get all meetings and insights
    meetings = db.query(Meeting).all()
    insights = db.query(Insight).all()
    
    # Decisions per week
    meeting_dates = [m.date for m in meetings]
    decisions_count = []
    
    for insight in insights:
        decisions = json.loads(insight.decisions)
        decisions_count.append(len(decisions))
    
    # Create visualizations
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Chart 1: Decisions per meeting
    ax1.bar(range(len(decisions_count)), decisions_count)
    ax1.set_title('Decisions per Meeting')
    ax1.set_xlabel('Meeting ID')
    ax1.set_ylabel('Number of Decisions')
    
    # Chart 2: Action items distribution
    action_items_count = []
    for insight in insights:
        action_items = json.loads(insight.action_items)
        action_items_count.extend(action_items)
    
    # Count participants with most action items
    participants = [item.split(':')[0].strip() for item in action_items_count if ':' in item]
    participant_counts = Counter(participants).most_common(5)
    
    if participant_counts:
        names, counts = zip(*participant_counts)
        ax2.bar(names, counts)
        ax2.set_title('Top 5 Participants with Most Action Items')
        ax2.set_xlabel('Participant')
        ax2.set_ylabel('Number of Action Items')
        ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('meeting_analytics.png')
    plt.show()
    
    db.close()

if __name__ == "__main__":
    generate_analytics()