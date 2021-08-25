def eval_direction():
    return 0

def main():
    f = open("day12.txt","r")
    moves = f.read().split("\n")
    ship_direction = 1
    #east = 1
    net_movement = [0,0,0,0]
    #n,e,s,w
    for move in moves:
        if "N" in move:
            net_movement[0] += int(move[1:])
        elif "E" in move:
            net_movement[1] += int(move[1:])
        elif "S" in move:
            net_movement[2] += int(move[1:])
        elif "W" in move:
            net_movement[3] += int(move[1:])
        elif "F" in move:
            net_movement[ship_direction] +=int(move[1:])
        elif "R" in move:
            if "90" in move:
                ship_direction = (ship_direction + 1) % 4
            elif "180" in move:
                ship_direction = (ship_direction + 2) % 4
            else:
                ship_direction = (ship_direction + 3) % 4
        elif "L" in move:
            if "90" in move:
                ship_direction = (ship_direction + 3) % 4
            elif "180" in move:
                ship_direction = (ship_direction + 2) % 4
            else:
                ship_direction = (ship_direction + 1) % 4
    manhattan_distance_y = net_movement[0] - net_movement[2]
    manhattan_distance_x = net_movement[1] - net_movement[3]
    print(manhattan_distance_x)
    print(manhattan_distance_y)
    #part2
    waypoint = [1,10,0,0]
    part2 = [0,0,0,0]
    #part2 = [a + b for a, b in zip(waypoint, part2)]
    for move in moves:
        if "N" in move:
            waypoint[0] += int(move[1:])
        elif "E" in move:
            waypoint[1] += int(move[1:])
        elif "S" in move:
            waypoint[2] += int(move[1:])
        elif "W" in move:
            waypoint[3] += int(move[1:])
        elif "F" in move:
            part2 = [a*int(move[1:]) + b for a, b in zip(waypoint, part2)]
        elif "R" in move:
            #rotate by 1
            if "90" in move:
                waypoint=waypoint[-1:]+waypoint[:-1]
            elif "180" in move:
                waypoint=waypoint[-1:]+waypoint[:-1]
                waypoint=waypoint[-1:]+waypoint[:-1]
            else:
                waypoint=waypoint[1:]+waypoint[0:1]
        elif "L" in move:
            if "90" in move:
                waypoint=waypoint[1:]+waypoint[0:1]
            elif "180" in move:
                waypoint=waypoint[1:]+waypoint[0:1]
                waypoint=waypoint[1:]+waypoint[0:1]
            else:
                waypoint=waypoint[-1:]+waypoint[:-1]
    print(part2)
    part2_y = part2[0] - part2[2]
    part2_x = part2[1] - part2[3]
    print(part2_x)
    print(part2_y)
if __name__ == "__main__":
    main()