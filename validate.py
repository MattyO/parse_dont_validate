def is_odd(number):
    return bool(number % 2 )

def is_even(number):
    return not is_odd(number)

def is_between(number, compare_to_one, compare_to_two, ):
    larger = max(compare_to_one, compare_to_two)
    smaller  = min(compare_to_one, compare_to_two)
    return larger <= number <= smaller

def is_outside(number, compare_to_one, compare_to_two):
    return not is_between(number, compare_to_one, compare_to_two)
