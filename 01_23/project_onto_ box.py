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
    return(box)



rs.EnableRedraw(False)

#create a plane that is rotate 45 degress with respect to the x axis
vert_plane = rs.WorldZXPlane()
obl_plane = rs.RotatePlane(vert_plane, 45, (1,0,0))

#create a vector for projection
base_vector = (1,0,0)

#rotate the planes and vectors around the z axis a number times.
planes = []
vectors = []
for i in range(0,360,10):
    rot_plane = rs.RotatePlane(obl_plane, i, (0,0,1))
    vector = rs.VectorRotate(base_vector, i, (0,0,1))
    vectors.append(vector)
    planes.append(rot_plane)

#create circles one each of the planes
circles = []
for i in planes:
    circle = rs.AddCircle(i, 50)
    circles.append(circle)
    
#create a box to project onto
box = center_box((0,0,0), 100, 100, 100)

#project the circles onto the box 
curves = []
for i in range(len(circles)):
    curve = rs.ProjectCurveToSurface([circles[i]], [box], vectors[i])
    curves.append(curve)

    
