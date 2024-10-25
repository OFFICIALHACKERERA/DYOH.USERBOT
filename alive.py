import asyncio
import random
import time
from datetime import timedelta
from platform import python_version
from telethon import TelegramClient, events, functions, Button, version
from telethon.sessions import StringSession
from telethon.errors import ChatAdminRequiredError, UserNotParticipantError
from config import APP_ID, API_HASH, LEGEND_STRINGS, BOT_USERNAME, ALLOWED_USER_ID  # Import from config

# Constants
IPIC = "https://telegra.ph/file/6bb3994d5789d8e7f2c99.mp4"
legendversion = "1.0"
StartTime = time.time()

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
        f"**┣{emoji} Python Version :** `{python_version()}`\n"
        f"**┣{emoji} Uptime :** {uptime}\n"
        f"**┣{emoji} Master:** @{BOT_USERNAME}\n"
        f"╰─────────────────\n"
    )

    buttons = [[Button.url("Repo", "https://github.com/ITS-LEGENDBOT/LEGENDBOT")]]

    await event.client.send_file(
        event.chat_id,
        IPIC,
        caption=legend_caption,
        buttons=buttons
    )

async def register_handlers(legend):
    @legend.on(events.NewMessage(pattern="alive$"))
    async def alive_handler(event):
        await handle_alive_command(event)

# Aap yahan se `main()` function ko implement kar sakte hain
