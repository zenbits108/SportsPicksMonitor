"""
Prevents Telegram flood-wait bans.
"""
import asyncio, time
LAST = 0
INTERVAL = 1.2  # seconds

async def rate_limit():
    global LAST
    delta = time.time() - LAST
    if delta < INTERVAL:
        await asyncio.sleep(INTERVAL - delta)
    LAST = time.time()
