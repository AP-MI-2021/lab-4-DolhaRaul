def read_list():
    '''
    Subprogramul introduce intr o lista numerele introduse de utilizator, sepratae printr un spatiu(sun trimise in string)
    '''
    lst = []
    numere_sir = input("Introduceti numere aici: ")
    numere_sir_split = numere_sir.split(' ')
    for num in numere_sir_split:
        lst.append(float(num))
    return lst

def integer_list(lst):
    '''
    Functia returneaza partea intreaga a fiecarui numar din lista(float), toate puse intr o lista
    :param lst: O lista de float
    :return: O lista de int
    '''
    result = []
    for num in lst:
        result.append(int(num))
    return result

def test_integer_list():
    assert integer_list([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    assert integer_list([]) == []
    assert integer_list([1.5, -3, 8, 9.8]) == [1, -3, 8, 9]

def numbers_in_interval(lst, st, dr):
    '''
    Functia retunreaza toate numerele din lista care se afla in intervalul deschis (st, dr), numere de tip float
    :param lst: O lista de float
    :param st: Capatul din stanga al intervalului, introdus de utilizator
    :param dr: Capatul din dreapta al intervalului, introdus de utlizator
    :return: Numerele din lista ce se afla in st, dr
    '''
    result = []
    for num in lst:
        if num > st and num < dr:#apartine intervalului
            result.append(num)
    return result

def test_numbers_in_interval():
    assert numbers_in_interval([1.5, -3.3, 8, 9.8, 3.2], -4, 5) == [1.5, -3.3, 3.2]
    assert numbers_in_interval([-4, -3.3, 8, 9.8, 3.2], -4, 5) == [-3.3, 3.2]
    assert numbers_in_interval([-4, 5], -4, 5) == []
    assert numbers_in_interval([], -4, 5) == []

def main():
    lst = []
    while True:
        optiune = input("Introduceti optiunea dorita aici: ")
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            print(integer_list(lst))
        elif optiune == '3':
            st = int(input('Introduceti capatul din stanga al intervalului: '))
            dr = int(input('Introduceti capatul din dreapta al intervalului: '))
            print(numbers_in_interval(lst, st, dr))
        elif optiune == '4':
            pass
        elif optiune == '5':
           pass
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida")


if __name__ == '__main__':
    test_numbers_in_interval()
    test_integer_list()
    main()
