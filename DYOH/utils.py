import sys
import logging
import importlib
from telethon import events
from pathlib import Path

# List of sudo users (replace with actual user IDs)
SUDO_USERS = []

def load_plugins(plugin_name):
    # Check if the plugin is in the 'plugins' or 'assistant' directory
    plugin_path = Path(f"DYOH/plugins/{plugin_name}.py")
    assistant_path = Path(f"DYOH/assistant/{plugin_name}.py")

    if plugin_path.exists():
        path = plugin_path
        name = "DYOH.plugins.{}".format(plugin_name)
    elif assistant_path.exists():
        path = assistant_path
        name = "DYOH.assistant.{}".format(plugin_name)
    else:
        print(f"[ERROR] Plugin {plugin_name} not found in either directory.")
        return

    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules[name] = load
    print("[INFO] [DYOH UBOT] Successfully Imported 🔰" + plugin_name)

async def edit_or_reply(event, text):
    if event.sender_id in SUDO_USERS:
        reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(text)
        return await event.reply(text)
    return await event.edit(text)