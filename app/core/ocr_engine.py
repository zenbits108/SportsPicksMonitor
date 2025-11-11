"""
OCR abstraction layer.

Why:
- Allows fallback (LLaVA → Tesseract).
- Keeps model logic independent from parser.
"""
import logging, pytesseract, aiohttp, base64, os
from PIL import Image
from config import settings

async def extract_text(image_path: str) -> str:
    log = logging.getLogger("ocr_engine")
    try:
        # Try LLaVA first
        with open(image_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode("utf-8")
        payload = {
            "model": "llava:13b",
            "prompt": "Extract clearly any sports picks, odds, or team names.",
            "images": [img_b64]
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{settings.OLLAMA_URL}/api/generate",
                                    json=payload, timeout=90) as r:
                js = await r.json()
                if "response" in js and js["response"].strip():
                    return js["response"].strip()
    except Exception as e:
        log.warning(f"LLaVA failed, fallback to Tesseract: {e}")

    # Fallback OCR
    try:
        return pytesseract.image_to_string(Image.open(image_path),
                                           lang=settings.TESSERACT_LANGUAGE)
    except Exception as e:
        log.error(f"Tesseract failed: {e}")
        return ""
