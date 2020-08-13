from tkinter import *
import csv
import random
import datetime
import os
from tkinter import messagebox
from matplotlib import pyplot as plt
root=Tk()
root.title("Stock Management")
root.iconbitmap("cycle1.ico")
root.geometry("600x400")
import os.path
from os import path



def createitem():
    for widget in framei1.winfo_children():
        widget.destroy()
    # global ei1,ei2
    li1=Label(framei1,text="Enter the name of item : ").grid(row=0,column=0)
    ei1=Entry(framei1,width=50)
    ei1.grid(row=0,column=1)

    li2=Label(framei1,text="Enter the min qty of item needed: ").grid(row=1,column=0)
    ei2=Entry(framei1,width=50)
    ei2.grid(row=1,column=1)
    # global r
    r=IntVar()
    r.set("1")
    Radiobutton(framei1,text="Single multiplier",variable=r,value=1).grid(row=2,column=0,columnspan=2)
    Radiobutton(framei1,text="Dozen multiplier",variable=r,value=12).grid(row=3,column=0,columnspan=2)
    Radiobutton(framei1,text="Goods multiplier",variable=r,value=144).grid(row=4,column=0,columnspan=2)
    def sr():
        f=0
        try:
            float(ei2.get())
            f=0
            if(path.isfile('Raw.csv')==True):
                with open("Raw.csv","r") as cse:
                    cr=csv.reader(cse)
                    for line in cr:
                        if(line[0]==ei1.get()):
                            f=f+1
                        next(cr)
            
        except:
            f=1
        if f==0 :
            l=[]
            l.append(ei1.get())
            l.append(0)
            l.append((r.get())*float(ei2.get()))
            with open("Raw.csv","a") as cs:
                cr=csv.writer(cs)
                cr.writerow(l)
            messagebox.showinfo("Success!!","Item registered successfully in database",parent=raw)
            ei1.delete(0,END)
            ei2.delete(0,END)
        else:
            messagebox.showerror("Invalid data input!!!!!!!",parent=raw)
            ei1.delete(0,END)
            ei2.delete(0,END)

    
    button_quit=Button(framei1,text="Quit",command=raw.quit).grid(row=5,column=0)
    suit=Button(framei1,text="Submit",command=sr).grid(row=5,column=1)

   

def additem():
    for widget in framei1.winfo_children():
        widget.destroy()
    l=[]
    

    
    try:
        with open("Raw.csv","r") as cse:
            cr=csv.reader(cse)
            for line in cr:
                l.append(line[0])
                next(cr)
    except:
        pass
    li3=Label(framei1,text="Select the name of item : ").grid(row=0,column=0)        
    a=StringVar()
    drop=OptionMenu(framei1,a,*l)
    drop.grid(row=0,column=1,ipadx=130)

    li4=Label(framei1,text="Enter the qty of item added: ").grid(row=1,column=0)
    ei4=Entry(framei1,width=50)
    ei4.grid(row=1,column=1)

    re=IntVar()
    re.set("1")
    Radiobutton(framei1,text="Single multiplier",variable=re,value=1).grid(row=2,column=0,columnspan=2)
    Radiobutton(framei1,text="Dozen multiplier",variable=re,value=12).grid(row=3,column=0,columnspan=2)
    Radiobutton(framei1,text="Goods multiplier",variable=re,value=144).grid(row=4,column=0,columnspan=2)
    
    def fg():
        f=1
        try:
            qty=float(ei4.get())
            f=0
        except:
            f=1
        if f==0:
            qty=qty*re.get()
            with open("raw.csv","r") as cse:
                cr=csv.reader(cse)
                try:
                    for line in cr:
                        if a.get()==line[0] :
                            line[1]=float(line[1])+qty
                            r="success"
                        with open("temp.csv","a") as sw:
                            cw=csv.writer(sw)
                            cw.writerow(line)
                            next(cr)
                except:
                    pass
            os.remove("Raw.csv")
            os.rename(r'temp.csv',r'Raw.csv' )
            messagebox.showinfo("Success!!","Item updated successfully in database",parent=raw)
            ei4.delete(0,END)
        else:
            messagebox.showerror("Invalid data input!!!!!!!",parent=raw)
            ei4.delete(0,END)
    

    button_quit=Button(framei1,text="Quit",command=raw.quit).grid(row=5,column=0)
    suit=Button(framei1,text="Submit",command=fg).grid(row=5,column=1)
    
    


