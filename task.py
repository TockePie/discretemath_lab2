import functions
import os
from tkinter import *

from data import coord_dict1, coord_dict3, coord_dict2, coord_dict4, coord_dict5, coord_dict_w, coord_dict_gd, \
    womenlist, menlist, set_u


def second_window():
    def set_adder():
        selected_listbox = women_listbox if setnum.get() == 1 else men_listbox
        selected_set = set_a if setnum.get() == 1 else set_b
        print(selected_listbox.get(ANCHOR))
        selected_set.add(selected_listbox.get(ANCHOR))

    def save_set_to_file(set_to_save, file_name):
        with open(file_name, "w") as f:
            f.write("\n".join(set_to_save))

    def read_set_from_file(set_to_update, file_name):
        with open(file_name, "r") as f:
            set_to_update.clear()
            temp = f.read().strip().split("\n")
            set_to_update.update(temp)

            print(temp)
            print(set_to_update)

    def clear_set_and_file(set_to_clear, file_name):
        set_to_clear.clear()
        os.remove(file_name)

    root2 = Tk()
    root2.title("Вікно 2")
    root2.geometry("500x350")

    setnum = IntVar(root2)
    women_listbox = Listbox(root2)
    women_listbox.place(x=50, y=10)
    women_listbox.insert(END, *womenlist)
    men_listbox = Listbox(root2)
    men_listbox.place(x=300, y=10)
    men_listbox.insert(END, *menlist)

    Radiobutton(root2, text="Множина А", variable=setnum, value=1).place(x=60, y=180)
    Radiobutton(root2, text="Множина B", variable=setnum, value=2).place(x=320, y=180)
    Button(root2, width=8, text="Додати", font="Arial 10", command=set_adder).place(x=200, y=120)
    Button(root2, width=15, text="Зберегти А у файл", font="Arial 10",
           command=lambda: save_set_to_file(set_a, "Adata.txt")).place(x=0 + 50, y=240)
    Button(root2, width=15, text="Зберегти В у файл", font="Arial 10",
           command=lambda: save_set_to_file(set_b, "Bdata.txt")).place(x=0 + 50, y=270)
    Button(root2, width=10, text="Зчитати А", font="Arial 10",
           command=lambda: read_set_from_file(set_a, "Adata.txt")).place(x=140 + 50, y=240)
    Button(root2, width=10, text="Зчитати В", font="Arial 10",
           command=lambda: read_set_from_file(set_b, "Bdata.txt")).place(x=140 + 50, y=270)
    Button(root2, width=10, text="Очистити А", font="Arial 10",
           command=lambda: clear_set_and_file(set_a, "Adata.txt")).place(x=320, y=240)
    Button(root2, width=10, text="Очистити В", font="Arial 10",
           command=lambda: clear_set_and_file(set_b, "Bdata.txt")).place(x=320, y=270)


def third_window():
    def populate_listbox(listbox, some_set, x_position, y_position):
        listbox.place(x=x_position, y=y_position)
        for item in some_set:
            listbox.insert(END, item)

    root3 = Tk()
    root3.title("Вікно 3")
    root3.geometry("1000x500")

    canvas = Canvas(root3, bg="white", width=1000, height=500)
    canvas.place(x=0, y=0)

    functions.granddaugter(set_a, set_b, set_s)
    functions.wife(set_a, set_b, set_r)

    for i in set_r:
        if i in coord_dict_w:
            canvas.create_line(coord_dict_w[i], arrow="last")
    for i in set_s:
        if i in coord_dict_gd:
            canvas.create_line(coord_dict_gd[i], arrow="last")

    populate_listbox(Listbox(root3), set_a, 50, 100)
    populate_listbox(Listbox(root3), set_b, 200, 100)

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


def fourth_window():
    root4 = Tk()
    root4.title("Вікно 4")
    root4.geometry("1000x750")

    canvas = Canvas(root4, bg="white", width=1000, height=1000)
    canvas.place(x=0, y=0)

    for i in set_r.union(set_s):
        if i in coord_dict1:
            canvas.create_line(coord_dict1[i], arrow="last")
    for i in set_r.intersection(set_s):
        if i in coord_dict3:
            canvas.create_line(coord_dict3[i], arrow="last")
    for i in set_r.difference(set_s):
        if i in coord_dict2:
            canvas.create_line(coord_dict2[i], arrow="last")
    for i in set_u.difference(set_r):
        if i in coord_dict4:
            canvas.create_line(coord_dict4[i], arrow="last")
    for i in set_s:
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


group = 32
number_in_list = 16
variant = (number_in_list + group % 60) % 30 + 1

root = Tk()
root.title("Вікно 1")
root.geometry("500x200")

set_a, set_b, set_s, set_r = set(), set(), set(), set()

Label(root, text='Крадожон Максим Романович', font='Arial 14').place(x=110, y=10)
Label(root, text=f'Група {group}', font='Arial 12').place(x=10, y=160)
Label(root, text=f'Номер в списку: {number_in_list}', font='Arial 12').place(x=85, y=160)
Label(root, text=f'Варіант завдання: {variant}', font='Arial 12').place(x=330, y=160)

Button(root, width=8, text="Вікно 2", font="Arial 10", command=second_window).place(x=125, y=110)
Button(root, width=8, text="Вікно 3", font="Arial 10", command=third_window).place(x=205, y=110)
Button(root, width=8, text="Вікно 4", font="Arial 10", command=fourth_window).place(x=285, y=110)
root.mainloop()
