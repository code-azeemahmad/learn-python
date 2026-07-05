import random
color = ["green", "yellow", "brown"]
color = random.choice(color)

if color == "green":
    print(color,": unripe")
elif color == "yellow":
    print(color,": ripe")
else:
    print(color,": overripe")