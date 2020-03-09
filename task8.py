def choice_to_number(choice):
    place = {'Usain' : 1, 'Me': 2, 'Aybek': 3}
    return place.get(choice)
def number_to_choice(number):
    name = {3 : 'Aybek', 2 : 'Me', 1 : 'Usain'}
    return name.get(number)
"""Convert number to choice."""
# if number is 1 then return usain bolt.

#DO NOT remove lines below here, this is designed to test your code.
def test_choice_to_number():
    assert choice_to_number('Usain') == 1
    assert choice_to_number('Me') == 2
    assert choice_to_number('Aybek') == 3


def test_number_to_choice():
    assert number_to_choice(1) == 'Usain'
    assert number_to_choice(2) == 'Me'
    assert number_to_choice(3) == 'Aybek'


def test_all():
    try:
        test_choice_to_number()
        test_number_to_choice()
    except AssertionError:
        print('WRONG')
    else:
        print('SUCCESS')
#test your code by un-commenting the line(s) below
test_all()