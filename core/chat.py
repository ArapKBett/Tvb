# core/chat.py
import websocket
import time
from config.config import OAUTH_TOKEN, BOT_USERNAME, CHANNEL_NAME, CHAT_MESSAGES, MESSAGE_INTERVAL
from utils.helpers import log, random_delay, random_message

class ChatBot:
    def __init__(self):
        self.ws = websocket.WebSocket()
        self.connected = False

    def connect(self):
        """Connect to Twitch IRC server with error handling."""
        try:
            self.ws.connect("wss://irc-ws.chat.twitch.tv:443")
            self.ws.send(f"PASS {OAUTH_TOKEN}")
            self.ws.send(f"NICK {BOT_USERNAME}")
            self.ws.send(f"JOIN {CHANNEL_NAME}")
            self.connected = True
            log(f"Connected to {CHANNEL_NAME}")
        except Exception as e:
            log(f"Failed to connect to Twitch IRC: {e}")
            raise

    def send_message(self, message=None):
        """Send a message to the Twitch chat."""
        if not self.connected:
            log("Cannot send message: Not connected")
            return
        message = message or random_message(CHAT_MESSAGES)
        try:
            self.ws.send(f"PRIVMSG {CHANNEL_NAME} :{message}")
            log(f"Sent message: {message}")
        except Exception as e:
            log(f"Failed to send message: {e}")

    def run_chat(self):
        """Run the chat bot: connect and send multiple messages."""
        try:
            self.connect()
            for _ in range(3):  # Send 3 messages
                self.send_message()
                random_delay(MESSAGE_INTERVAL - 10, MESSAGE_INTERVAL + 10)  # Vary interval
        except Exception as e:
            log(f"Chat bot error: {e}")
        finally:
            self._disconnect()

    def _disconnect(self):
        """Safely disconnect from the server."""
        if self.connected:
            try:
                self.ws.close()
                log("Disconnected from chat")
                self.connected = False
            except Exception as e:
                log(f"Error disconnecting: {e}")

def run_chat():
    try:
        bot = ChatBot()
        bot.run_chat()
    except Exception as e:
        log(f"Chat run failed: {e}")
