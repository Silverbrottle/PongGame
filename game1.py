from tkinter import *
import random
import time
import winsound

counter1=0
counter2=0

class Ball:
    
    def __init__(self,canvas,paddle1,paddle2,color):
        self.canvas=canvas
        self.paddle1=paddle1
        self.paddle2=paddle2
        self.id=canvas.create_oval(10,10,30,30,fill=color)
        self.canvas.move(self.id,330,400)
        start=[-3,3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.s=StringVar()
        self.s1=StringVar()
        self.s2=StringVar()
        self.l1=Label(self.canvas,text=self.s,font=('Arial',60),fg='white',bg='black')
        self.l2=Label(self.canvas,text=self.s1,font=('Arial',60),fg='white',bg='black')
        self.l3=Label(self.canvas,text=self.s2,font=('Arial',30),fg='white',bg='black')
    def hit_paddle1(self,pos):
        paddle_pos=self.canvas.coords(self.paddle1.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[0]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                winsound.PlaySound("Sonar ping.wav",winsound.SND_ASYNC)
                return True
            return False
    def hit_paddle2(self,pos):
        paddle_pos=self.canvas.coords(self.paddle2.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[2]>=paddle_pos[0] and pos[2]<=paddle_pos[2]:
                winsound.PlaySound("Sonar ping.wav",winsound.SND_ASYNC)
                return True
            return False
        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if self.hit_paddle1(pos)==True:
            self.x=3
        elif self.hit_paddle2(pos)==True:
            self.x=-3
        elif pos[0]<=0:
            self.x=3
            winsound.PlaySound("Sonar ping.wav",winsound.SND_ASYNC)
            self.score(1)
        elif pos[2]>=self.canvas_width:
            self.x=-3
            winsound.PlaySound("Sonar ping.wav",winsound.SND_ASYNC)
            self.score(2)
        elif pos[1]<=0:
            self.y=3
            winsound.PlaySound("Sonar ping.wav",winsound.SND_ASYNC)
        elif pos[3]>=self.canvas_height:
            self.y=-3
            winsound.PlaySound("Sonar ping.wav",winsound.SND_ASYNC)
    
        

    def score(self,val):
        global counter1
        global counter2

        if val==1:
            counter1+=1
            self.l1.config(text=str(counter1))
            self.l1.place(x=475,y=40)

        if val==2:
            counter2+=1
            self.l2.config(text=str(counter2))
            self.l2.place(x=175,y=40)
class Paddle1:
    
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,25,100,fill=color)
        self.canvas.move(self.id,5,330)
        self.y=0
        self.canvas.bind_all('w',self.turn_up)
        self.canvas.bind_all('s',self.turn_down)
        self.canvas_width=self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=self.canvas_height:
            self.y=0
            
    def turn_up(self,evt):
        self.y=-4
        
    def turn_down(self,evt):
        self.y=4
        
class Paddle2:
    
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,25,100,fill=color)
        self.canvas.move(self.id,670,330)
        self.y=0
        self.canvas.bind_all('<KeyPress-Up>',self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>',self.turn_down)
        self.canvas_width=self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=self.canvas_height:
            self.y=0
            
    def turn_up(self,evt):
        self.y=-4
        
    def turn_down (self,evt):
        self.y=4
class Run:
    def __init__(self):
        self.tk=Tk()
        self.tk.title("CG-Pong")
        self.tk.resizable(0,0)
        self.tk.wm_attributes("-topmost",1)
        self.canvas=Canvas(self.tk,width=700, height=700,bd=0,highlightthickness=0)
        self.canvas.config(bg='black')
        self.canvas.pack()
        self.tk.update()
        self.canvas.create_line(350,0,350,700,fill='white')
        self.b1=Button(self.canvas,text="Play Again",font=('Arial',20),fg='red',bg='white',command=self.run)
        self.paddle1=Paddle1(self.canvas,'blue')
        self.paddle2=Paddle2(self.canvas,'pink')      
        self.ball=Ball(self.canvas,self.paddle1,self.paddle2,'orange')
    def run(self):
        self.b1.destroy()
        self.ball.l3.config(text="")
        global counter1
        global counter2
        while 1:
            if counter1==5:
                self.ball.x=0
                self.ball.y=0
                self.paddle1.y=0
                self.paddle2.y=0
                counter1=counter2=0
                self.ball.y=3
                self.ball.l3.config(text="Player 2 WINS!",font=('Arial',30),fg='red')
                self.ball.l3.place(x=200,y=300)
                self.b1=Button(self.canvas,text="Play Again",relief=RAISED,bd=1,highlightthickness=0,font=('Arial',20),fg='red',bg='white',command=self.run)
                self.b1.config(activebackground="white",activeforeground="#F22C2C",cursor="hand2")
                self.b1.place(x=265,y=350)
                break
            elif counter2==5:
                self.ball.x=0
                self.ball.y=0
                self.paddle1.y=0
                self.paddle2.y=0
                counter1=counter2=0
                self.ball.y=3
                self.ball.l3.config(text="Player 1 WINS!",font=('Arial',30),fg='red')
                self.ball.l3.place(x=200,y=300)
                self.b1=Button(self.canvas,text="Play Again",relief=RAISED,bd=1,highlightthickness=0,font=('Arial',20),fg='red',bg='white',command=self.run)
                self.b1.config(activebackground="white",activeforeground="#F22C2C",cursor="hand2")
                self.b1.place(x=265,y=350)
                break
            else:
                self.ball.draw()
                self.paddle1.draw()
                self.paddle2.draw()
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.005)
        self.tk.mainloop()
   
a=Run()
a.run()
