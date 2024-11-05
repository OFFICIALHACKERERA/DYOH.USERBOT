import logging
import asyncio
import glob
from pathlib import Path
from telethon import Button
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from DYOH.utils import load_plugins
from DYOH import ubots, dybot, GROUP_ID  # Ensure these are valid Telebot instances
from config import UPIC, ubotversion , UPDATES_CHANNEL , OWNER_USERNAME 
from telethon import __version__ 
from platform import python_version

OWNER_ID = "raoxc"

# Logging configuration
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

text = "**ᴜʙᴏᴛ ᴀꜱꜱɪꜱᴛᴀɴᴛ ɪꜱ ᴏɴʟɪɴᴇ**\n\n"
pm_caption = f"ᴜʙᴏᴛ ᴠᴇʀꜱɪᴏɴ `{ubotversion}`\n"
pm_caption += f"ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ `{python_version()}\n"
pm_caption += f"ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ `{__version__}\n"
pm_caption += f"ᴅʏᴏʜ ᴜʙᴏᴛ ꜱᴏᴜʀᴄᴇ [ᴄʟɪᴄᴋ](https://github.com/OFFICIALHACKERERA)\n\n"
pm_caption += f"ᴜʙᴏᴛ ꜱᴛᴀʀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!"
text += pm_caption





# Load all plugins
def load_all_plugins():
    paths = ["DYOH/plugins/*.py", "DYOH/assistant/*.py"]
    for path in paths:
        files = glob.glob(path)
        if not files:
            logging.warning(f"No plugins found in {path}.")
        for name in files:
            plugin_name = Path(name).stem
            try:
                load_plugins(plugin_name)
                logging.info(f"[DYOH UBOT] ✅ Loaded plugin: {plugin_name}")
            except Exception as e:
                logging.error(f"[DYOH UBOT] ❌ Failed to load plugin {plugin_name}: {e} 💥")

async def start_bot(bot_instance, name):
    logging.info(f"[DYOH UBOT] 🔰 Starting {name}... 💯")
    try:
        await bot_instance.start()
        logging.info(f"[DYOH UBOT] 🌐 {name} is running... ")
    except Exception as e:
        logging.error(f"⚠️ Failed to start {name}: {e}❌")




               

async def start_ubots():
    for ubot in ubots:
        try:
            await ubot.start()
            logging.info("✨ Userbot is running...")
            logging.info("🔰 Session started: %s ♦️", ubot.session)

            # Send the startup message to the owner
            message = "🌐 DYOH UBOT HAS STARTED SUCCESSFULLY!"
            await ubot.send_message(OWNER_ID, message)  # Sending message to the owner
            logging.info("[DYOH UBOT] ✅ Startup message sent successfully!")

            # Automatically join the channel and group
            try:
                await ubot(JoinChannelRequest(channel='DYOH_UBOT'))  # Replace with your channel's username
                logging.info("[DYOH UBOT] ✅ Joined the channel successfully!")
            except Exception as e:
                logging.error(f"[DYOH UBOT] ❌ Failed to join channel: {e}")

            try:
                await ubot(JoinChannelRequest(channel='DYOH_UBOT_CHAT'))  # Replace with your group's username
                logging.info("[DYOH UBOT] ✅ Joined the group successfully!")
            except Exception as e:
                logging.error(f"[DYOH UBOT] ❌ Failed to join group: {e}")

            await ubots.run_until_disconnected()  # Keep Ubot running

        except Exception as e:
            logging.error(f"Failed to start userbot {ubot}: {e}")
            
            print("🌐 [DYOH UBOT] STARTED SUCCESSFULLY! ✨")


async def start_dybot():
    logging.info("[DYOH UBOT] 🔳 Dybot is starting... 🚩")
    try:
        await dybot.start()
        logging.info(f"[DYOH UBOT] ✅ Fetching entity for group ID: {GROUP_ID}")
        group_entity = await dybot.get_entity(GROUP_ID)

        buttons = [
    [Button.url("Owner", f'https://t.me/{OWNER_USERNAME}'), Button.url("Channel", f'https://t.me/{UPDATES_CHANNEL}')]
]

        await dybot.send_file(GROUP_ID, file=UPIC, caption=text, buttons=buttons)
        logging.info("[DYOH UBOT] ✅ Message sent successfully!")
        await dybot.run_until_disconnected()
    except Exception as e:
        logging.error(f"[DYOH UBOT] ❌ Error while running dybot: {e}")
        

async def health_check():
    while True:
        logging.info("[DYOH UBOT] 🌐 Checking bot statuses...")
        await asyncio.sleep(60)

async def start_all_bots():
    logging.info("[DYOH UBOT] ✅ Starting all bots...")
    tasks = [start_ubots(), start_dybot(), health_check()]
    await asyncio.gather(*tasks)

def main():
    logging.info("[DYOH UBOT] ✅ Loading plugins...")
    load_all_plugins()
    logging.info("[DYOH UBOT] ✅ Plugins loaded.")

if __name__ == "__main__":
    main()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_all_bots())  # Run all bots
    except Exception as e:
        logging.error(f"[ DYOH UBOT ] [❌] Error in main event loop: {e}")