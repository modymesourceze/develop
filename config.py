from mody import Mody
from pyrogram import Client,filters,enums
import redis

r = redis.Redis(
  host='redis-17811.c323.us-east-1-2.ec2.cloud.redislabs.com',
  port=17811,
  password='y41sFD7N8cY5Ob2MGPZkGdrTndVFY92h')

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
