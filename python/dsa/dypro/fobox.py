def box(points):
    a = 0
    b = 0
    for p in points:
        a, b = b, max(a+p, b)

    return b


if __name__ == '__main__':
    all_places = [
        [3, 10, 5, 2, 1], [6, 10, 6], [9, 11, 1, 1, 7]
    ]
    for places in all_places:
        print(f'For {places} the best growth would be {box(places)}')
