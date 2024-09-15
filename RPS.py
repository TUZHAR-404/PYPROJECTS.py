game = set()

game.add("ROCK")
game.add("PAPER")
game.add("SCISSOR")

val = input("Want to play game:")
if (val == "yes"):
    print("ROCK......PAPER.......SCISSOR....:",game.pop())
else:
    print("GAME OVER")

