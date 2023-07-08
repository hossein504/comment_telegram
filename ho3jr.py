from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import random

#Get api_id and api_hash from this link (https://my.telegram.org/auth)
api_id = 12345 
api_hash = "0123456789abcdef0123456789abcdef"

app = Client("ho3jr_Client_name", api_id=api_id, api_hash=api_hash)
cms=["اره","نه","جالیه","اوک"] #Enter your comments here
cms_random = random.choice(cms)

@app.on_message(filters.text & filters.channel)
async def newMessageListener(client, event):
    new_message_id = event.id
    channel_id = event.chat.id

    m = await client.get_discussion_message(channel_id, new_message_id)
    await m.reply(cms_random)

test_channel_ids = [-1111111111,-11111111111] #Enter channel IDs here
my_handler = MessageHandler(newMessageListener, filters.chat(test_channel_ids))
app.add_handler(my_handler)
app.run()
