def IBAN(number_of_iban):
    number_of_iban = str(number_of_iban).lower()
    list_of_number = list(number_of_iban)
    if len(number_of_iban) == 28:
        four_last_digits = list_of_number[4:] + list_of_number[0:4]
        four_last_digits[-4] = 25
        four_last_digits[-3] = 21
        num = int("".join(str(i) for i in four_last_digits))
        the_rest_of_number = num % 97
        if the_rest_of_number == 1:
            return True
        else:
            print(the_rest_of_number)
            return False
    else:
        return False
