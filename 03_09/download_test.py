
import Rhino

import urllib

import rhinoscriptsyntax as rs

import System.Drawing.Bitmap as Bitmap
#url = urllib.urlopen('https://github.com/mcericson/Lossy_2023/blob/main/01_26/web_mountains_small.jpg')

import urllib
import shutil


url = 'https://th.bing.com/th/id/R.cb40a975df8613d46877ba64581ac0d1?rik=7si7Jndem7EV7w&riu=http%3a%2f%2fwallpapercave.com%2fwp%2f33vtxnj.jpg&ehk=YyEzwqk%2bAweaRJ6QGEjPRIIUIZ%2fVAz75FSwN4CHJedk%3d&risl=&pid=ImgRaw&r=0'
file_path = "test.jpg"
urllib.urlretrieve(url, file_path)



def image_to_circle(file_path, resolution):
    rs.EnableRedraw(False)
    img = Bitmap.FromFile(file_path)
    #get image width from img object
    width = img.Width
    height = img.Height
    #create a step based on resolution and convert to integer
    #so it will work in the range function
    w_step = int(width/resolution)
    h_step = int(height/resolution)
    
    
    print (width, height)
    
    #create a loop for a 2d grid that covers the dimensions of the image.
    for i in range(0, width, w_step):
        x = i
        for j in range(0, height, h_step):
            y = j
            #get the r,g, b, a values from the img object
            r, g, b, a = img.GetPixel(x,y)
            location = (x, y, r/5)
            circle = rs.AddCircle(location, 10)
            color = rs.CreateColor(r, g, b, a)
            rs.ObjectColor(circle, color)

image_to_circle(file_path, 100)