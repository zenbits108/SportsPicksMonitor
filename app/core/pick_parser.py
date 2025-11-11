"""
Simple regex-based parser.  Replace with NLP later.

Why:
- Keeps parsing logic modular; easy to unit-test.
"""
import re
from datetime import datetime
from models.pick import Pick

def parse_picks(text: str):
    picks = []
    for line in text.splitlines():
        if not line.strip(): continue
        m = re.search(r'([A-Za-z ]+)\s([-+]\d+\.?\d*)', line)
        if m:
            picks.append(Pick(
                id=f"{m[1]}_{datetime.utcnow().timestamp()}",
                sport="unknown",
                teams=m[1].strip(),
                pick=m[2],
                confidence=0.0,
                source_message_id=0,
                extracted_text=line,
                timestamp=datetime.utcnow()
            ))
    return picks
