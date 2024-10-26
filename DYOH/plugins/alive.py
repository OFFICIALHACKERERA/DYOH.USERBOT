import random
import time
from datetime import timedelta
from telethon import events, Button
from platform import python_version
from telethon import version

mention = "@raoxc"
ubotversion = "1.0"
StartTime = time.time()
IPIC = "https://telegra.ph/file/6bb3994d5789d8e7f2c99.mp4"

def get_readable_time(seconds):
    return str(timedelta(seconds=seconds))

async def register_alive_handler(client, allowed_user_id):
    @client.on(events.NewMessage(pattern=".alive$"))
    async def alive_handler(event):
        if event.sender_id != allowed_user_id:
            return

        uptime = get_readable_time(time.time() - StartTime)
        emoji = random.choice(["✥", "✔️", "⭐", "✨", "☣️", "🔰", "🏴", "‍☠️", "🚀"])  
        my = random.choice(["🏴‍☠️"])  

        ubot_caption = (
            f"**───────────────────**\n"
            f"**𝐃𝐘𝐎𝐇  𝐔𝐁𝐎𝐓  𝐈𝐒  𝐎𝐍𝐋𝐈𝐍𝐄 {my}**\n"
            f"**───────────────────**\n"
            f"**╭───────────────**\n"
            f"**┣{emoji} Telethon version :** `{version.__version__}`\n"
            f"**┣{emoji} Userbot Version :** `{ubotversion}`\n"
            f"**┣{emoji} Python Version :** `{python_version()}`\n"
            f"**┣{emoji} Uptime :** {uptime}\n"
            f"**┣{emoji} Master:** {mention}\n"
            f"**┣{emoji} 𝐃𝐘𝐎𝐇 ᆖ [𝐎𝐖𝐍𝐄𝐑](https://t.me/raoxc)**\n"
            f"╰─────────────────\n"
        )

        buttons = [[Button.url("Repo", "https://github.com")]]

        await event.client.send_file(
            event.chat_id,
            IPIC,
            caption=ubot_caption,
            buttons=buttons
        )

        # Delete the command message
        await event.delete()