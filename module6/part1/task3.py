def square(filled):
    if (filled):
        for i in range(10):
            for j in range(10):
                print("*", end=" ")
            print()
    else:
        for i in range(10):    
            for j in range(10):
                if j == 0 or i == 0:
                    print("*", end=" ")
                elif j == 9 or i == 9:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

square(False)