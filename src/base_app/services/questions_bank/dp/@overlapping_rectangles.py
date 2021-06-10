def area(x1, y1, x2, y2):
    if (x2-x1) > 0 and (y2-y1) > 0:
        return (x2-x1) * (y2-y1)
    else:
        return 0


def overlapping_rectangles(rect1, rect2):
    x1 = max(rect1[0][0], rect2[0][0])
    x2 = min(rect1[1][0], rect2[1][0])

    y1 = max(rect1[0][1], rect2[0][1])
    y2 = min(rect1[1][1], rect2[1][1])

    return area(x1, y1, x2, y2)


rect1=[[2,1], [5,5]]
rect2=[[3,2], [5,7]]
print(overlapping_rectangles(rect1, rect2))