def granddaugter(a, b, s):
    relationships = {
        ("Марія", "Володимир"): ("Марія", "Володимир"),
        ("Валерія", "Юрій"): ("Валерія", "Юрій"),
        ("Вікторія", "Юрій"): ("Вікторія", "Юрій"),
        ("Анна", "Іван"): ("Анна", "Іван"),
        ("Анна", "Олег"): ("Анна", "Олег")
    }

    for condition, elements in relationships.items():
        if elements[0] in a and elements[1] in b:
            s.add(condition)

    print(s)


def wife(a, b, r):
    relationships = {
        ("Анастасія", "Юрій"): ("Анастасія", "Юрій"),
        ("Валерія", "Олексій"): ("Валерія", "Олексій"),
        ("Вікторія", "Іван"): ("Вікторія", "Іван")
    }

    for condition, elements in relationships.items():
        if elements[0] in a and elements[1] in b:
            r.add(condition)

    print(r)
