"""
Handles connection to Telegram using Telethon.

Why separate:
- Keeps network IO isolated from business logic.
- Allows us to replace Telethon later if Telegram adds an official API SDK.
"""
import asyncio, logging, os
from telethon import TelegramClient, events
from config import settings
from core.message_processor import process_message
from core.rate_limiter import rate_limit

class TelegramMonitor:
    def __init__(self):
        self.client = None
        self.logger = logging.getLogger("telegram_monitor")

    async def initialize(self):
        self.client = TelegramClient(
            session=os.getenv("TG_SESSION", "monitor_session"),
            api_id=settings.API_ID,
            api_hash=settings.API_HASH
        )
        await self.client.start()
        self.logger.info("Telegram client started")

    async def run_forever(self):
        @self.client.on(events.NewMessage(chats=settings.TARGET_CHANNEL))
        async def handler(event):
            await rate_limit()
            await process_message(event.message)
        self.logger.info("Listening for new messages…")
        await self.client.run_until_disconnected()
