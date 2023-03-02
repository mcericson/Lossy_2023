import rhinoscriptsyntax as rs



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
    return box



rs.EnableRedraw(False)

def vertical_plane(angle_of_rotation):
    """create a plane that is rotate 45 degress with respect to the x axis"""
    vert_plane = rs.WorldZXPlane()
    obl_plane = rs.RotatePlane(vert_plane, angle_of_rotation, (1,0,0))
    return obl_plane

#create a vector for projection
base_vector = (1,0,0)

#rotate the planes and vectors around the z axis a number times.
def radial_planes(plane, number, axis):
    planes = []
    step = int(360/number)
    for i in range(0, 360, step):
        rot_plane = rs.RotatePlane(plane, i, axis)
        planes.append(rot_plane)
    return planes

def radial_vectors(vector, number, axis):
    vectors = []
    step = int(360/number)
    for i in range(0, 360, step):
        vector = rs.VectorRotate(base_vector, i, axis)
        vectors.append(vector)
    return vectors

def add_circle_to_plane(radius, planes):
    circles = []
    for i in planes:
        circle = rs.AddCircle(i, radius)
        circles.append(circle)
    return circles

def radial_projection(angle, object, number, axis, radius):
    
    plane = vertical_plane(angle)
    base_vector = (0,0,1)
    planes = radial_planes(plane, number, axis)
    vectors = radial_vectors(base_vector, number, axis)
    circles = add_circle_to_plane(radius, planes)
    curves = []
    for i in range(len(circles)):
        curve = rs.ProjectCurveToSurface([circles[i]], [object], vectors[i])
        curves.append(curve)
    return curves, vectors
    
def main():
    #create a box to project onto
    #box = center_box((0,0,0), 100, 100, 100)

    base_1 = rs.RotatePlane((rs.WorldXYPlane()),180, (1,0,0))
    base_2 = rs.MovePlane(base_1, (0,0,150))
#    cone_1 = rs.AddCone(base_2, 200, 100)
#    cone_2 = rs.AddSphere(base_2, 300)
#    cone_3 = rs.AddTorus(base_2, 400, 100)
#    cone_4 = rs.AddCone(base_2, 500, 100)

    cone= rs.GetObjects()
    curves, vectors = radial_projection(60, cone, 10, (0,0,1), 50)
    point= rs.AddPoint(0,0,0)
    points = []
    for i in curves:
        point = rs.DivideCurve(i, 2, True)[0]
        points.append(point)
    for i in range(len(vectors)):
        point_mv = rs.MoveObject(points[i],vectors[i])
        path = rs.AddLine((0,0,0), point_mv)
        rs.ExtrudeCurve(curves[i], path)



main()


    
