import socket


class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

    def __repr__(self):
        return 'Scanner:{}'.format(self.ip)

    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport + 1):
            if self.is_open(port):
                print(port)
                self.add_port(port)

    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((self.ip, port))
        # print('Port {}:      {}'.format(port, result))
        s.close()
        return result == 0

    def write(self, filepath):
        openport = map(str, self.open_ports)
        with open(filepath, 'w') as f:
            f.write('\n'.join(openport))


def main():
    # entered_ip = input('Enter the IP Address or range to scan: ')
    ip = '192.168.91.129'  # entered_ip  # entered_ip
    scanner = Scanner(ip)
    scanner.scan(1, 22)
    scanner.write('./open_ports.txt')


if __name__ == '__main__':
    main()
