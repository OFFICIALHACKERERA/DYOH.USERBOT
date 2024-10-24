
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from config import APP_ID, API_HASH, LEGEND_STRINGS
from commands import register_handlers  # Import from commands file

async def main():
    legends = [
        TelegramClient(StringSession(session), api_id=APP_ID, api_hash=API_HASH, auto_reconnect=True)
        for session in LEGEND_STRINGS
    ]
    await asyncio.gather(*[register_handlers(legend) for legend in legends])
    await asyncio.gather(*[legend.start() for legend in legends])
    await asyncio.gather(*[legend.run_until_disconnected() for legend in legends])

if __name__ == "__main__":
    asyncio.run(main())
