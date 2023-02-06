#mark ericson
#RGB cube 10/26/22

import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino
import System
from imp import reload

#user libraries
import color_tools as ct

reload(ct)


def save_obj(Objects,FileName,NewFolder):


    #This function exports an obj file of whatever geometry is placed in to the objects position.
    #Mark Ericson 3.19.21

    rs.SelectObjects(Objects)
    
    folder = System.Environment.SpecialFolder.Desktop
    path = System.Environment.GetFolderPath(folder)
    #convert foldername and file name sto string
    FName = str(NewFolder)
    File = str(FileName)
    #combine foldername and desktop path
    Dir = System.IO.Path.Combine(path,FName)
    NFolder = System.IO.Directory.CreateDirectory(Dir)
    Dir = System.IO.Path.Combine(Dir,FileName +".obj")
    cmd = "_-Export " + Dir + " _Enter PolygonDensity=1 _Enter"
    rs.Command(cmd)

def cubic_grid(x_num, y_num, z_num, space):
    points = []
    for i in range(0, x_num, space):
        x = i
        for j in range(0, y_num, space):
            y = j
            for p in range(0, z_num, space):
                z = p
                point = (x,y,z)
                points.append(point)
    return points
    
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

def funny_thing(radius, offset):
    s_1 = rs.AddSphere((0,0,0), radius)
    s_2 = rs.AddSphere((0,offset,0), radius)
    s_3 = rs.AddSphere((0,0,offset), radius)
    union_set = [s_1, s_2, s_3]
    funny_stuff = rs.BooleanUnion(union_set)
    centroid = rs.SurfaceVolumeCentroid(funny_stuff)[0]
    return funny_stuff, centroid

def rgb_cube(x_num, y_num, z_num, space, brep):
    points = cubic_grid(x_num, y_num, z_num, space)
    brep_object = rs.coercebrep(brep)
    for i in points:
        point = rs.AddPoint(i)
        new_point = rs.coerce3dpoint(point)
        if brep_object.IsPointInside(new_point, 0.1, True) == False:
            cube = center_cube(i, float(space/2.0))

def main():
    rs.EnableRedraw(False)
    cube_dim = rs.GetInteger("Please provide a dimension for the cube", minimum=4, maximum=20)
    brep = funny_thing(cube_dim/2, cube_dim/8)[0]
    rgb_cube(cube_dim, cube_dim, cube_dim, 1, brep)

main()