from mody import Mody
from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 6581896306
bot_user = "r4dbbot"
api_id = Mody.APP_ID
api_hash = Mody.API_HASH
session = Mody.SESSION
token = Mody.TG_BOT_TOKEN
sudo_command = [6581896306]
pm = "6581896306"
mention = "6581896306"
plugins = dict(root="plugins")
app = Client("user:r4dbbot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("r4dbbot",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
