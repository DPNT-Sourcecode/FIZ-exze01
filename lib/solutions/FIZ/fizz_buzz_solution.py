# noinspection PyUnusedLocal
def fizz_buzz(number):
    if not (1 <= number <= 9999):
        raise ValueError("NUmber not between 1 and 9999")
    if number > 10 and len(set(str(number))) == 1 and (_check_multiple_of(number,3) or ('3' in str(number))) and (_check_multiple_of(number,5) or ('5' in str(number))) :
        if _check_multiple_of(number,2):
            return  "fizz buzz deluxe" 
        else:
            return "fizz buzz fake deluxe"  
    elif (_check_multiple_of(number,3) or ('3' in str(number))) and (_check_multiple_of(number,5) or ('5' in str(number))):
        return  "fizz buzz" 
    elif number > 10 and len(set(str(number))) == 1  and ( _check_multiple_of(number,3) or ('3' in str(number))):
        if _check_multiple_of(number,2):
            return  "fizz deluxe"
        else:
            return "fizz fake deluxe"
    elif number > 10 and len(set(str(number))) == 1  and ( _check_multiple_of(number,5) or ('5' in str(number))):
        if _check_multiple_of(number,2):
            return  "buzz deluxe"
        else:
            return  "buzz fake deluxe"
    elif number > 10 and len(set(str(number))) == 1:
        if _check_multiple_of(number,2): 
            return "deluxe"
        else:
            return "fake deluxe"   
    elif _check_multiple_of(number,3) or ('3' in str(number)):
        return "fizz"
    elif _check_multiple_of(number,5) or ('5' in str(number)):
        return "buzz"
    else:
        return number
   

def _check_multiple_of(n, k):
    if n % k == 0:
        return True
