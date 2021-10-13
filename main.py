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


def integer_number(n):
    '''
    Subprogramul verifica daca un numar n este intreg sau nu
    :param n:un numar natural n
    :return: True daca este intreg sau False in caz contrar
    '''
    if n == int(n):
        return True
    return False


def show_integers(lst):
    '''
    Functia returneaza toate numere intregi dintr o lista data
    :param lst: o lista de numere(de tip float)
    :return: o lista de numere intregi
    '''
    result = []
    for num in lst:
        if integer_number(num) == True:
            result.append(int(num))
    return result


def test_show_integers():
    assert show_integers([2.3, 2.0, 4.0, 5.6, 5.7333]) == [2.0, 4.0]
    assert show_integers([2.0, 2.0, 4.0, 5.6, 5.7333]) == [2.0, 2.0, 4.0]
    assert show_integers([2.3, 5.6, 5.7333]) == []
    assert show_integers([2.3, 2.0, 5.6, 5.7333]) == [2.0]


def show_biggest_number_divided_by_n(lst, n):
    '''
    Functia retunreaza cel mai mare numar(intreg si pozitiv) divizibil cu un numar introdus de utilizator(n)
    :param lst: o lista de float uri
    :param n: un numar natural n
    :return: cel mai mare numar intreg din lista lst divizibil cu n
    '''
    result = -1
    gasit = False
    for num in lst:
        if integer_number(num) and num > 0:
            if num % n == 0:
                if gasit == False:  # este primul nr gasit
                    gasit = True
                    result = num
                elif result < num:
                    result = num
    return result

def test_show_biggest_number_divided_by_n():
    assert show_biggest_number_divided_by_n([1, 2, 5.333, 8], 4) == 8
    assert show_biggest_number_divided_by_n([1, 2, 5.333], 4) == -1
    assert show_biggest_number_divided_by_n([1, 2, 5.333, 8, 12], 4) == 12
    assert show_biggest_number_divided_by_n([1, 2, 5.333, 8.0], 4) == 8


def show_all_fractionary_palindromes(lst):
    '''
    Functia retunreaza toate numerele fractionare din lista cu proprietatea ca partea lor fractionara este palindrom
    :param lst: o lista de numere de tip float
    :return: toate numere cu proprietatea ceruta
    '''
    result = []
    for num in lst:
        if integer_number(num) == False:#nu este intreg
            num = str(num)
            value = num.split('.')[1]
            if value == value[::-1]:#este palindrom
                result.append(float(num))
    return result

def test_show_all_fractionary_palindromes():
    assert show_all_fractionary_palindromes([1, 2, 2.11, 2.121]) == [2.11, 2.121]
    assert show_all_fractionary_palindromes([1, 2, 2.11]) == [2.11]
    assert show_all_fractionary_palindromes([1, 2]) == []
    assert show_all_fractionary_palindromes([]) == []

def is_prime(n):
    '''
    Functia verifica daca un numar este prim sau nu
    :param n: un numar natural n
    :return: True daca este prim sau False in caz contrar
    '''
    if n < 2: return False
    if n == 2: return True
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(5) == True
    assert is_prime(17) == True
    assert is_prime(17*19) == False

def show_sqrt_numbers_is_prime(lst):
    '''
    Afiseaza toate numerele din lista(ca stringuri, cu caractrele in ordine inversa) care au propietatea ca sqrt(numar) e prim
    :param lst: O lista de numere introduse de utilizator
    :return: O lista de numere(stringuri, cu caracterele in ordine inversa de cea initiala) cu prorpietatea ceriuta
    '''
    result = []
    for num in lst:
        radique = int(num ** 0.5)
        if is_prime(radique) == True:#resp propr
            num = str(num)[::-1]#bagam cu caracterele in ordine inversa
            result.append(num)
        else:
            result.append((num))
    return result

def test_show_sqrt_numbers_is_prime():
    assert show_sqrt_numbers_is_prime([10.0, 100.0, 12.45, 50.0, 101.2]) == ['0.01', 100.0, '54.21', '0.05', 101.2]
    assert show_sqrt_numbers_is_prime([100.0, 12.45, 50.0, 101.2]) == [100.0, '54.21', '0.05', 101.2]
    assert show_sqrt_numbers_is_prime([100.0, 101.2]) == [100.0, 101.2]
    assert show_sqrt_numbers_is_prime([]) == []

def main():
    lst = []
    while True:
        optiune = input("Introduceti optiunea dorita aici: ")
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            print(show_integers(lst))
        elif optiune == '3':
            n = int(input("Introduceti numarul aici: "))
            print(show_biggest_number_divided_by_n(lst, n))
        elif optiune == '4':
            print(f'Toate numerele fractionare din lista {lst} care respecta proprietatea sunt {show_all_fractionary_palindromes(lst)}')
        elif optiune == '5':
            print(f'Numere cu proprietatea ceruta din {lst} sunt {show_sqrt_numbers_is_prime(lst)}')
        elif optiune == 'x':
            break
        else:
            print("Optiune imvalida")


if __name__ == '__main__':
    test_show_sqrt_numbers_is_prime()
    test_is_prime()
    test_show_all_fractionary_palindromes()
    test_show_biggest_number_divided_by_n()
    test_show_integers()
    main()
