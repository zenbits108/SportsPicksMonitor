"""
Pipeline coordinator for new Telegram messages.

Why:
- Central place to call OCR → parser → DB insert.
"""
import os, logging, datetime
from core.ocr_engine import extract_text
from core.pick_parser import parse_picks
from core.database import store_picks

async def process_message(message):
    log = logging.getLogger("message_processor")
    if not getattr(message, "media", None):
        return
    try:
        image_path = await message.download_media(file="/tmp/")
        text = await extract_text(image_path)
        picks = parse_picks(text)
        if picks:
            store_picks(picks, source_id=message.id, raw_text=text)
            log.info(f"{len(picks)} picks saved from msg {message.id}")
        os.remove(image_path)
    except Exception as e:
        log.error(f"Failed to process message {message.id}: {e}")
