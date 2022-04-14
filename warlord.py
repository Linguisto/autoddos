import asyncio
import dotenv
import re
import parser

from telethon import TelegramClient, events
from spam_units import Unit
from winger import Winger

conf = dotenv.dotenv_values()

api_id = conf.get('tg_api_id')
api_hash = conf.get('tg_api_hash')

client = TelegramClient('f.russia', int(api_id), api_hash)


async def attack(units: [Unit]):
    for unit in units:
        await Winger(unit).attack()


async def main():
    await client.start()
    pattern = re.compile(
        r'[\W\w]+(https?://[\w\-\.]+\.\w{2,5})|(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|(\d+)/(tcp|udp|http)',
        re.M | re.I
    )

    @client.on(events.NewMessage(pattern=pattern))
    async def handler(event):
        # check whether the message contains any IP
        ips = re.compile(
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
            re.M
        ).findall(event.message.message)
        if len(ips) == 0:
            return

        units = parser.msg_parse_units(event.message.message)
        await attack(units)

    await client.run_until_disconnected()


asyncio.run(main())
