# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if _check_type(x,int,[0,100]) and _check_typ(y,int,[0,100])
        return x + y

def _check_type(obj, type, range):
    if isinstance(obj,type) and (range[0] <= obj <= range[1]) :
        return True
    else:
        raise ValueError("The {obj} is not of type {type} or is not between {range}".format(obj=obj,type=type,range=range))



