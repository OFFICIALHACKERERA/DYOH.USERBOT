
import asyncio
import random
import time
from datetime import timedelta
from telethon import events, version
from config import BOT_USERNAME, ALLOWED_USER_ID  # Ensure these are defined

IPIC = "https://telegra.ph/file/6bb3994d5789d8e7f2c99.mp4"
RAID = ["hello ", "hii "]
StartTime = time.time()
legendversion = "1.0"

def get_readable_time(seconds):
    return str(timedelta(seconds=seconds))

async def is_user_allowed(event):
    return event.sender_id == ALLOWED_USER_ID

async def handle_alive_command(event):
    if not await is_user_allowed(event):
        return

    uptime = get_readable_time(time.time() - StartTime)
    emoji = random.choice(["✥", "✔️", "⭐", "✨", "☣️", "🔰", "🏴", "‍☠️", "🚀"])
    my = random.choice(["🇦🇱", "💠", "🔷", "🔹"])

    legend_caption = (
        f"**─────────────────**\n"
        f"**DYOH USERBOT IS ONLINE {my}**\n"
        f"**─────────────────**\n"
        f"**╭───────────────**\n"
        f"**┣{emoji} Telethon version :** `{version.__version__}`\n"
        f"**┣{emoji} Userbot Version :** `{legendversion}`\n"
        f"**┣{emoji} Uptime :** {uptime}\n"
        f"**┣{emoji} Master:** @{BOT_USERNAME}\n"
        f"╰─────────────────\n"
    )

    await event.client.send_file(event.chat_id, IPIC, caption=legend_caption)

async def register_handlers(legend):
    @legend.on(events.NewMessage(pattern="alive$"))
    async def alive_handler(event):
        await handle_alive_command(event)

    
