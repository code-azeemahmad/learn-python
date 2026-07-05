# Problem: Recommend a type of pet food based on the pet's species andage. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = "cat"
age = 8

match species, age:
    case ("dog", a) if a < 2:
        print("puppy food")
    case ("cat", a) if a > 5:
        print("senior cat food")
    case (_, _):
        print("other food deals")