import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'www.python.org'
    port = 80
    result = s.connect_ex((host, port))
    print()
    print('Result is {}'.format(result))
    s.close()


if __name__ == '__main__':
    main()
