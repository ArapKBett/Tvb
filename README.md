# Twitch Viewer Bot (Educational)
A theoretical Twitch bot for learning purposes. Simulates viewers and interacts with chat.

## Setup
1. Install Python and dependencies: `pip install -r requirements.txt`
2. Install ChromeDriver and add to PATH (see instructions below).
3. Update `config/config.py` with your stream URL, proxies, and Twitch credentials.
4. Run: `python main.py`

## ChromeDriver Setup
- Download from https://chromedriver.chromium.org/downloads matching your Chrome version.
- Place in PATH (e.g., `/usr/local/bin` on Linux/macOS, `C:\WebDrivers` on Windows).

## Notes
- Requires a Twitch OAuth token from https://twitchapps.com/tmi/.
- Proxies are optional but recommended for viewer simulation.
- For educational use only—do not violate Twitch's Terms of Service.
