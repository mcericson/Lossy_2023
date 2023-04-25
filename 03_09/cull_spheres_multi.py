
import rhinoscriptsyntax as rs
import random
import Rhino



def cubic_grid(x_num, y_num, z_num, space):
    points = []
    for i in range(0, int(x_num*space), int(space)):
        x = i
        for j in range(0, int(y_num*space), int(space)):
            y = j
            for p in range(0, int(z_num*space), int(space)):
                z = p
                point = (x,y,z)
                points.append(point)
    return points 

def random_spheres(points, radius, number):
    spheres = []
    for i in range(number):
        max = len(points) - 1
        index = random.randint(0,max)
        sphere = rs.AddSphere(points[index], radius)
        spheres.append(sphere)
    return spheres

def cull_with_breps(points, breps):
    new_points = []
    for i in points:
        point = rs.AddPoint(i)
        new_points.append(point)
        new_point = rs.coerce3dpoint(point)
        for brep in breps:
            brep_object = rs.coercebrep(brep)
            if brep_object.IsPointInside(new_point, .01, True) == True:
                rs.DeleteObject(point)
    return(new_points)

def center_cube(center, radius):
    #confirm that a point exist and is valid and get its coordinates
    check_point = rs.coerce3dpoint(center)
    if check_point:
        if check_point.IsValid:
            cx, cy, cz = rs.PointCoordinates(center)
    
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


def main():
    rs.EnableRedraw(False)
    points = cubic_grid(10,10,10,4)
    spheres = random_spheres(points,10, 10)
    new_points = cull_with_breps(points, spheres)
    for i in new_points:
        center_cube(i, 2)
    
    rs.DeleteObjects(spheres)

main()