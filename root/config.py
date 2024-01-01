"""
© Mrvishal2k2
RenameBot
This file is a part of mrvishal2k2 rename repo
Dont kang !!!
© Mrvishal2k2
"""
import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID","8733404"))
    API_HASH = os.environ.get("API_HASH","f19aed00b0c74abed0359016afc1733f")
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN","5567847114:AAGrO_uulshxfHcqc1X7zygDxahRuyY2C4g")
    AUTH_USERS = [int(x) for x in os.environ.get("AUTH_USERS", "").split()]
    DOWNLOAD_LOCATION = "./bot/DOWNLOADS"
    DB_URI = os.environ.get("DATABASE_URL","postgres://ypbpwwzqrntoqn:821ffc75f621cfd2faeea5e95f71224ca773f48a19add6d24c6c1138f021b7db@ec2-23-21-207-93.compute-1.amazonaws.com:5432/dfl6oogvkl08qq")
    # owner is for log cmd only owner can use (this can be multiple users)
    OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID","807374433").split(" ")]
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "BotDunia")
    CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", False)
