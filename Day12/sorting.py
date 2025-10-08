from collections import namedtuple

Player = namedtuple('Player', ['name', 'score'])
players = [Player('John', 95), Player('Alice', 88), Player('Bob', 99)]

sorted_players = sorted(players, key=lambda x: x.score, reverse=True)
for p in sorted_players:
    print(p.name, p.score)
