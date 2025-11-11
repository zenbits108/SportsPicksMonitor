from pydantic import BaseModel
from datetime import datetime

class Pick(BaseModel):
    id: str
    sport: str
    teams: str
    pick: str
    confidence: float
    source_message_id: int
    extracted_text: str
    timestamp: datetime
    processed: bool = False
