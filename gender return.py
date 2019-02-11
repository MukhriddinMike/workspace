'''
def gender_finder(sex='Unknown'):
    if sex is 'm':
        sex='Male'
    elif sex is 'f':
        sex='Female'
    print(sex)
gender_finder('m')
gender_finder('f')
gender_finder()
'''


def number_total(*argsf):
    total=0
    for a in argsf:
        total+=a
    print(total)


number_total(3)
number_total(3,9)