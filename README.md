# Reversi

Reversi/Othello is a board game for two players. The rules can be found on [Wikipedia](https://en.wikipedia.org/wiki/Reversi). This repository contains a simple Python implementation of the game using sockets and a console UI.

```
    A   B   C   D   E   F   G   H
  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗
1 ║   │   │   │   │   │   │   │   ║ 1
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
2 ║   │   │   │   │   │   │   │   ║ 2
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
3 ║   │   │   │   │   │   │   │   ║ 3
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
4 ║   │   │   │ ● │ ○ │   │   │   ║ 4
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
5 ║   │   │   │ ○ │ ● │   │   │   ║ 5
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
6 ║   │   │   │   │   │   │   │   ║ 6
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
7 ║   │   │   │   │   │   │   │   ║ 7
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
8 ║   │   │   │   │   │   │   │   ║ 8
  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝
    A   B   C   D   E   F   G   H
```

## Getting started

Both clients need the repository and must be on the same network.

The first client starts a new game with the given port:

```shell
python3 reversi -n <port>
```

The second client can join the game with the first clients ip address and port:

```shell
python3 reversi -j <ip>:<port>
```

To place a piece, enter the desired position like `a1`.

## Testing

Unit tests for the main game logic are located in `/test`.

Run all unit tests:

```shell
python3 -m unittest
```