def modifyitem():
    for widget in framei1.winfo_children():
        widget.destroy()
    l=[]
    

    try:
        with open("Raw.csv","r") as cse:
            cr=csv.reader(cse)
            for line in cr:
                l.append(line[0])
                next(cr)
    except:
        pass
    li3=Label(framei1,text="Select the name of item found damaged : ").grid(row=0,column=0)        
    a=StringVar()
    drop=OptionMenu(framei1,a,*l)
    drop.grid(row=0,column=1,ipadx=130)

    li4=Label(framei1,text="Enter the qty of item added: ").grid(row=1,column=0)
    ei4=Entry(framei1,width=50)
    ei4.grid(row=1,column=1)

    rf=IntVar()
    rf.set("1")
    Radiobutton(framei1,text="Single multiplier",variable=rf,value=1).grid(row=2,column=0,columnspan=2)
    Radiobutton(framei1,text="Dozen multiplier",variable=rf,value=12).grid(row=3,column=0,columnspan=2)
    Radiobutton(framei1,text="Goods multiplier",variable=rf,value=144).grid(row=4,column=0,columnspan=2)

    def fg():
        f=1
        try:
            qty=float(ei4.get())
            f=0
        except:
            f=1
        if f==0:
            qty=qty*rf.get()
            with open("raw.csv","r") as cse:
                cr=csv.reader(cse)
                try:
                    for line in cr:
                        if a.get()==line[0] :
                            line[1]=float(line[1])-qty
                            r="success"
                        with open("temp.csv","a") as sw:
                            cw=csv.writer(sw)
                            cw.writerow(line)
                            next(cr)
                except:
                    pass
            os.remove("Raw.csv")
            os.rename(r'temp.csv',r'Raw.csv' )
            messagebox.showinfo("Success!!","Item updated successfully in database",parent=raw)
            ei4.delete(0,END)
        else:
            messagebox.showerror("Invalid data input!!!!!!!",parent=raw)
            ei4.delete(0,END)
    

    button_quit=Button(framei1,text="Quit",command=raw.quit).grid(row=5,column=0)
    suit=Button(framei1,text="Submit",command=fg).grid(row=5,column=1)
    

def raw_material():
    global raw
    raw=Toplevel()
    raw.iconbitmap("cycle1.ico")
    raw.geometry("610x400")
    raw.title("Raw Material Management")
    lr=Label(raw,text="Raw Material Management", font=("arial",30)).grid(ipadx=80,row=0,column=0,columnspan=3)
    b1r=Button(raw,text="Create Item",command=createitem,borderwidth=13).grid(row=2,column=0)
    b2r=Button(raw,text="Add Item",command=additem,borderwidth=13).grid(row=2,column=1)
    b3r=Button(raw,text="Modify Item",command=modifyitem,borderwidth=13).grid(row=2,column=2)
    global framei1
    framei1=LabelFrame(raw,text="Raw material console",padx=10,pady=10)
    framei1.grid(row=3,column=0,columnspan=3)
    raw.mainloop()









