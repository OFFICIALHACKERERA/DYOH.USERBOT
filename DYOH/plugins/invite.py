import asyncio
from telethon import functions, events
from telethon.errors import ChatAdminRequiredError, UserNotParticipantError, ChannelPrivateError
from config import ALLOWED_USER_ID  # Ensure this is defined in your config
from telethon.tl.functions.channels import InviteToChannelRequest


async def register_channel_commands(ubot):
    @ubot.on(events.NewMessage(pattern=r".join ([\s\S]+)"))
    async def join_channel(event):
        if event.sender_id != ALLOWED_USER_ID:
            return

        channel_username = event.pattern_match.group(1).strip()
        joining_message = await event.reply("Joining...")

        try:
            channel = await ubot.get_entity(channel_username)
            me = await ubot.get_me()

            # Check if the bot is already a member of the channel
            try:
                await ubot(functions.channels.GetParticipantRequest(channel, me.id))
                await joining_message.delete()
                await event.reply("The bot is already a member of this channel.")
                return  # Exit after sending this message
            except (UserNotParticipantError, ChannelPrivateError):
                # The bot is not a member; continue to join
                pass

            # Attempt to join the channel
            await ubot(functions.channels.JoinChannelRequest(channel))
            await joining_message.delete()
            await event.reply("Joined successfully.")
        except ChatAdminRequiredError:
            await joining_message.delete()
            await event.reply("Error: The bot needs to be an admin to join this channel.")
        except Exception as e:
            await joining_message.delete()
            await event.reply(f"An error occurred: {str(e)}")
        finally:
            await event.delete()  # Delete the command message

    @ubot.on(events.NewMessage(pattern=r".leave ([\s\S]+)"))
    async def exit_channel(event):
        if event.sender_id != ALLOWED_USER_ID:
            return

        channel_username = event.pattern_match.group(1).strip()
        leaving_message = await event.reply("Leaving...")

        try:
            channel = await ubot.get_entity(channel_username)
            await ubot(functions.channels.LeaveChannelRequest(channel))
            await leaving_message.delete()
            await event.reply("Left the channel successfully.")
        except Exception as e:
            await leaving_message.delete()
            await event.reply(f"An error occurred: {str(e)}")
        finally:
            await event.delete()  # Delete the command message

    @ubot.on(events.NewMessage(pattern=r".inviteall ([\s\S]*)"))
    async def invite_users(event):
        if event.sender_id != ALLOWED_USER_ID:
            return

        target_channel = event.pattern_match.group(1).strip()
        restricted_channels = ["@raoxc", "@raoxc"]
        
        if target_channel in restricted_channels:
            await event.reply("You can't invite members from this channel.")
            await ubot.send_message("@raoxc", "Attempted to invite members from a restricted channel.")
            await event.delete()  # Delete the command message
            return

        status_message = await event.reply("`Processing...`")

        if event.is_private:
            await status_message.edit("`Sorry, can't add users here.`")
            await event.delete()  # Delete the command message
            return
        
        success_count = 0
        failure_count = 0
        error_message = "None"

        await status_message.edit("**[OWNER](https://t.me/raoxc)**\n\n`Inviting Users...`")
        async for user in ubot.iter_participants(target_channel):
            try:
                await ubot(InviteToChannelRequest(channel=event.chat_id, users=[user.id]))
                success_count += 1
                await status_message.edit(
                    f"**Inviting Users**\n\n"
                    f"**Invited :**  `{success_count}` users \n"
                    f"**Failed to Invite :**  `{failure_count}` users.\n\n"
                    f"**Error :**  `{error_message}`"
                )
            except Exception as e:
                error_message = str(e)
                failure_count += 1

        await status_message.edit(
            f"[DYOH OWNER](https://t.me/raoxc)\n\n"
            f"Successfully Invited `{success_count}` users \n"
            f"Failed to Invite `{failure_count}` users"
        )
        await event.delete()  # Delete the command message

    @ubot.on(events.NewMessage(pattern=r".invitesall ([\s\S]*)"))
    async def get_users(event):
        if event.sender_id != ALLOWED_USER_ID:
            return

        rao = await event.reply("`Processing...`")
        
        if event.is_private:
            await rao.edit("`Sorry, can't add users here`")
            await event.delete()  # Delete the command message
            return

        s = 0
        f = 0
        error = "None"

        await rao.edit("**Terminal Status**\n\n`Collecting Users.......`")
        async for user in event.client.iter_participants(event.pattern_match.group(1)):
            try:
                if error.startswith("Too"):
                    return await rao.edit(
                        f"**Terminal Finished With Error**\n(`May Got Limit Error from Telethon Please try again later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people"
                    )
                tol = user.id
                await ubot(InviteToChannelRequest(channel=event.chat_id, users=[tol]))
                s += 1
                await rao.edit(
                    f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× Last Error:** `{error}`"
                )
            except Exception as e:
                error = str(e)
                f += 1

        await rao.edit(
            f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• Failed to invite `{f}` people"
        )
        await event.delete()  # Delete the command message