# main.py
from core.viewer import run_viewer
from core.chat import run_chat
from core.proxy_manager import ProxyManager
from config.config import NUM_VIEWERS
from utils.helpers import log, random_delay
import threading

def main():
    log("Starting Twitch Viewer Bot")
    proxy_manager = ProxyManager()

    # Start viewers
    viewer_threads = []
    for _ in range(NUM_VIEWERS):
        proxy = proxy_manager.get_next_proxy()
        thread = threading.Thread(target=run_viewer, args=(proxy,))
        viewer_threads.append(thread)
        thread.start()
        random_delay(2, 5)  # Stagger viewer starts

    # Start chat bot
    chat_thread = threading.Thread(target=run_chat)
    chat_thread.start()

    # Wait for all threads to complete
    for thread in viewer_threads:
        thread.join()
    chat_thread.join()

    log("Bot execution completed")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Bot stopped by user")
    except Exception as e:
        log(f"Unexpected error in main: {e}")