def createproduct():
    dii=[]
    t="Nothing"
    for widget in framei2.winfo_children():
        widget.destroy()
    # global ei1,ei2
    li1=Label(framei2,text="Enter the name of product : ").grid(row=0,column=0)
    ei1=Entry(framei2,width=50)
    ei1.grid(row=0,column=1,columnspan=2)

    li2=Label(framei2,text="Enter the min qty of product needed: ").grid(row=1,column=0)
    ei2=Entry(framei2,width=50)
    ei2.grid(row=1,column=1,columnspan=2)

    li3=Label(framei2,text="Enter the components required to make it 1 by 1. When all components are added ,then click on submit : ").grid(row=2,column=0,columnspan=3)


    lte=[]
    try:
        with open("Raw.csv","r") as cse:
            cr=csv.reader(cse)
            for line in cr:
                lte.append(line[0])
                next(cr)
    except:
        pass
    li5=Label(framei2,text="Select the name of component : ").grid(row=3,column=0)        
    a=StringVar()
    drop=OptionMenu(framei2,a,*lte)
    drop.grid(row=3,column=1,ipadx=130,columnspan=2)

    li4=Label(framei2,text="Enter the qty of component required: ").grid(row=4,column=0)
    ei4=Entry(framei2,width=50)
    ei4.grid(row=4,column=1,columnspan=2)
    
    li456=LabelFrame(framei2,text="Items added")
    li456.grid(row=6,column=0,columnspan=3)

    def adprod():
        f=1
        try:
            qty=float(ei2.get())
            f=0
            if(path.isfile('Product.csv')==True):
                with open("Product.csv","r") as cse:
                    cr=csv.reader(cse)
                    for line in cr:
                        if(line[0]==ei1.get()):
                            f=f+1
                        next(cr)



            
            
        except:
            f=1
        if(f==0):
            l=[]
            l.append(ei1.get())
            l.append(dii)
            l.append(0)
            l.append(qty)
            with open("Product.csv","a") as csh:
                cr=csv.writer(csh)
                cr.writerow(l)
            messagebox.showinfo("Success!!","Product registered successfully in database",parent=prod)
            ei1.delete(0,END)
            ei2.delete(0,END)
        else:
            messagebox.showerror("Invalid data input!!!!!!!",parent=prod)
            ei1.delete(0,END)
            ei2.delete(0,END)
            
        
        





    def adco():
        j=[]
        j.append(a.get())
        j.append(ei4.get())
        dii.append(j)
        ei4.delete(0,END)
        t=a.get()
        Label(li456,text=t+"has been added.").pack()
        
    
    button_quit=Button(framei2,text="Quit",command=prod.quit).grid(row=5,column=0)
    comp=Button(framei2,text="Add ",command=adco).grid(row=5,column=1)
    suit=Button(framei2,text="Submit ",command=adprod).grid(row=5,column=2)


def addproduct():
    for widget in framei2.winfo_children():
        widget.destroy()
    l=[]
    

    
    try:
        with open("Product.csv","r") as cse:
            cr=csv.reader(cse)
            for line in cr:
                l.append(line[0])
                next(cr)
    except:
        pass
    li3=Label(framei2,text="Select the name of product : ").grid(row=0,column=0)        
    a=StringVar()
    drop=OptionMenu(framei2,a,*l)
    drop.grid(row=0,column=1,ipadx=130)

    li4=Label(framei2,text="Enter the qty of product added: ").grid(row=1,column=0)
    ei4=Entry(framei2,width=50)
    ei4.grid(row=1,column=1)
    def realmodifyitem(a,qty):
        with open("raw.csv","r") as cse:
            cr=csv.reader(cse)
            try:
                for line in cr:
                    if a==line[0] :
                        line[1]=float(line[1])-qty
                        r="success"
                    with open("temp.csv","a") as sw:
                        cw=csv.writer(sw)
                        cw.writerow(line)
                        next(cr)
            except:
                pass
        os.remove("Raw.csv")
        os.rename(r'temp.csv',r'Raw.csv' )
    def sd():
        f=1
        lll=[]
        try:
            qty=float(ei4.get())
            f=0
        except:
            f=1
        if(f==0):
            with open("Product.csv","r") as cse:
                cr=csv.reader(cse)
                
                for line in cr:
                    if a.get()==line[0] :
                        line[2]=float(line[2])+qty
                        lll=eval(line[1])
                    with open("temp.csv","a") as sw:
                        cw=csv.writer(sw)
                        cw.writerow(line)
                        next(cr) 
            os.remove("Product.csv")
            os.rename(r'temp.csv',r'Product.csv')
            for i in lll:
                name=str(i[0])
                qty=float(i[1])*qty
                realmodifyitem(name,qty)
            messagebox.showinfo("Success!!","Item updated successfully in database",parent=prod)
            ei4.delete(0,END)
        else:
            messagebox.showerror("Invalid data input!!!!!!!",parent=prod)
            ei4.delete(0,END)
    

    button_quit=Button(framei2,text="Quit",command=prod.quit).grid(row=5,column=0)
    suit=Button(framei2,text="Submit",command=sd).grid(row=5,column=1)
    





