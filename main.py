from display import *
from draw import *

s = new_screen()
c = [ 255, 255, 0 ]

draw_line(425, 250, 375, 300, s, c)
draw_line(375, 300, 325, 325, s, c)
draw_line(325, 325, 325, 300, s, c)
draw_line(325, 300, 300, 275, s, c)
draw_line(275, 275, 300, 275, s, c)
draw_line(275, 275, 270, 325, s, c)
draw_line(270, 325, 262, 305, s, c)
draw_line(238, 305, 262, 305, s, c)
draw_line(238, 305, 230, 325, s, c)
draw_line(230, 325, 225, 275, s, c)

draw_line(75, 250, 125, 300, s, c)
draw_line(125, 300, 175, 325, s, c)
draw_line(175, 325, 175, 300, s, c)
draw_line(175, 300, 200, 275, s, c)
draw_line(200, 275, 225, 275, s, c)

draw_line(425, 250, 400, 212, s, c)
draw_line(75, 250, 100, 212, s, c)

draw_line(400, 212, 350, 187, s, c)
draw_line(100, 212, 150, 187, s, c)

draw_line(350, 187, 325, 217, s, c)
draw_line(325, 217, 300, 192, s, c)

draw_line(300, 192, 282, 212, s, c)
draw_line(282, 212, 250, 175, s, c)

draw_line(250, 175, 218, 212, s, c)
draw_line(218, 212, 200, 192, s, c)

draw_line(200, 192, 175, 217, s, c)
draw_line(175, 217, 150, 187, s, c)

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
