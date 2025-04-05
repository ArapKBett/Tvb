# core/proxy_manager.py
from config.config import PROXY_LIST
from utils.helpers import log

class ProxyManager:
    def __init__(self):
        self.proxies = PROXY_LIST
        self.index = 0
        self._validate_proxies()

    def _validate_proxies(self):
        """Check if proxies are provided and valid."""
        if not self.proxies:
            log("Warning: No proxies provided. Running without proxies.")
        else:
            log(f"Loaded {len(self.proxies)} proxies")

    def get_next_proxy(self):
        """Get the next proxy in the list, cycling if necessary."""
        if not self.proxies:
            return None
        proxy = self.proxies[self.index]
        self.index = (self.index + 1) % len(self.proxies)
        return proxy

    def has_proxies(self):
        """Check if there are any proxies available."""
        return len(self.proxies) > 0
