import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 5000
    s.connect((host, port))
    print('it works')


if __name__ == '__main__':
    main()
