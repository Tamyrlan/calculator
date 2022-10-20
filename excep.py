def get_value():
    value = input('Enter number here:')
    try:
        value = float(value)
        return value
    except ValueError:
        print('It is not a nuber, please try again :-(')
        return get_value()

