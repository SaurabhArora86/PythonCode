def find_max(lt):
    max = lt[0]
    for number in lt:
        if number > max:
            max = number
    return (max)


def find_min(lt):
    min = lt[0]
    for number in lt:
        if number < min:
            min = number
    return (min)
