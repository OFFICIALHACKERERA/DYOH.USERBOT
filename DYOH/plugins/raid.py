import asyncio
import random
from telethon import events

RAID = ["hello ", "hii "]
active_raids = {}

async def register_raid_handlers(ubot, ALLOWED_USER_ID):

    @ubot.on(events.NewMessage(pattern=r".raid (\d+)(?: (\d+))?"))
    async def raid(event):
        if not await is_user_allowed(event, ALLOWED_USER_ID):
            return

        count = int(event.pattern_match.group(1))
        user_id = event.pattern_match.group(2)  # Capture optional user ID

        if not event.reply_to_msg_id and not user_id:
            await event.reply("Please reply to a user's message or provide a user ID to start the raid.")
            await event.delete()  # Delete the command message
            return

        if user_id:
            try:
                user_id = int(user_id)
                user = await event.client.get_entity(user_id)
            except Exception:
                await event.reply("Could not retrieve user. Make sure the user ID is valid.")
                await event.delete()  # Delete the command message
                return
        else:
            reply_msg = await event.get_reply_message()
            if not reply_msg:
                await event.reply("Could not retrieve the reply message.")
                await event.delete()  # Delete the command message
                return
            user = await event.client.get_entity(reply_msg.sender_id)

        username = f"[{user.first_name}](tg://user?id={user.id})"

        # Countdown before starting the raid
        countdown_message = await event.reply("Starting the raid in 10 seconds...")

        for i in range(10, 0, -1):
            await asyncio.sleep(1)  # Wait for 1 second
            await countdown_message.edit(f"{i} seconds remaining...")  # Update the same message

        await countdown_message.edit("Starting the raid now...")

        for _ in range(count):
            await event.client.send_message(event.chat_id, f"{username} {random.choice(RAID)}")
            await asyncio.sleep(0.1)

        await event.delete()  # Delete the command message

    @ubot.on(events.NewMessage(pattern=r".replyraid$"))
    async def add_reply_raid(event):
        if not await is_user_allowed(event, ALLOWED_USER_ID):
            return

        if event.reply_to_msg_id is None:
            await event.reply("Reply to a user's message to activate raid on them.")
            await event.delete()  # Delete the command message
            return

        reply_msg = await event.get_reply_message()
        if not reply_msg:
            await event.reply("Could not retrieve the reply message.")
            await event.delete()  # Delete the command message
            return

        user = await event.client.get_entity(reply_msg.sender_id)

        if event.chat_id not in active_raids:
            active_raids[event.chat_id] = []

        if user.id in active_raids[event.chat_id]:
            await event.reply("The user is already enabled with Raid.")
            await event.delete()  # Delete the command message
            return

        active_raids[event.chat_id].append(user.id)
        await event.reply(f"Raid has been started for {user.first_name}.")
        await event.delete()  # Delete the command message

    @ubot.on(events.NewMessage(pattern=r".dreplyraid$"))
    async def remove_reply_raid(event):
        if not await is_user_allowed(event, ALLOWED_USER_ID):
            return

        if event.reply_to_msg_id is None:
            await event.reply("Reply to a user's message to stop the raid on them.")
            await event.delete()  # Delete the command message
            return

        reply_msg = await event.get_reply_message()
        if not reply_msg:
            await event.reply("Could not retrieve the reply message.")
            await event.delete()  # Delete the command message
            return

        user_id = reply_msg.sender_id
        chat_id = event.chat_id

        if chat_id in active_raids and user_id in active_raids[chat_id]:
            active_raids[chat_id].remove(user_id)
            await event.reply("Raid has been stopped for the user.")
            # Clean up if there are no more active raids for the chat
            if not active_raids[chat_id]:
                del active_raids[chat_id]
        else:
            await event.reply("The user is not activated with raid.")
        await event.delete()  # Delete the command message

    @ubot.on(events.NewMessage(incoming=True))
    async def ai_reply(event):
        if event.chat_id in active_raids and event.sender_id in active_raids[event.chat_id]:
            await event.reply(random.choice(RAID))

async def is_user_allowed(event, ALLOWED_USER_ID):
    return event.sender_id == ALLOWED_USER_ID