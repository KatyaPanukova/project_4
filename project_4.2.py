print('Привет ,данная программа ничего полезного не несет,'
      'она создана ради развлечения.')
print('Мы предлагаем указать, чем бы вы хотели рисовать.')

list_1 = input()

print('Что бы вы хотели бы нарисовать для начала'
      ' введенным символом?')
print('- Человека \n- Квадрат \n- Без разницы')

answer = input()

if answer == 'Без разницы':

    ot = ' '
    list_1 *= 10
    kol = 1
    a = 1

    while a != 5 and kol != 5:

        if a == 1 and kol == 1:

            lis_1 = list_1[a] * 23
            print(ot, lis_1)
            a += 1
            kol += 1

        elif a == 2 and kol == 2:

            lis_1 = list_1[a]
            print(ot, lis_1, ot * 20, lis_1 * 10, '\t')
            a += 1
            kol += 1

        elif a == 3 and kol == 3:

            lis_1 = list_1[a]
            print(ot, lis_1, ot * 29, lis_1, '\t')
            a += 1
            kol += 1

        elif a == 4 and kol == 4:

            lis_1 = list_1[a]
            print(ot, lis_1, ot * 20, lis_1 * 10, '\t')
            a += 1
            kol += 1

    lis_1 = list_1[1] * 23
    a += 1
    kol +=1
    print(ot, lis_1)
    answer_2 = input('Хотели бы вы ,чтобы ваш рисунок ожил?\n')

elif answer == 'Человека':

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

    answer_2 = input('Хотели бы вы ,чтобы ваш рисунок ожил?\n')

elif answer == 'Квадрат':

    ot = ' '
    lis_1 = list_1[0]
    kol = 1
    b = 1
    a = 1

    while b != 6 and a != 6:

        lis_1 += list_1[0]
        a += 1
        b += 1

        if b == 6 and a == 6:

            for k in range(1, 4):

                print(ot * 5, lis_1)

    answer_2 = input('Хотели бы вы ,чтобы ваш рисунок ожил?\n')