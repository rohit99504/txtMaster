import os

API_ID = API_ID = 27498866

API_HASH = os.environ.get("API_HASH", "96fbb6ad2e11ab04e83ca09ef3f42455")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7166257969:AAFbVtNiIEPqgaH8mDW3ymED0P7bJPAhZ-k")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6488911325))

LOG = -1002059340064

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6488911325").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
