import os
from tkinter import *
import functios


# Вікно 2
def second_window():
    def set_adder():
        a = setnum.get()
        print(a)
        if a == 1:
            print(f'Жінки: {women_listbox.get(ANCHOR)}')
            A.add(women_listbox.get(ANCHOR))
        else:
            print(f'Чоловіки: {men_listbox.get(ANCHOR)}')
            B.add(men_listbox.get(ANCHOR))

    def saver1():
        f = open(r"Adata.txt", "w")
        f.write(str(A))
        f.close()

    def saver2():
        f = open(r"Bdata.txt", "w")
        f.write(str(B))
        f.close()

    def reader1():
        f = open(r"Adata.txt", "r")
        A.clear()
        tempa = f.read()[1: -1].replace("\'", "").split(", ")
        A.update(tempa)
        f.close()
        print(tempa)
        print(A)

    def reader2():
        f = open(r"Bdata.txt", "r")
        B.clear()
        tempb = f.read()[1: -1].replace("\'", "").split(", ")
        B.update(tempb)
        f.close()
        print(tempb)
        print(B)

    def clear1():
        A.clear()
        os.remove(r"Adata.txt")

    def clear2():
        B.clear()
        os.remove(r"Bdata.txt")

    root2 = Tk()
    root2.title("Вікно 2")
    root2.geometry("1000x500")
    setnum = IntVar(root2)

    women_listbox = Listbox(root2)
    women_listbox.place(x=0)
    for i in womenlist:
        women_listbox.insert(END, i)
    men_listbox = Listbox(root2)
    men_listbox.place(x=200)
    for i in menlist:
        men_listbox.insert(END, i)

    Radiobutton(root2, text="Множина А", variable=setnum, value=1).place(x=0, y=170)
    Radiobutton(root2, text="Множина B", variable=setnum, value=2).place(x=100, y=170)
    Button(root2, width=8, text="Додати", font="Arial 10", command=set_adder).place(x=0, y=200)
    Button(root2, width=15, text="Зберегти А у файл", font="Arial 10", command=saver1).place(x=0, y=240)
    Button(root2, width=15, text="Зберегти В у файл", font="Arial 10", command=saver2).place(x=0, y=270)
    Button(root2, width=10, text="Зчитати А", font="Arial 10", command=reader1).place(x=140, y=240)
    Button(root2, width=10, text="Зчитати В", font="Arial 10", command=reader2).place(x=140, y=270)
    Button(root2, width=10, text="Очистити А", font="Arial 10", command=clear1).place(x=320, y=240)
    Button(root2, width=10, text="Очистити В", font="Arial 10", command=clear2).place(x=320, y=270)


# Вікно 3
def third_window():
    root3 = Tk()
    root3.title("Вікно 3")
    root3.geometry("1000x500")
    canvas = Canvas(root3, bg="white", width=1000, height=500)
    canvas.place(x=0, y=0)
    functios.granddaugter(A, B, S)
    functios.wife(A, B, R)
    coord_dict_gd = {('Марія', 'Володимир'): (705, 55, 705, 175),
                     ('Вікторія', 'Юрій'): (505, 55, 605, 175),
                     ('Анна', 'Іван'): (405, 55, 405, 175),
                     ('Анна', 'Олег'): (405, 55, 505, 175),
                     ('Валерія', 'Юрій'): (605, 55, 605, 175)}
    coord_dict_w = {('Валерія', 'Олексій'): (605, 305, 805, 425),
                    ('Анастасія', 'Юрій'): (805, 305, 605, 425),
                    ('Вікторія', 'Іван'): (505, 305, 405, 425)}
    for i in R:
        if i in coord_dict_w:
            canvas.create_line(coord_dict_w[i], arrow="last")
    for i in S:
        if i in coord_dict_gd:
            canvas.create_line(coord_dict_gd[i], arrow="last")
    A_listbox = Listbox(root3)
    A_listbox.place(x=0)
    for i in A:
        A_listbox.insert(END, i)
    B_listbox = Listbox(root3)
    B_listbox.place(x=200)
    for i in B:
        B_listbox.insert(END, i)
    Label(root3, text='A онука В', font='Arial 12').place(x=400)
    for i in range(len(womenlist)):
        Label(root3, text=womenlist[i], font='Arial 10').place(x=400 + i * 100, y=20)
        canvas.create_oval(400 + i * 100, 45, 410 + i * 100, 55, fill="black")
    for i in range(len(menlist)):
        Label(root3, text=menlist[i], font='Arial 10').place(x=400 + i * 100, y=190)
        canvas.create_oval(400 + i * 100, 175, 410 + i * 100, 185, fill="black")

    Label(root3, text='A дружина В', font='Arial 12').place(x=400, y=250)
    for i in range(len(womenlist)):
        Label(root3, text=womenlist[i], font='Arial 10').place(x=400 + i * 100, y=270)
        canvas.create_oval(400 + i * 100, 295, 410 + i * 100, 305, fill="black")
    for i in range(len(menlist)):
        Label(root3, text=menlist[i], font='Arial 10').place(x=400 + i * 100, y=440)
        canvas.create_oval(400 + i * 100, 425, 410 + i * 100, 435, fill="black")


