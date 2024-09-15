dice = set()

dice.add("1")
dice.add("2")
dice.add("3")
dice.add("4")
dice.add("5")
dice.add("6")
print(dice.pop())

cheats = input("want dice with 1 & 6 only:")
if (cheats == "yes"):
    print("cheats activated....")
    ndice = set()
    ndice.add("6")
    ndice.add("1")
    print(ndice.pop())
else:
    print("ohkk....")
    