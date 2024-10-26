import asyncio
import sys
from telethon import TelegramClient
from telethon.sessions import StringSession

from config import APP_ID, API_HASH, STRING_SESSION, ALLOWED_USER_ID, OWNER_ID  # Ensure OWNER_ID is defined in config
from DYOH.plugins.alive import register_alive_handler
from DYOH.plugins.invite import register_channel_commands
from DYOH.plugins.spam import register_handlers
from DYOH.plugins.raid import register_raid_handlers
from DYOH.plugins.commands import CommandHandlers

IPIC = "https://telegra.ph/file/6bb3994d5789d8e7f2c99.mp4"


text = "**̾̍ͨ͐ͤ̚͏͏̷̝̪̫̪͈͍̱̣Ū̷͉̭̬̩̦̫̟͓̝̣͙̞͓̀̒̌ͮ͐͂̈́ͯ̌͡S̛͇͉͈̖̦͕̬͔̹ͥ͊̉̄̾͌̓͜͡E̤͙̰̖̘̣͕̰ͫͪ͢R̈́̐̽͡͏̸̠̫͖͓̯͓̉̇̃̍B̸̸̠̬̲͉̱̠̖͙͇͙͉̯̞̦̌̅ͥ̉͒̌͌̒͟͠Oͫ̌͟T̉ͣ̾́̋ͩ͏̧̫̦̥͙ ̝̣͔̝͎̎̃̈́̾̈̇̓̑́͞I̷͕̣̦̫̟͓̝̣͙̞͓͛̏ͨͦ̃͂̈́ͯ̌͡S̛͇͉͈ͥ͊̉̄̾͜͡ A̟̤̖̗͈̦͔̮̥̘͐̒̇ͩ͋̃̾̇ͭ̕͠L̏ͦ̀ͯͨ͋͟͏̣̪̝̣͔̝͎̎̃̈́̾̈̇̓̑́͘͞I̡͕̣̭̳̹͚͛̏ͨͦ̃̅͂̔̓̔̍V͇̘̥͖͙̖̦͕̬͔̹̈ͩ̉͌̓E̤͙̰̖̘̣͕̰ͫͪ͢ **\n\n"
pm_caption = f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0`\n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/Broken_Heart_72)\n"
pm_caption += f"┣Support ~ [Support](https://t.me/HEPPYLIFI)\n"
pm_caption += f"┣Owner ~ [OFFICIAL HACKER](https://t.me/OFFICIALHACKERERA)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"Dyoh userbot started successfully!\n"



text += pm_caption

async def loading_animation():
    for i in range(1, 101):
        print(f"\rLoading... {i}%", end="")
        await asyncio.sleep(0.1)
    print("\rLoading complete!              ")

async def send_startup_message(ubot):
    try:
        # Send a message to the user's saved messages with the image file
        me = await ubot.get_me()
        await ubot.send_file(me, file=IPIC, caption=text)

        # Send a message to the OWNER_ID
        entity = await ubot.get_input_entity(OWNER_ID)
        await ubot.send_message(entity, "DYOH USERBOT STARTED SUCCESSFULLY!")
    except Exception as e:
        print(f"Error sending message: {e}")

async def main():
    await loading_animation()  # Show loading animation

    ubots = [
        TelegramClient(StringSession(session), api_id=APP_ID, api_hash=API_HASH, auto_reconnect=True)
        for session in STRING_SESSION 
    ]

    for ubot in ubots:
        await ubot.start()
        await register_alive_handler(ubot, ALLOWED_USER_ID)
        await register_channel_commands(ubot)
        await register_handlers(ubot)
        await register_raid_handlers(ubot, ALLOWED_USER_ID)

        command_handlers = CommandHandlers(ubot, ALLOWED_USER_ID)
        await command_handlers.register_handlers()

        # Send the startup messages after starting the client
        await send_startup_message(ubot)

    print("DYOH USERBOT STARTED SUCCESSFULLY!")  # Success message
    await asyncio.gather(*[ubot.run_until_disconnected() for ubot in ubots])

if __name__ == "__main__":
    asyncio.run(main())
    
    
    
    
    
                                                   
                                                   
                                                   