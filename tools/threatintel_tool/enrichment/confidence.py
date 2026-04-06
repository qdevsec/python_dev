from datetime import datetime

def calculate_confidence(num_scores, last_seen):
    score = 0

    # Source weight
    score += min(num_scores * 20, 60)

    # Recency boost
    age_hours = (datetime.now((datetime.timezone.utc)) - last_seen).total_seconds() / 3600
    if age_hours < 24:
        score += 30
    elif age_hours < 72:
        score += 20
    else:
        score += 10
    
    return min(score, 100)