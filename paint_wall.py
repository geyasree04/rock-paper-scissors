import math
def cans(h,w,cover):
    ncans = (h*w)/cover
    result = math.ceil(ncans)
    return result


height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
coverage = 7
print(cans(height, width, coverage))