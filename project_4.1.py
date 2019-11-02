import local as lc
import string
import time

print(lc.TXT_1)
print(lc.TXT_2)

list_1 = input()

print(lc.TXT_3)
print(lc.TXT_5)
print(lc.TXT_4)

result = lc.TXT_7
answer_2 = input(lc.TXT_6,)

for garb in string.punctuation:
    answer_2 = answer_2.replace(garb, '')

if answer_2 != lc.TXT_7:

    x = 0

    for num in range(4, 1, -1):

        if answer_2 != lc.TXT_7:

            print(lc.TXT_9, num - 1)
            print(lc.TXT_17, result[x])
            answer_2 = input(lc.TXT_6,)

            for garb in string.punctuation:

                answer_2 = answer_2.replace(garb, '')

        elif answer_2 == lc.TXT_7:
            ot = ' '
            b = 1
            a = 1
            lis_1 = ''
            k = 1

            while b != 6 and a != 6:

                lis_1 += list_1[0]
                a += 1
                b += 1

                if b == 6 and a == 6:

                    for k in range(1, 4):
                        print(ot * 5, lis_1)

            for i in range(1, 3):
                print(ot * 7, lis_1[0])

            while b != 7 and a != 7:

                lis_1 += list_1[0]
                a += 1
                b += 1

                if b == 7 and a == 7:

                    for k in range(1, 6):

                        if k == 1:

                            print(ot * 2, lis_1 * 2)

                        elif k >= 2 or k <= 4:

                            print(ot, list_1[0], ot, lis_1, ot, list_1[0])

            for i in range(1, 5):

                print(ot * 5, lis_1[0], ot * 2, lis_1[0])
            print()
            for seconds in range(3):
                if seconds == 0:
                    print(lc.TXT_8)
                elif seconds == 1:
                    print(lc.TXT_20)
                elif seconds == 2:
                    print(lc.TXT_19)
                time.sleep(1)

            break
        x += 1

    else:
        print(lc.TXT_10)

        answer_3 = input()

        if answer_3 == lc.TXT_11:

            ot = ' '
            b = 1
            a = 1
            lis_1 = ''
            k = 1

            while b != 6 and a != 6:

                lis_1 += list_1[0]
                a += 1
                b += 1

                if b == 6 and a == 6:

                    for k in range(1, 4):
                        print(ot * 5, lis_1)

            for i in range(1, 3):
                print(ot * 7, lis_1[0])

            while b != 7 and a != 7:

                lis_1 += list_1[0]
                a += 1
                b += 1

                if b == 7 and a == 7:

                    for k in range(1, 6):

                        if k == 1:

                            print(ot * 2, lis_1 * 2)

                        elif k >= 2 or k <= 4:

                            print(ot, list_1[0], ot, lis_1, ot, list_1[0])

            for i in range(1, 5):
                print(ot * 5, lis_1[0], ot * 2, lis_1[0])
            print()
            print(lc.TXT_12)
        else:
            print()
            print(lc.TXT_13)

elif answer_2 == lc.TXT_7:

    ot = ' '
    b = 1
    a = 1
    lis_1 = ''
    k = 1

    while b != 6 and a != 6:

        lis_1 += list_1[0]
        a += 1
        b += 1

        if b == 6 and a == 6:

            for k in range(1, 4):

                print(ot * 5, lis_1)

    for i in range(1, 3):

        print(ot * 7, lis_1[0])

    while b != 7 and a != 7:

        lis_1 += list_1[0]
        a += 1
        b += 1

        if b == 7 and a == 7:

            for k in range(1, 6):

                if k == 1:

                    print(ot * 2, lis_1 * 2)

                elif k >= 2 or k <= 4:

                    print(ot, list_1[0], ot, lis_1, ot, list_1[0])

    for i in range(1, 5):

        print(ot * 5, lis_1[0], ot * 2, lis_1[0])

    for seconds in range(3):
        if seconds == 0:
            print(lc.TXT_8)
        elif seconds == 1:
            print(lc.TXT_20)
        elif seconds == 2:
            print(lc.TXT_19)
        time.sleep(1)