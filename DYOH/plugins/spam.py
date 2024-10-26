import asyncio
from telethon import events
from config import ALLOWED_USER_ID

async def is_user_allowed(event):
    return event.sender_id == ALLOWED_USER_ID

async def register_handlers(ubot):
    @ubot.on(events.NewMessage(pattern=r".spam (\d+) (.+)"))
    async def spammer_handler(event):
        if not await is_user_allowed(event):
            return await event.reply("You are not allowed to use this command.")

        try:
            count = int(event.pattern_match.group(1))
            text = event.pattern_match.group(2)
        except (ValueError, IndexError):
            return await event.reply("Usage: .spam <count> <text>")

        sleep_time = 1 if count > 50 else 0.5
        await event.delete()  # Delete the original command message
        
        for _ in range(count):
            await event.respond(text)
            await asyncio.sleep(sleep_time)