def saleproduct():
    for widget in framei2.winfo_children():
        widget.destroy()
    l=[]
    

    
    try:
        with open("Product.csv","r") as cse:
            cr=csv.reader(cse)
            for line in cr:
                l.append(line[0])
                next(cr)
    except:
        pass
    li3=Label(framei2,text="Select the name of product : ").grid(row=0,column=0)        
    a=StringVar()
    drop=OptionMenu(framei2,a,*l)
    drop.grid(row=0,column=1,ipadx=130)

    li4=Label(framei2,text="Enter the qty of product sold: ").grid(row=1,column=0)
    ei4=Entry(framei2,width=50)
    ei4.grid(row=1,column=1)

    def sd():
        f=1
        try:
            qty=float(ei4.get())
            f=0
        except:
            f=1
        if(f==0):
            with open("Product.csv","r") as cse:
                cr=csv.reader(cse)
                try:
                    for line in cr:
                        if a.get()==line[0] :
                            line[2]=float(line[2])-qty
                        with open("temp.csv","a") as sw:
                            cw=csv.writer(sw)
                            cw.writerow(line)
                            next(cr)
                except:
                    pass 
            os.remove("Product.csv")
            os.rename(r'temp.csv',r'Product.csv')
            messagebox.showinfo("Success!!","Item updated successfully in database",parent=prod)
            ei4.delete(0,END)
        else:
            messagebox.showerror("Invalid data input!!!!!!!",parent=prod)
            ei4.delete(0,END)
    

    button_quit=Button(framei2,text="Quit",command=prod.quit).grid(row=5,column=0)
    suit=Button(framei2,text="Submit",command=sd).grid(row=5,column=1)



def product():
    global prod
    prod=Toplevel()
    prod.iconbitmap("cycle1.ico")
    prod.geometry("610x400")
    prod.title("Product Management")
    lr=Label(prod,text="Product Management", font=("arial",30)).grid(ipadx=80,row=0,column=0,columnspan=3)
    b1r=Button(prod,text="Create Product",command=createproduct,borderwidth=13).grid(row=2,column=0)
    b2r=Button(prod,text="Add Product",command=addproduct,borderwidth=13).grid(row=2,column=1)
    b3r=Button(prod,text="Sale Product",command=saleproduct,borderwidth=13).grid(row=2,column=2)
    global framei2
    framei2=LabelFrame(prod,text="Product console",padx=10,pady=10)
    framei2.grid(row=3,column=0,columnspan=3)
    prod.mainloop()


def stockraw():
    for widget in framei3.winfo_children():
        widget.destroy()

    s=""

    slices = []
    labels = []


    with open("Raw.csv","r") as cse:
        cr=csv.reader(cse)
        for line in cr:
            s=f"Stock of {line[0]} is {line[1]} \n"+s
            labels.append(line[0])
            slices.append(line[1])
            next(cr)
    li3=Label(framei3,text=s).pack()
    

    plt.style.use("fivethirtyeight")


    plt.pie(slices, labels=labels, shadow=True,
            startangle=90, autopct='%1.1f%%',
            wedgeprops={'edgecolor': 'black'})

    plt.title("Stock of Raw Material")
    plt.tight_layout()
    plt.show()
    