# Вікно 4
def fourth_window():
    root4 = Tk()
    root4.title("Вікно 4")
    root4.geometry("1000x1000")
    canvas = Canvas(root4, bg="white", width=1000, height=1000)
    canvas.place(x=0, y=0)
    coord_dict1 = {('Валерія', 'Олексій'): (210, 55, 410, 175),
                   ('Анастасія', 'Юрій'): (410, 55, 210, 175),
                   ('Вікторія', 'Іван'): (110, 55, 10, 175),
                   ('Марія', 'Володимир'): (310, 55, 310, 175),
                   ('Вікторія', 'Юрій'): (110, 55, 210, 175),
                   ('Анна', 'Іван'): (10, 55, 10, 175),
                   ('Анна', 'Олег'): (10, 55, 110, 175),
                   ('Валерія', 'Юрій'): (210, 55, 210, 175)}
    coord_dict2 = {('Валерія', 'Олексій'): (710, 55, 910, 175),
                   ('Анастасія', 'Юрій'): (910, 55, 710, 175),
                   ('Вікторія', 'Іван'): (610, 55, 510, 175),
                   ('Марія', 'Володимир'): (810, 55, 810, 175),
                   ('Вікторія', 'Юрій'): (610, 55, 710, 175),
                   ('Анна', 'Іван'): (510, 55, 510, 175),
                   ('Анна', 'Олег'): (510, 55, 610, 175),
                   ('Валерія', 'Юрій'): (710, 55, 710, 175)}
    coord_dict3 = {('Валерія', 'Олексій'): (205, 305, 405, 425),
                   ('Анастасія', 'Юрій'): (405, 305, 205, 425),
                   ('Вікторія', 'Іван'): (105, 305, 5, 425),
                   ('Марія', 'Володимир'): (305, 305, 305, 425),
                   ('Вікторія', 'Юрій'): (105, 305, 205, 425),
                   ('Анна', 'Іван'): (5, 305, 5, 425),
                   ('Анна', 'Олег'): (5, 305, 105, 425),
                   ('Валерія', 'Юрій'): (205, 305, 205, 425)}
    coord_dict4 = {('Валерія', 'Олексій'): (710, 305, 910, 425),
                   ('Анастасія', 'Юрій'): (910, 305, 710, 425),
                   ('Вікторія', 'Іван'): (610, 305, 510, 425),
                   ('Марія', 'Володимир'): (810, 305, 810, 425),
                   ('Вікторія', 'Юрій'): (610, 305, 710, 425),
                   ('Анна', 'Іван'): (510, 305, 510, 425),
                   ('Анна', 'Олег'): (510, 305, 610, 425),
                   ('Валерія', 'Юрій'): (710, 305, 710, 425)}
    coord_dict5 = {('Валерія', 'Олексій'): (210, 555, 410, 675),
                   ('Анастасія', 'Юрій'): (410, 555, 210, 675),
                   ('Вікторія', 'Іван'): (110, 555, 10, 675),
                   ('Марія', 'Володимир'): (310, 555, 310, 675),
                   ('Вікторія', 'Юрій'): (110, 555, 210, 675),
                   ('Анна', 'Іван'): (10, 555, 10, 675),
                   ('Анна', 'Олег'): (10, 555, 110, 675),
                   ('Валерія', 'Юрій'): (210, 555, 210, 675)}
    RS_uni = functios.association_action(R, S)
    RS_pere = functios.peretun(R, S)
    RS_riz = functios.riznutsya(R, S)
    UR_riz = functios.uni_riznutsya(U, R)
    for i in RS_uni:
        if i in coord_dict1:
            canvas.create_line(coord_dict1[i], arrow="last")
    for i in RS_pere:
        if i in coord_dict3:
            canvas.create_line(coord_dict3[i], arrow="last")
    for i in RS_riz:
        if i in coord_dict2:
            canvas.create_line(coord_dict2[i], arrow="last")
    for i in UR_riz:
        if i in coord_dict4:
            canvas.create_line(coord_dict4[i], arrow="last")
    for i in S:
        if i in coord_dict5:
            canvas.create_line(coord_dict5[i], arrow="first")
    Label(root4, text='R ∪ S', font='Arial 12').place(x=0)
    for i in range(len(womenlist)):
        Label(root4, text=womenlist[i], font='Arial 10').place(x=0 + i * 100, y=20)
        canvas.create_oval(5 + i * 100, 45, 15 + i * 100, 55, fill="black")
    for i in range(len(menlist)):
        Label(root4, text=menlist[i], font='Arial 10').place(x=0 + i * 100, y=190)
        canvas.create_oval(5 + i * 100, 175, 15 + i * 100, 185, fill="black")
    Label(root4, text='R ∩ S', font='Arial 12').place(x=0, y=250)
    for i in range(len(womenlist)):
        Label(root4, text=womenlist[i], font='Arial 10').place(x=0 + i * 100, y=270)
        canvas.create_oval(5 + i * 100, 295, 15 + i * 100, 305, fill="black")
    for i in range(len(menlist)):
        Label(root4, text=menlist[i], font='Arial 10').place(x=0 + i * 100, y=440)
        canvas.create_oval(5 + i * 100, 425, 15 + i * 100, 435, fill="black")
    Label(root4, text='R\S', font='Arial 12').place(x=500)
    for i in range(len(womenlist)):
        Label(root4, text=womenlist[i], font='Arial 10').place(x=500 + i * 100, y=20)
        canvas.create_oval(505 + i * 100, 45, 515 + i * 100, 55, fill="black")
    for i in range(len(menlist)):
        Label(root4, text=menlist[i], font='Arial 10').place(x=500 + i * 100, y=190)
        canvas.create_oval(505 + i * 100, 175, 515 + i * 100, 185, fill="black")
    Label(root4, text='U\R', font='Arial 12').place(x=500, y=250)
    for i in range(len(womenlist)):
        Label(root4, text=womenlist[i], font='Arial 10').place(x=500 + i * 100, y=270)
        canvas.create_oval(505 + i * 100, 295, 515 + i * 100, 305, fill="black")
    for i in range(len(menlist)):
        Label(root4, text=menlist[i], font='Arial 10').place(x=500 + i * 100, y=440)
        canvas.create_oval(505 + i * 100, 425, 515 + i * 100, 435, fill="black")
    Label(root4, text='S^-1', font='Arial 12').place(x=0, y=500)
    for i in range(len(womenlist)):
        Label(root4, text=womenlist[i], font='Arial 10').place(x=0 + i * 100, y=520)
        canvas.create_oval(5 + i * 100, 545, 15 + i * 100, 555, fill="black")
    for i in range(len(menlist)):
        Label(root4, text=menlist[i], font='Arial 10').place(x=0 + i * 100, y=690)
        canvas.create_oval(5 + i * 100, 675, 15 + i * 100, 685, fill="black")


