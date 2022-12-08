import math



def area(length, width):
    return  length * width
def per(length, width):
    return 2*(length + width)


def check_shape(length, width):
    area = length*width
    shape = ""
    if length**2 or width**2 == area:
        shape = "the shape is square"
    else:
        shape = "the shape is a rectangle"

    return shape
    # if length == width:
    #     shape ="the shape is square"
    # else:
    #     shape = "the shape is a rectangle"

#
# def check():
#
#     shape = ""
#     if math.sqrt(area) == length or width:
#         return shape = "the shape is a square"
#
#     else:
#         return shape = "the is a rectangle"
length = 12
width = 12
print(area(length,width), per(length,width))
print(check_shape(length, width))