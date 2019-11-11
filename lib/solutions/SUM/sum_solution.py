# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    """
    Function to caluclate two integers 
     arg: a (int): a positive integer between 0-100
     arg: b (int): a positive integer between 0-100
     returns (int): an Integer representing the sum of the two numbers
    """
    if _check_type(x,int,[0,100]) and _check_type(y,int,[0,100]):
        return x + y

def _check_type(obj, type, range):
    """
    Function to check the type of object and if the object is betwwen a range:
    obj (obj): the pobject to be checked
    type: the type of the object
    range: (list): the range (a list with 2 elements; min and max) of the which the number should be checked; eg: [0,1]

    """
    if isinstance(obj,type) and (range[0] <= obj <= range[1]) :
        return True
    else:
        raise ValueError("The {obj} is not of type {type} or is not between {range}".format(obj=obj,type=type,range=range))



