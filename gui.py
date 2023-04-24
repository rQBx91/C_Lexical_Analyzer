from tkinter import *
from  tkinter import ttk


def run(tokens, delim):

    root  = Tk()
    root.title('Result')
    root.resizable(False, False)

    frame = Frame(root)
    frame.pack()

    scroll = Scrollbar(frame)
    scroll.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(frame,yscrollcommand=scroll.set,height=35,selectmode="extended")

    tree.pack()

    scroll.config(command=tree.yview)

    tree['columns'] = ('token', 'type', 'row', 'column', 'block')

    tree.column("#0", width=0, stretch=YES)
    tree.column("token",anchor=CENTER,width=350, stretch=YES)
    tree.column("type",anchor=CENTER,width=200, stretch=YES)
    tree.column("row",anchor=CENTER,width=80, stretch=YES)
    tree.column("column",anchor=CENTER,width=80,stretch=YES)
    tree.column("block",anchor=CENTER,width=80,stretch=YES)

    tree.heading("#0",text="",anchor=CENTER)
    tree.heading("token",text="token",anchor=CENTER)
    tree.heading("type",text="type",anchor=CENTER)
    tree.heading("row",text="row",anchor=CENTER)
    tree.heading("column",text="column",anchor=CENTER)
    tree.heading("block",text="block",anchor=CENTER)

    tree.pack(expand=1)
    
    for index,token in enumerate(tokens):
        if not delim:
            if 'SYMBOL' in token[1]:
                continue
        tree.insert(parent='',index='end',iid=index,text='', values=((token[0]), (token[1]), (token[3]), (token[2]), (token[4])))

    root.mainloop()