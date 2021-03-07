from tkinter import*
coord=[[20,30], [120,30], [220, 30], [70,80], [170,80]]
coul=["red", "yellow", "blue", "green", "black"]
def drawall():
     i=0
     while i<5:
          x1,y1=coord[i][0],coord[i][1]
          can.create_oval(x1, y1, x1+100, y1 +100, width =2, outline =coul[i])
          i=i+1
def drawcircle1():
     x1,y1=coord[0][0],coord[0][1]
     can.create_oval(x1,y1,x1+100, y1+100, width=2, outline=coul[0])
def drawcircle2():
     x1,y1=coord[1][0],coord[1][1]
     can.create_oval(x1,y1,x1+100, y1+100, width=2, outline=coul[1])
def drawcircle3():
     x1,y1=coord[2][0],coord[2][1]
     can.create_oval(x1,y1,x1+100, y1+100, width=2, outline=coul[2])
def drawcircle4():
     x1,y1=coord[3][0],coord[3][1]
     can.create_oval(x1,y1,x1+100, y1+100, width=2, outline=coul[3])
def drawcircle5():
     x1,y1=coord[4][0],coord[4][1]
     can.create_oval(x1,y1,x1+100, y1+100, width=2, outline=coul[4])
def delete():
     can.delete(ALL)
fen1=Tk()
can=Canvas(fen1, width =335, height =200, bg ="white")
can.pack()
bou=Button(fen1, text ="Quitter", command =fen1.quit)
bou.pack(side = RIGHT)
bou2=Button(fen1, text='Tout dessiner', command=drawall)
bou2.pack()
bou3=Button(fen1, text="1", command=drawcircle1)
bou3.pack(side=LEFT)
bou4=Button(fen1, text="2", command=drawcircle2)
bou4.pack(side=LEFT)
bou5=Button(fen1, text="3", command=drawcircle3)
bou5.pack(side=LEFT)
bou6=Button(fen1, text='4', command=drawcircle4)
bou6.pack(side=LEFT)
bou7=Button(fen1, text="5", command=drawcircle5)
bou7.pack(side=LEFT)
bou8=Button(fen1, text='Effacer', command=delete)
bou8.pack()
fen1.mainloop()