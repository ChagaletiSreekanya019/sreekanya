# from tkinter import *
# # import tkinter
# import tkinter
# r =Tk()
# r.title('Counting Seconds')
# button =Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()


# from cProfile import label
# from tkinter import *
# import tkinter
# deep=tkinter.Tk()
# deep=label(deep,text="My name is deepu

# import imp
# from tkinter import *
# import tkinter
# r = tkinter.Tk()
# r.title('Counting Seconds')
# button = tkinter.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()
# # ####TKINTER##############
# from tkinter import*
# root=Tk()
# l=Label(root,text="hello world i love python !!")
# l.pack()
# root.mainloop()

# from tkinter import*
# root=Tk()
# root.title("my box GUI")
# root.iconbitmap("apple.ico")
# root.geometry("200x100")
# l1=Label(root,text="hi")
# l2=Label(root,text="how you doing today").pack()
# root.mainloop()

# from tkinter import*
# root=Tk()
# w=Canvas(root,width=40,height=60).pack()
# root.geometry("200x500")
# l1=Label(root,text="hi").pack()
# l2=Label(root,text="how you doing today").pack()
# root.mainloop()


# from tkinter import*
# root=Tk()
# root.title("my GUI APP")
# # root.iconbitmap("star.ico")
# root.geometry("500x500")
# l1=Label(root,text="my new GUI app")
# l2=Label(root,text="hello GUI APP")
# l1.grid(row=0,column=0)
# l2.grid(row=2,column=0)
# root.mainloop()



from tkinter import*
root=Tk()
root.title("my GUI APP")
# root.iconbitmap("star.ico")
root.geometry("500x500")

def my_click():
    l1=Label(root,text="welcome to the course",fg="brown")
    l1.pack()
button=Button(root,text="hey click this",command=my_click,fg="red",bg="green",padx=30,pady=50)
button.pack()
root.mainloop()

# #############firstname,last name#################
# from tkinter import*
# root=Tk()
# root.title("my GUI APP")
# # root.iconbitmap("star.ico")
# root.geometry("800x800")

# e=Entry(root,width=50,fg="red")
# e.grid(row=0,column=1)

# ee=Entry(root,width=50,fg="black")
# ee.grid(row=0,column=2)

# def clickme():
#     l1=Label(root,text="hello" + e.get())
#     l1.grid(row=3,column=1)
#     e.delete(0,END)

# def click2():
#     l1=Label(root,text="hello" + ee.get())
#     l1.grid(row=3,column=2)
#     ee.delete(0,END)

# button=Button(root,text="enter your first name",padx=10,pady=10,bg="white",fg="green",command=clickme)
# button.grid(row=2,column=1)

# button=Button(root,text="enter your last name",padx=10,pady=10,bg="white",fg="red",command=click2)
# button.grid(row=2,column=2)


# root.mainloop()

# import tkinter
# from tkinter import*
# from tkinter import messagebox

# root=tkinter.Tk()
# root.title("demo")
# root.geometry("600x600")


# # # label
# '''label=tkinter.Label(root,text="hai i am sreekanya").pack()
# # # Button
# # b=Button(root,text="hello python",bg="blue",fg="pink")
# # b.grid(column=1,row=0)

# #radio
# r=Radiobutton(root,text="python",value=1)
# r.grid(column=2,row=1)
# r1=Radiobutton(root,text="c",value=1)
# r1.grid(column=2,row=2)
# r2=Radiobutton(root,text="c++",value=1)
# r2.grid(column=2,row=3)

# #entry
# t=Entry(root,width=100)
# t.grid(column=3,row=0)


# #message
# def Button1():
#     messagebox.showinfo("status","study well about python")
# b=Button(root,text="python life",command=Button1)
# b.pack()'''


# root.mainloop()
