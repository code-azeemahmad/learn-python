distance = 16

# Structural Pattern Matching

match distance:
    case d if d < 3:
        print(d,":","walk")
    case d if d >= 3 and d <= 15:
        print(d,":","bike")
    case d_:    # '_ ' acts as the default 'else' catch-all
        print(d,":","car")

# Unlike a C++ switch, which only accepts discrete integral constants, 
# Python's match-case allows you to use conditional guards (if), 
# making it capable of handling ranges!

