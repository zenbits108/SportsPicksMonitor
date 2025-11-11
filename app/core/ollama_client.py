import aiohttp
import base64

OLLAMA_URL = "http://192.168.0.111:11434/api/generate"

async def llava_extract_text(image_path: str) -> str:
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")

    payload = {
        "model": "llava:13b",
        "prompt": "Extract all visible betting picks, odds, and teams from this image clearly.",
        "images": [img_b64]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(OLLAMA_URL, json=payload, timeout=120) as resp:
            data = await resp.json()
            return data.get("response", "").strip()
