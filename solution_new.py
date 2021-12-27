dict_of_facing = {
    "N": 0,  # 360
    "NE": 45,
    "E": 90,
    "SE": 135,
    "S": 180,
    "SW": 225,
    "W": 270,
    "NW": 315
}


def direction(facing, turn):
    current_degrees = dict_of_facing[facing]
    turn_degrees = current_degrees + turn
    if turn_degrees > 360:
        d = turn_degrees // 360
        turn_degrees = turn_degrees - d * 360
    if turn_degrees < 0:
        d = -turn_degrees // 360
        turn_degrees = 360 + turn_degrees + 360 * d
    if turn_degrees == 0 or turn_degrees == 360:
        return "N"
    else:
        for key in dict_of_facing:
            if dict_of_facing[key] == turn_degrees:
                return key


if __name__ == '__main__':
    print(direction("S", 180))
    print(direction("SE", -45))
    print(direction("W", 495))
    print(direction("N", -1090))
    print(direction("SW", 810))
    print(direction("SE", 945))
    print(direction("N", 675))
