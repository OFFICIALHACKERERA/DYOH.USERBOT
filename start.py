
import asyncio
from telethon import TelegramClient
from config import APP_ID, LEGEND_STRINGS  # Ensure you import any required config

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
