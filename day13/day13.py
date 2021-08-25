import numpy as np
def main():
    current_time = 1008169
    bus_ids = [29,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',41,'x','x','x',37,'x','x','x','x','x',653,'x','x','x','x','x','x','x','x','x','x','x','x',13,'x','x','x',17,'x','x','x','x','x',23,'x','x','x','x','x','x','x',823,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',19]
    nearest_id = 0
    nearest_time = 12
    #time to wait is 
    #bus_id - (time mod bus_id), unless time mod bus_id is 0, in which case it's 0
    for id in bus_ids:
        if id != 'x':
            print(id)
            temp_nearest_time = (id - current_time % id)
            if nearest_time > temp_nearest_time:
                nearest_time = temp_nearest_time
                nearest_id = id
    print(nearest_id)
    print(nearest_time)
    #part2
    offset = []
    bus = []
    for count, id in enumerate(bus_ids):
        if id != 'x':
            offset.append(count)
            bus.append(id)
    print(offset)
    print(bus)
    t, step = 0, 1
    for (bus, offset) in zip(bus, offset):
        while (t + offset) % bus:
            t += step
        step *= bus
    print(step)
if __name__ == "__main__":
    main()