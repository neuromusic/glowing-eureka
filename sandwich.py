
def sandwichify(any_string):
    if '_sandwich' in any_string:
        return any_string
    else:
        return '{}_sandwich'.format(any_string)
