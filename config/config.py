# config/config.py
# Stream settings
STREAM_URL = "https://www.twitch.tv/your_channel_name"  # Target stream URL
NUM_VIEWERS = 3  # Number of viewers to simulate

# Proxy settings
PROXY_LIST = [
    "http://proxy1:port",  # Replace with real proxies
    "http://proxy2:port",
    "http://proxy3:port"
]

# Chat bot credentials
OAUTH_TOKEN = "oauth:your_token_here"  # Get from https://twitchapps.com/tmi/
BOT_USERNAME = "your_bot_username"     # Your Twitch bot's username
CHANNEL_NAME = "#your_channel_name"    # Channel to join (e.g., "#streamername")

# Runtime settings
VIEWER_DURATION = 300  # Seconds each viewer stays (5 minutes)
CHAT_MESSAGES = [
    "Hello from bot!",
    "Great stream!",
    "Keep it up!"
]  # List of messages to send randomly
MESSAGE_INTERVAL = 60  # Seconds between chat messages
