# utils/helpers.py
import random
import time

def random_delay(min_delay=1, max_delay=10):
    """Add a random delay to mimic human behavior."""
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)
    return delay

def random_message(messages):
    """Select a random message from a list."""
    return random.choice(messages)

def log(message):
    """Simple logging with timestamp."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")
