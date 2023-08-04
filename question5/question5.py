trying1 = 0
trying2 = 0
n = int(input("Enter the floor: "))

def drop_egg_floor(start, add):
    global trying1 
    array=[]
    actual_floor = start
    trying = 0
    while actual_floor <= 100:
        trying += 1
        if (actual_floor >= n):
            return trying
        actual_floor += add
        array.append(trying)
        trying1 = array[-1]

    return trying
        

def main():

    for add in [20, 30, 10]:  
        print(f"First egg interval {add}")
        start = add  
        egg1_trying = drop_egg_floor(start, add)  

        if egg1_trying == 1:
            min_trying = 1
            break
        trying2 = egg1_trying
        start = (egg1_trying - 1) * add + 1
        egg2_trying = drop_egg_floor(start, 1)  
        
        print(f"Number off attempts: Egg1: {trying2}, Egg2: {trying1 }")

        
if __name__ == "__main__":
    main()
