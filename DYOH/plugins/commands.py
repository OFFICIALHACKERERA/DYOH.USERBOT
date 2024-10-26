import random
import time
from telethon import events

class CommandHandlers:
    def __init__(self, client, allowed_user_id):
        self.client = client
        self.allowed_user_id = allowed_user_id
        self.start_time = time.time()
        
        # Define your media link here
        self.IPIC = "https://telegra.ph/file/6bb3994d5789d8e7f2c99.mp4"

    async def handle_help_command(self, event):
        # Check if the user is the owner
        if event.sender_id != self.allowed_user_id:
            await event.respond("You do not have permission to use this command.")
            return
        
        # Define the help text with dot prefix
        help_text = (
            "**Available Commands:**\n"
            "`.alive` - Check if the bot is online.\n"
            "`.spam <count> <text>` - Spam the specified text <count> times.\n"
            "`.raid <count>` - Raid a user by replying to their message <count> times.\n"
            "`.join <channel>` - Join a specified channel.\n"
            "`.leave <channel>` - Leave a specified channel.\n"
            "`.help` - Show this help message.\n"
            "`.replyraid` - Activate raid on a replied user.\n"
            "`.dreplyraid` - Deactivate raid on a replied user.\n"
            "`.inviteall` - Invite all users.\n"
            "`.invitesall` - Invite all users to a group."
        )

        # Send the media file with the help text as a caption
        await self.client.send_file(
            event.chat_id,
            file=self.IPIC,
            caption=help_text
        )

        # Delete the command message
        await event.delete()

    async def register_handlers(self):
        @self.client.on(events.NewMessage(pattern=r"\.help"))
        async def help_handler(event):
            await self.handle_help_command(event)