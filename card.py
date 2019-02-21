def credit_card_verification(number_of_credit_card):
    index = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9, ]
    number_of_credit_card = str(number_of_credit_card)
    if 9 <= len(number_of_credit_card) <= 19:
        try:
            first_part = sum(int(num) for num in number_of_credit_card [-1::-2])
            second_part = sum(index[int(num)] for num in number_of_credit_card[-2::-2])
            return (second_part + first_part) % 10 == 0
        except ValueError:
            return False
    else:
        return False
