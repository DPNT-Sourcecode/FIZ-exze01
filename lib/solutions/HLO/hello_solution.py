

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if isinstance(friend_name,str):
        return "Hello, {friend_name}!".format(friend_name=friend_name)
    else:
        raise ValueError("give a name")





