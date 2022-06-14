from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("BABqhC8y13OWVscqiOHB-Zse6mvEHROKK_rT2PenD7vsHUq_bQOPg78iFFbmQVvckqaAsD2KvX87H_U0O7NdzRHYbg-UDm7YhMXOfEevZrd5qhcjWUKxhfU7_iNXBj1JN9HeuhkHGvWe-9Xmw5YGMXvwXgNkS-Un85CDaBHTSdta5Z8yHr05MPJVr9wq1LlkRDv7CjSK4NsVkB1Bfh6LlORlYNW8_uD7OsVJ_pf2eD8Y8-mzPMz0FEVp3pfk9P5PYjvlmTaVRST14Q6YUCzSGtLqYfzmSBQLPyjMn8qLRaEMt4knncGiKCoFkIDsJlsvjNwqXyB525Bg1wI53lMIYjWqAAAAAFsLb9EA", "session")
BOT_TOKEN = getenv("5211551773:AAEGPgnO6C-1GDiwn-R6QY4gl6JW_OOaROE")
BOT_NAME = getenv("MytMusic", "MytMüzik") 
API_ID = int(getenv("3939406"))
API_HASH = getenv("e11d0eaec136b1047974ab098041e9f2")
BOT_USERNAME = getenv("BOT_USERNAME", "Myt_Music_Bot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "59"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
