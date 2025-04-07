import argparse
import re

from socket_connection import SocketConnection
from console_ui import ConsoleUI


def __parse_ip_port(string):
    if not re.match(r'^(\d+\.){3}\d+:\d+$', string):
        raise argparse.ArgumentError(
            'The game host must be specified in the format <ip>:<port>')

    ip, port = string.split(':')
    return (ip, int(port))


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-n', '--new', metavar='<port>', type=int,
                       help='start a new game')
    group.add_argument('-j', '--join', metavar='<ip>:<port>',
                       type=__parse_ip_port, help='join a game')

    args = parser.parse_args()
    sc = SocketConnection(ConsoleUI())
    if args.new:
        sc.host(args.new)
    else:
        ip, port = args.join
        sc.join(ip, port)


if __name__ == '__main__':
    main()
