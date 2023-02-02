import rhinoscriptsyntax as rs



def assign_material_color(object, color):
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex(object)
    rs.MaterialColor(index, color)

def grid(x_num, y_num):
    points = []
    for i in range(x_num):
        for j in range(y_num):
            x = i
            y = j
            point = (x,y)
            points.append(point)
    return points

def funny_thing(radius, offset):
    s_1 = rs.AddSphere((0,0,0), radius)
    s_2 = rs.AddSphere((0,offset,0), radius)
    s_3 = rs.AddSphere((0,0,offset), radius)
    union_set = [s_1, s_2, s_3]
    funny_stuff = rs.BooleanUnion(union_set)
    centroid = rs.SurfaceVolumeCentroid(funny_stuff)[0]
    return funny_stuff, centroid


def funny_grid(number):
    funny_object, center = funny_thing(1, .5)
    rs.AddBlock([funny_object], center, name="funny_thing", delete_input=True)
    
    points = grid(number, number)
    blocks = []
    for i in points:
        block = rs.InsertBlock("funny_thing", i, scale=(1, 1, i[0]), angle_degrees=i[0]*40)
        if block == None:
            pass
        else:
            blocks.append(block)
    rs.Command("ExplodeBlock ")
    
    objects = rs.GetObjects()
    
    for i in objects:
        assign_material_color(i, (255, 100, 255))

funny_grid(10)