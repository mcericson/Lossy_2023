from PIL import Image


def color_channel_modify(file_path, channel, scale_value):
    
    img = Image.open(file_path).convert('RGB')
    
    r, g, b = img.split()
    
    if channel == 'red':
        r = r.point(lambda i: i * scale_value)
    if channel == 'green':
        g = g.point(lambda i: i * scale_value)
    if channel == 'blue':
        b = b.point(lambda i: i * scale_value)
        
    
    
    
    with Image.open ("StudyCube_1.png") as im:
        px = im.load ()
        
    print(px[4,4])
    px[4,4] = (0,0,0)
    print (px[4,4])
    
  
    
#class PixelAccess:
#__setitem__(self, xy, color):
    

    result = Image.merge('RGB', (r, g, b))

    result.save('StudyCube_2_Thonny_blue.png')

color_channel_modify('StudyCube_1.png', 'blue', 10)
    
