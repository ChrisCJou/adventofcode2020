import time
start_time = time.time()

def read_file_into_array(file_name):
    f = open(file_name,"r")
    slope_array = f.readlines()
    f.close()
    return slope_array

def check_tree(line, xPos):
    return (line[xPos % 31] == '#' )

def main():
    slope = read_file_into_array('day3.txt')
    #part1
    numTrees = 0
    xPos = 0
    for line in slope:
        if check_tree(line, xPos):
            numTrees +=1 
        xPos +=3
    print("PART 1: " + str(numTrees))
    #part2
    numTrees1_1 = 0
    numTrees3_1 = 0
    numTrees5_1 = 0
    numTrees7_1 = 0
    numTrees1_2 = 0
    xPos1_1 = 0
    xPos3_1 = 0
    xPos5_1 = 0
    xPos7_1 = 0
    xPos1_2 = 0
    
    for index, line in enumerate(slope):
        if check_tree(line, xPos1_1):
            numTrees1_1 +=1
        if check_tree(line, xPos3_1):
            numTrees3_1 +=1 
        if check_tree(line, xPos5_1):
            numTrees5_1 +=1 
        if check_tree(line, xPos7_1):
            numTrees7_1 +=1 
        if check_tree(line, int(xPos1_2)) and (index % 2 == 0):
            numTrees1_2 +=1
        xPos1_1 +=1
        xPos3_1 +=3
        xPos5_1 +=5
        xPos7_1 +=7
        xPos1_2 +=.5
    print("Number of Trees 1 x 1:" + str(numTrees1_1))
    print("Number of Trees 3 x 1:" + str(numTrees3_1))
    print("Number of Trees 5 x 1:" + str(numTrees5_1))
    print("Number of Trees 7 x 1:" + str(numTrees7_1))
    print("Number of Trees 1 x 2:" + str(numTrees1_2))
    print(numTrees1_1 * numTrees3_1 * numTrees5_1 * numTrees7_1* numTrees1_2)
    print(time.time() - start_time)

if __name__ == "__main__":
    main()