def stockproduct():
    for widget in framei3.winfo_children():
        widget.destroy()


    s=""
    slices = []
    labels = []
    with open("Product.csv","r") as cse:
        cr=csv.reader(cse)
        for line in cr:
            s=f"Stock of {line[0]} is {line[2]} \n"+s
            labels.append(line[0])
            slices.append(line[1])
            next(cr)
    li3=Label(framei3,text=s).pack()

    plt.style.use("fivethirtyeight")


    plt.pie(slices, labels=labels, shadow=True,
            startangle=90, autopct='%1.1f%%',
            wedgeprops={'edgecolor': 'black'})

    plt.title("Stock of Raw Material")
    plt.tight_layout()
    plt.show()
    
def minstockraw():
    for widget in framei3.winfo_children():
        widget.destroy()


    s=""

    slices = []
    labels = []
    with open("Raw.csv","r") as cse:
        cr=csv.reader(cse)
        for line in cr:
            if(line[1]<=line[2]):
                s=f"Stock of {line[0]} is {line[1]} \n"+s
                labels.append(line[0])
                slices.append(line[1])
            next(cr)
    li3=Label(framei3,text=s).pack()

    plt.style.use("fivethirtyeight")


    plt.pie(slices, labels=labels, shadow=True,
            startangle=90, autopct='%1.1f%%',
            wedgeprops={'edgecolor': 'black'})

    plt.title("Stock of Raw Material")
    plt.tight_layout()
    plt.show()
    
def minstockproduct():
    for widget in framei3.winfo_children():
        widget.destroy()

    s=""
    slices = []
    labels = []
    with open("Product.csv","r") as cse:
        cr=csv.reader(cse)
        for line in cr:
            if(line[2]<=line[3]):
                s=f"Stock of {line[0]} is {line[2]} \n"+s
                labels.append(line[0])
                slices.append(line[1])
            next(cr)
    li3=Label(framei3,text=s).pack()

    plt.style.use("fivethirtyeight")


    plt.pie(slices, labels=labels, shadow=True,
            startangle=90, autopct='%1.1f%%',
            wedgeprops={'edgecolor': 'black'})

    plt.title("Stock of Raw Material")
    plt.tight_layout()
    plt.show()



def stock():
    global stoc
    stoc=Toplevel()
    stoc.iconbitmap("cycle1.ico")
    stoc.geometry("610x400")
    stoc.title("Stock Management")
    lr=Label(stoc,text="Stock Management", font=("arial",30)).grid(ipadx=80,row=0,column=0,columnspan=4)
    b1r=Button(stoc,text="Raw",command=stockraw,borderwidth=13).grid(row=2,column=0)
    b2r=Button(stoc,text="Product",command=stockproduct,borderwidth=13).grid(row=2,column=1)
    b3r=Button(stoc,text="Raw Min",command=minstockraw,borderwidth=13).grid(row=2,column=2)
    b4r=Button(stoc,text="Product Min",command=minstockproduct,borderwidth=13).grid(row=2,column=3)
    global framei3
    framei3=LabelFrame(stoc,text="Product console",padx=10,pady=10)
    framei3.grid(row=3,column=0,columnspan=4)
    stoc.mainloop()
    




Label(root,text="Jeet Sales Co.", font=("arial",50)).grid(ipadx=80,row=0,column=0,columnspan=3)

