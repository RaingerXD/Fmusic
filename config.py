from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "27025466"))
API_HASH = getenv("API_HASH", "750ca688d4a6e58826e48d321ae4d498")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))

OWNER_ID = int(getenv("OWNER_ID", "5615921474"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/2e2a2cd8c9db45ae73de6.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2e2a2cd8c9db45ae73de6.jpg")

SESSION = getenv("SESSION", "BQGcYDoAcGtL3w338d7UAsvyomqY6EA1AYiaJDty-OkD9u-P2TAO0bIETYNN4H6kK3GtkdGQ01fTthaMqv19JwZ1aa2QXTkHark5mqITCODNx9yBlq0orVe-kCwOggn-uBNrmpJueTCYdYvXeCGAygSSQ2cLwd-wIezP9fPUs_oTS-e7bQQvk9hsnqf9zgitnhYm1Jt664qp4aprCcbCxEP8x6S5wC0h8Ms7j8jleCwehQzfHmlfBAbUIewDDY3oJ9rXbChXWvq4cHyD_lpv7bTaDz4ss39WwquDdcz-0NtTa1c3Cq3QwaJet-bCHfpK88sFdcRm4dD9_qu6L2GGSAEQLDpgAAAABl18tsAA ")

MUST_JOIN = getenv("MUST_JOIN", "raingerproject")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/raingersupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/raingerproject")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5615921474").split()))


FAILED = "https://telegra.ph/file/2e2a2cd8c9db45ae73de6.jpg"
