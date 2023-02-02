import rhinoscriptsyntax as rs


object = rs.AddSphere((0,0,0), 50)
layer_name =  rs.AddLayer("Spheres")
rs.ObjectLayer(object, layer=layer_name)