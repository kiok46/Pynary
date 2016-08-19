def number_to_binary(value):
    '''
    Convert number to binary for example:
        66: 01000010
    '''
    result = ''
    while value > 0:
        result = chr((value & 1) + 0x30) + result
        value = value >> 1
    return result


def convert_to_string(value):
    '''
    Convert binary to string for example:
    01000010 to B (i.e. 66)
    '''
    print_ascii = ''

    for abuse in value:
        abuse = list(abuse)
        abuse.reverse()
        temp = 0
        for i in range(len(abuse)):
            if abuse[i] == '1':
                temp = temp + 2**(i)

        print_ascii += chr(temp)

    return print_ascii


def convert_to_binary(value):
    '''
    Convert String to binary for example:
        B: 01000010
    '''
    print_string = ''

    for abuse in value:
        abuse = list(abuse)
        for i in range(len(abuse)):
            a = ord(abuse[i])
            print_string += number_to_binary(a) + '\n'
    return print_string
