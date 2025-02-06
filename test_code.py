from new_func import a,b, add_two_numbers,subtract_two_numbers,multiply_two_numbers,divide_two_numbers

#print(a,b,add_two_numbers(a,b),subtract_two_numbers(a,b),multiply_two_numbers(a,b),divide_two_numbers(a,b))

def test_a_functionality():
    a = 10
    b = 20

    assert add_two_numbers (a,b) == 30

def test_b_functionality():
    a,b = 10, 20

    assert subtract_two_numbers(a,b) == -10
    assert multiply_two_numbers(a,b) == 200
