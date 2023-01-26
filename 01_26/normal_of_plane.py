import rhinoscriptsyntax as rs
import Rhino

plane = rs.WorldZXPlane()

vector = plane.Normal

print(vector)

