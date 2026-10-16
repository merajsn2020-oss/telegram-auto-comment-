import os
import asyncio
import logging
from telethon import TelegramClient, events

logging.basicConfig(level=logging.INFO)

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION = os.environ["SESSION"]
CHANNEL = os.environ["CHANNEL"]
COMMENT = os.environ.get("COMMENT", "سلام")

client = TelegramClient(SESSION, API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNEL))
async def new_post(event):
    if event.is_channel:
        logging.info("New post detected: %s", event.id)

async def main():
    await client.start()
    logging.info("Connected. Monitoring %s", CHANNEL)
    await client.run_until_disconnected()

asyncio.run(main())
