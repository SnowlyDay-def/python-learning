magic = []

while True:
    spell = input("Какое заклинание выучить? (или напиши 'выход'):")

    if spell == "выход":
        print("Вы закрыли книгу заклинаний")
        break
    if spell == "забыть":
        delete = input("Какое заклинание препочитаете забыть?")
        if delete in magic:
            magic.remove(delete)
            print(f"(Заклинание {delete} успешно забыто!")
    else:
        print("У тебя нет данного заклинания!")


    if spell == "fire ball":
        magic.append(spell)
        print("Вы изучилии заклинание fire ball!!!")
    elif spell == "water ball":
        magic.append(spell)
        print("Вы изучили заклинание water ball!!!")
    elif spell == "wind ball":
        magic.append(spell)
        print("Вы изучили заклинание wind ball!!!")
    else:
        print("Недостаточно опыта для изучения заклинания")

    print("Ваши изученные заклинания:")
    for spell_name in magic:
        print("-", spell_name)
