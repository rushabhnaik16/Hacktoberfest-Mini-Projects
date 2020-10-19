from tkinter import *
from tkinter import ttk


def main():
    notebook.add(frame1, text="One")
    notebook.add(frame2, text="Two")
    notebook.add(frame3, text="Three")
    notebook.add(frame4, text="Four")
    notebook.add(frame5, text="Five")
    notebook.add(frame6, text="Six")
    notebook.add(frame7, text="Seven")
    notebook.add(frame8, text="Eight")
    notebook.add(frame9, text="Nine")
    notebook.add(frame10, text="Ten")

    Label(frame1, text="Who has most Ballon D'or in football history?").grid(row=2, column=2)
    Button(frame1, text="Lionel Messi", command=correct1).grid(row=3, column=1)
    Button(frame1, text="Sadio Mane", command=incorrect1).grid(row=3, column=2)
    Button(frame1, text="Cristiano Ronaldo", command=incorrect1).grid(row=3, column=3)

    Label(frame2, text="When did India won it's first Cricket World Cup?").grid(row=2, column=2)
    Button(frame2, text="2011", command=incorrect2).grid(row=3, column=1)
    Button(frame2, text="1983", command=correct2).grid(row=3, column=2)
    Button(frame2, text="2007", command=incorrect2).grid(row=3, column=3)

    Label(frame3, text="Amazon Forest is located in which Continent?").grid(row=2, column=2)
    Button(frame3, text="Asia", command=incorrect3).grid(row=3, column=1)
    Button(frame3, text="Africa", command=correct3).grid(row=3, column=2)
    Button(frame3, text="Europe", command=incorrect3).grid(row=3, column=3)

    Label(frame4, text="In which year was Google founded?").grid(row=2, column=2)
    Button(frame4, text="2001", command=incorrect4).grid(row=3, column=1)
    Button(frame4, text="1998", command=correct4).grid(row=3, column=2)
    Button(frame4, text="1996", command=incorrect4).grid(row=3, column=3)

    Label(frame5, text="J2ee stands for").grid(row=2, column=2)
    Button(frame5, text="Java 2 enterprises edition", command=correct5).grid(row=3, column=1)
    Button(frame5, text="Java 2 elite edition", command=incorrect5).grid(row=3, column=2)
    Button(frame5, text="Java 2 entertainment edition", command=incorrect5).grid(row=3, column=3)

    Label(frame6, text="When did second world war ended?").grid(row=2, column=2)
    Button(frame6, text="1945", command=correct6).grid(row=3, column=1)
    Button(frame6, text="1923", command=incorrect6).grid(row=3, column=2)
    Button(frame6, text="1939", command=incorrect6).grid(row=3, column=3)

    Label(frame7, text="The first President of India was?").grid(row=2, column=2)
    Button(frame7, text="Rajendra Prasad", command=correct7).grid(row=3, column=1)
    Button(frame7, text="Mahatma Gandhi", command=incorrect7).grid(row=3, column=2)
    Button(frame7, text="Bhagat Singh", command=incorrect7).grid(row=3, column=3)

    Label(frame8,text="Who discovered first medical thermometer?").grid(row=2, column=2)
    Button(frame8, text="Sir Thomas Allbut", command=correct8).grid(row=3, column=1)
    Button(frame8, text="Sir Thomas Edison", command=incorrect8).grid(row=3, column=2)
    Button(frame8, text="Sir Isaac Newton", command=incorrect8).grid(row=3, column=3)

    Label(frame9, text="Where is Kohinoor diamond currently?").grid(row=2,column=2)
    Button(frame9, text="India", command=incorrect9).grid(row=3, column=1)
    Button(frame9, text="United Kingdom", command=correct9).grid(row=3, column=2)
    Button(frame9, text="France", command=incorrect9).grid(row=3, column=3)

    Label(frame10, text="Who is the Captain of Indian Cricket team?").grid(row=2, column=2)
    Button(frame10, text="Rohit Sharma", command=incorrect10).grid(row=3, column=1)
    Button(frame10, text="M.S.Dhoni", command=incorrect10).grid(row=3, column=2)
    Button(frame10, text="Virat Kohli", command=correct10).grid(row=3, column=3)

    notebook.pack()

    Label(root, text="Total:").pack()
    Label(root, textvariable=total).pack()


def correct1():
    Label(frame1, text="Correct").grid(row=1, column=2)
    counter()


def incorrect1():
    Label(frame1, text="Incorrect").grid(row=1, column=2)


def correct2():
    Label(frame2, text="Correct").grid(row=1, column=2)
    counter()


def incorrect2():
    Label(frame2, text="Incorrect").grid(row=1, column=2)


def correct3():
    Label(frame3, text="Correct").grid(row=1, column=2)
    counter()


def incorrect3():
    Label(frame4, text="Incorrect").grid(row=1, column=2)

def incorrect4():
    Label(frame4, text="Incorrect").grid(row=1, column=2)

def correct4():
    Label(frame4, text="Correct").grid(row=1, column=2)
    counter()

def incorrect4():
    Label(frame4, text="Incorrect").grid(row=1, column=2)



def correct5():
    Label(frame5, text="Correct").grid(row=1, column=2)
    counter()

def incorrect5():
    Label(frame5, text="Incorrect").grid(row=1, column=2)

def incorrect5():
    Label(frame5, text="Incorrect").grid(row=1, column=2)

def correct6():
    Label(frame6, text="Correct").grid(row=1, column=2)
    counter()

def incorrect6():
    Label(frame6, text="Incorrect").grid(row=1, column=2)

def incorrect6():
    Label(frame6, text="Incorrect").grid(row=1, column=2)

def correct7():
    Label(frame7, text="Correct").grid(row=1, column=2)
    counter()

def correct7():
    Label(frame7, text="Correct").grid(row=1, column=2)
    counter()

def incorrect7():
    Label(frame7, text="Incorrect").grid(row=1, column=2)

def correct8():
    Label(frame8, text="Correct").grid(row=1, column=2)
    counter()

def incorrect8():
    Label(frame8, text="Incorrect").grid(row=1, column=2)

def incorrect8():
    Label(frame8, text="Incorrect").grid(row=1, column=2)

def incorrect9():
    Label(frame9, text="Incorrect").grid(row=1, column=2)

def correct9():
    Label(frame8, text="Correct").grid(row=1, column=2)
    counter()

def incorrect9():
    Label(frame9, text="Incorrect").grid(row=1, column=2)

def incorrect10():
    Label(frame10, text="Incorrect").grid(row=1, column=2)

def incorrect10():
    Label(frame10, text="Incorrect").grid(row=1, column=2)

def correct10():
    Label(frame10, text="Correct").grid(row=1, column=2)






def counter():
    total.set(total.get() + 1)


root = Tk()

total = IntVar()

notebook = ttk.Notebook(root)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)
frame5 = ttk.Frame(notebook)
frame6 = ttk.Frame(notebook)
frame7 = ttk.Frame(notebook)
frame8 = ttk.Frame(notebook)
frame9 = ttk.Frame(notebook)
frame10 = ttk.Frame(notebook)


main()

root.mainloop()
Frame.show()