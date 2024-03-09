def granddaugter(a, b, s):
    if "Марія" in a and "Володимир" in b:
        s.add(("Марія", "Володимир"))
    if "Валерія" in a and "Юрій" in b:
        s.add(("Валерія", "Юрій"))
    if "Вікторія" in a and "Юрій" in b:
        s.add(("Вікторія", "Юрій"))
    if "Анна" in a and "Іван" in b:
        s.add(("Анна", "Іван"))
    if "Анна" in a and "Олег" in b:
        s.add(("Анна", "Олег"))
    print(s)


def wife(a, b, r):
    if "Анастасія" in a and "Юрій" in b:
        r.add(("Анастасія", "Юрій"))
    if "Валерія" in a and "Олексій" in b:
        r.add(("Валерія", "Олексій"))
    if "Вікторія" in a and "Іван" in b:
        r.add(("Вікторія", "Іван"))
    print(r)


def association_action(r, s):
    a = r.union(s)
    return a


def peretun(r, s):
    a = r.intersection(s)
    return a


def riznutsya(r, s):
    a = r.difference(s)
    return a


def uni_riznutsya(u, r):
    a = u.difference(r)
    return a
