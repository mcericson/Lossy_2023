#mark ericson
#10/3/2022
#This program generates geometry from images


from imp import reload
import rhinoscriptsyntax as rs
import System.Drawing.Bitmap as Bitmap

import color_tools as ct

reload(ct)




def assign_material_color(object, color):
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex(object)
    rs.MaterialColor(index, color)

def center_cube(center, radius):
    cx, cy, cz = center
    
    #lower 4 points
    p1 = (cx - radius, cy - radius, cz - radius)
    p2 = (cx + radius, cy - radius, cz - radius)
    p3 = (cx + radius, cy + radius, cz - radius)
    p4 = (cx - radius, cy + radius, cz - radius)
    
    #upper 4 points
    p5 = (cx - radius, cy - radius, cz + radius)
    p6 = (cx + radius, cy - radius, cz + radius)
    p7 = (cx + radius, cy + radius, cz + radius)
    p8 = (cx - radius, cy + radius, cz + radius)
    
    points = [p1, p2, p3, p4, p5, p6, p7, p8]
    
    cube = rs.AddBox(points)
    return(cube)
def center_box(center, width, length, height):
    cx, cy, cz = center
    
    #lower 4 points
    h = height/2
    w = width/2
    l = length/2
    p1 = (cx - w, cy - l, cz - h)
    p2 = (cx + w, cy - l, cz - h)
    p3 = (cx + w, cy + l, cz - h)
    p4 = (cx - w, cy + l, cz - h)
    
    #upper 4 points
    p5 = (cx - w, cy - l, cz + h)
    p6 = (cx + w, cy - l, cz + h)
    p7 = (cx + w, cy + l, cz + h)
    p8 = (cx - w, cy + l, cz + h)
    
    points = [p1, p2, p3, p4, p5, p6, p7, p8]
    
    box = rs.AddBox(points)
    return(box)

def image_to_cube(file_path, resolution):
    rs.EnableRedraw(False)
    img = Bitmap.FromFile(file_path)
    
    width = img.Width
    height = img.Height
    
    print (width, height)
    
    w_step = int(width/resolution)
    h_step = int(height/resolution)
    for i in range(0, width, w_step):
        x = i
        for j in range(0, height, h_step):
            y = j
            r, g, b, a = img.GetPixel(x, y)
            x2, y2, z2 = ct.radial_transform_pixel(r, g, b)
            location = (x2, y2, z2)
            cube = center_box(location, 5, 5, 5)
            color = rs.CreateColor(r, g, b, a)
            rs.ObjectColor(cube, color)
            assign_material_color(cube, color)

file_path  = "web_mountains_small.jpg"

image_to_cube(file_path, 100)