b1=Button(root,text="Raw Material",command=raw_material,borderwidth=13).grid(row=2,column=0)
b2=Button(root,text="Products",command=product,borderwidth=13).grid(row=2,column=1,ipadx=10)
b3=Button(root,text="Stock",command=stock,borderwidth=13).grid(row=2,column=2,ipadx=20)
louis=["YOU'VE COME TOO FAR TO QUIT.","BE JHakass",'Let them sleep while you grind. Let them party while you work. The difference will show.', "Our greatest fear should not be of failure, but of succeeding at things in life that don't really matter.", 'Money and success don’t change people; they merely amplify what is already there. – Will Smith ','Today you will work hard, you will study late night, you will skip parties, you will avoid hanging out with friends. But then tomorrow, you will enjoy your life in a much better way. Think about tomorrow, not today.', 'You can’t cheat the grind, it knows how much you have invested. It wont give you anything you haven’t worked for. ', "As Albert Einstein rightly said, The world won't be destroyed by those who do evil, but by those who watch them without doing anything.", 'A dream does not become reality through magic; it takes sweat, determination and hard work.', 'A year from now, we’ll see who was really working. ', 'Money and success don’t change people; they merely amplify what is already there. – Will Smith','You become strong by lifting others up, not pulling them down.', "Without God, you can do nothing. With God, there is nothing you can't do.", 'Talent is God given. Be humble. Fame is man-given. Be grateful. Conceit is self-given. Be careful. ', 'Once the game is over, the king and the pawn go back in the same box. -Italian Proverb', 'Being u matters', "Don't ever get to the point where you feel like I made it. Set new goals, keep learning and stay hungry.", "The real measure of our wealth is how much we'd be worth if we lost all our money", 'You don’t want to look back and know you could have done better', 'Live in the lead, but work hard like you’re trying to catch up.', 'Don’t worry about anything; instead pray about everything.','The tallest buildings start with a single brick. ', 'The greatest miracle of all is to be alive. Every morning you wake up, remember you have seen a miracle. ', 'Challenge yourself and find out precisely how good you are with words!', "Don't let people rush you with the timelines", 'Remember, when you are not training, someone somewhere is training; and when you meet him, he will win. ', "You're going to go through tough times - that's life. But I say, 'Nothing happens to you, it happens for you See the positive in negative events. – Joel Osteen ", "Everything happens when it needs to happen. But don't wait for extraordinary opportunities. Seize common occasions and make them great.", 'Don’t let the fear of the time it will take to accomplish something stand in the way of your doing it. The time will pass anyway; we might just as well put that passing time to the best possible use. – Earl Nightingale',"It isn't where you came from. It's where you're going that counts. – Ella Fitzgerald", "Don't be upset about the results you didn't get, from the work you didn't do.", 'If you’re confident about your strength, you don’t need to show me by putting somebody else down. Show me by lifting somebody else up. – BarackObama', "Do your little bit of good where you are; it's those little bits of good put together that overwhelm the world. – Desmond Tutu ", 'You can always be better', 'Courage doesn’t always roar. Sometimes courage isthe little voice at the end of the day that says I’ll try again tomorrow. —Mary Anne Radmacher', "The difference between a dreamer and a doer isn't luck, talent, skill or money. Unlike some dreamers who never get around to putting their dreams into action, doers make a promise to themselves to reach a goal and honor that commitment by taking determined action", "What you're supposed to do when you don't like a thing is change it. If you can't change it, change the way you think about it. Don't complain. –Maya Angelou", 'If youare building a house and a nail breaks, do you stop building or do you change the nail? — Rwandan proverb ','Don’t expect anyone to know your thoughts and feelings except yourself. Be brave enough to express and explain them to those worthy when needed.', "Just because something works doesn't mean it can't be improved. There's always room for improvement.", 'Before putting others in their place put yourself in their place.', 'If at first you don’t succeed, then skydiving definitely isn’t for you. – Steven Wright ', "Keep it moving, but don't mistake movement for progress. ","Isn't it scary knowing that any time could be the last time you talk to someone? Always keep that in mind.", 'Be proud of yourself for how far you have come, and never stop pushing to be the best you can be.', "There's far more that you can perceive than only through the 5 human senses. –Deepak Chopra", 'Visualize yourself in the future as you want to be. Make that thought into a picture then step into the picture. Do this constantly', "Never forget how far you've come. Everything you have gotten through. All the times you have pushed on even when you felt you couldn't. All the mornings you got out of bed no matter how hard it was. All the times you wanted to give up but you got through another day. Keep going! ", "Don't be deceived by the spirit ofcomplacency and think you have achieved enough. Try to become better than you've been", "There may be peoplewho have more talent than you, but there's no excuse for anyone to work harder than you do - and I believe that", 'Never look down on anybody unless you’re helping them up. – Jesse Jackson', 'Never let an opportunity pass you by. Seize it with everything you have.','Don’t take someone else’s word on what you can accomplish', "When someone says you can't do it, do it twice and take pictures", "picture-perfect, you don't need no filter", 'If there be any truer measure of a man than by what he does, it must be by what he gives', 'if someone wants to be with you, nothing will stop them from doing so. Love doesn’t create excuses', 'People look at you and say you changed, as if you worked that hard to stay the same', 'Don’t be discouraged. It’s often the last key in the bunch that opens the lock', 'The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will. – Vince Lombardi Jr', 'Positive thinking can actually help increase your lifespan, strengthen your immune system and lower rates of depression', 'May you have every reason to raise your voice and your hands in praise. We hope every day of this month gives you a reason to smile and be happy. ', 'Shame is among the toughest, if not the toughest opponent we will ever face. It is never easy, ever. But because it’s so difficult, if we are brave enough to fight, the rewards it can yield can be life changing. Believe in you and never short change your value', 'It is impossible for a man to learn what he thinks he already knows.', 'THERE IS POWER IN KNOWING NOTHING!', 'The only thing worse than starting something and failing is not starting something.', '“The future starts today, not tomorrow.” – Pope John Paul II', 'Never discount the value of small acts and small gestures. Especially when it comes to kindness.', 'If you do tomorrow what you did today, you will get tomorrow what you got today. - Benjamin Franklin', 'Why don’t you focus on where you’re going and less on where you came from?', "Appreciate people for the little things. It feels good to be appreciated. It doesn't take much for you to show appreciation. You never know what someone is going through, sometimes a little encouragement from you is all it takes to give someone motivation to turn their life around. ", 'People look at you and say you changed, as if you worked that hard to stay the same. – Jay Z', 'If you admire someone, you should go ahead and tell them. People never get the flowers while they can still smell them.', 'The connections you have in your life should add value, not take value away. ', "There is only one person you spend your whole life with, and that is you. If you aren't ok with you, there is a problem.", 'The greatest man is not the one who never fell but rather the one who fell and was able to rise up again...it is possible to come out of anything!', 'There may be someone out there who has more talent than you, but there is no excuse for someone to work harder than you.', 'The past is a place of reference, not a place of residence; the past is a place of learning, not a place of living. –Roy T. Bennett', 'Loss of any kind is not easy. We feel some, if not all difficult emotions. Feel them, face them, don’t lock them up, but do so with a brave sense of accountability. All of us are tested now more than ever. Stay in touch and in tune with you, try to find lessons in any hardship. ', 'To the essential workers helping us all, to those that are struggling with the challenges these times bring mentally, physically, financially, and for those battling illness, this is for you', 'I wish nothing but the best for you', 'Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing', 'No matter how good or bad you have it, wake up each day thankful for your life. Someone somewhere else is desperately fighting for theirs', 'A man who views the world the same at 50 as he did at 20 has wasted 30 years of his life. –Muhammad Ali ', "It doesn'tmatter how you look. As long as you train hard, you focus and you're hungry, and that drive is in you to follow your dreams, everything is possible","Look inside of you and find that whisper","MD Loves YOu Bro","Be grateful","Loss of any kind is not easy.We feel some,if not all difficult emotions.Feel them,don't lock them up,but do so with a brave sense of accountability","Fu** the rest, u r the best","Be satisfied -Preeti Jain"]
frame=LabelFrame(root,text="Thought of the day",padx=10,pady=10)
frame.grid(row=3,column=0,columnspan=3)
tde=datetime.datetime.today()
m=(int(tde.month))
d=(int(tde.day))
u=(m%3)*30+d
ghee=louis[u]
lew=Label(frame,text=ghee).pack()




root.mainloop()