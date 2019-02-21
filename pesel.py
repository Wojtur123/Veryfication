def pesel(number):
    months = {1: " January", 2: " February", 3: " March", 4: " April", 5: " May", 6: " June", 7: " July",
              8: " August", 9: " September", 10: " November", 11: " October", 12: " December"}
    if len(number) == 11:
        try:
            x = int(number)
            if x % 10 == ((9 * int(number[0]) + 7 * int(number[1]) + 3 * int(number[2]) + int(number[3]) + 9 * int(number[4]) +
                           7 * int(number[5]) + 3 * int(number[6]) + int(number[7]) + 9 * int(number[8]) + 7 * int(number[9])) % 10):

                day = 10 * int(number[2]) + int(number[3])

                if day < 13:
                    print(number[4] + number[5] + months[day] + " 19" + number[0] + number[1])

                elif day < 33:
                    day2 = day - 20
                    print(number[4] + number[5] + months[day2] + " 20" + number[0] + number[1])

                elif day < 53:
                    day2 = day - 40
                    print(number[4] + number[5] + months[day2] + " 21" + number[0] + number[1])

                elif day < 73:
                    day2 = day - 60
                    print(number[4] + number[5] + months[day2] + " 22" + number[0] + number[1])

                elif day < 93:
                    day2 = day - 80
                    print(number[4] + number[5] + months[day2] + " 18" + number[0] + number[1])
                return True

            else:
                return False
        except ValueError:
            return False

    else:
        return False
