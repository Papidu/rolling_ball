from animation import start_animations


if __name__ == "__main__":
    while(1):
        mass = int(input("Input mass in kg ")) 
        if(mass < 1 or mass > 100):
            print("Too much... ")
            continue

        radius = int(input("Input radius "))
        if(radius < 1 or radius >100):
            print("Too much... ")
            continue

        x = input("Entering the height and width of a block separated by a space ").split(' ')

        list_cords = list(map(int, x))
        print("A rubber ball and its friction force is 1")
        print("A block of wood and its friction force is 0.4")

        start_animations(mass, radius, 1, (2, list_cords[0]+2), 0.1, [(0, list_cords[0]), (list_cords[1], 0)])#(1240, 0)])