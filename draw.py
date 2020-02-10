from display import *

def octant_number(x0, y0, x1, y1):
    slope = (y1 - y0) / (x1 - x0)
    if slope >= 0 and slope <= 1:
        return 1
    elif slope > 1:
        return 2
    elif slope < 0 and slope >= -1:
        return 8
    elif slope < -1:
        return 7

def draw_line( x0, y0, x1, y1, screen, color ):
    # Vertical lines
    try:
        octant = octant_number(x0, y0, x1, y1)
        A = y1 - y0
        B = -1 * (x1 - x0)
        if octant == 1:
            if y0 > y1 and x0 > x1:
                draw_line(x1, y1, x0, y0, screen, color)
            else:
                for i in range(x1 - x0):
                    x = x0
                    y = y0
                    d = 2 * A + B
                    while x <= x1:
                        plot(screen, color, x, y)
                        if d > 0:
                            y += 1
                            d += 2 * B
                        x += 1
                        d += 2 * A
        if octant == 2:
            if y0 > y1 and x0 > x1:
                draw_line(x1, y1, x0, y0, screen, color)
            else:
                for i in range(x1 - x0):
                    x = x0
                    y = y0
                    d = A + 2 * B
                    while y <= y1:
                        plot(screen, color, x, y)
                        if d < 0:
                            x += 1
                            d += 2 * A
                        y += 1
                        d += 2 * B
        if octant == 8:
            if y0 < y1 and x0 > x1:
                draw_line(x1, y1, x0, y0, screen, color)
            else:
                for i in range(x1 - x0):
                    x = x0
                    y = y0
                    d = 2 * A - B
                    while x <= x1:
                        plot(screen, color, x, y)
                        if d < 0:
                            y -= 1
                            d += -2 * B
                        x += 1
                        d += 2 * A
        if octant == 7:
            if y0 < y1 and x0 > x1:
                draw_line(x1, y1, x0, y0, screen, color)
            else:
                for i in range(x1 - x0):
                    x = x0
                    y = y0
                    d = A + -2 * B
                    while y >= y1:
                        plot(screen, color, x, y)
                        if d > 0:
                            x += 1
                            d += 2 * A
                        y -= 1
                        d += -2 * B
    except ZeroDivisionError as e:
        if y0 > y1:
            draw_line(x1, y1, x0, y0, screen, color)
        else:
            for i in range(y1 - y0):
                y = y0
                while y <= y1:
                    plot(screen, color, x0, y)
                    y += 1
