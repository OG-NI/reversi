import argparse
import re

from reversi import socket_connection, console_ui


def __parse_ip_port(string):
    if not re.match(r'^(\d+\.){3}\d+:\d+$', string):
        raise argparse.ArgumentError(
            'The game host must be specified in the format <ip>:<port>')

    ip, port = string.split(':')
    return (ip, int(port))


def main():
    parser = argparse.ArgumentParser(prog="python3 -m reversi")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-n', '--new', metavar='<port>', type=int,
                       help='start a new game')
    group.add_argument('-j', '--join', metavar='<ip>:<port>',
                       type=__parse_ip_port, help='join a game')

    args = parser.parse_args()
    sc = socket_connection.SocketConnection(console_ui.ConsoleUI())
    if args.new:
        sc.host(args.new)
    else:
        ip, port = args.join
        sc.join(ip, port)


if __name__ == '__main__':
    main()
