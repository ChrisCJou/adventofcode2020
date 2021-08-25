def simulateSeats(seats):
    #output seats
    new_seats = []
    # seat_n
    # seat_ne
    # seat_e
    # seat_se
    # seat_s
    # seat_sw
    # seat_w
    # seat_nw
    for i, seat_row in enumerate(seats):
        for j, seat in enumerate(seats[i]):
            print(" i : " + str(i)  + " j : "+ str(j) + " seat : " + seat)
    return 0

#maybe need helper function to get adjacent?

f = open("day11test.txt","r")
seats = f.read().splitlines()
print(simulateSeats(seats))

#to track when it stops changing, just keep a tab when it changes

