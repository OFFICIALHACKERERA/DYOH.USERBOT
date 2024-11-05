import logging
from telethon import TelegramClient
from telethon.sessions import StringSession

# Set up logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)

# Version information
deadlyversion = "v0.3.0"

# Command handler prefix and SUDO user setup
CMD_HNDLR = "/"  # Command handler prefix
UBOT_HNDLR = ""  # Custom command handler

# Function to get the Bot token
def get_bot_token():
    bot_token = input("Enter your Bot Token: ")
    return bot_token

# Function to get the group ID, ensuring it's an integer
def get_group_id():
    while True:
        try:
            group_id = int(input("Enter the Group ID: "))
            return group_id
        except ValueError:
            print("Invalid Group ID. Please enter a valid integer.")

# Function to get the list of SUDO users, ensuring they're integers
def get_sudo_users():
    while True:
        try:
            sudo_users_input = input("Enter comma-separated SUDO_USER IDs (e.g., 1234567890, 9876543210): ")
            sudo_users = [int(user.strip()) for user in sudo_users_input.split(",")]
            return sudo_users
        except ValueError:
            print("Invalid SUDO User ID(s). Please enter valid comma-separated integers.")

# Function to get the API credentials
def get_api_credentials():
    api_id = input("Enter your API ID: ")
    api_hash = input("Enter your API Hash: ")
    return api_id, api_hash

# Function to get string sessions from user
def get_string_sessions():
    sessions = []
    num_sessions = int(input("How many string sessions do you want to enter? "))
    
    for i in range(num_sessions):
        session = input(f"Enter string session {i + 1}: ")
        if session:  # Check if the session string is not empty
            sessions.append(session)
        else:
            print("Session string cannot be empty. Please try again.")
            break  # Exit if the user inputs an empty session

    return sessions

# Function to get OWNER_ID from the user
def get_owner_id():
    while True:
        try:
            owner_id = int(input("Enter the OWNER_ID: "))
            return owner_id
        except ValueError:
            print("Invalid OWNER_ID. Please enter a valid integer.")

# Prompt user for all configuration details
API_ID, API_HASH = get_api_credentials()
BOT_TOKEN = get_bot_token()
GROUP_ID = get_group_id()  # Ensure Group ID is an integer
SUDO_USERS = get_sudo_users()
OWNER_ID = get_owner_id()  # Get the OWNER_ID from the user

# Get string sessions from the user
STRING_SESSION = get_string_sessions()

# Initialize the main bot
ubots = [
    TelegramClient(StringSession(session), API_ID, API_HASH, auto_reconnect=True)
    for session in STRING_SESSION
]
dybot = TelegramClient("dybot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Initialize the telebot instance with the first token

# If you want to keep multiple bots for other functionalities, you can store them in a list.
# For now, we will use only one for the command handling.
logging.info("[INFO] Successfully started all bot clients. Now loading plugins!")

# Here you can load your plugins or additional functionality
# Example: load_all_plugins() or similar function

# Example usage of group and sudo users
logging.info(f"Group ID: {GROUP_ID}")
logging.info(f"SUDO Users: {SUDO_USERS}")
logging.info(f"OWNER ID: {OWNER_ID}")
