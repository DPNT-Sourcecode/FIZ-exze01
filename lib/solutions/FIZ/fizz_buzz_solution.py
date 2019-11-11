# noinspection PyUnusedLocal
def fizz_buzz(number):
    if _check_multiple_of(number,3):
        return "fizz"
    elif _check_multiple_of(number,5):
        return 
    raise NotImplementedError()


def _check_multiple_of(n, k):
    if n % k == 0:
        return True


