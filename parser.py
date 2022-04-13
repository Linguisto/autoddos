import re

from spam_units import Unit, IP, Port


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
