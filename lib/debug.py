#!/usr/bin/env python3
import ipdb
from faker import Faker
import random

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

fake = Faker()

game1 = Game(fake.color_name())
game2 = Game(fake.color_name())
game3 = Game(fake.color_name())
game4 = Game(fake.color_name())

player1 = Player(fake.name()[2:16])
player2 = Player(fake.name()[2:16])
player3 = Player(fake.name()[2:16])
player4 = Player(fake.name()[2:16])
player5 = Player(fake.name()[2:16])
player6 = Player(fake.name()[2:16])

rs1 = Result(player1, game1, random.randint(1,100))
rs2 = Result(player2, game1, random.randint(1,100))
rs3 = Result(player1, game2, random.randint(1,100))
rs4 = Result(player6, game1, random.randint(50, 700))
rs5 = Result(player3, game3, random.randint(1,100))
rs6 = Result(player2, game4, random.randint(1,100))
rs7 = Result(player2, game4, random.randint(1,100))
rs8 = Result(player6, game4, random.randint(1,100))
rs9 = Result(player4, game2, random.randint(1,100))


if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    ipdb.set_trace()

