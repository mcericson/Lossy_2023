
import rhinoscriptsyntax as rs

def funny_thing(radius, offset):
    s_1 = rs.AddSphere((0,0,0), radius)
    s_2 = rs.AddSphere((0,offset,0), radius)
    s_3 = rs.AddSphere((0,0,offset), radius)
    union_set = [s_1, s_2, s_3]
    funny_stuff = rs.BooleanUnion(union_set)
    centroid = rs.SurfaceVolumeCentroid(funny_stuff)[0]
    return funny_stuff, centroid



funny_thing(10,4)