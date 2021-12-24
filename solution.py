dict_of_values = {
    "NE": [22.5, 67.5],
    "E": [67.5, 112.5],
    "SE": [112.5, 157.5],
    "S": [157.5, 202.5],
    "SW": [202.5, 247.5],
    "W": [247.5, 292.5],
    "NW": [292.5, 337.5],
    "N": [337.5, 22.5]
}

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
    for key in dict_of_values:
        if 22.5 >= turn_degrees >= 0 or 360 >= turn_degrees >= 337.5:
            return "N"
        if (dict_of_values[key][0] if turn_degrees >= 0 else 360) <= turn_degrees <= dict_of_values[key][1]:
            return key


if __name__ == '__main__':
    print(direction("S", 180))
    print(direction("SE", -45))
    print(direction("W", 495))
    print(direction("N", -1090))
    print(direction("SW", 810))
    print(direction("SE", 945))
    print(direction("N", 675))
