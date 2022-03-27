class Port:
    def __init__(self, number: int, protocol: str = 'TCP'):
        self.number = number
        self.protocol = protocol


class IP:
    ports: [Port] = []

    def __init__(self, address: str):
        self.address = address


class Unit:
    ips: [IP] = []

    def __init__(self, site: str = ''):
        self.site = site
