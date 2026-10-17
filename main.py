import os
import asyncio
import logging
from telethon import TelegramClient, events
from telethon.sessions import StringSession

logging.basicConfig(level=logging.INFO)

client = TelegramClient(
    StringSession(os.environ["SESSION"]),
    int(os.environ["API_ID"]),
    os.environ["API_HASH"]
)

CHANNEL = os.environ["CHANNEL"]

@client.on(events.NewMessage(chats=CHANNEL))
async def handler(event):
    if event.is_channel:
        logging.info("New post detected: %s", event.id)

async def main():
    await client.start()
    logging.info("Monitoring %s", CHANNEL)
    await client.run_until_disconnected()

asyncio.run(main())