# Вікно 1
G = 21
N = 27
L = (N + G % 60) % 30 + 1
root = Tk()
root.title("Вікно 1")
root.geometry("500x200")
Label(root, text='Тишнюк Іван Олегович', font='Arial 14').place(x=0)
Label(root, text=f'Група {G}', font='Arial 12').place(x=0, y=24)
Label(root, text=f'Номер в списку: {N}', font='Arial 12').place(x=75, y=24)
Label(root, text=f'Варіант завдання: {L}', font='Arial 12').place(x=0, y=46)
A = set()
B = set()
S = set()
R = set()
U = {('Анастасія', 'Юрій'),
     ('Валерія', 'Олексій'),
     ('Вікторія', 'Іван'),
     ('Анна', 'Олег'),
     ('Вікторія', 'Юрій'),
     ('Валерія', 'Юрій'),
     ('Марія', 'Володимир'),
     ('Анна', 'Іван'),
     ('Катерина', 'Микита')}
womenlist = ["Анна", "Вікторія", "Валерія", "Марія", "Анастасія"]
menlist = ["Іван", "Олег", "Юрій", "Володимир", "Олексій"]

Button(root, width=8, text="Вікно 2", font="Arial 10", command=second_window).place(x=5, y=100)
Button(root, width=8, text="Вікно 3", font="Arial 10", command=third_window).place(x=85, y=100)
Button(root, width=8, text="Вікно 4", font="Arial 10", command=fourth_window).place(x=165, y=100)
root.mainloop()
