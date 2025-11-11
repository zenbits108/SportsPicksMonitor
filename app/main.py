"""
Entry point for the Sports Picks Monitor.

Why:
- Keeps the orchestration layer minimal.
- Allows future CLI args or FastAPI entry without touching core logic.
"""
import asyncio
from core.telegram_monitor import TelegramMonitor

async def main():
    monitor = TelegramMonitor()
    await monitor.initialize()
    await monitor.run_forever()

if __name__ == "__main__":
    asyncio.run(main())
