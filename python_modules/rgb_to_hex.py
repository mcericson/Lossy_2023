def rgb_to_hex(r,g,b):
    hex_color = '%02x%02x%02x' % (r, g, b)
    return hex_color
    

new_color = rgb_to_hex(191,63,255)

print (new_color)