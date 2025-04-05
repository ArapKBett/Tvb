# core/viewer.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time
from config.config import STREAM_URL, VIEWER_DURATION
from utils.helpers import log, random_delay

class ViewerBot:
    def __init__(self, proxy=None):
        self.proxy = proxy
        self.driver = None
        try:
            self.driver = self._setup_driver()
        except WebDriverException as e:
            log(f"Failed to initialize driver with proxy {self.proxy}: {e}")
            raise

    def _setup_driver(self):
        """Set up a headless Chrome driver with proxy."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")  # For Termux/Linux compatibility
        chrome_options.add_argument("--disable-dev-shm-usage")
        if self.proxy:
            chrome_options.add_argument(f"--proxy-server={self.proxy}")
        return webdriver.Chrome(options=chrome_options)

    def start_viewer(self):
        """Simulate a viewer watching the stream."""
        try:
            log(f"Starting viewer with proxy: {self.proxy or 'No proxy'}")
            self.driver.get(STREAM_URL)
            random_delay(2, 5)  # Random initial delay
            time.sleep(VIEWER_DURATION)
        except WebDriverException as e:
            log(f"Viewer error with proxy {self.proxy}: {e}")
        finally:
            self.stop_viewer()

    def stop_viewer(self):
        """Safely close the driver."""
        if self.driver:
            try:
                self.driver.quit()
                log(f"Viewer stopped with proxy: {self.proxy or 'No proxy'}")
            except Exception as e:
                log(f"Error stopping viewer: {e}")

def run_viewer(proxy):
    try:
        bot = ViewerBot(proxy)
        bot.start_viewer()
    except Exception as e:
        log(f"Viewer run failed with proxy {proxy}: {e}")
