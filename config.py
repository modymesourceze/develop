from mody import Mody
from pyrogram import Client,filters,enums
import redis

r = redis.Redis(
  host='redis-16032.c232.us-east-1-2.ec2.redns.redis-cloud.com',
  port=16032,
  password='4CA0Qkc5pNlGP0vlWIF1XYSGL3MOVlJ0')

sudo_id = 6581896306
bot_user = Mody.BOT_USER
via_user = Mody.VIA_USER
elhyba = bot_user
via = via_user
api_id = Mody.APP_ID
api_hash = Mody.API_HASH
session = Mody.SESSION
token = Mody.TG_BOT_TOKEN
sudo_command = [6581896306]
pm =  Mody.MENTION
mention = "6581896306"
plugins = dict(root="plugins")
app = Client(via,api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client(elhyba,api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
