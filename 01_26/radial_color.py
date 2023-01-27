import rhinoscriptsyntax as rs
import color_tools as ct
from math import sin
from math import cos
from math import radians

def circle_points(radius):
    points = []
    for i in range(0,360,10):
        angle = radians(i)
        x = cos(angle)* radius
        y = sin(angle)* radius
        point = rs.AddPoint(x,y)
        hue = i/255
        print(i)
        r, g, b = ct.hsv_to_rgb(hue, 1, 1)
        print (r, g, b)
        color = rs.CreateColor(r,g,b)
        rs.ObjectColor(point, color)
    return points, hue


circle_points(100)