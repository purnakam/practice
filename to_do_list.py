import tkinter
from tkinter import *

MyList = Tk()
MyList.title('To Do List')
MyList.geometry('400x580')
MyList.resizable(False,True)

target_list = []

def taskopen():
    with open('tasklist.txt','r') as taskfile:
        tasks = taskfile.readline()
        
    for task in tasks:
        if task !='\n':
            task_list.append(task)
            listbox.insert(END,task)


heading = Label(MyList,text='Your Task',fg='white',bg='#32405b',height=4,width=70,font=('arial bold',15))
heading.place(x=-230,y=20)

#main
MyList_frame=Frame(MyList,width=400,height=50,bg='white')
MyList_frame.place(x=0,y=120)

task=StringVar()
task_entry=Entry(MyList_frame,width=18,font="arial 20",bd=0,cursor='tcross')
task_entry.place(x=10,y=7)
task_entry.focus()


button=Button(MyList_frame,text='Add',font='arial 20 bold',width=6,bg='#006400',fg='#EED5B7',bd=0,cursor='hand2')
button.place(x=300,y=0)

#listbox
MyList_frame1=Frame(MyList,bd=3,width=700,height=280,bg='#32405b')
MyList_frame1.pack(pady=(200,0))

listbox=Listbox(MyList_frame1,font=('arial',12),width=40,height=16,bg='#32405b',fg='white',cursor='hand2',selectbackground='#5a95ff')
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(MyList_frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


#delete
Button(MyList,text='Delete',bd=0,bg='#8B2323',font='arial 20 bold italic',fg='#EED5B7',cursor='hand2').pack(side=BOTTOM,pady=13)


MyList.mainloop()