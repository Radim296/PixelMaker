from tkinter import *
from tkinter.colorchooser import *

class gui():
    bg = "#2A2A2A"
    bgb = "#8B8B8B"
    fgb = "#24ACF2"
    fg = "black"
    icon = "paint.png"
    color = "black"
    height = 13
    width = height
    colors = []
    mapcolors = {}
    a = 0
    g = 0
    try:
        file = open("colors.txt")
        for i in file.read().splitlines():
            colors.append(i)
        file.close()
    except:
        file = open("colors.txt", "w")
        file.close()
    h = {}; gg = {}

    def __init__(self):
        self.root = Tk()
        self.root.title("PixelPainter")
        self.root.geometry()
        mainmenu = Menu(self.root) 
        self.root.config(menu=mainmenu) 
        mainmenu.add_command(label='Справка')
        self.root["bg"] = self.bg 
        self.root.resizable(False, False)     # Ограничения в расширений окна 
        self.root.option_add("*Font", "courier 12")   # Шрифт 
        self.root.iconbitmap(self.icon)
        self.paintDesk = Frame(self.root, bg = self.bg)
        self.functionsDesk = Frame(self.root)
        self.functionsDesk.config(bg = "#2A2A2A", bd = 9)
        self.functionsDesk.grid(row = 0, column = 1)
        self.colorDesk = Frame(self.root)
        self.colorDesk.config(bg = "#2A2A2A", bd = 9)
        self.colorDesk.grid(row = 0, column = 3)

    def getColor(self):                          # Инструмент с помощью которого можно подобрать цвет
        try:
            color = askcolor()
            print(color[1])
            self.color = color[1]
            self.b6.config(bg = self.color)
            with open("colors.txt", "a") as file:
                file.write(self.color + "\n")
            self.co(self.color)
        except:
            pass
    def get(self, y,x):
        a = str(x) + " " + str(y)
        return a 

    def clear(self, c):
        com = lambda x = c : self.draw(x)
        self.gg[c].config(bg = "white", command = com)
    
    def clearall(self):
        for i in self.h:
            self.clear(i)
    
    def drawall(self):
        print("fdgd")
        for i in self.h:
            com = lambda x = i : self.draw(x)
            self.gg[i].config(bg = self.color, command = com)

    def draw(self, c):
            com = lambda x = c:self.draw(x)
            self.gg[c].config(bg = self.color, command = com)
    def gpass(self):
        pass
    def eraser(self):
        self.color = "white"
    def clean(self):
        with open("colors.txt", "w") as file:
            pass
    
    def makeFuncDesk(self):
        b1 = Button(self.functionsDesk, text = "  Заливка   ", width = 13,bg = self.bgb, bd = 3,command = self.drawall).grid(row = 1, column = 1)
        b1 = Button(self.functionsDesk, text = "Очистить все", bg = self.bgb, width = 13,bd = 3,command = self.clearall).grid(row = 2, column = 1)
        b1 = Button(self.functionsDesk, text = "Палитра", bg = self.bgb, width = 13,bd = 3,command = self.getColor).grid(row = 3, column = 1)
        b1 = Button(self.functionsDesk, text = "Ластик", bg = self.bgb, width = 13,bd = 3,command = self.eraser).grid(row = 4, column = 1)
        b1 = Button(self.functionsDesk, text = "Очистить историю цветов", bg = self.bgb, width = 13,bd = 3,command = self.clean).grid(row = 5, column = 1)
        b1 = Label(self.functionsDesk, text = '',bg = self.bg).grid(row = 6, column=1)
        b1 = Label(self.functionsDesk, text = '',bg = self.bg).grid(row = 7, column=1)
        b1 = Label(self.functionsDesk, text = '',bg = self.bg).grid(row = 8, column=1)
        b1 = Label(self.functionsDesk, text = '',bg = self.bg).grid(row = 9, column=1)
        b1 = Label(self.functionsDesk, text = '',bg = self.bg).grid(row = 10, column=1)
        b1 = Label(self.functionsDesk, text = '',bg = self.bg).grid(row = 11, column=1)
        b1 = Label(self.functionsDesk, text = '',bg = self.bg).grid(row = 12, column=1)
        b1 = Label(self.functionsDesk, text = '',bg = self.bg).grid(row = 13, column=1)
        b1 = Label(self.functionsDesk, text = '',bg = self.bg).grid(row = 14, column=1)
        b1 = Label(self.functionsDesk, text = '',bg = self.bg).grid(row = 15, column=1)
        self.b6 = Button(self.functionsDesk, text = "", bg = self.color, width = 13,bd = 3,command = self.gpass)
        self.b6.grid(row = 16, column = 1)
    
    def newcolor(self, c):
        self.color = c
        self.b6.config(bg = self.color)
    def co(self, i):
        com = lambda x = i : self.newcolor(x)
        if self.a % 11 == 0:
          self.g+=1
          self.a=0
        if self.g == 0:
            self.g = 1
        self.a += 1
        b = Button(self.colorDesk, text = " ", height = 1, width = 2, bd = 4)
        b.grid(row = self.a, column = self.g)
        b.configure(bg = i)
        b.configure(command = com)
    def makeColor(self):
        for j,i in enumerate(self.colors):
            self.co(i)
    def makeDesk(self):
        for y in range(1, (self.height+1)):
            for x in range(1, (self.width+1)):
                cl = self.get(y,x)
                com = lambda c = cl : self.draw(c)
                self.h[cl] = Button(self.paintDesk, text = " ", height = 1, width = 2, bd = 4)
                self.h[cl].grid(row = y, column = x)
                self.h[cl].configure(bg = "white")
                self.h[cl].configure(command = com)
        for i in self.h:
            if i not in self.gg:
                self.gg[i] = self.h[i]
        self.paintDesk.grid(row = 0, column = 2)
        #self.paintDesk.pack(side="left")
    
    def run(self):
        try:
            self.root.mainloop()
        except:
            pass

def main():
    root = gui()
    root.makeFuncDesk()
    root.makeDesk()
    root.makeColor()
    root.run()

if __name__ == "__main__":
    main()