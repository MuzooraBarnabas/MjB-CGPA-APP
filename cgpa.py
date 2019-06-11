#import africastalking
from tkinter import*
from tkinter import ttk, messagebox, filedialog, simpledialog, scrolledtext
from datetime import datetime, date, time
import time, webbrowser, sqlite3
from itertools import cycle
import tkinter as tk
from time import sleep
from math import trunc
import tkinter.font as tkFont


gpa = Tk()
gpa.title("MjB GPA CALC") 
gpa.geometry("1245x730+0+5")
gpa.minsize(1000,500)
gpa.iconbitmap("pics/logo.ico")
gpa.config(relief=GROOVE, bg='CadetBlue4', bd=3)

#-----------mainFrame-----------
mainFrame = Frame(gpa, bg="gray40")
mainFrame.pack(side=TOP, fill=BOTH)

#---------------notebook starts here-------------------
note = ttk.Notebook(mainFrame)

#--------------tabs start here-------
tab1 = Frame(note, bg='white')
tab2 = Frame(note, bg='white')
tab3 = Frame(note, bg='white')
tab4 = Frame(note, bg='white')
tab5 = Frame(note, bg='white')
tab6 = Frame(note, bg='white')
tab7 = Frame(note, bg='white')
tab8 = Frame(note, bg='white')
tab9 = Frame(note, bg='white')
tab10 = Frame(note, bg='white')
tab11 = Frame(note, bg='white')

note.grid(sticky=N+E+S+W, row=2, column=0)
tab1.grid(pady=5, padx=10)
tab2.grid(pady=5, padx=10)
tab3.grid(pady=5, padx=10)
tab4.grid(pady=5, padx=10)
tab5.grid(pady=5, padx=10)
tab6.grid(pady=5, padx=10)
tab7.grid(pady=5, padx=10)
tab8.grid(pady=5, padx=10)
tab9.grid(pady=5, padx=10)
tab10.grid(pady=5, padx=10)
tab11.grid(pady=5, padx=10)

#--------------heading pics----------
loginI=PhotoImage(file='pics/logintab.png')
signI=PhotoImage(file='pics/signtab.png')
dashI=PhotoImage(file='pics/dashtab.png')
marksI=PhotoImage(file='pics/markstab.png')
printI=PhotoImage(file='pics/printtab.png')
mannI=PhotoImage(file='pics/manualtab.png')
devI=PhotoImage(file='pics/devinfotab.png')
contI=PhotoImage(file='pics/contacttab.png')
adminI=PhotoImage(file='pics/admindash.png')
gradeI=PhotoImage(file='pics/gradingtab.png')
cgpaI=PhotoImage(file='pics/cgpatab.png')
#-----------tabs headings-------------
note.add(tab1, text="MjB-LOGIN", image=loginI)
note.add(tab2, text="MjB-SIGN UP", image=signI)
note.add(tab3, text="MjB-DASHBORD", image=dashI)
note.add(tab4, text="MjB-MARKS ENTRY", image=marksI)
note.add(tab5, text="MjB-PRINT PREVIEW", image=printI)
note.add(tab6, text="MjB-APP MANNUAL", image=mannI)
note.add(tab7, text="MjB-DEV INFO", image=devI)
note.add(tab8, text="CONTACT US", image=contI)
note.add(tab9, text="ADMIN DASHBORD", image=adminI)
note.add(tab10, text="GRADING SYSTEM", image=gradeI)
note.add(tab11, text="GPA & CGPA PAGE", image=cgpaI)


#---------------hide tabs-----------
note.tab(1, state="hidden")
note.tab(2, state="hidden")
note.tab(3, state="hidden")
note.tab(4, state="hidden")
note.tab(5, state="hidden")
note.tab(6, state="hidden")
note.tab(7, state="hidden")
note.tab(8, state="hidden")
note.tab(9, state="hidden")
note.tab(10, state="hidden")
#-------------notebook ends-----------


#-----------header----------
headerF = Frame(mainFrame, bg="Cyan4")
headerF.grid(sticky=(E+W),row=0)
logo1 = PhotoImage(file='pics/header.png')
Label(headerF, image=logo1, bg="Cyan4").grid(row=0, column=0, sticky=(E+W), ipady=2,columnspan=2, padx=20)
headerF.rowconfigure(0, weight=1)
headerF.columnconfigure(0, weight=1)

#-----------time---------
clockpic = PhotoImage(file='pics/clock.png')
clock = Label(headerF, relief='solid', bd=1, bg="Cyan4", cursor="exchange", font=('times', 20, 'bold'))
clock.grid(row=0, column=1, ipady=5, ipadx=10, padx=20)

today = date.today()
now = today.strftime("%A, %d %B %Y")

time1 = ''

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
    if((time.strftime('%H')<=str(12)) and (time.strftime('%M') <str(1))):
        clock.config(image=clockpic,text=" "+time2+"", compound=LEFT)
    else:
        clock.config(image=clockpic,text=" "+time2+"", compound=LEFT)        
        
    clock.after(200, tick) 
tick()

#------------------tooltip--------------------
class ToolTipBase:
    def __init__(self, button):
        self.button = button
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self._id1 = self.button.bind("<Enter>", self.enter)
        self._id2 = self.button.bind("<Leave>", self.leave)
        self._id3 = self.button.bind("<ButtonRelease-1>", self.leave)
        self._id4 = self.button.bind("<KeyPress>", self.leave)

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.button.after(500, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.button.after_cancel(id)

    def showtip(self):
        if self.tipwindow:
            return
        # The tip window must be completely outside the button;
        # otherwise when the mouse enters the tip window we get
        # a leave event and it disappears, and then we get an enter
        # event and it reappears, and so on forever :-(
        x = self.button.winfo_rootx()+10
        y = self.button.winfo_rooty() + self.button.winfo_height() + 2
        self.tipwindow = tw = Toplevel(self.button)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        self.showcontents()

    def showcontents(self, text="Your text here"):
        # Override this in derived class
        label = Label(self.tipwindow, text=text,
                      background="gray", fg='black', relief=SOLID, borderwidth=1, font=('arial', 10, 'bold'))
        label.pack()
        label1 = Label(self.tipwindow, text=text,
                      background="gray", fg='black', relief=SOLID, borderwidth=1, font=('arial', 10))
        label1.pack()

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

class ToolTip(ToolTipBase):
    def __init__(self, button, text):
        ToolTipBase.__init__(self, button)
        self.text = text
    def showcontents(self):
        ToolTipBase.showcontents(self, self.text)

class tooltip(ToolTipBase):
    def __init__(self, button, items):
        ToolTipBase.__init__(self, button)
        self.items = items
    def showcontents(self):
        listbox = Label(self.tipwindow,relief=SOLID, bd=1,fg='brown', background="gold", font=('arialblack', 10))
        listbox.pack()
        for item in self.items:
            listbox.config(text=str(item))
#----------------tooltip ends---------------------

#---------tab1 frames---------
mFrame = Frame(tab1, bg='gray', relief=FLAT, bd=1)
mFrame.pack(padx=100, pady=20)

#------------left frame--------
lFrame = Frame(mFrame, bg="lightgray", relief=FLAT, bd=1)
lFrame.pack(side=LEFT, pady=10, padx=10 , fill=Y)

#------------slide show--------------
images = ["pics/face1.png", "pics/face2.png", "pics/face3.png"]
photos = cycle(PhotoImage(file=image) for image in images)

def slideShow():
  img = next(photos)
  disaplyscreen.config(image=img, bg="lightgray")
  gpa.after(5000, slideShow)

disaplyscreen = Label(lFrame, text='\n', compound=BOTTOM, font=('times', 10, 'bold'))
disaplyscreen.pack()
gpa.after(10, lambda: slideShow())


#------------right frame--------
rFrame = Frame(mFrame, relief=FLAT, bg="white", bd=1)
rFrame.pack(side=RIGHT, pady=10, padx=10)
rFrame.rowconfigure(0, weight=1)
rFrame.columnconfigure(0, weight=1)

#---------------login part------------
try:
  conn = sqlite3.connect('dbs/mjbgpadata.db')
  conn.execute('''CREATE TABLE IF NOT EXISTS accounts
  (FIRSTNAME VARCHAR UNIQUE,
  LASTNAME VARCHAR UNIQUE,
  PHONE_NO VARCHAR,
  UNIVERSITY VARCHAR,
  PASSWORD VARCHAR,
  PIN VARCHAR)''')

  conn.execute("INSERT INTO accounts (FIRSTNAME, LASTNAME,PHONE_NO, UNIVERSITY,PASSWORD, PIN)\
  VALUES ('MjB','ADMIN','0750941273','BISHOP STUART UNIVERSITY','@admin@','@13579@')")
  conn.commit()
  conn.close()
except Exception as e:
  pass

val='null'
try:
  conn = sqlite3.connect('dbs/mjbgpadata.db')
  cursor = conn.cursor()
  cursor.execute('SELECT LASTNAME FROM accounts')
  value = cursor.fetchall()
  val = value 
  conn.close()
except Exception as e:
  print(e)

Label(rFrame, text="MjB Login", font=("Verdana", 20,"bold"), bg="white", fg="gray").grid(row=0, sticky=N, pady=20, padx=10)
Label(rFrame, text="Last Name", font=("Verdana", 15,"bold"), bg="white", fg="gray").grid(row=1, column=0, sticky=W, padx=10)
userN = ttk.Combobox(rFrame, values=val, width=19, font=("Verdana", 15,"bold"),justify="center")
userN.grid(row=2, column=0, padx=10)
tip = tooltip(userN, ["Last name is required!"])



lmsg1 = Label(rFrame, fg="red",bg="white", font=("Verdana", 10,"italic"))
lmsg1.grid(row=3)

Label(rFrame, text="Pin", font=("Verdana", 15,"bold"), bg="white", fg="gray").grid(row=4, column=0, sticky=W, padx=10)
passW = ttk.Entry(rFrame, width=20, show="•",font=("Verdana", 15,"bold"),justify="center")
passW.grid(row=5, column=0, padx=10)
lmsg2 = Label(rFrame, fg="red",bg="white", font=("Verdana", 10,"italic"))
lmsg2.grid(row=6)
tip = tooltip(passW, ["PIN is required!"])


def alerts(*args):
  lmsg1.config(text="")
  lmsg2.config(text="")
userN.bind("<Button-1>", alerts)
passW.bind("<Button-1>", alerts)

def alert1(*args):
  lmsg1.config(text="")

def press(*args):
  if userN.get()=='ADMIN':
    messagebox.showinfo("MjB-Login bot!", "You MUST be authorized to use the ADMIN account.\n\nElse signup to create account!")
  else:
    passW.focus() 
passW.bind('<Button-1>', press)

def alert2(*args):
  lmsg2.config(text="")



def login(*args):
  LASTNAME=" "
  PIN=" "
  if(userN.get()=="") and (passW.get()==""):
    lmsg1.config(text="This field is required!")
    lmsg2.config(text="This field is required!")
    userN.focus()
    userN.bind("<KeyPress>", alerts)
    passW.bind("<KeyPress>", alerts)


  elif(userN.get()==""):
    lmsg1.config(text="Last name is required!")
    lmsg2.config(text="")
    userN.focus()
    userN.bind("<KeyPress>", alert1)
 
  elif(passW.get()==""):
    lmsg2.config(text="Pin is required!")
    lmsg1.config(text="") 
    passW.focus()
    passW.bind("<KeyPress>", alert2)
 
  else:
    lmsg2.config(text="")
    lmsg1.config(text="")
    try:
      conn = sqlite3.connect('dbs/mjbgpadata.db')
      cursor = conn.cursor()
      sql3 = ('SELECT FIRSTNAME, LASTNAME,PIN FROM accounts WHERE LASTNAME=? and PIN=?' )
      valz = (userN.get(), passW.get())
      cursor.execute(sql3, valz)
      value = cursor.fetchall()
      for (FIRSTNAME, LASTNAME,PIN) in value:
        pass
      if(userN.get()==LASTNAME) and passW.get()==PIN:
        if LASTNAME=="ADMIN" and PIN=="@13579@":
          note.tab(0, state="hidden")
          editGRAD.grid()
          note.select(8)
          userL1.config(text="Hello, "+FIRSTNAME+" "+LASTNAME+"!")
          userL2.config(text="Hello, "+FIRSTNAME+" "+LASTNAME+"!")
        else:
          note.tab(0, state="hidden")
          note.select(2)
          editGRAD.grid_remove()
        x = scoreOUT.get_children()
        for item in x:
          scoreOUT.delete(item)
        retSVal.set(str(len(scoreOUT.get_children()))+' item(s)')  
        tooltip(scoreOUT , [str(len(scoreOUT.get_children()))+' Course Unit(s)'])
        try:
          conn = sqlite3.connect('dbs/mjbgpadata.db')
          cursor = conn.cursor()
          sqlt = (str(userN.get()),)
          cursor.execute("SELECT * FROM tests WHERE NAME =?",sqlt)
          result = cursor.fetchall()
          for row in result:            
            scoreOUT.insert('', END, values=row)
          conn.close()
          retSVal.set(str(len(scoreOUT.get_children()))+' item(s)')  
        except Exception as e:
          print(e)
        finally:
          retSVal.set(str(len(scoreOUT.get_children()))+' item(s)') 
          tooltip(scoreOUT , [str(len(scoreOUT.get_children()))+' Course Unit(s)'])
        userL.config(text="Hello, "+str(FIRSTNAME)+" "+str(LASTNAME)+".")
        userL2.config(text="Hello, "+str(FIRSTNAME)+" "+str(LASTNAME)+".")
      else:
        messagebox.showerror("MjB-error bot", "Incorrect Last Name or Password!\n\nRetry or signup Now!")

    except Exception as e:
      print(e)
userN.bind('<Return>', login)
passW.bind('<Return>', login)

#-----------logi buttons-----------
lognn = PhotoImage(file='pics/login.png')
log = Button(rFrame, text="Login",command=login,image=lognn, cursor='hand2',bg="white",relief="flat")
log.grid(row=7, pady=10, padx=5, sticky=(W+E))
tip = tooltip(log , ["Click to login!"])


def Pwrd(event):
  foGt.config(fg="blue")
  note.tab(0, state="hidden")
  note.select(1)

def Pwrd1(event):
  foGt.config(fg="gray")

signp = PhotoImage(file='pics/signup.png')
foGt = Label(rFrame, image=signp, cursor='hand2', compound=LEFT,fg="gray",relief="flat",bg="white", font=("Verdana", 15,))
foGt.grid(row=8)
foGt.bind("<Button-1>", Pwrd)
foGt.bind("<ButtonRelease-1>", Pwrd1)
tip = tooltip(foGt , ["Create a new account now!"])
tip = tooltip(clock , [now])

def frgtE(*args):
  frgt.config(font=("arial", 10, 'bold'), fg="blue")
def frgtL(*args):
  frgt.config(font=("arial", 10, 'bold'), fg="gray")

frgt = Label(rFrame, text="Forgot Pin?", cursor="hand2", fg="gray", bg="white", font=("arial", 10, 'bold'))
frgt.grid(row=9)
frgt.bind("<Enter>",frgtE)
frgt.bind("<Leave>",frgtL)

#--------------sign up part---------------
Label(tab2, text="MjB CREATE ACCOUNT",fg="blue", bg="lightgray", font=("timesnewromans", 15, "bold")).pack(fill=X, anchor=NE)


#---------------sign up main, left and right frames---------------
sF1 = LabelFrame(tab2, bg="lightgray", text="BIO INFORMATION", relief="solid", bd=1, font=('arial', 12, 'bold'))
sF1.pack(pady=10)

progress = ttk.Progressbar(tab2, length=500)
progress.pack(pady=10)


sLF = Frame(sF1, bg="lightgray")
sLF.pack(side=LEFT, padx=10)
sRF = Frame(sF1, bg="lightgray", relief=SOLID)
sRF.pack(side=LEFT, padx=10, anchor=NE, fill=Y)

Label(sLF,text="FIRST NAME", font=("Verdana", 12,"bold"), bg="lightgray").grid(row=0, column=0, sticky=W)
Label(sLF,text="LAST NAME", font=("Verdana", 12,"bold"), bg="lightgray").grid(row=1, column=0, sticky=W)
Label(sLF,text="PHONE NO.", font=("Verdana", 12,"bold"), bg="lightgray").grid(row=2, column=0, sticky=W)
Label(sLF,text="UNIVERSITY", font=("Verdana", 12,"bold"), bg="lightgray").grid(row=3, column=0, sticky=W)
Label(sLF,text="PASSWORD", font=("Verdana", 12,"bold"), bg="lightgray").grid(row=4, column=0, sticky=W)
Label(sLF,text="CREATE PIN", font=("Verdana", 12,"bold"), bg="lightgray").grid(row=5, column=0, sticky=W)

fname = ttk.Entry(sLF)
fname.grid(row=0, column=1, sticky=W, padx=10, pady=10)
fname.config(font=("Verdana", 12,"bold"))
tip = tooltip(fname , ["First name required."])

lname = ttk.Entry(sLF)
lname.grid(row=1, column=1, sticky=W, padx=10, pady=10)
lname.config(font=("Verdana", 12,"bold"))
tip = tooltip(lname , ["Last name required."])

pnumber = ttk.Entry(sLF)
pnumber.grid(row=2, column=1, sticky=W, padx=10, pady=10)
pnumber.config(font=("Verdana", 12,"bold"))
tooltip(pnumber , ["Will help reset your PIN."])

univ = ttk.Entry(sLF)
univ.grid(row=3, column=1, sticky=W, padx=10, pady=10)
univ.config(font=("Verdana", 12,"bold"))
tip = tooltip(univ , ["University is required."])

passw = ttk.Entry(sLF,show="*")
passw.grid(row=4, column=1, sticky=W, padx=10, pady=10)
passw.config(font=("Verdana", 12,"bold"))
tip = tooltip(passw , ["Choose a strong password."])

pin = ttk.Entry(sLF, state="disabled",show="•")
pin.grid(row=5, column=1, sticky=W, padx=10, pady=10)
pin.config(font=("Verdana", 12,"bold"))
tip = tooltip(pin, ["Use the number pad on the right."])

msginfo = Label(sLF,bg="lightgray", font=("Verdana", 8,"bold","italic"))
msginfo.grid(row=6,columnspan=2)

def bt1E(*args):
  btL1.config(fg="blue")
def bt1L(*args):
  btL1.config(fg="black")
def bt2E(*args):
  btL2.config(fg="blue")
def bt2L(*args):
  btL2.config(fg="black") 
def bt3E(*args):
  btL3.config(fg="blue")
def bt3L(*args):
  btL3.config(fg="black")
def bt4E(*args):
  btL4.config(fg="blue")
def bt4L(*args):
  btL4.config(fg="black")
def bt5E(*args):
  btL5.config(fg="blue")
def bt5L(*args):
  btL5.config(fg="black")
def bt6E(*args):
  btL6.config(fg="blue")
def bt6L(*args):
  btL6.config(fg="black")
def bt7E(*args):
  btL7.config(fg="blue")
def bt7L(*args):
  btL7.config(fg="black")
def bt8E(*args):
  btL8.config(fg="blue")
def bt8L(*args):
  btL8.config(fg="black")
def bt9E(*args):
  btL9.config(fg="blue")
def bt9L(*args):
  btL9.config(fg="black")
def bt0E(*args):
  btL0.config(fg="blue")
def bt0L(*args):
  btL0.config(fg="black")

#------------pin starts here--------
def getPin1(*args):
  pin.config(state="normal")
  pin.insert(END, "1")
  pin.config(state="disabled")
btL1 = Button(sRF, text="1", command=getPin1,bg="lightgray", width=5, relief="flat", font=("Verdana", 12,"bold"))
btL1.grid(row=1, column=0, padx=10, pady=10)
btL1.bind("<Enter>",bt1E)
btL1.bind("<Leave>",bt1L)

def getPin2(*args):
  pin.config(state="normal")
  pin.insert(END, "2")
  pin.config(state="disabled")
btL2 = Button(sRF, text="2", command=getPin2,bg="lightgray", width=5, relief="flat", font=("Verdana", 12,"bold"))
btL2.grid(row=1, column=1, padx=10, pady=10)
btL2.bind("<Enter>",bt2E)
btL2.bind("<Leave>",bt2L)
def getPin3(*args):
  pin.config(state="normal")
  pin.insert(END, "3")
  pin.config(state="disabled")
btL3 = Button(sRF, text="3", command=getPin3,bg="lightgray", width=5, relief="flat", font=("Verdana", 12,"bold"))
btL3.grid(row=1, column=2)
btL3.bind("<Enter>",bt3E)
btL3.bind("<Leave>",bt3L)
def getPin4(*args):
  pin.config(state="normal")
  pin.insert(END, "4")
  pin.config(state="disabled")
btL4 = Button(sRF, text="4", command=getPin4,bg="lightgray", width=5, relief="flat", font=("Verdana", 12,"bold"))
btL4.grid(row=2, column=0, padx=10, pady=10)
btL4.bind("<Enter>",bt4E)
btL4.bind("<Leave>",bt4L)
def getPin5(*args):
  pin.config(state="normal")
  pin.insert(END, "5")
  pin.config(state="disabled")
btL5 = Button(sRF, text="5", command=getPin5,bg="lightgray", width=5, relief="flat", font=("Verdana", 12,"bold"))
btL5.grid(row=2, column=1, padx=10, pady=10)
btL5.bind("<Enter>",bt5E)
btL5.bind("<Leave>",bt5L)
def getPin6(*args):
  pin.config(state="normal")
  pin.insert(END, "6")
  pin.config(state="disabled")
btL6 = Button(sRF, text="6", command=getPin6,bg="lightgray", width=5, relief="flat", font=("Verdana", 12,"bold"))
btL6.grid(row=2, column=2, padx=10, pady=10)
btL6.bind("<Enter>",bt6E)
btL6.bind("<Leave>",bt6L)
def getPin7(*args):
  pin.config(state="normal")
  pin.insert(END, "7")
  pin.config(state="disabled")
btL7 = Button(sRF, text="7", command=getPin7,bg="lightgray", width=5, relief="flat", font=("Verdana", 12,"bold"))
btL7.grid(row=3, column=0, padx=10, pady=10)
btL7.bind("<Enter>",bt7E)
btL7.bind("<Leave>",bt7L)
def getPin8(*args):
  pin.config(state="normal")
  pin.insert(END, "8")
  pin.config(state="disabled")
btL8 = Button(sRF, text="8", command=getPin8,bg="lightgray", width=5, relief="flat", font=("Verdana", 12,"bold"))
btL8.grid(row=3, column=1, padx=10, pady=10)
btL8.bind("<Enter>",bt8E)
btL8.bind("<Leave>",bt8L)
def getPin9(*args):
  pin.config(state="normal")
  pin.insert(END, "9")
  pin.config(state="disabled")
btL9 = Button(sRF, text="9", command=getPin9,bg="lightgray", width=5, relief="flat", font=("Verdana", 12,"bold"))
btL9.grid(row=3, column=2, padx=10, pady=10)
btL9.bind("<Enter>",bt9E)
btL9.bind("<Leave>",bt9L)
def getPin0(*args):
  pin.config(state="normal")
  pin.insert(END, "0")
  pin.config(state="disabled")
btL0 = Button(sRF, text="0", command=getPin0,bg="lightgray", width=5, relief="flat", font=("Verdana", 12,"bold"))
btL0.grid(row=4, column=1, padx=10, pady=10)
btL0.bind("<Enter>",bt0E)
btL0.bind("<Leave>",bt0L)
def delPin(*args):
  pin.config(state="normal")
  pin.delete(0, END)
  pin.config(state="disabled")
btdel = Button(sRF, text="x",fg="red", command=delPin,bg="lightgray", width=5, relief="flat", font=("Verdana", 12,"bold"))
btdel.grid(row=4, column=2, padx=10, pady=10)
tip = tooltip(btdel , ["Resets PIN entry."])


def signUpev(*args):
  msginfo.config(text="")
fname.bind("<Button-1>", signUpev)
lname.bind("<Button-1>", signUpev)
passw.bind("<Button-1>", signUpev)
pin.bind("<Button-1>", signUpev)
univ.bind("<Button-1>", signUpev)
pnumber.bind("<Button-1>", signUpev)
fname.bind("<KeyPress>", signUpev)
lname.bind("<KeyPress>", signUpev)
passw.bind("<KeyPress>", signUpev)
pnumber.bind("<KeyPress>", signUpev)
pin.bind("<KeyPress>", signUpev)
univ.bind("<KeyPress>", signUpev)
fname.bind("<KeyRelease>", signUpev)
lname.bind("<KeyRelease>", signUpev)
passw.bind("<KeyRelease>", signUpev)
pin.bind("<KeyRelease>", signUpev)
pnumber.bind("<KeyRelease>", signUpev)
univ.bind("<KeyRelease>", signUpev)


def submitS(*args):
  signUpev()
  try:
    if(fname.get()==""):
      msginfo.config(text="Please fill out all the fields.", fg="red")
      fname.focus()
    elif(lname.get()==""):
      msginfo.config(text="Please fill out all the fields.", fg="red")
      lname.focus()
    elif(pnumber.get()==""):
      msginfo.config(text="Please fill out all the fields.", fg="red")
      pno.focus()
    elif(len(pnumber.get())<10):
      msginfo.config(text="Hone number should have atleast 10 digits.", fg="red")
      pnumber.focus()
    elif(univ.get()==""):
      msginfo.config(text="Please fill out all the fields.", fg="red")
      univ.focus()
    elif(passw.get()==""):
      msginfo.config(text="Create password please.", fg="red")
      passw.focus()
    elif(pin.get()==""):
      msginfo.config(text="Create pin please.", fg="red")
    elif(int(len(pin.get())<4)):
      msginfo.config(text="Pin length should atleast be 4.", fg="red")

    else:
      conn = sqlite3.connect('dbs/mjbgpadata.db')
      print("Opened database successfully")
      conn.execute('''CREATE TABLE IF NOT EXISTS accounts
      (FIRSTNAME VARCHAR NOT NULL,
      LASTNAME VARCHAR NOT NULL,
      PHONE_NO VARCHAR NOT NULL,
      UNIVERSITY VARCHAR NOT NULL,
      PASSWORD VARCHAR NOT NULL,
      PIN VARCHAR NOT NULL)''')    
      print("Table created successfully")
      
      sql1 = ("INSERT INTO accounts (FIRSTNAME, LASTNAME, PHONE_NO, UNIVERSITY,PASSWORD, PIN)VALUES (?,?,?,?,?,?)")
      firstN = (fname.get()).upper()
      lastN = (lname.get()).upper()
      univer = (univ.get()).upper()
      sql2 = (firstN, lastN, pnumber.get(),univer , passw.get(), pin.get())
      conn.execute(sql1, sql2)
      conn.commit()
      filelist = range(4)
      step = trunc(100/len(filelist))

      def MAIN():
        for x in filelist:
          sleep(1)
          progress.step(step)
          progress.update()
      progress.after(5, MAIN)
      conn.close()
      messagebox.showinfo("MjB-Login bot!", "Account created successfully!\n\nYou`re about to be redirected to login now?")
      note.tab(1, state="hidden")
      note.select(0)
      fname.delete(0, END)
      lname.delete(0, END)
      univ.delete(0, END)
      passw.delete(0, END)
      pnumber.delete(0, END)
      pin.config(state='normal')
      pin.delete(0, END)
      pin.config(state='disabled')
  except Exception as e:
    print(e)
  finally:
    try:
      conn = sqlite3.connect('dbs/mjbgpadata.db')
      cursor = conn.cursor()
      cursor.execute('SELECT LASTNAME FROM accounts')
      result = cursor.fetchall()
      userN.config(values=result)
    except Exception as e:
      raise e
def logN():
  note.tab(1, state="hidden")
  note.select(0)
  fname.delete(0, END)
  lname.delete(0, END)
  univ.delete(0, END)
  passw.delete(0, END)
  pnumber.delete(0, END)
  pin.config(state='normal')
  pin.delete(0, END)
  pin.config(state='disabled')

go = ttk.Button(sLF, text="Submit", command=submitS)
go.grid(row=7, column=1, pady=10, sticky=E)
ttk.Button(sLF, text="Login Instead", command=logN).grid(row=7, column=1, pady=10, sticky=W)
tip = tooltip(go , ["By Submiting, you agree to create a new account!"])




#-------------------home page starts here--------------------
Hfr = Frame(tab3, relief=SOLID, bd=1, bg="gray")
Hfr.pack(fill=BOTH, padx=20, pady=20)
userL = Label(Hfr, text="Hello User.", font=('arial',18,"bold"), bg="lightgray", fg="blue")
userL.pack(fill=X)
Label(Hfr, text="Welcome to the MjB GPA APP, This tool will help you monitor your scores forever!", font=('arial',15,"italic"), bg="white", fg="blue").pack(fill=X)


headF = Frame(Hfr, bg="lightgray")
headF.pack(padx=5, pady=20)
svar = StringVar()
svar1 = StringVar()
deli = 1000

def shif():
  shif.msg = shif.msg[1:]+shif.msg[0]
  svar.set(shif.msg)
  svar1.set(shif.msg)
  gpa.after(deli, shif)

def sign():
  try:
      
    shif.msg =  "    DASHBORD TO AVAILABLE TOOLS.            " 
    shif()  
    darsh.config(textvariable=svar, font=('arial',15,"bold"), fg="white", bg="black") 
    darsh1.config(textvariable=svar1, font=('arial',15,"bold"), fg="white", bg="black")   
  
  except Exception as e:
    print(e)

darsh = Label(headF, font=('arial',15,"bold"), fg="white", bg="black")
darsh.pack(side=TOP, anchor=N, fill=X)




LHf = LabelFrame(headF, text="TOOL PAGES",bg="light gray", font=('times',12,"bold"))
LHf.pack(side=LEFT, fill=Y, pady=5, padx=5)
Label(LHf, text="MjB MAIN PAGES.", fg="white", bg="black", font=('arial',12,"bold")).grid(row=0, columnspan=2, sticky=(W+E))

def gototest(*args):
  note.select(3)
  x = scoreOUT.get_children()
  for item in x:
    scoreOUT.delete(item)
  retSVal.set(str(len(scoreOUT.get_children()))+' item(s)')
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    sqlt = (str(userN.get()),)
    cursor.execute("SELECT * FROM tests WHERE NAME =?",sqlt)
    result = cursor.fetchall()
    for row in result:
      scoreOUT.insert('', END, values=row)
    conn.close()
    retSVal.set(str(len(scoreOUT.get_children()))+' item(s)')  
  except Exception as e:
    print(e)
  finally:
    retSVal.set(str(len(scoreOUT.get_children()))+' item(s)') 

def gpPE(*args):
  gpP.config(fg="dim gray", relief="solid", bd=1, bg="white", text="MARKS ENTRY PAGE", font=('arial',12,"bold"))
def gpPL(*args):
  gpP.config(relief="flat", bg="dim gray", fg="white", text="MARKS ENTRY PAGE")
gpP = Button(LHf, text="MARKS ENTRY PAGE", relief="flat",cursor="hand2", width=18, bd=1, bg="dim gray", fg="white", font=('arial',12,"bold"))
gpP.grid(row=1, columnspan=2, pady=10)
gpP.bind("<Enter>", gpPE)
gpP.bind("<Leave>", gpPL)
gpP.bind("<1>",gototest)


def cgpaPE(*args):
  cgpaP.config(fg="dim gray", relief="solid", bd=1, bg="white", text="GPA & CGPA PAGE", font=('arial',12,"bold"))
def cgpaPL(*args):
  cgpaP.config(relief="flat", bg="dim gray",cursor="hand2", fg="white", text="GPA & CGPA PAGE")
def gotoGPA1():
  note.select(10)

cgpaP = Button(LHf, text="GPA & CGPA PAGE", command=gotoGPA1, relief="flat",cursor="hand2", width=18, bd=1, bg="dim gray", fg="white", font=('arial',12,"bold"))
cgpaP.grid(row=2, columnspan=2, pady=10, padx=10)
cgpaP.bind("<Enter>", cgpaPE)
cgpaP.bind("<Leave>", cgpaPL)

def gotoGrade():
  note.select(9)


def contPE(*args):
  contAPa.config(fg="dim gray", relief="solid", bd=1, bg="white", text="GRADING SYSTEM", font=('arial',12,"bold"))
def contPL(*args):
  contAPa.config(relief="flat", bg="dim gray",cursor="hand2", fg="white", text="GRADING SYSTEM")
contAPa = Button(LHf, text="GRADING SYSTEM", relief="flat", command=gotoGrade,cursor="hand2", width=18, bd=1, bg="dim gray", fg="white", font=('arial',12,"bold"))
contAPa.grid(row=3, columnspan=2, pady=10, padx=10)
contAPa.bind("<Enter>", contPE)
contAPa.bind("<Leave>", contPL)


RHff = LabelFrame(headF, text="ACTION PAGES.", bg="light gray", font=('times',12,"bold"))
RHff.pack(side=RIGHT, fill=Y, anchor=E, pady=5, padx=5)


RHf = Frame(headF, bg="light gray")
RHf.pack(side=RIGHT, fill=Y, anchor=W, pady=5)

rghtpic = PhotoImage(file="pics/back.png")
Label(RHf, image=rghtpic, compound=TOP, fg="white", bg="light gray").pack(fill=Y)

#------------------------dash actions-------------------
tips = Label(RHff, text="MjB OTHER PAGES.", fg="white", bg="black", width=20, font=('arial',12,"bold"))
tips.grid(row=3, columnspan=2, sticky=(W+E))

def contPE(*args):
  contP.config(fg="dim gray", relief="solid", bd=1, bg="white", text="CONTACT US", font=('arial',12,"bold"))
def contPL(*args):
  contP.config(relief="flat", bg="dim gray",cursor="hand2", fg="white", text="CONTACT US")
contP = Button(RHff, text="CONTACT US", relief="flat",cursor="hand2", width=20, bd=1, bg="dim gray", fg="white", font=('arial',12,"bold"))
contP.grid(row=4, column=0, pady=10, padx=10)
contP.bind("<Enter>", contPE)
contP.bind("<Leave>", contPL)


def devPE(*args):
  devP.config(fg="dim gray", relief="solid", bd=1, bg="white", text="DEVELOPER", font=('arial',12,"bold"))
def devPL(*args):
  devP.config(relief="flat", bg="dim gray",cursor="hand2", fg="white", text="DEVELOPER")
devP = Button(RHff, text="DEVELOPER", relief="flat",cursor="hand2", width=20, bd=1, bg="dim gray", fg="white", font=('arial',12,"bold"))
devP.grid(row=5, column=0, pady=10, padx=10)
devP.bind("<Enter>", devPE)
devP.bind("<Leave>", devPL)

def manPE(*args):
  manP.config(fg="dim gray", relief="solid", bd=1, bg="white", text="MANNUAL", font=('arial',12,"bold"))
def manPL(*args):
  manP.config(relief="flat", bg="dim gray",cursor="hand2", fg="white", text="MANNUAL")
manP = Button(RHff, text="MANNUAL", relief="flat",cursor="hand2", width=20, bd=1, bg="dim gray", fg="white", font=('arial',12,"bold"))
manP.grid(row=6, column=0, pady=10, padx=10)
manP.bind("<Enter>", manPE)
manP.bind("<Leave>", manPL)


#--------------------dash admin action pages---------------

Hfr1 = Frame(tab9, relief=SOLID, bd=1, bg="gray")
Hfr1.pack(fill=BOTH, padx=20, pady=20)

userL1 = Label(Hfr1, text="Hello User.", font=('arial',18,"bold"), bg="lightgray", fg="blue")
userL1.pack(fill=X)
Label(Hfr1, text="Welcome to the MjB GPA APP, This tool will help you monitor your scores forever!", font=('arial',15,"italic"), bg="white", fg="blue").pack(fill=X)

headF1 = Frame(Hfr1 , bg="lightgray")
headF1.pack(padx=5, pady=20, side=TOP, anchor=N)


darsh1 = Label(headF1, font=('arial',15,"bold"), fg="white", bg="black")
darsh1.pack(side=TOP, anchor=N, fill=X)
if __name__ == '__main__':
  sign()

ll1 = Frame(headF1, )
ll1.pack()

RHff1 = LabelFrame(ll1, text="ACTION PAGES.", font=('times',12,"bold"))
RHff1.pack(side=RIGHT, fill=Y, anchor=E, pady=5, padx=5)

LHf1 = LabelFrame(ll1, text="TOOL PAGES", font=('times',12,"bold"))
LHf1.pack(side=LEFT, fill=Y, pady=5, padx=5)
Label(LHf1, text="MjB ADMIN PAGES.", fg="white", bg="black", font=('arial',12,"bold")).grid(row=0, columnspan=2, sticky=(W+E))


def gpPE(*args):
  gpPA.config(fg="dim gray", relief="solid", bd=1, bg="white", text="MARKS ENTRY PAGE", font=('arial',12,"bold"))
def gpPL(*args):
  gpPA.config(relief="flat", bg="dim gray", fg="white", text="MARKS ENTRY PAGE")
gpPA = Button(LHf1, text="MARKS ENTRY PAGE", relief="flat",cursor="hand2", width=20, bd=1, bg="dim gray", fg="white", font=('arial',12,"bold"))
gpPA.grid(row=1, columnspan=2, pady=10)
gpPA.bind("<Enter>", gpPE)
gpPA.bind("<Leave>", gpPL)
gpPA.bind("<1>",gototest)


def cgpaPE(*args):
  cgpaPA.config(fg="dim gray", relief="solid", bd=1, bg="white", text="GPA & CGPA PAGE", font=('arial',12,"bold"))
def cgpaPL(*args):
  cgpaPA.config(relief="flat", bg="dim gray",cursor="hand2", fg="white", text="GPA & CGPA PAGE")
def gotoGPA():
  note.select(10)

cgpaPA = Button(LHf1, text="GPA & CGPA PAGE", command=gotoGPA, relief="flat",cursor="hand2", width=20, bd=1, bg="dim gray", fg="white", font=('arial',12,"bold"))
cgpaPA.grid(row=2, columnspan=2, pady=10, padx=10)
cgpaPA.bind("<Enter>", cgpaPE)
cgpaPA.bind("<Leave>", cgpaPL)

#---------------------admin action pages----------

tips = Label(RHff1, text="MjB OTHER PAGES.", fg="white", width=20, bg="black", font=('arial',12,"bold"))
tips.grid(row=0, columnspan=2, sticky=(W+E))

def contPE(*args):
  contAP.config(fg="gray", relief="solid", bd=1, bg="white", text="GRADING SYSTEM", font=('arial',12,"bold"))
def contPL(*args):
  contAP.config(relief="flat", bg="gray",cursor="hand2", fg="white", text="GRADING SYSTEM")
contAP = Button(RHff1, text="GRADING SYSTEM", relief="flat", command=gotoGrade,cursor="hand2", width=20, bd=1, bg="dim gray", fg="white", font=('arial',12,"bold"))
contAP.grid(row=1, column=0, pady=10, padx=10)
contAP.bind("<Enter>", contPE)
contAP.bind("<Leave>", contPL)

def manAPE(*args):
  manAP.config(fg="dim gray", relief="solid", bd=1, bg="white", text="MANNUAL", font=('arial',12,"bold"))
def manAPL(*args):
  manAP.config(relief="flat", bg="dim gray",cursor="hand2", fg="white", text="MANNUAL")
manAP = Button(RHff1, text="MANNUAL", relief="flat",cursor="hand2", bd=1, bg="dim gray", fg="white", font=('arial',12,"bold"))
manAP.grid(row=2, column=0, pady=10, padx=10, sticky=(W+E))
manAP.bind("<Enter>", manAPE)
manAP.bind("<Leave>", manAPL)
#------------------gpa and cgpa page--------------------
def clear():
  gpaYrVal.set(value="--Select--")
  cgpaYrVal.set(value="--Select--")
  gpaSemVal.set(value="--Select--")
  msginfo12.config(text='')
  msginfo2.config(text='')
  gpaRES.config(text='')
  cgpaRES.config(text='')
  degWRES.config(text='')
  degCRES.config(text='')
def hideGPA(*arsg):
  clear()
  note.tab(10, state="hidden")

Button(tab11,bg="red", fg="white", text="X", command=hideGPA, font=('arial',10,"bold"), relief=FLAT).pack(side=RIGHT, anchor=N)
Hfr2 = Frame(tab11, relief=SOLID, bd=1, bg="gray")
Hfr2.pack(fill=BOTH, padx=20, pady=20)

userL2 = Label(Hfr2, text="Hello User.", font=('arial',18,"bold"), bg="lightgray", fg="blue")
userL2.pack(fill=X)
Label(Hfr2, text="Here are the overall results, choose what you want to see!", font=('arial',15,"italic"), bg="white", fg="blue").pack(fill=X)

headF2 = Frame(Hfr2, bg="lightgray")
headF2.pack(padx=5, pady=20, side=TOP, anchor=N)

#----------------gpa view-------------------
gpaF = LabelFrame(headF2, )
gpaF.grid(row=0, column=0, sticky=(W+E+N+S), pady=10, padx=10)

Label(gpaF, text="GPA RESULTS.", fg="white", bg="black", font=('arial',12,"bold")).grid(row=0, columnspan=2, sticky=(W+E))

Label(gpaF, text="SELECT YEAR", fg="white", bg="blue", font=('arial',12,"bold")).grid(row=1, column=0, sticky=(W+E), pady=5, padx=5)

Label(gpaF, text="SEMESTER", fg="white", bg="blue", font=('arial',12,"bold")).grid(row=1, column=1, sticky=(W+E), pady=5, padx=5)

#-------------YEAR ENTRIES------------
def strict3(*args):
  gpaYr.delete(11, END)
  gpaYrVal.set(value="--Select--")
  msginfo12.config(text='Select from list please!')

def click3(*args):
  msginfo12.config(text='')
  msginfo2.config(text='')


gpaYrVal = StringVar()
yrvals = ['One','Two','Three','Four']
gpaYr = ttk.Combobox(gpaF, font=('arial', 10, 'bold'), textvariable=gpaYrVal,width=14, values=yrvals, justify="center")
gpaYr.grid(row=2, column=0, pady=5, padx=5)
gpaYrVal.set(value="--Select--")
gpaYr.bind('<KeyPress>', strict3)
gpaYr.bind('<KeyRelease>', strict3)
gpaYr.bind('<1>', click3)

#-------------SEMESTER ENTRIES------------
def strict2(*args):
  gpaSem.delete(11, END)
  gpaSemVal.set(value="--Select--")
  msginfo12.config(text='Select from list please!')

def click2(*args):
  msginfo12.config(text='')
  msginfo2.config(text='')

gpaSemVal = StringVar()
semvals = ['One','Two']
gpaSem = ttk.Combobox(gpaF, font=('arial', 10, 'bold'), textvariable=gpaSemVal,width=10, values=semvals, justify="center")
gpaSem.grid(row=2, column=1, pady=5, padx=5)
gpaSemVal.set(value="--Select--")
gpaSem.bind('<KeyPress>', strict2)
gpaSem.bind('<KeyRelease>', strict2)
gpaSem.bind('<1>', click2)

msginfo12 = Label(gpaF, text="", fg='red', font=('arial', 8, 'bold', 'italic'))
msginfo12.grid(row=3, columnspan=2)

def hooverB(*args):
  fetchBt.config(bg="white", fg="green", relief=SOLID, bd=1)
def leaveB(*args):
  fetchBt.config(bg="green", fg="white", relief=FLAT, bd=1)

#------------------fetch scores button----------------
fetchBt = Button(gpaF, text="   FETCH   ",bg="green", fg="white", font=('arial', 10, 'bold'), bd=1, relief="flat")
fetchBt.grid(row=4, columnspan=2, pady=5, padx=5)
fetchBt.bind("<Enter>",hooverB)
fetchBt.bind("<Leave>",leaveB)

#---------------------results display-7--------------
gpaRES = Label(gpaF, text="", fg="black", bg="white", relief=GROOVE,  font=('arial',20,"bold"))
gpaRES.grid(row=5, columnspan=2, sticky=(W+E), pady=10, padx=10)


#----------------cgpa view-------------------
cgpaF = LabelFrame(headF2, )
cgpaF.grid(row=0, column=1, sticky=(W+E+N+S), pady=10)
Label(cgpaF, text="CGPA RESULTS.", fg="white", bg="black", font=('arial',12,"bold")).grid(row=0, columnspan=2, sticky=(W+E))

Label(cgpaF, text="SELECT YEAR", fg="white", bg="blue", font=('arial',12,"bold")).grid(row=1, columnspan=2, sticky=(W+E), pady=5, padx=5)

#-------------YEAR ENTRIES------------

def strict1(*args):
  cgpaYr.delete(11, END)
  cgpaYrVal.set(value="--Select--")
  msginfo2.config(text='Select from list please!')

def click1(*args):
  msginfo2.config(text='')
  msginfo12.config(text='')

cgpaYrVal = StringVar()
yrval = ['One','Two','Three','Four','Total']
cgpaYr = ttk.Combobox(cgpaF, font=('arial', 10, 'bold'), textvariable=cgpaYrVal,width=14, values=yrval, justify="center")
cgpaYr.grid(row=2, column=0, pady=5, padx=5)
cgpaYrVal.set(value="--Select--")
cgpaYr.bind('<KeyPress>',strict1)
cgpaYr.bind('<KeyRelease>',strict1)
cgpaYr.bind('<1>',click1)

msginfo2 = Label(cgpaF, text="", fg='red', font=('arial', 8, 'bold', 'italic'))
msginfo2.grid(row=3, columnspan=2)

#------------------fetch scores button----------------
def hooverB1(*args):
  fetchBt1.config(bg="white", fg="green", relief=SOLID, bd=1)
def leaveB1(*args):
  fetchBt1.config(bg="green", fg="white", relief=FLAT, bd=1)

fetchBt1 = Button(cgpaF, text="   FETCH   ",bg="green", fg="white", font=('arial', 10, 'bold'), bd=1, relief="flat")
fetchBt1.grid(row=4, columnspan=2, pady=5, padx=5)
fetchBt1.bind("<Enter>",hooverB1)
fetchBt1.bind("<Leave>",leaveB1)

#---------------------results display---------------
cgpaRES = Label(cgpaF, text="", fg="black", bg="white", relief=GROOVE,  font=('arial',20,"bold"))
cgpaRES.grid(row=5, columnspan=2, sticky=(W+E), pady=10, padx=10)


#----------------degree view-------------------
degF = LabelFrame(headF2, )
degF.grid(row=0, column=2, sticky=(W+E+N+S), pady=10, padx=10)
Label(degF, text="DEGREE RESULTS.", fg="white", bg="black", font=('arial',12,"bold")).grid(row=0, columnspan=2, sticky=(W+E))

Label(degF, text="WEIGHT", fg="white",width=26, bg="blue", font=('arial',12,"bold")).grid(row=1, columnspan=2, sticky=(W+E), pady=5, padx=5)
#---------------------results display---------------
degWRES = Label(degF, text="", fg="black", bg="white", relief=FLAT,  font=('arial',20,"bold"))
degWRES.grid(row=2, columnspan=2, sticky=(W+E), pady=5, padx=10)

Label(degF, text="CLASS", fg="white", bg="blue", font=('arial',12,"bold")).grid(row=3, columnspan=2, sticky=(W+E), pady=5, padx=5)
#---------------------results display---------------
degCRES = Label(degF, text="", fg="black", bg="white", relief=FLAT,  font=('arial',20,"bold"))
degCRES.grid(row=4, columnspan=2, sticky=(W+E), pady=5, padx=10)


#------------------grading system------------------
#------------------grading system table database------------------
def gradingSyS(*args):
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS grading (ID INTEGER PRIMARY KEY  AUTOINCREMENT, fro_Score INTEGER NOT NULL , to_Score INTEGER NOT NULL , let_Score VARCHAR NOT NULL , weg_Score VARCHAR NOT NULL )')
    print('Grading tests table created.')

    insertSql1 = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
    letter1=('80','100','A','5.0')
    insertSql2 = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
    letter2=('75','79.9','B+','4.5')
    insertSql3 = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
    letter3=('70','74.9','B','4.0')
    insertSql4 = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
    letter4=('65','69.9','C+','3.5')
    insertSql5 = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
    letter5=('60','64.9','C','3.0')
    insertSql6 = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
    letter6=('55','59.9','D+','2.5')
    insertSql7 = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
    letter7=('50','54.9','D','2.0')
    insertSql8 = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
    letter8=('00','49.9','F','0.0')

    cursor.execute(insertSql1,letter1)
    cursor.execute(insertSql2,letter2)
    cursor.execute(insertSql3,letter3)
    cursor.execute(insertSql4,letter4)
    cursor.execute(insertSql5,letter5)
    cursor.execute(insertSql6,letter6)
    cursor.execute(insertSql7,letter7)
    cursor.execute(insertSql8,letter8)
    print('All added successfully!')
    conn.commit()
  except Exception as e:
    pass
gradingSyS()

hideF = Frame(tab10)
hideF.pack(side=TOP, fill=X)
Label(hideF, text="UNIVERSITY GRADING SYSTEM", font=('arial', 18, "bold"), bg="lightgray", fg="blue").pack(fill=X)

def hideGRADING(*args):
  note.tab(9, state="hidden")

hideSYS = Button(hideF, text="X",command=hideGRADING, relief=FLAT, font=("arial", 8,"bold"), fg="white", bg="red")
hideSYS.pack(side=RIGHT, fill=X)

gradeF = Frame(tab10, bg="lightgray")
gradeF.pack(padx=10, pady=10)
editF = Frame(gradeF,width=10, height=10, bg='red')
editF.grid(padx=10, pady=10, row=0, column=0, sticky=(N+S))
savedF1 = Frame(gradeF)
savedF1.grid(padx=10, pady=10,row=0, column=1, sticky=(N+S))
editF.grid_remove()

#-----------------------edit grade button----------
def editSCALE():
  editF.grid()
  editGRAD.grid_remove()
  UpdateB.grid()
  UpdateB1.grid()


edPic = PhotoImage(file='pics/ed.png')
editGRAD = Button(gradeF, text=" EDIT ",cursor="hand2", command=editSCALE, image=edPic,compound=LEFT, relief=SOLID, bd=1, fg="white", bg="brown", font=('arial',10,"bold"))
editGRAD.grid(row=1, column=1, padx=5, pady=5)

#------------------edit grading system----------------
Label(editF, text="EDIT GRADING SYSTEM", fg="white", bg="black", font=('arial',12,"bold")).grid(row=0, sticky=(W+E))

savedF2 = LabelFrame(editF, bg="lavender")
savedF2.grid(row=1)

Label(savedF2, text="Score Range.", bg="saddle brown", fg="white", font=('arial',12,"bold")).grid(row=0,columnspan=2, column=0, sticky=(W+E), padx=2, pady=2)
Label(savedF2, text=" From ", bg="saddle brown", fg="white", font=('arial',8,"bold",'italic')).grid(row=1,column=0, sticky=(W+E), padx=2, pady=2)
Label(savedF2, text=" To ", bg="saddle brown", fg="white", font=('arial',8,"bold",'italic')).grid(row=1,column=1, sticky=(W+E), padx=2, pady=2)

#----------------scale score values---------------
#---------------1. SCORES------------------
#--------------first score value (from)-----------------
from1 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
from1.grid(row=2, column=0, pady=2, padx=5)
from2 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
from2.grid(row=3, column=0, pady=2, padx=5)
from3 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
from3.grid(row=4, column=0, pady=2, padx=5)
from4 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
from4.grid(row=5, column=0, pady=2, padx=5)
from5 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
from5.grid(row=6, column=0, pady=2, padx=5)
from6 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
from6.grid(row=7, column=0, pady=2, padx=5)
from7 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
from7.grid(row=8, column=0, pady=2, padx=5)
from8 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
from8.grid(row=9, column=0, pady=2, padx=5)

#--------------last score value (to)-----------------
to1 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
to1.grid(row=2, column=1, pady=2, padx=5)
to2 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
to2.grid(row=3, column=1, pady=2, padx=5)
to3 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
to3.grid(row=4, column=1, pady=2, padx=5)
to4 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
to4.grid(row=5, column=1, pady=2, padx=5)
to5 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
to5.grid(row=6, column=1, pady=2, padx=5)
to6 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
to6.grid(row=7, column=1, pady=2, padx=5)
to7 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
to7.grid(row=8, column=1, pady=2, padx=5)
to8 = ttk.Entry(savedF2, font=('arial', 10, 'bold'), width=4, justify="center")
to8.grid(row=9, column=1, pady=2, padx=5)

#---------------2. SCORES LETTERS------------------
Label(savedF2, text="Grade letter.", bg="saddle brown", fg="white", font=('arial',12,"bold")).grid(row=0,columnspan=1, column=3, sticky=(W+E))
valz = ['A','B+','B','C+','C','D+','D','F']

let1 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz, width=3, justify="center")
let1.grid(row=2, column=3, pady=2, padx=5)

let2 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz, width=3, justify="center")
let2.grid(row=3, column=3, pady=2, padx=5)

let3 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz, width=3, justify="center")
let3.grid(row=4, column=3, pady=2, padx=5)

let4 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz, width=3, justify="center")
let4.grid(row=5, column=3, pady=2, padx=5)

let5 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz, width=3, justify="center")
let5.grid(row=6, column=3, pady=2, padx=5)

let6 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz, width=3, justify="center")
let6.grid(row=7, column=3, pady=2, padx=5)

let7 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz, width=3, justify="center")
let7.grid(row=8, column=3, pady=2, padx=5)

let8 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz, width=3, justify="center")
let8.grid(row=9, column=3, pady=2, padx=5)


#---------------3.  LETTERS WEIGHT------------------
Label(savedF2, text="Letter Weight.", bg="saddle brown", fg="white", font=('arial',12,"bold")).grid(row=0,columnspan=1, column=4, sticky=(W+E), padx=2, pady=2)
valz1 = ['5.0','4.5','4.0','3.5','3.0','2.5','2.0','1.0']

weg1 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz1, width=3, justify="center")
weg1.grid(row=2, column=4, pady=2, padx=5)

weg2 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz1, width=3, justify="center")
weg2.grid(row=3, column=4, pady=2, padx=5)

weg3 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz1, width=3, justify="center")
weg3.grid(row=4, column=4, pady=2, padx=5)

weg4 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz1, width=3, justify="center")
weg4.grid(row=5, column=4, pady=2, padx=5)

weg5 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz1, width=3, justify="center")
weg5.grid(row=6, column=4, pady=2, padx=5)

weg6 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz1, width=3, justify="center")
weg6.grid(row=7, column=4, pady=2, padx=5)

weg7 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz1, width=3, justify="center")
weg7.grid(row=8, column=4, pady=2, padx=5)

weg8 = ttk.Combobox(savedF2, font=('arial', 10, 'bold'), values=valz1, width=3, justify="center")
weg8.grid(row=9, column=4, pady=2, padx=5)


#--------------------update button-----------------
updI = PhotoImage(file="pics/upd.png")
UpdateB = Button(gradeF, text="  UPDATE ", font=('arial',10,"bold"), cursor='hand2', image=updI,compound=LEFT, relief=SOLID, bd=1, fg="white", bg="blue")
UpdateB.grid(row=1, column=0, padx=5, pady=5)
UpdateB.grid_remove()

def doNe():
  UpdateB1.grid_remove()
  UpdateB.grid_remove()
  editF.grid_remove()
  editGRAD.grid()

backI = PhotoImage(file=('pics/bck.png'))
UpdateB1 = Button(gradeF, text="BACK ", image=backI, cursor='hand2', compound=RIGHT, command=doNe, font=('arial',10,"bold"), relief=SOLID, bd=1, fg="white", bg="green")
UpdateB1.grid(row=1, column=1, padx=5, pady=5)
UpdateB1.grid_remove()

#-------------------current grading system-----------------
Label(savedF1, text="CURRENT GRADING SYSTEM", fg="white", bg="black", font=('arial',12,"bold")).grid(row=0, sticky=(W+E))
savedF = LabelFrame(savedF1, bg="lavender")
savedF.grid(row=1)

Label(savedF, text="Score Range.", bg="saddle brown", fg="white", font=('arial',12,"bold")).grid(row=0, column=0, sticky=(W+E), padx=2, pady=2)
Label(savedF, text="Grade letter.", bg="saddle brown", fg="white", font=('arial',12,"bold")).grid(row=0, column=1, sticky=(W+E))
Label(savedF, text="Letter Weight.", bg="saddle brown", fg="white", font=('arial',12,"bold")).grid(row=0, column=2, sticky=(W+E), padx=2, pady=2)

#------------------score grade----------------
rangeA = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
rangeA.grid(row=1, column=0, sticky=W+E, pady=2)
rangeBp = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
rangeBp.grid(row=2, column=0, sticky=W+E, pady=2)
rangeB = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
rangeB.grid(row=3, column=0, sticky=W+E, pady=2)
rangeCp = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
rangeCp.grid(row=4, column=0, sticky=W+E, pady=2)
rangeC = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
rangeC.grid(row=5, column=0, sticky=W+E, pady=2)
rangeDp = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
rangeDp.grid(row=6, column=0, sticky=W+E, pady=2)
rangeD = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
rangeD.grid(row=7, column=0, sticky=W+E, pady=2)
rangeF = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
rangeF.grid(row=8, column=0, sticky=W+E, pady=2)

#-----------------LETTER GRADES-------------------
letterA = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
letterA.grid(row=1, column=1, sticky=W+E, pady=2)
letterBp = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
letterBp.grid(row=2, column=1, sticky=W+E, pady=2)
letterB = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
letterB.grid(row=3, column=1, sticky=W+E, pady=2)
letterCp = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
letterCp.grid(row=4, column=1, sticky=W+E, pady=2)
letterC = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
letterC.grid(row=5, column=1, sticky=W+E, pady=2)
letterDp = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
letterDp.grid(row=6, column=1, sticky=W+E, pady=2)
letterD = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
letterD.grid(row=7, column=1, sticky=W+E, pady=2)
letterF = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
letterF.grid(row=8, column=1, sticky=W+E, pady=2)

#--------------Grade letter--------------
gradeA = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
gradeA.grid(row=1, column=2, sticky=W+E, pady=2)
gradeBp = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
gradeBp.grid(row=2, column=2, sticky=W+E, pady=2)
gradeB = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
gradeB.grid(row=3, column=2, sticky=W+E, pady=2)
gradeCp = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
gradeCp.grid(row=4, column=2, sticky=W+E, pady=2)
gradeC = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
gradeC.grid(row=5, column=2, sticky=W+E, pady=2)
gradeDp = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
gradeDp.grid(row=6, column=2, sticky=W+E, pady=2)
gradeD = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
gradeD.grid(row=7, column=2, sticky=W+E, pady=2)
gradeF = Label(savedF, font=('arial',12,"bold"), bg="lightgray")
gradeF.grid(row=8, column=2, sticky=W+E, pady=2)

#----------------------database-action---------------
def insertValz(*args):
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ID ,fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=1")
    result = cursor.fetchall()
    for (ID ,fro_Score, to_Score, let_Score, weg_Score) in result:
      pass

    from1.insert(0, str(fro_Score))
    to1.insert(0, str(to_Score))
    let1.insert(0, str(let_Score))
    weg1.insert(0, str(weg_Score))
    rangeA.config(text=str(fro_Score)+" - "+str(to_Score))
    letterA.config(text=str(let_Score))
    gradeA.config(text=str(weg_Score))

    cursor.execute("SELECT ID ,fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=2")
    result = cursor.fetchall()
    for (ID ,fro_Score, to_Score, let_Score, weg_Score) in result:
      pass

    from2.insert(0, str(fro_Score))
    to2.insert(0, str(to_Score))
    let2.insert(0, str(let_Score))
    weg2.insert(0, str(weg_Score))
    rangeBp.config(text=str(fro_Score)+" - "+str(to_Score))
    letterBp.config(text=str(let_Score))
    gradeBp.config(text=str(weg_Score))

    cursor.execute("SELECT ID ,fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=3")
    result = cursor.fetchall()
    for (ID ,fro_Score, to_Score, let_Score, weg_Score) in result:
      pass

    from3.insert(0, str(fro_Score))
    to3.insert(0, str(to_Score))
    let3.insert(0, str(let_Score))
    weg3.insert(0, str(weg_Score))
    rangeB.config(text=str(fro_Score)+" - "+str(to_Score))
    letterB.config(text=str(let_Score))
    gradeB.config(text=str(weg_Score))

    cursor.execute("SELECT ID ,fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=4")
    result = cursor.fetchall()
    for (ID ,fro_Score, to_Score, let_Score, weg_Score) in result:
      pass

    from4.insert(0, str(fro_Score))
    to4.insert(0, str(to_Score))
    let4.insert(0, str(let_Score))
    weg4.insert(0, str(weg_Score))
    rangeCp.config(text=str(fro_Score)+" - "+str(to_Score))
    letterCp.config(text=str(let_Score))
    gradeCp.config(text=str(weg_Score))

    cursor.execute("SELECT ID ,fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=5")
    result = cursor.fetchall()
    for (ID ,fro_Score, to_Score, let_Score, weg_Score) in result:
      pass

    from5.insert(0, str(fro_Score))
    to5.insert(0, str(to_Score))
    let5.insert(0, str(let_Score))
    weg5.insert(0, str(weg_Score))
    rangeC.config(text=str(fro_Score)+" - "+str(to_Score))
    letterC.config(text=str(let_Score))
    gradeC.config(text=str(weg_Score))

    cursor.execute("SELECT ID ,fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=6")
    result = cursor.fetchall()
    for (ID ,fro_Score, to_Score, let_Score, weg_Score) in result:
      pass

    from6.insert(0, str(fro_Score))
    to6.insert(0, str(to_Score))
    let6.insert(0, str(let_Score))
    weg6.insert(0, str(weg_Score))
    rangeDp.config(text=str(fro_Score)+" - "+str(to_Score))
    letterDp.config(text=str(let_Score))
    gradeDp.config(text=str(weg_Score))

    cursor.execute("SELECT ID ,fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=7")
    result = cursor.fetchall()
    for (ID ,fro_Score, to_Score, let_Score, weg_Score) in result:
      pass

    from7.insert(0, str(fro_Score))
    to7.insert(0, str(to_Score))
    let7.insert(0, str(let_Score))
    weg7.insert(0, str(weg_Score))
    rangeD.config(text=str(fro_Score)+" - "+str(to_Score))
    letterD.config(text=str(let_Score))
    gradeD.config(text=str(weg_Score))

    cursor.execute("SELECT ID ,fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=8")
    result = cursor.fetchall()
    for (ID ,fro_Score, to_Score, let_Score, weg_Score) in result:
      pass

    from8.insert(0, str(fro_Score))
    to8.insert(0, str(to_Score))
    let8.insert(0, str(let_Score))
    weg8.insert(0, str(weg_Score))
    rangeF.config(text=str(fro_Score)+" - "+str(to_Score))
    letterF.config(text=str(let_Score))
    gradeF.config(text=str(weg_Score))

  except Exception as e:
    print(e)    
insertValz()

#-------------clear grading table-----------
def clearGrades():
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE grading')
    conn.commit()
    print('Grading table cleared!')
  except Exception as e:
    raise e


def clearEntr():
  try:
    from1.delete(0, END)
    to1.delete(0, END)
    let1.delete(0, END)
    weg1.delete(0, END)

    from2.delete(0, END)
    to2.delete(0, END)
    let2.delete(0, END)
    weg2.delete(0, END)

    from3.delete(0, END)
    to3.delete(0, END)
    let3.delete(0, END)
    weg3.delete(0, END)

    from4.delete(0, END)
    to4.delete(0, END)
    let4.delete(0, END)
    weg4.delete(0, END)

    from5.delete(0, END)
    to5.delete(0, END)
    let5.delete(0, END)
    weg5.delete(0, END)

    from6.delete(0, END)
    to6.delete(0, END)
    let6.delete(0, END)
    weg6.delete(0, END)

    from7.delete(0, END)
    to7.delete(0, END)
    let7.delete(0, END)
    weg7.delete(0, END)

    from8.delete(0, END)
    to8.delete(0, END)
    let8.delete(0, END)
    weg8.delete(0, END)

  except Exception as e:
    raise e
#-------------------update grading system-------------
def updateSCALE():
  clearGrades()
  try:
      conn = sqlite3.connect('dbs/mjbgpadata.db')
      cursor = conn.cursor()

      cursor.execute('CREATE TABLE IF NOT EXISTS grading (ID INTEGER PRIMARY KEY  AUTOINCREMENT, fro_Score INTEGER NOT NULL , to_Score INTEGER NOT NULL , let_Score VARCHAR NOT NULL , weg_Score VARCHAR NOT NULL )')
      print('Grading tests table created.')

      updt1sql = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
      updt1val = (float(from1.get()), float(to1.get()), str(let1.get()), str(weg1.get()) )

      updt2sql = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
      updt2val = (float(from2.get()), float(to2.get()), str(let2.get()), str(weg2.get()) )

      updt3sql = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
      updt3val = (float(from3.get()), float(to3.get()), str(let3.get()), str(weg3.get()) )

      updt4sql = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
      updt4val = (float(from4.get()), float(to4.get()), str(let4.get()), str(weg4.get()) )

      updt5sql = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
      updt5val = (float(from5.get()), float(to5.get()), str(let5.get()), str(weg5.get()) )

      updt6sql = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
      updt6val = (float(from6.get()), float(to6.get()), str(let6.get()), str(weg6.get()) )

      updt7sql = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
      updt7val = (float(from7.get()), float(to7.get()), str(let7.get()), str(weg7.get()) )

      updt8sql = "INSERT INTO grading (fro_Score, to_Score, let_Score, weg_Score)VALUES (?,?,?,?)"
      updt8val = (float(from8.get()), float(to8.get()), str(let8.get()), str(weg8.get()) )

      cursor.execute(updt1sql, updt1val)
      cursor.execute(updt2sql, updt2val)
      cursor.execute(updt3sql, updt3val)
      cursor.execute(updt4sql, updt4val)
      cursor.execute(updt5sql, updt5val)
      cursor.execute(updt6sql, updt6val)
      cursor.execute(updt7sql, updt7val)
      cursor.execute(updt8sql, updt8val)

      conn.commit()
      clearEntr()
      insertValz()
      messagebox.showinfo('MjB Update','Grading System Updated successfully!')

  except Exception as e:
    messagebox.showerror('MjB-Update Erro','Grading system not updated!\nAn error occured!')
    print(e)
    
UpdateB.config(command = updateSCALE)

#---------------------calcultions------------------------
PdtVal = DoubleVar()
SumVal = DoubleVar()
PdtVal1 = DoubleVar()
SumVal1 = DoubleVar()
PdtVal2 = DoubleVar()
SumVal2 = DoubleVar()
PdtVal3 = DoubleVar()
SumVal3 = DoubleVar()
#---------------------gpa calculations----------------
def filtergpa(*args):
  msginfo12.config(text='')
  gpaRES.config(text='')
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    sw = "SELECT * FROM gpadata WHERE NAME=? and YEAR=? and SEMESTER=? "
    sm = (str(userN.get()), str(gpaYr.get()), str(gpaSem.get()) )
    cursor.execute(sw, sm)
    result = cursor.fetchall()
    for row in result:
      print(row)

    pdtsql = ("SELECT sum(PRODUCT) FROM gpadata AS SUM WHERE NAME=? and YEAR=? and SEMESTER=?")
    pdtval = (str(userN.get()), str(gpaYr.get()), str(gpaSem.get()) )
    cursor.execute(pdtsql, pdtval)
    result = cursor.fetchall()
    for PRODUCT in result:
      Pdt.delete(0, END)
    PdtVal.set(value=PRODUCT)
    sgps = float(Pdt.get())

    sumsql = ("SELECT sum(CREDITUNITS) FROM gpadata AS SUM WHERE NAME=? and YEAR=? and SEMESTER=?")
    sumval = (str(userN.get()), str(gpaYr.get()), str(gpaSem.get()) )
    cursor.execute(sumsql, sumval)
    result = cursor.fetchall()
    for SUM in result:
      sUm.delete(0, END)
    SumVal.set(value=SUM)
    scus = float(sUm.get())

    gpaRES.config(text=str(round((sgps/scus),3)))
    print(sgps)
    print(scus)

  except Exception as e:
    gpaRES.config(text='')
    msginfo12.config(text='Can`t find your results! Check Input!')
fetchBt.config(command=filtergpa)

def filtercgpa(*args):
  msginfo2.config(text='')
  cgpaRES.config(text='')
  degWRES.config(text='')
  degCRES.config(text='')
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()

    #--------------------------year one------------------------
    if str(cgpaYr.get())=='One':
      pdtsql = ("SELECT sum(PRODUCT) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      pdtval = (str(userN.get()), str(cgpaYr.get()))
      cursor.execute(pdtsql, pdtval)
      result = cursor.fetchall()
      for PRODUCT in result:
        Pdt.delete(0, END)
      PdtVal.set(value=PRODUCT)
      sgps = float(Pdt.get())

      sumsql = ("SELECT sum(CREDITUNITS) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      sumval = (str(userN.get()), str(cgpaYr.get()))
      cursor.execute(sumsql, sumval)
      result = cursor.fetchall()
      for SUM in result:
        sUm.delete(0, END)
      SumVal.set(value=SUM)
      scus = float(sUm.get())

      cgpaRES.config(text=str(round((sgps/scus),3)))
      print(sgps)
      print(scus)

      if(4.5 <= float((round((sgps/scus),3))) < 5.1):
        degCRES.config(text='FIRST' , fg='blue')
        degWRES.config(text=str(round((sgps/scus),2)))

      elif (3.6 <= float((round((sgps/scus),3))) < 4.5):
        degCRES.config(text='SECOND UPPER' , fg='blue')
        degWRES.config(text=str(round((sgps/scus),2)))

      elif (2.6 <= float((round((sgps/scus),3))) < 3.6):
        degCRES.config(text='SECOND LOWER', fg='green')
        degWRES.config(text=str(round((sgps/scus),2)))

      elif (0.0 <= float((round((sgps/scus),3))) < 2.6):
        degCRES.config(text='PASS', fg='red')
        degWRES.config(text=str(round((sgps/scus),2)))


      #----------------------year one and two-------------------------
      #------------------------year one--------------------
    elif(str(cgpaYr.get())=='Two'):
      print(str(cgpaYr.get()))
      pdtsql1 = ("SELECT sum(PRODUCT) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      pdtval1 = (str(userN.get()), 'One')
      cursor.execute(pdtsql1, pdtval1)
      result = cursor.fetchall()
      for PRODUCT1 in result:
        Pdt1.delete(0, END)
      PdtVal1.set(value=PRODUCT1)
      sgps1 = float(Pdt1.get())

      sumsql1 = ("SELECT sum(CREDITUNITS) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      sumval1 = (str(userN.get()), 'One')
      cursor.execute(sumsql1, sumval1)
      result = cursor.fetchall()
      for SUM1 in result:
        sUm1.delete(0, END)
      SumVal1.set(value=SUM1)
      scus1 = float(sUm1.get())

      #-------------------------year two----------------
      pdtsql2 = ("SELECT sum(PRODUCT) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      pdtval2 = (str(userN.get()), 'Two')
      cursor.execute(pdtsql2, pdtval2)
      result = cursor.fetchall()
      for PRODUCT2 in result:
        Pdt2.delete(0, END)
      PdtVal2.set(value=PRODUCT2)
      sgps2 = float(Pdt2.get())

      sumsql2 = ("SELECT sum(CREDITUNITS) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      sumval2 = (str(userN.get()), 'Two')
      cursor.execute(sumsql2, sumval2)
      result = cursor.fetchall()
      for SUM2 in result:
        sUm2.delete(0, END)
      SumVal2.set(value=SUM2)
      scus2 = float(sUm2.get())


      cgpaRES.config(text=str(round(((sgps1+sgps2)/(scus1+scus2)),3)))
      print(sgps2)
      print(scus2)

      if(4.5 <= float((round(((sgps1+sgps2)/(scus1+scus2)),3))) < 5.1):
        degCRES.config(text='FIRST' , fg='blue')
        degWRES.config(text=str(round(((sgps1+sgps2)/(scus1+scus2)),2)))

      elif (3.6 <= float((round(((sgps1+sgps2)/(scus1+scus2)),3))) < 4.5):
        degCRES.config(text='SECOND UPPER' , fg='blue')
        degWRES.config(text=str(round(((sgps1+sgps2)/(scus1+scus2)),2)))

      elif (2.6 <= float((round(((sgps1+sgps2)/(scus1+scus2)),3))) < 3.6):
        degCRES.config(text='SECOND LOWER', fg='green')
        degWRES.config(text=str(round(((sgps1+sgps2)/(scus1+scus2)),2)))

      elif (0.0 <= float((round(((sgps1+sgps2)/(scus1+scus2)),3))) < 2.6):
        degCRES.config(text='PASS', fg='red')
        degWRES.config(text=str(round(((sgps1+sgps2)/(scus1+scus2)),2)))

      #----------------------year one and two and three-------------------------
      #------------------------year one--------------------
    elif(str(cgpaYr.get())=='Three'):
      print(str(cgpaYr.get()))
      pdtsql1 = ("SELECT sum(PRODUCT) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      pdtval1 = (str(userN.get()), 'One')
      cursor.execute(pdtsql1, pdtval1)
      result = cursor.fetchall()
      for PRODUCT1 in result:
        Pdt1.delete(0, END)
      PdtVal1.set(value=PRODUCT1)
      sgps1 = float(Pdt1.get())

      sumsql1 = ("SELECT sum(CREDITUNITS) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      sumval1 = (str(userN.get()), 'One')
      cursor.execute(sumsql1, sumval1)
      result = cursor.fetchall()
      for SUM1 in result:
        sUm1.delete(0, END)
      SumVal1.set(value=SUM1)
      scus1 = float(sUm1.get())

      #-------------------------year two----------------
      pdtsql2 = ("SELECT sum(PRODUCT) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      pdtval2 = (str(userN.get()), 'Two')
      cursor.execute(pdtsql2, pdtval2)
      result = cursor.fetchall()
      for PRODUCT2 in result:
        Pdt2.delete(0, END)
      PdtVal2.set(value=PRODUCT2)
      sgps2 = float(Pdt2.get())

      sumsql2 = ("SELECT sum(CREDITUNITS) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      sumval2 = (str(userN.get()), 'Two')
      cursor.execute(sumsql2, sumval2)
      result = cursor.fetchall()
      for SUM2 in result:
        sUm2.delete(0, END)
      SumVal2.set(value=SUM2)
      scus2 = float(sUm2.get())

      #-----------------------------year three-------------
      pdtsql3 = ("SELECT sum(PRODUCT) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      pdtval3 = (str(userN.get()), 'Three')
      cursor.execute(pdtsql3, pdtval3)
      result = cursor.fetchall()
      for PRODUCT3 in result:
        Pdt3.delete(0, END)
      PdtVal3.set(value=PRODUCT3)
      sgps3 = float(Pdt3.get())

      sumsql3 = ("SELECT sum(CREDITUNITS) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      sumval3 = (str(userN.get()), 'Two')
      cursor.execute(sumsql3, sumval3)
      result = cursor.fetchall()
      for SUM3 in result:
        sUm3.delete(0, END)
      SumVal3.set(value=SUM3)
      scus3 = float(sUm3.get())


      cgpaRES.config(text=str(round(((sgps1+sgps2+sgps3)/(scus1+scus2+scus3)),3)))
      print(sgps3)
      print(scus3)

      if(4.5 <= float((round(((sgps1+sgps2+sgps3)/(scus1+scus2+scus3)),3))) < 5.1):
        degCRES.config(text='FIRST' , fg='blue')
        degWRES.config(text=str(round(((sgps1+sgps2+sgps3)/(scus1+scus2+scus3)),2)))

      elif (3.6 <= float((round(((sgps1+sgps2+sgps3)/(scus1+scus2+scus3)),3))) < 4.5):
        degCRES.config(text='SECOND UPPER' , fg='blue')
        degWRES.config(text=str(round(((sgps1+sgps2+sgps3)/(scus1+scus2+scus3)),2)))

      elif (2.6 <= float((round(((sgps1+sgps2+sgps3)/(scus1+scus2+scus3)),3))) < 3.6):
        degCRES.config(text='SECOND LOWER', fg='green')
        degWRES.config(text=str(round(((sgps1+sgps2+sgps3)/(scus1+scus2+scus3)),2)))

      elif (0.0 <= float((round(((sgps1+sgps2+sgps3)/(scus1+scus2+scus3)),3))) < 2.6):
        degCRES.config(text='PASS', fg='red')
        degWRES.config(text=str(round(((sgps1+sgps2+sgps3)/(scus1+scus2+scus3)),2)))


      #----------------------year one and two and three and four-------------------------
      #------------------------year one--------------------
    elif(str(cgpaYr.get())=='Four'):
      print(str(cgpaYr.get()))
      pdtsql = ("SELECT sum(PRODUCT) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      pdtval = (str(userN.get()), str(cgpaYr.get()))
      cursor.execute(pdtsql, pdtval)
      result = cursor.fetchall()
      for PRODUCT in result:
        Pdt.delete(0, END)
      PdtVal.set(value=PRODUCT)
      sgps = float(Pdt.get())

      sumsql = ("SELECT sum(CREDITUNITS) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      sumval = (str(userN.get()), str(cgpaYr.get()))
      cursor.execute(sumsql, sumval)
      result = cursor.fetchall()
      for SUM in result:
        sUm.delete(0, END)
      SumVal.set(value=SUM)
      scus = float(sUm.get())

      #-------------------year two-------------------
      pdtsql1 = ("SELECT sum(PRODUCT) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      pdtval1 = (str(userN.get()), 'One')
      cursor.execute(pdtsql1, pdtval1)
      result = cursor.fetchall()
      for PRODUCT1 in result:
        Pdt1.delete(0, END)
      PdtVal1.set(value=PRODUCT1)
      sgps1 = float(Pdt1.get())

      sumsql1 = ("SELECT sum(CREDITUNITS) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      sumval1 = (str(userN.get()), 'One')
      cursor.execute(sumsql1, sumval1)
      result = cursor.fetchall()
      for SUM1 in result:
        sUm1.delete(0, END)
      SumVal1.set(value=SUM1)
      scus1 = float(sUm1.get())

      #-------------------------year two----------------
      pdtsql2 = ("SELECT sum(PRODUCT) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      pdtval2 = (str(userN.get()), 'Two')
      cursor.execute(pdtsql2, pdtval2)
      result = cursor.fetchall()
      for PRODUCT2 in result:
        Pdt2.delete(0, END)
      PdtVal2.set(value=PRODUCT2)
      sgps2 = float(Pdt2.get())

      sumsql2 = ("SELECT sum(CREDITUNITS) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      sumval2 = (str(userN.get()), 'Two')
      cursor.execute(sumsql2, sumval2)
      result = cursor.fetchall()
      for SUM2 in result:
        sUm2.delete(0, END)
      SumVal2.set(value=SUM2)
      scus2 = float(sUm2.get())

      #-----------------------------year three-------------
      pdtsql3 = ("SELECT sum(PRODUCT) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      pdtval3 = (str(userN.get()), 'Three')
      cursor.execute(pdtsql3, pdtval3)
      result = cursor.fetchall()
      for PRODUCT3 in result:
        Pdt3.delete(0, END)
      PdtVal3.set(value=PRODUCT3)
      sgps3 = float(Pdt3.get())

      sumsql3 = ("SELECT sum(CREDITUNITS) FROM gpadata AS SUM WHERE NAME=? and YEAR=?")
      sumval3 = (str(userN.get()), 'Two')
      cursor.execute(sumsql3, sumval3)
      result = cursor.fetchall()
      for SUM3 in result:
        sUm3.delete(0, END)
      SumVal3.set(value=SUM3)
      scus3 = float(sUm3.get())



      cgpaRES.config(text=str(round(((sgps+sgps1+sgps2+sgps3)/(scus+scus1+scus2+scus3)),3)))
      print(sgps3)
      print(scus3)

      if(4.5 <= float((round(((sgps+sgps1+sgps2+sgps3)/(scus+scus1+scus2+scus3)),3))) < 5.1):
        degCRES.config(text='FIRST' , fg='blue')
        degWRES.config(text=str(round(((sgps+sgps1+sgps2+sgps3)/(scus+scus1+scus2+scus3)),2)))

      elif (3.6 <= float((round(((sgps+sgps1+sgps2+sgps3)/(scus+scus1+scus2+scus3)),3))) < 4.5):
        degCRES.config(text='SECOND UPPER' , fg='blue')
        degWRES.config(text=str(round(((sgps+sgps1+sgps2+sgps3)/(scus+scus1+scus2+scus3)),2)))

      elif (2.6 <= float((round(((sgps+sgps1+sgps2+sgps3)/(scus+scus1+scus2+scus3)),3))) < 3.6):
        degCRES.config(text='SECOND LOWER', fg='green')
        degWRES.config(text=str(round(((sgps+sgps1+sgps2+sgps3)/(scus+scus1+scus2+scus3)),2)))

      elif (0.0 <= float((round(((sgps+sgps1+sgps2+sgps3)/(scus+scus1+scus2+scus3)),3))) < 2.6):
        degCRES.config(text='PASS', fg='red')
        degWRES.config(text=str(round(((sgps+sgps1+sgps2+sgps3)/(scus+scus1+scus2+scus3)),2)))
    else:
      msginfo2.config(text='No data to show!')
      cgpaRES.config(text='')
      degCRES.config(text='')
      degWRES.config(text='')

  except Exception as e:
    msginfo2.config(text='No data to show!')
    cgpaRES.config(text='')
    degCRES.config(text='')
    degWRES.config(text='')
fetchBt1.config(command=filtercgpa)

#-------------------home page ends here----------------------



#-----------footer----------------
def mail1(*args):
  mail2.config(fg="blue")  
  webbrowser.open_new(r"http://malto:bmuzoora@gmail.com")

def bgchm(*args):
  mail2.config(fg="black")

def bgchw(*args):
  wtsa.config(fg="black")

def tsapp(*args):
  wtsa.config(fg="blue")  
  webbrowser.open_new(r"https://api.whatsapp.com/send?phone=+256750941273&text=Contact%20Us")


Label(gpa, text="© MjB SYSTEMS 2018 - "+today.strftime("%Y")+" | ALL RIGHTS RESERVED", font=("arial", 10, "bold"), bg="black", fg="lightgray").pack(side=BOTTOM, fill=X, anchor=N, ipady=5)
footerF = Frame(gpa, bg='CadetBlue4', relief=FLAT, bd=1)
footerF.pack(side=BOTTOM, anchor=N)

#----------------social media-----------
def enter(*args):
  mail2.config(fg="blue", font=('arial',11, 'bold', 'underline'))

def leave(*args):
  mail2.config(fg="black", font=('arial',10, 'bold'))

def enter1(*args):
  wtsa.config(fg="blue", font=('arial',11, 'bold', 'underline'))

def leave1(*args):
  wtsa.config(fg="black", font=('arial',10, 'bold'))

mail = PhotoImage(file='pics/email.png')
wtsapp = PhotoImage(file='pics/wapp.png')
mail2 = Label(footerF, text="Send us a mail",compound=TOP, font=('arial',10, 'bold'), image=mail, bg='CadetBlue4', cursor='hand2')
mail2.grid(row=0, column=0, pady=5, padx=5)
mail2.bind("<Button-1>", mail1)
mail2.bind("<ButtonRelease-1>", bgchm)
mail2.bind('<Enter>', enter)
mail2.bind('<Leave>', leave)


Label(footerF, text='    ', bg='CadetBlue4').grid(row=0, column=1)


wtsa = Label(footerF, text="Whatsapp with us",compound=TOP, font=('arial',10, 'bold'), image=wtsapp, bg='CadetBlue4', cursor='hand2')
wtsa.grid(row=0, column=2)
wtsa.bind("<Button-1>", tsapp)
wtsa.bind("<ButtonRelease-1>", bgchw)
wtsa.bind('<Enter>', enter1)
wtsa.bind('<Leave>', leave1)


#----------------popup menu---------
popup = Menu(gpa, tearoff=0)
popup.add_command(label="Send mail now.", command=mail1)
popup.add_command(label="Send message now.", command=tsapp)

def do_popup(event):
    # display the popup menu
    try:
        popup.tk_popup(event.x_root, event.y_root, 1)
    except Exception as e:
      pass
    finally:
        # make sure to release the grab (Tk 8.0a1 only)
        popup.grab_release()
mail2.bind("<Button-3>", do_popup)
wtsa.bind("<Button-3>", do_popup)

#------------------------save as----------------


#------------------marks entry start here--------------
Label(tab4, text="PROVIDE INFORMATION TO USE IN CALCULATING YOUR CGPA",fg='blue', bg="lightgray", font=('arial', 15, 'bold')).pack(fill=X)

Mscore = Frame(tab4, bg="gray", relief="solid", bd=2)
Mscore.pack(padx=5, pady=5)


Fsc0 = Frame(Mscore, bg="gray")
Fsc0.grid(row=0, column=0)
Mscore.rowconfigure(0, weight=1)
Mscore.columnconfigure(0, weight=1)
Fsc0.rowconfigure(0, weight=1)
Fsc0.columnconfigure(0, weight=1)

Fsc = LabelFrame(Fsc0, text="PROVIDE CORRECT INFORMATION PLEASE",fg="white", font=('arial', 10, 'bold',"italic"), bg="gray")
Fsc.grid(row=0, column=0,pady=5, padx=20)
Fsc1 = LabelFrame(Fsc0, text="DASHBORD",fg="white", font=('arial', 10, 'bold',"italic"), bg="gray")
Fsc1.grid(row=0, column=1, pady=10, padx=20)
Fsc.rowconfigure(0, weight=1)
Fsc.columnconfigure(0, weight=1)
Fsc1.rowconfigure(0, weight=1)
Fsc1.columnconfigure(0, weight=1)

Label(Fsc, text="COUSE UNIT INFORMATION.", font=('arial', 10, 'bold'), bg="black", fg="white").grid(row=0,columnspan=7, padx=5, sticky=(E+W))
Label(Fsc, text="Name", font=('arial', 10, 'bold'), width=6, bg="blue", fg="white").grid(row=1, column=0, padx=5, sticky=(E+W))
Label(Fsc, text="Code", font=('arial', 10, 'bold'), bg="blue", fg="white").grid(row=1, column=2, padx=5, sticky=(E+W))
Label(Fsc, text="Credit Units", font=('arial', 10, 'bold'), bg="blue", fg="white").grid(row=1, column=4, padx=5, sticky=(E+W))

scoreF = Frame(Fsc, bg="gray")
scoreF.grid(columnspan=7, sticky=(E+W))
Label(scoreF, text="SCORES INFORMATION", font=('arial', 10, 'bold'), bg="black", fg="white").grid(row=0,columnspan=4, padx=5, sticky=(E+W))
Label(scoreF, text="CourseWork ( /40 )", font=('arial', 10, 'bold'), bg="blue", fg="white").grid(row=1, column=0, padx=5, sticky=(E+W))
Label(scoreF, text="Final Exams ( /60 )", font=('arial', 10, 'bold'), bg="blue", fg="white").grid(row=1, column=2, padx=5, sticky=(E+W))
Label(scoreF, text="SEMESTER.", font=('arial', 10, 'bold'), bg="black", fg="white").grid(row=0, column=6, columnspan=2, padx=5, sticky=(E+W))
Label(scoreF, text="YEAR", font=('arial', 10, 'bold'), bg="black", fg="white").grid(row=0, column=4, padx=5, sticky=(E+W))

msginfo1 = Label(Fsc, text="", font=('arial', 10,'bold', 'italic'), fg="red", bg="gray")
msginfo1.grid(row=5,columnspan=2, column=0)

#-------------------course unit entries------------
def enterInt(*args):
  try:
    cU.delete(0, END)
    msginfo1.config(text="Select from list!")
  except ValueError:
    msginfo1.config(text="")
    cU.delete(0, END)
def click1(*args):
  msginfo1.config(text="")

def enterInt1(*args):
  try:
    if float(testSc.get()) >40:
      testSc.delete(1, END)
      msginfo1.config(text="Value shouldnt be higher than 40.")
    elif((testSc.get())==""):
      msginfo1.config(text="")
    else:
      msginfo1.config(text="")
  except ValueError:
    msginfo1.config(text="Invalid input!")
    testSc.delete(0, END)

def enterInt2(*args):
  try:
    if float(FExam.get()) >60:
      FExam.delete(1, END)
      msginfo1.config(text="Value shouldnt be higher than 60.")
    elif((FExam.get())==""):
      msginfo1.config(text="")
    else:
      msginfo1.config(text="")
  except ValueError:
    msginfo1.config(text="Invalid input!")
    FExam.delete(0, END)
def clck(*args):
  msginfo1.config(text="")

def enterInt3(*args):
  try:
    Year1.delete(0, END)
    msginfo1.config(text="Select from list!")
  except ValueError:
    msginfo1.config(text="")
    Year1.delete(0, END)
def click2(*args):
  msginfo1.config(text="")

def enterInt4(*args):
  try:
    Sem1.delete(0, END)
    msginfo1.config(text="Select from list!")
  except ValueError:
    msginfo1.config(text="")
    Sem1.delete(0, END)
def click3(*args):
  msginfo1.config(text="")

def enterInt0(*args):
  try:
    if str(cuN.get()) == int(cuN.get()):
      msginfo1.config(text="")
    elif cuN.get()=="":
      msginfo1.config(text="")
    else:
      cuN.delete(0,END)
      msginfo1.config(text="Invalid input!")
  except Exception as e:
    pass
    msginfo1.config(text="")


cuN = ttk.Entry(Fsc, font=('arial', 10, 'bold'), justify="center")
cuN.grid(row=1, column=1, ipadx=30, pady=2, padx=5)
tooltip(cuN , ["Enter Course Unit."])
cuN.bind("<KeyPress>",enterInt0)
cuN.bind("<KeyRelease>",enterInt0)
cuN.bind("<1>",clck)
cuN.bind("<3>",clck)


cuC = ttk.Entry(Fsc, font=('arial', 10, 'bold'), width=8, justify="center")
cuC.grid(row=1, column=3, pady=2, padx=5)
tooltip(cuC , ["Enter Course Unit Code."])

cUvar = IntVar()
cUval = [2,3,4,5] 
cU = ttk.Combobox(Fsc, font=('arial', 10, 'bold'), textvariable=cUvar, values=cUval, width=4, justify="center")
cU.grid(row=1, column=6, pady=2, padx=5)
tooltip(cU , ["Select Credit Units."])
cUvar.set(value=3)
cU.bind("<KeyPress>",enterInt)
cU.bind("<KeyRelease>",enterInt)
cU.bind("<1>",click1)
cU.bind("<3>",click1)
#-------------------score entries--------------
tesctVal = IntVar()
examVal = IntVar()

testSc = ttk.Entry(scoreF, font=('arial', 10, 'bold'), textvariable=tesctVal, width=8, justify="center")
testSc.grid(row=1, column=1, pady=2, padx=5)
tooltip(testSc , ["Enter Course Work score."])
testSc.bind("<KeyPress>",enterInt1)
testSc.bind("<KeyRelease>",enterInt1)

FExam = ttk.Entry(scoreF, font=('arial', 10, 'bold'), textvariable=examVal, width=8, justify="center")
FExam.grid(row=1, column=3, pady=2, padx=5)
tooltip(FExam , ["Enter Exams score."])
FExam.bind("<KeyPress>",enterInt2)
FExam.bind("<KeyRelease>",enterInt2)

semval = ("One","Two")
yrval = ("One","Two","Three","Four")

Year1 = ttk.Combobox(scoreF, font=('arial', 10, 'bold'), values=yrval, justify="center", width=9)
Year1.grid(row=1, column=4, pady=2, padx=5, sticky=(W+E))
tooltip(Year1 , ["Select Year of study from the list."])
Year1.bind("<KeyPress>",enterInt3)
Year1.bind("<KeyRelease>",enterInt3)
Year1.bind("<1>",click2)
Year1.bind("<3>",click2)

Sem1 = ttk.Combobox(scoreF, font=('arial', 10, 'bold'), values=semval, justify="center", width=9)
Sem1.grid(row=1, column=6, pady=2, padx=5)
tooltip(Sem1 , ["Select Semester from the list."])
Sem1.bind("<KeyPress>",enterInt4)
Sem1.bind("<KeyRelease>",enterInt4)
Sem1.bind("<1>",click3)
Sem1.bind("<3>",click3)

savpic = PhotoImage(file='pics/save.png')
def entr1(*args):
  savebt.config(relief=SOLID,bg="white", fg="blue", text="Save »")

def entr0(*args):
  savebt.config(relief=FLAT, bg="blue", fg="white", text="Save")

savebt = Button(Fsc, text=' Save', image=savpic, compound=LEFT , cursor='hand2', font=('arial', 10, 'bold'), bg="blue", fg="white", relief="flat")
savebt.grid(row=5,column=2, columnspan=2, pady=5,)
savebt.bind("<Enter>", entr1)
savebt.bind("<Leave>", entr0)



def entr1(*args):
  updbt.config(relief=SOLID,bg="white", fg="green", text="Update »")

def entr0(*args):
  updbt.config(relief=FLAT, bg="green", fg="white", text="Update")

updbt = Button(Fsc, text='Update', width=10 , cursor='hand2', font=('arial', 10, 'bold'), bg="green", fg="white", relief="flat")
updbt.grid(row=5,column=2, columnspan=2, pady=5,)
updbt.bind("<Enter>", entr1)
updbt.bind("<Leave>", entr0)
updbt.grid_remove()



def closeTest():
  note.tab(3, state='hidden')
  cuN.delete(0,END)
  cuC.delete(0,END)
  cU.delete(0,END)
  testSc.delete(0,END)
  FExam.delete(0,END)
  Year1.delete(0,END)
  Sem1.delete(0,END)
  cuN.focus()
  tesctVal.set(value=0)
  examVal.set(value=0)
  cUvar.set(value=3)
  msginfo1.config(text="")

Button(Mscore, text="X", fg="white",command=closeTest, bg='red', width=3, font=('arial',8,'bold'), relief=FLAT).grid(row=0, column=1, sticky=N)


FscOUT = LabelFrame(Mscore, text="RESULTS OUTPUT AS SUBMITTED", font=('arial', 10, 'bold'), bg="gray", fg="white")
FscOUT.grid(padx=20, pady=10)
FscOUT.rowconfigure(0, weight=1)
FscOUT.columnconfigure(0, weight=1)

out2Iv = Frame(FscOUT, bg="white")
out2Iv.pack(side=BOTTOM, fill=X)

cols=("NAME", "YEAR", "SEMESTER","COURSE_UNIT","COURSE_UNIT_CODE", "CREDIT_UNITS","COURSE_WORK", "FINAL_EXAM","TOTAL_SCORES","GRADE","GRADE_POINTS")
scoreOUT = ttk.Treeview(FscOUT, height=9, column=cols, show="headings")
scoreOUT.pack(side=LEFT, fill=BOTH)
scoreOUTv = Scrollbar(FscOUT, command=scoreOUT.yview)
scoreOUTv.pack(side=RIGHT, fill=Y)
scoreOUTh = Scrollbar(out2Iv,orient=HORIZONTAL, command=scoreOUT.xview)
scoreOUTh.pack(fill=X)
scoreOUT.config(yscrollcommand=scoreOUTv.set, xscrollcommand=scoreOUTh.set)
scoreOUT.column(0, width=100)
scoreOUT.column(1, width=80)
scoreOUT.column(2, width=80)
scoreOUT.column(3, width=100)
scoreOUT.column(4, width=150)
scoreOUT.column(5, width=100)
scoreOUT.column(6, width=100)
scoreOUT.column(7, width=80)
scoreOUT.column(8, width=100)
scoreOUT.column(9, width=80)
scoreOUT.column(10, width=100)
tooltip(scoreOUT , [str(len(scoreOUT.get_children()))+' Course Unit(s)'])



for column in cols:
  scoreOUT.heading(column, text=column)

scoreOUT.rowconfigure(0, weight=1)
scoreOUT.columnconfigure(0, weight=1)



#------------------treeview menu--------------
def delt():
  selected = scoreOUT.selection() 
  try:
    for select in selected:
      scoreOUT.delete(select)    
  except Exception as e:
    pass

def edt():
  updbt.grid()
  savebt.grid_remove()
  for selected in scoreOUT.selection():
    NAME, YEAR, SEMESTER,COURSE_UNIT, COURSE_UNIT_CODE,CREDIT_UNITS,COURSE_WORK, FINAL_EXAM, TOTAL_SCORES, GRADE, GRADE_POINTS = scoreOUT.item(selected, 'values')
  cuN.delete(0,END)
  cuC.delete(0,END)
  cU.delete(0,END)
  testSc.delete(0,END)
  FExam.delete(0,END)
  Year1.delete(0,END)
  Sem1.delete(0,END)

  cuN.insert(0, str(COURSE_UNIT))
  cuC.insert(0, str(COURSE_UNIT_CODE))
  cU.insert(0, str(CREDIT_UNITS))
  testSc.insert(0, str(COURSE_WORK))
  FExam.insert(0, str(FINAL_EXAM))
  Year1.insert(0, str(YEAR))
  Sem1.insert(0, str(SEMESTER))

 


def dele():
  try:
    for selected in scoreOUT.selection():
      NAME, YEAR, SEMESTER,COURSE_UNIT, COURSE_UNIT_CODE,CREDIT_UNITS,COURSE_WORK, FINAL_EXAM, TOTAL_SCORES, GRADE, GRADE_POINTS= scoreOUT.item(selected, 'values')
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    sqll = ("DELETE FROM tests WHERE COURSEUNIT=? and COURSEUNIT_CODE=? and YEAR=? and SEMESTER=? and NAME=?")
    sqlll = ("DELETE FROM gpadata WHERE NAME=?  and YEAR=? and SEMESTER=? and COURSEUNIT=? and CREDITUNITS=?")
    vl = (str(COURSE_UNIT), str(COURSE_UNIT_CODE), str(YEAR), str(SEMESTER), str(NAME))
    vll = (str(NAME), str(YEAR), str(SEMESTER),str(COURSE_UNIT), str(CREDIT_UNITS))
    cursor.execute(sqll,vl)
    cursor.execute(sqlll,vll)
    conn.commit()
    delt()
    tooltip(scoreOUT , [str(len(scoreOUT.get_children()))+' Course Unit(s)'])
    retSVal.set(str(len(scoreOUT.get_children()))+' item(s)')
    messagebox.showinfo('MjB-Success','Result(s) cleared.')
    updbt.grid_remove()
    savebt.grid()
  except Exception as e:
    raise e

def dele1():
  try:
    for selected in scoreOUT.selection():
      NAME, YEAR, SEMESTER,COURSE_UNIT, COURSE_UNIT_CODE,CREDIT_UNITS,COURSE_WORK, FINAL_EXAM, TOTAL_SCORES, GRADE, GRADE_POINTS= scoreOUT.item(selected, 'values')
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    sqll = ("DELETE FROM tests WHERE COURSEUNIT=? and COURSEUNIT_CODE=? and YEAR=? and SEMESTER=? and NAME=?")
    vl = (str(COURSE_UNIT), str(COURSE_UNIT_CODE), str(YEAR), str(SEMESTER), str(NAME))

    sqlll = ("DELETE FROM gpadata WHERE NAME=?  and YEAR=? and SEMESTER=? and COURSEUNIT=? and CREDITUNITS=?")
    vll = (str(NAME), str(YEAR), str(SEMESTER),str(COURSE_UNIT), str(CREDIT_UNITS))
    cursor.execute(sqll,vl)
    cursor.execute(sqlll,vll)
    conn.commit()
    delt()
    tooltip(scoreOUT , [str(len(scoreOUT.get_children()))+' Course Unit(s)'])
    retSVal.set(str(len(scoreOUT.get_children()))+' item(s)')
  except Exception as e:
    raise e

def updateResults():
  try:
    dele1()
    saveTESTRE()
    tooltip(scoreOUT , [str(len(scoreOUT.get_children()))+' Course Unit(s)'])
    retSVal.set(str(len(scoreOUT.get_children()))+' item(s)')
    messagebox.showinfo('MjB-Success','Result(s) Updated.')
    updbt.grid_remove()
    savebt.grid()
  except Exception as e:
    raise e
updbt.config(command=updateResults)

def popup(event):
  id=scoreOUT.identify_row(event.y)
  if id:
    scoreOUT.selection_set(id)
    menu1.post(event.x_root, event.y_root)    

scoreOUT.configure(selectmode="extended")

menu1 = Menu(gpa, tearoff=0)
menu1.add_command(label="Edit", command=edt)
menu1.add_command(label="Delete", command=dele)
scoreOUT.bind("<Button-3>", popup)


#--------------Fsc1 dashbord-------------
dashF = Frame(Fsc1, bg="gray")
dashF.pack()


dashF1 = Frame(dashF, bg="gray")
dashF1.grid()

retSVal = IntVar()
retSVal.set("0 item(s)")

Label(dashF1, text="RETURNED ITEMS", font=('arial', 12, 'bold'), fg="white", bg='black', width=20).pack()
retS = Label(dashF1, text="", textvariable=retSVal, font=('arial', 12, 'bold'), fg="white", bg='blue', width=20)
retS.pack()

dashF2 = Frame(dashF, bg="gray")
dashF2.grid()

prnt = PhotoImage(file='pics/fileprint.png')
def entr1(*args):
  printScB.config(relief=SOLID, bg="white", fg="blue", text="Print Preview »", font=('arial', 10, 'bold'))

def entr0(*args):
  printScB.config(relief=FLAT, bg="blue", fg="white", text="Print Preview", font=('arial', 10, 'bold'))

Label(dashF2, text="COMMAND", font=('arial', 12, 'bold'), fg="white", bg='black', width=20).grid()

printScB = Button(dashF2, text=' Print Preview', image=prnt, compound=LEFT , cursor='hand2', font=('arial', 10, 'bold'), bg="blue", fg="white", relief="flat")
printScB.grid(pady=2)
printScB.bind("<Enter>", entr1)
printScB.bind("<Leave>", entr0)

def testsFinalv():
  LASTNAME = "null"
  PIN = "null"
  deloutput1()
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    sql3 = ('SELECT LASTNAME,PIN FROM accounts WHERE LASTNAME=? and PIN=?' )
    valz = (userN.get(), passW.get())
    cursor.execute(sql3, valz)
    value = cursor.fetchall()
    for (LASTNAME,PIN) in value:
      pass
    if(userN.get()==LASTNAME) and passW.get()==PIN:
      note.tab(3, state="normal")
      note.select(3)      
    else:
      messagebox.showerror("MjB-Login error", "You must be logged in to view tests results.")  
  except Exception as e:
    print(e)

#-----------------------save details------------------

sumPdt = Frame(tab11, )
sumPdt.pack()

sUm = Entry(sumPdt, fg="white", bg="black", textvariable=SumVal)
sUm.grid(row=0, column=0)

Pdt = Entry(sumPdt, fg="white", bg="black", textvariable=PdtVal)
Pdt.grid(row=1, column=0)

sUm1 = Entry(sumPdt, fg="white", bg="black", textvariable=SumVal1)
sUm1.grid(row=0, column=1)

Pdt1 = Entry(sumPdt, fg="white", bg="black", textvariable=PdtVal1)
Pdt1.grid(row=1, column=1)

sUm2 = Entry(sumPdt, fg="white", bg="black", textvariable=SumVal2)
sUm2.grid(row=0, column=2)

Pdt2 = Entry(sumPdt, fg="white", bg="black", textvariable=PdtVal2)
Pdt2.grid(row=1, column=2)

sUm3 = Entry(sumPdt, fg="white", bg="black", textvariable=SumVal3)
sUm3.grid(row=0, column=3)

Pdt3 = Entry(sumPdt, fg="white", bg="black", textvariable=PdtVal3)
Pdt3.grid(row=1, column=3)
sUm.grid_remove()
Pdt.grid_remove()
sUm1.grid_remove()
Pdt1.grid_remove()
sUm2.grid_remove()
Pdt2.grid_remove()
sUm3.grid_remove()
Pdt3.grid_remove()


def saveTESTRE():
  if (cuN.get()==""):
    msginfo1.config(text="Enter Course Unit.")
    cuN.focus()
  elif(cuC.get()==""):
    msginfo1.config(text="Enter Course Unit Code.")
    cuC.focus()
  elif(cU.get()==""):
    msginfo1.config(text="Enter Credit Units.")
    cU.focus()
  elif(testSc.get()==""):
    msginfo1.config(text="Enter Course Work scores.")
    testSc.focus()
  elif(FExam.get()==""):
    msginfo1.config(text="Select Final Exams scores.")
    FExam.focus()
  elif(Year1.get()==""):
    msginfo1.config(text="Select year of study.")
    Year1.focus()
  elif(Sem1.get()==""):
    msginfo1.config(text="Select Semester.")
    Sem1.focus()
  else:
    msginfo1.config(text="")
    x = scoreOUT.get_children()
    for item in x:
      scoreOUT.delete(item)
    try:
      conn = sqlite3.connect('dbs/mjbgpadata.db')
      cursor = conn.cursor()
      #----------------fetch grades-----------
      cursor.execute("SELECT fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=1")
      result = cursor.fetchall()
      for (fro_Score, to_Score, let_Score, weg_Score) in result:
        fro1 = fro_Score
        too1 = to_Score
        let1 = let_Score
        weg1 = weg_Score
      cursor.execute("SELECT fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=2")
      result = cursor.fetchall()
      for (fro_Score, to_Score, let_Score, weg_Score) in result:
        fro2 = fro_Score
        too2 = to_Score
        let2 = let_Score
        weg2 = weg_Score
      cursor.execute("SELECT fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=3")
      result = cursor.fetchall()
      for (fro_Score, to_Score, let_Score, weg_Score) in result:
        fro3 = fro_Score
        too3 = to_Score
        let3 = let_Score
        weg3 = weg_Score
      cursor.execute("SELECT fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=4")
      result = cursor.fetchall()
      for (fro_Score, to_Score, let_Score, weg_Score) in result:
        fro4 = fro_Score
        too4 = to_Score
        let4 = let_Score
        weg4 = weg_Score
      cursor.execute("SELECT fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=5")
      result = cursor.fetchall()
      for (fro_Score, to_Score, let_Score, weg_Score) in result:
        fro5 = fro_Score
        too5 = to_Score
        let5 = let_Score
        weg5 = weg_Score
      cursor.execute("SELECT fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=6")
      result = cursor.fetchall()
      for (fro_Score, to_Score, let_Score, weg_Score) in result:
        fro6 = fro_Score
        too6 = to_Score
        let6 = let_Score
        weg6 = weg_Score
      cursor.execute("SELECT fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=7")
      result = cursor.fetchall()
      for (fro_Score, to_Score, let_Score, weg_Score) in result:
        fro7 = fro_Score
        too7 = to_Score
        let7 = let_Score
        weg7 = weg_Score
      cursor.execute("SELECT fro_Score, to_Score, let_Score, weg_Score FROM grading WHERE ID=8")
      result = cursor.fetchall()
      for (fro_Score, to_Score, let_Score, weg_Score) in result:
        fro8 = fro_Score
        too8 = to_Score
        let8 = let_Score
        weg8 = weg_Score
      try:
        sco = int(int(testSc.get()) + int(FExam.get()))
        if float(fro1) <=float(sco)<=float(too1):
          SCOREGRADE1 = str(let1)
          GRADEWEIGHT1 = str(weg1)
          print(sco)
          print(SCOREGRADE1)
          print(GRADEWEIGHT1)
        elif float(fro2) <=float(sco)<float(too2):
          SCOREGRADE1 = str(let2)
          GRADEWEIGHT1 = str(weg2)
          print(sco)
          print(SCOREGRADE1)
          print(GRADEWEIGHT1)
        elif float(fro3) <=float(sco)<float(too3):
          SCOREGRADE1 = str(let3)
          GRADEWEIGHT1 = str(weg3)
          print(sco)
          print(SCOREGRADE1)
          print(GRADEWEIGHT1)
        elif float(fro4) <=float(sco)<float(too4):
          SCOREGRADE1 = str(let4)
          GRADEWEIGHT1 = str(weg4)
          print(sco)
          print(SCOREGRADE1)
          print(GRADEWEIGHT1)
        elif float(fro5) <=float(sco)<float(too5):
          SCOREGRADE1 = str(let5)
          GRADEWEIGHT1 = str(weg5)
          print(sco)
          print(SCOREGRADE1)
          print(GRADEWEIGHT1)
        elif float(fro6) <=float(sco)<float(too6):
          SCOREGRADE1 = str(let6)
          GRADEWEIGHT1 = str(weg6)
          print(sco)
          print(SCOREGRADE1)
          print(GRADEWEIGHT1)
        elif float(fro7) <=float(sco)<float(too7):
          SCOREGRADE1 = str(let7)
          GRADEWEIGHT1 = str(weg7)
          print(sco)
          print(SCOREGRADE1)
          print(GRADEWEIGHT1)
        elif float(fro8)<=float(sco)<float(too8):
          SCOREGRADE1 = str(let8)
          GRADEWEIGHT1 = str(weg8)
          print(sco)
          print(SCOREGRADE1)
          print(GRADEWEIGHT1)
      except Exception as e:
        print(e)

    except Exception as e:
      print(e)
    try:
      conn = sqlite3.connect('dbs/mjbgpadata.db')
      cursor = conn.cursor()

      cursor.execute('CREATE TABLE IF NOT EXISTS tests (NAME VARCHAR, YEAR VARCHAR  NOT NULL, SEMESTER VARCHAR  NOT NULL, COURSEUNIT VARCHAR NOT NULL, COURSEUNIT_CODE VARCHAR NOT NULL , CREDITUNITS INTEGER  NOT NULL, COURSEWORK INTEGER  NOT NULL, FINALEXAM INTEGER  NOT NULL,TOTALSCORE INTEGER  NOT NULL, GRADE VARCHAR, GRADEPOINTS FLOAT NOT NULL)')
      print('tests table created.')
      testsql = 'INSERT INTO tests (NAME, YEAR, SEMESTER ,COURSEUNIT,COURSEUNIT_CODE, CREDITUNITS, COURSEWORK, FINALEXAM,TOTALSCORE, GRADE, GRADEPOINTS) VALUES (?,?,?,?,?,?,?,?,?,?,?)'
      cuname = str(cuN.get())
      cucode = str(cuC.get())
      testVal = (str(userN.get()), Year1.get(), Sem1.get(), cuname.upper(), cucode.upper(), int(cU.get()),int(testSc.get()),int(FExam.get()),int(int(testSc.get()) + int(FExam.get())),SCOREGRADE1,float(GRADEWEIGHT1))
      cursor.execute(testsql,testVal)
      conn.commit()
      print("Test results added")
      cuN.delete(0,END)
      cuC.delete(0,END)
      cU.delete(0,END)
      testSc.delete(0,END)
      FExam.delete(0,END)
      Year1.delete(0,END)
      Sem1.delete(0,END)
      cuN.focus()
      tesctVal.set(value=0)
      examVal.set(value=0)
      cUvar.set(value=3)
      msginfo1.config(text="")

      try:
        conn = sqlite3.connect('dbs/mjbgpadata.db')
        cursor = conn.cursor()

        gpalist = []
        cursor.execute("CREATE TABLE IF NOT EXISTS gpadata (NAME VARCHAR, YEAR VARCHAR, SEMESTER VARCHAR, COURSEUNIT VARCHAR, CREDITUNITS INTEGER, PRODUCT FLOAT)")

        print('Done...')

        cursor.execute("SELECT NAME, YEAR, SEMESTER, COURSEUNIT, CREDITUNITS,GRADEPOINTS FROM tests")
        result = cursor.fetchall()
        for NAME, YEAR, SEMSTER, COURSEUNIT, CREDITUNITS,GRADEPOINTS in result:
          pass
        print(GRADEPOINTS)
        print(CREDITUNITS)
        print(COURSEUNIT)

        cursor.execute("SELECT (CREDITUNITS)*(GRADEPOINTS) FROM tests AS PRODUCT")
        result = cursor.fetchall()
        for PRODUCT in result:
          pass
        Pdt.delete(0, END)
        PdtVal.set(value = PRODUCT)
        print(float(Pdt.get()))

        sw = ("INSERT INTO gpadata (NAME, YEAR, SEMESTER, COURSEUNIT, CREDITUNITS,PRODUCT) VALUES (?,?,?,?,?,?) ")
        sm = (NAME, YEAR, SEMSTER, COURSEUNIT, CREDITUNITS, float(Pdt.get()))

        cursor.execute(sw, sm)
        print('Added...........')
        conn.commit()

      except Exception as e:
        raise e

    except Exception as e:
      msginfo1.config(text="Error:Check repeated information.")
      print(e)
    finally:
      sqlt = (str(userN.get()),)
      cursor.execute("SELECT * FROM tests WHERE NAME =?",sqlt)
      result = cursor.fetchall()
      for row in result:
        scoreOUT.insert('', END, values=row)
      conn.close()
      retSVal.set(str(len(scoreOUT.get_children()))+' item(s)')
      tooltip(scoreOUT , [str(len(scoreOUT.get_children()))+' Course Unit(s)'])
savebt.config(command=saveTESTRE)



def prntTest():
  note.tab(4, state="normal")
  note.select(4)
  display1.config(state="normal")
  display1.delete('1.0', END)
  txthd = "\t\t\tMjB RESULTS PRINT PREVIEW FOR "+str(userN.get())+"\n\t\t_________________________________________________________\n"
  display1.insert('1.0', txthd)
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    t1 =(str(userN.get()),)
    cursor.execute("SELECT YEAR, SEMESTER, COURSEUNIT,COURSEUNIT_CODE, CREDITUNITS,COURSEWORK, FINALEXAM,TOTALSCORE, GRADE, GRADEPOINTS FROM tests WHERE NAME=?",t1)
    result = cursor.fetchall()

    for (YEAR, SEMESTER, COURSEUNIT,COURSEUNIT_CODE, CREDITUNITS,COURSEWORK, FINALEXAM,TOTALSCORE, GRADE, GRADEPOINTS) in result:
      display1.insert(END, ("\nCOURSE UNIT   :   "+ COURSEUNIT +".\nCOURSEUNIT CODE   :    "+COURSEUNIT_CODE+".\nCREDIT UNITS   :   "+str(CREDITUNITS)+".\nCOURSE WORK (/40)    :   " +str(COURSEWORK)+".\nEXAM (/60)    :   "+str(FINALEXAM)+".\nTOTAL SCORE (/100)   :   "+str(TOTALSCORE)+ ".\nYEAR    :   "+YEAR +". \nSEMESTER   :   " +SEMESTER+".\nGRADE : "+GRADE+". \nGRADE POINTS : "+str(GRADEPOINTS)+"\n"))
    conn.close()

    display1.insert(END, "\n______________________________________________________________\nPrinted on: "+str(now)+"; At: "+str(time.strftime('%H:%M:%S'))+". © MjB-GPA")
    display1.config(state="disabled")
  except Exception as e:
    raise e
  finally:
    messagebox.showinfo("MjB-SAVE RESULTS", "Right click to save or print results.")
printScB.config(command=prntTest)


def printTest():
  LASTNAME = "null"
  PIN = "null"
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    sql3 = ('SELECT LASTNAME,PIN FROM accounts WHERE LASTNAME=? and PIN=?' )
    valz = (userN.get(), passW.get())
    cursor.execute(sql3, valz)
    value = cursor.fetchall()
    for (LASTNAME,PIN) in value:
      pass
    if(userN.get()==LASTNAME) and passW.get()==PIN:
      note.tab(6, state="normal")
      note.select(6)
      prntTest()  
      retSVal.set(str(len(scoreOUT.get_children()))+' item(s)')  
      tooltip(scoreOUT , [str(len(scoreOUT.get_children()))+' Course Unit(s)'])  
    else:
      messagebox.showerror("MjB-Login error", "You must be logged in to save or print tests results.")  
  except Exception as e:
    print(e)
#--------------------tests end here----------------

def closeview3():
  note.tab(4, state='hidden')

appc3 = Button(tab5, text='x', fg='white', command=closeview3, bg='red', relief=FLAT, font=('Verdana', 8, 'bold'))
appc3.pack(side=TOP, anchor=NE)
tip = tooltip(appc3 , ["Close view."])
#-------------print--preview-----------
Label(tab5, text="MjB-RESULTS PRINT PREVIEW",fg="blue", bg="lightgray", font=("timesnewromans", 15, "italic")).pack(fill=X, anchor=NW, side=TOP)
mainF = Frame(tab5)
mainF.pack(fill=BOTH)
mainF.rowconfigure(0, weight=1)
mainF.columnconfigure(0, weight=1)

mainF1 = Frame(mainF)
mainF1.pack(pady=2)
mainF1.rowconfigure(0, weight=1)
mainF1.columnconfigure(0, weight=1)


display1 = scrolledtext.ScrolledText(mainF1,bg="white",font=("times", 13), relief="solid",bd=1, width=90, height=18)
scrolbh = Scrollbar(mainF1,orient="horizontal",command=display1.xview, relief="flat")
scrolbh.pack(side=BOTTOM, anchor=N, fill=X)
display1.pack(side=TOP, anchor=S, pady=10)
txthd = "\t\t\t\tMjB GPA APP PRINT PREVIEW\n\t\t_________________________________________________________\n"
display1.insert('1.0', txthd)
display1.config(xscrollcommand=scrolbh.set, state="disabled")
tip = tooltip(display1 , ["RIGHT CLICK TO SAVE OR PRINT THESE RESULTS."])

#----------------------popup command-------------
def saveRe():
  ans = filedialog.asksaveasfilename(title="Save file as?",filetypes=[('WORD DOCUMENT FILE','*.doc')])

  filename = ans  
  try:
    my = open(filename+".doc", 'w')
    my.write(display1.get("1.0", "end-1c"))
    my.close()
    messagebox.showinfo("MjB-SAVE results", "Your results have been saved successfully.")
  except Exception as e:
    messagebox.showerror("MjB-SAVE results", "Your results have not been save.\nPlease try again.")

def priNt(*args):
  import os
  try:
    filename =  open("MjB results.txt", 'w')
    filename.write(display1.get("1.0", "end-1c"))
    filename.close()
    os.startfile("MjB results.txt", "print")    
  except Exception as e:
    messagebox.showerror("MjB-PRINT results", "Your results have not been printed.\nPlease try again.")


#-------------------diaplsy popup here-----------
popup1 = Menu(gpa, tearoff=0)
popup1.add_command(label="Save to file.", command=saveRe)
popup1.add_command(label="Print on paper.", command=priNt)

def do_popup1(event):
    # display the popup menu
    try:
        popup1.tk_popup(event.x_root, event.y_root, 1)
    except Exception as e:
      pass
    finally:
        # make sure to release the grab (Tk 8.0a1 only)
        popup1.grab_release()
display1.bind("<Button-3>", do_popup1)

#-----------print--preview ends here---------------


#---------------change password--------
def changePass():
  LASTNAME = "null"
  PIN = "null"
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    sql3 = ('SELECT LASTNAME,PIN,PASSWORD FROM accounts WHERE LASTNAME=? and PIN=?' )
    valz = (userN.get(), passW.get())
    cursor.execute(sql3, valz)
    value = cursor.fetchall()
    for (LASTNAME,PIN,PASSWORD) in value:
      pass
    if(userN.get()==LASTNAME) and passW.get()==PIN:
      askpass = simpledialog.askinteger("MjB-PASSWORD change", "Enter your current PIN!\n\nTip : Enter the exact pin you used to log in!")
      if(str(askpass)==PIN):
        messagebox.showwarning("MjB-User Password","You cannot change your password at this time.\n\nYour official password is '"+PASSWORD+"'.")
      else:
        messagebox.showerror("MjB-PASSWORD error", "You provided an incorrect PIN.\n\nPlease try again.")     
    else:
      messagebox.showerror("MjB-Login error", "You must be logged in to change your password.")     
  except Exception as e:
    raise e  


#---------------change pin--------
def changePin():
  LASTNAME = "null"
  PIN = "null"
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    sql3 = ('SELECT LASTNAME,PIN,PASSWORD FROM accounts WHERE LASTNAME=? and PIN=?' )
    valz = (userN.get(), passW.get())
    cursor.execute(sql3, valz)
    value = cursor.fetchall()
    for (LASTNAME,PIN,PASSWORD) in value:
      pass
    if(userN.get()==LASTNAME) and passW.get()==PIN:
      passw1 = simpledialog.askstring("MjB-PIN change", "For security reasons, you are reqired to provide your password!\n\nTip : Enter the exact password you used to create a new account!")
      
      if(passw1==PASSWORD):
        pin1 = simpledialog.askinteger("MjB-PIN change", "Enter your current PIN!\n\nTip : Enter the exact pin you used to log in!")
        if(str(pin1)==PIN):
          newpin = simpledialog.askinteger("MjB-PIN change", "Enter new PIN!\n\nTip : PIN length should be more than 4 digits.")
          if str(newpin)!="":
            try:
              conn = sqlite3.connect('dbs/mjbgpadata.db')
              cursor = conn.cursor()
              sql5 = "UPDATE accounts set PIN = ? where PASSWORD =?"
              val = (str(newpin), str(passw1))
              cursor.execute(sql5, val)
              conn.commit()
              conn.close()
              passW.delete(0, END)
              passW.insert(0, str(newpin))
              messagebox.showinfo("MjB-PIN change success!","PIN changed successfully.\n\nYour new PIN is '"+str(newpin)+"'.")
            except Exception as e:
              print(e)
          else:
            pass
        else:
          messagebox.showerror('MjB-PASSWORD error', "Incorrect pin.\n\nPlaease try again!")

      else:
        messagebox.showerror('MjB-PASSWORD error', "Sorry, the password you have provided doesnot match your account.\n\nPlaease try again!")
    else:
      messagebox.showerror("MjB-Login error", "You must be logged in to effect PIN changes.")     

  except Exception as e:
    raise e


#-------------forgot pin------------
def forgotPIN(*args):
  name1 = simpledialog.askstring("MjB-PIN reset", "For security reasons provide your Last name please!\n\nTip : Enter the exact name you used to create a new account!")
  passw1 = simpledialog.askstring("MjB-PIN reset", "Provide Password corresponding to this account!")
  list1 = []
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    sql3 = ('SELECT LASTNAME,PASSWORD,PHONE_NO FROM accounts WHERE LASTNAME=? and PASSWORD=?')
    testVal1 = (name1,passw1)
    cursor.execute(sql3, testVal1)
    value = cursor.fetchall()
    for (LASTNAME,PASSWORD,PHONE_NO) in value:
      list1.append(LASTNAME)
      list1.append(PASSWORD)
      list1.append(PHONE_NO)
    if(name1 and passw1) in list1:
      askPhone = simpledialog.askstring("MjB-PIN reset", "Provide Phone Number corresponding to this account!")
      if askPhone in list1:
        newpin = simpledialog.askinteger("MjB-PIN change", "Enter new PIN!\n\nTip : PIN length should be more than 4 digits.")
        if (len(str(newpin))<4):
          messagebox.showerror("MjB-PIN reset error","New PIN should atleast be four digits.")
        else:
          try:
            conn = sqlite3.connect('dbs/mjbgpadata.db')
            cursor = conn.cursor()
            sql5 = "UPDATE accounts set PIN = ? where  LASTNAME=? and PASSWORD =?"
            val = (str(newpin),str(name1), str(passw1))
            cursor.execute(sql5, val)
            conn.commit()
            conn.close()
            messagebox.showinfo("MjB-PIN reset success!","PIN changed successfully.\n\nYour new PIN is '"+str(newpin)+"'.")
          except Exception as e:
            print(e)
      else:
        messagebox.showerror("MjB-PIN reset error.","PIN reset failed.\nPlease try again and provide correct info about your account.")
    else:
      messagebox.showerror("MjB-PIN reset error.","Last Name or Password is incorrect.\nPlease try again.")
  except Exception as e:
    raise e
  

frgt.bind("<Button-1>", forgotPIN)
#---------------user info---------------
def viewInfo():
  LASTNAME = "null"
  PIN = "null"
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    sql3 = ('SELECT LASTNAME, PHONE_NO,PIN, UNIVERSITY,FIRSTNAME FROM accounts WHERE LASTNAME=? and PIN=?' )
    valz = (userN.get(), passW.get())
    cursor.execute(sql3, valz)
    value = cursor.fetchall()
    for (LASTNAME, PHONE_NO,PIN, UNIVERSITY,FIRSTNAME) in value:
      pass
    if(userN.get()==LASTNAME) and passW.get()==PIN:
      ask5 = messagebox.askokcancel("MjB-User info", "You`re about to view your info!")
      if(ask5==True):
        messagebox.showinfo("MjB-User info", "You're logged in as : "+LASTNAME+".\n\nPhone Number :"+PHONE_NO+".\n\nFull name : "+FIRSTNAME+" "+LASTNAME+".\n\nUniversity : "+UNIVERSITY)
    else:
      messagebox.showerror("MjB-Login error", "You must be logged in to view your info!")     

  except Exception as e:
    raise e


#--------------logout-------------------
def logout(*args):
  LASTNAME = "null"
  PIN = "null"
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    sql3 = ('SELECT LASTNAME,PIN, UNIVERSITY,FIRSTNAME FROM accounts WHERE LASTNAME=? and PIN=?' )
    valz = (userN.get(), passW.get())
    cursor.execute(sql3, valz)
    value = cursor.fetchall()
    for (LASTNAME,PIN, UNIVERSITY,FIRSTNAME) in value:
      pass
    if(userN.get()==LASTNAME) and passW.get()==PIN:
      ask1 = messagebox.askokcancel('MjB-LOGOUT','Hello '+userN.get()+'!\n\n You`re about to logout of the MjB-GPA APP.\nAll the open tabs will be closed!\n\n\tLOGOUT NOW?')
      if ask1 == True:
        userN.delete(0, END)
        passW.delete(0, END)
        clrsms()
        Year1.delete(0, END)
        Sem1.delete(0, END)
        retSVal.set('0 item(s)')
        note.tab(1, state="hidden")
        note.tab(2, state="hidden")
        note.tab(3, state="hidden")
        note.tab(4, state="hidden")
        note.tab(5, state="hidden")
        note.tab(6, state="hidden")
        note.tab(7, state="hidden")
        note.tab(8, state="hidden")
        note.tab(9, state="hidden")
        note.tab(10, state="hidden")
        note.tab(0, state="normal")
        note.select(0)
        userN.focus()
      else:
        pass
    else:
      messagebox.showerror("MjB-Logout error", "Sorry, you're not logged in!")     
  except Exception as e:
    print(e)


#----------------exit app--------------

def close():
  ans=messagebox.askokcancel("MjB-Close!", "You`re about to exit MjB-GPA APP!\n\nNote that you will be logged out and all open tabs closed!")
  if ans==True:
    messagebox.showinfo("MjB-Appreciation!", "Thanks for using MjB-SYSTEMS' APPS!\nFeel free to share the app!\n\nDeveloped by MUZOORA BARNABAS\nTEL: +256750941273 or +256780317932\nEmail: bmuzoora@gmail.com ")
    gpa.destroy()
  else:
    pass







#---------------dev info------------
def blue(*args):
  maill.config(fg='brown')
def blac(*args):
  maill.config(fg='white')

def closemm():
  note.tab(6, state='hidden')


Label(tab7, text="Developer Info", bg='gray', fg='blue', font=('Verdana', 20, 'bold')).pack(side=TOP, anchor=N, fill=X)
  
Mf = Frame(tab7, bg='blue')
Mf.pack(padx=2, pady=10)
images = PhotoImage(file="pics/dev.png")
appc = Button(Mf, text='x', fg='white', bg='brown', relief=FLAT, command=closemm, font=('Verdana', 10, 'bold'))
appc.pack(side=TOP, anchor=NE)
tooltip(appc, ['Closes window'])
F1 = Frame(Mf, bg='white')
F1.pack(side=LEFT, fill=BOTH, padx=2, pady=2)

f = Frame(Mf, bg='white')
f.pack(fill=BOTH, padx=2, pady=2)

devpic = Label(F1, image=images, bg='black')
devpic.pack(side=LEFT, padx=2, pady=2, fill=BOTH)
tooltip(devpic, ['CEO MjB SYSTEMS'])

def ma1(*args):
  webbrowser.open_new(r"http://malto:bmuzoora@gmail.com")

Label(f, text="Name", bg='black', fg='white', font=('Verdana', 15, 'bold')).pack(fill=X, padx=1, pady=1)
name = Label(f, text="Muzoora Barnabas", bg='gray', fg='white', font=('Verdana', 18, 'bold'))
name.pack(fill=X, padx=1, pady=1)
tooltip(name, ['FACEBOOK USERNAME'])
Label(f, text="University", bg='black', fg='white', font=('Verdana', 15, 'bold')).pack(fill=X, padx=1, pady=1)
campo = Label(f, text="Bishop Stuart University", bg='gray', fg='white', font=('Verdana', 18, 'bold'))
campo.pack(fill=X, padx=1, pady=1)
tooltip(campo, ['OUR GOD REIGNS'])
Label(f, text="Company", bg='black', fg='white', font=('Verdana', 15, 'bold')).pack(fill=X, padx=1, pady=1)
camp = Label(f, text="MjB SYSTEMS", bg='gray', fg='white', font=('Verdana', 18, 'bold'))
camp.pack(fill=X, padx=1, pady=1)
tooltip(camp, ['WE`RE THE BIG DEAL.'])
Label(f, text="Email", bg='black', fg='white', font=('Verdana', 15, 'bold')).pack(fill=X, padx=1, pady=1)
maill = Label(f, text="bmuzoora@gmail.com", cursor='hand2', bg='gray', fg='white', font=('Verdana', 18, 'bold'))
maill.pack(fill=X, padx=1, pady=1)
maill.bind('<1>', ma1)
maill.bind('<Enter>', blue)
maill.bind('<Leave>', blac)

Label(f, text="Telphone Nos.", bg='black', fg='white', font=('Verdana', 15, 'bold')).pack(fill=X, padx=1, pady=1)
tel = Label(f, text="0750941273 & 0780317932", bg='gray', fg='white', font=('Verdana', 18, 'bold'))
tel.pack(fill=X, padx=1, pady=1)
tooltip(tel, ['CALL 24/7. ALWAYS AVAILABLE'])
Label(f, text="©2019-MjB SYSTEMS INFO", bg='black', fg='white', font=('Verdana', 10, 'bold','italic')).pack(fill=X, padx=1, pady=1)
#--------------dev info--------------------

#-----------------app usage----------------------
def closem():
  note.tab(5, state='hidden')

def appusage():
  note.tab(5, state='normal')
  note.select(5)

manP.config(command=appusage)
manAP.config(command=appusage)
appc = Button(tab6, text='x', fg='white', bg='red', relief=FLAT, command=closem, font=('Verdana', 8, 'bold'))
appc.pack(side=TOP, anchor=NE)
tip = tooltip(appc , ["Close mannual."])

about = scrolledtext.ScrolledText(tab6,bg="lightgray",font=("Verdana", 13, 'bold'), relief="flat",bd=1, width=110, height=18)
about.pack(padx=20, pady=5)
tip = tooltip(about , ["MjB GPA USER MANUAL"])
about.tag_configure('h1', font=('Verdana', 18, 'bold','underline'), foreground='brown')
about.tag_configure('h2', font=('Verdana', 15, 'bold','italic'), foreground='blue')
about.tag_configure('h3', font=('Verdana', 13, 'bold','italic'), foreground='black')
about.insert('1.0','\t\t\t\tMjB-GPA APP MANUAL\n', 'h1')
wlcm = """
 Welcome dear to this amazing Grade Point Average [GPA] desktop application [MjB GPA APP]; Please read the instructions below on
 how to use a few features in this appliction.
"""
about.insert(END, wlcm)
about.insert(END,'\n1.  LOGIN      ===>  ', 'h2')
loginPIC = PhotoImage(file='pics/Mlogin.png')
about.image_create(END, image=loginPIC)
logn = """
This part is meant to ensure security of the user`s saved data. The user`s Last name and Pin are required to login.
If the user has no account, its recommended that they signup to create a new account!

In the LAST NAME field, choose your account name; Then enter its PIN then LOGIN.
"""
about.insert(END, logn)
about.insert(END,'\n\n2.  SIGN UP      ===>  ', 'h2')
signPIC = PhotoImage(file='pics/Msignup.png')
about.image_create(END, image=signPIC)
sgn = """
In this part, Users are given a chance to create their own accounts by filling in the required fields. All provided information is kept
confidential.
BOTH PASSWORD and PIN are required.
NOTE : Use THE NUMBER PAD on the right of the APPLICATION to enter PIN.
"""
about.insert(END, sgn)
about.insert(END,'\n\n3.  USER DASHBORD    ===>  ', 'h2')
dashPIC = PhotoImage(file='pics/Mdash.png')
about.image_create(END, image=dashPIC)
testsinfo = """
This is called the USER QUICK DASHBORD MENU, here you can access multiple TOOLS by just selecting its BUTTON.
"""
about.insert(END, testsinfo)
about.insert(END,'\n\n4.  MARKS ENTRY PAGE  ===>  ', 'h2')
marksPIC = PhotoImage(file='pics/Mmarks.png')
about.image_create(END, image=marksPIC)
gpp = """
This is the MAIN part of this APPLICATION, Here You are required to fill the information as required; After use the "Save" button to
save the information in the database.

The APPLICATION provide a preview to your saved information including your GRADE POINTS, TOTAL SCORES,
GRADE, GRADE WEIGHT etc.
If there is an error in the saved data, you can SELECT that item and RIGHT CLICK on it; a menu will appear with EDIT
and DELETE options.
The choice is upon you.

The previewed results can be PRINTED or exported to an external WORD file.
"""
about.insert(END, gpp)
about.insert(END, '\n\n5. PRINT PREVIEW  ===>  ', 'h2')
printPIC = PhotoImage(file='pics/Mprint.png')
about.image_create(END, image=printPIC)
about.insert(END, '''
 Here, you can preview information saved in the database, especially information about the entered course units.
 To print, please RIGHT CLICK in the data shown; then make a choice between the two options tha will show.

 If you choose to save to file; the APPLICATION will open where you want to save your document;
enter document name, choose where to save the file and hit save.
 ''')
about.insert(END, '\n\n6. GPA and CGPA  ===> ', 'h2')
cgpaPIC = PhotoImage(file='pics/Mcgpa.png')
about.image_create(END, image=cgpaPIC)
about.insert(END, '''
  In this part, The program provides your score output according to what you want to preview.

  To get GPA;
1. Select a year in the year selection;
2. Select semester in the semester selection.
3. Click FETCH button.

   If the Information/marks where saved, the application will provide you with your exact GPA for the selection.
Repeat procedures 1 to 3 to know all your GPA results for every YEAR and SEMESTER.


 To get CGPA;
1. Select  year in the year selection;
2. Click FETCH button.

  Then the exact CGPA will show with correspondig DEGREE results; ie. WEIGHT and CLASS.

  ''')
about.insert(END,'\n\n7. GRADING SYSTEM  ===>  ', 'h2')
gradePIC = PhotoImage(file='pics/Mgrade.png')
about.image_create(END, image=gradePIC)
about.insert(END,"""
All calculations done by this APPLICATION are based on this GRADING SYSTEM, however if it changes;
since it varies with different instuitions, the ADMIN can EDIT or change it to vary with the GRADING you want.

To access the editable grading system, LOGIN with the provided ADMIN account; below is further information about ADMIN. 
 """)
about.insert(END, '\n\n8. ADMINISTRATOR  ===>  ', 'h2')
adminPIC = PhotoImage(file='pics/Madmin.png')
about.image_create(END, image=adminPIC)
about.insert(END,"""
  THIS IS THE DASHBOARD THAT SHOWS UP ONCE YOU HAVE GOT ADMIN ACCESS.

  ROLE OF THE ADMIN ACCOUNT.

>>> The admin majory is meant to provide the correct grading system to this application.
>>> To gain access to the ADMIN account, please call me via (+256)0780317932 or (+256)0750941273 for the PIN.
>>> PIN request will only cost 100,000 Ug Shs.
>>> Once you have got access to the ADMIN account, you can be able to change this PIN and the grading system.
""")
about.insert(END, '\n\n9. CHANGING GRADING SYSTEM  ===>  ', 'h2')
editPIC = PhotoImage(file='pics/Medit.png')
about.image_create(END, image=editPIC)
about.insert(END, """
    PROCEDURES.
1. ON the ADMIN DASHBOARD, click GRADING SYSTEM button.
2. The GRADING SYSTEM page will appear, select/click EDIT button.
3. The edit pannel will appear as shown in the image above.
4. Now you can make chages by entering the  NEW GRADING SYSTEM following the "Score Range", "Grade Letter" and "Letter Weight" or GRADE POINT.
    
    PLEASE ensure that all fields are entered and are not repeating.

Once the NEW GRADING SYSTEM is entered, Click UPDATE button to confirm changes.
The grading will ONLY AFFECT the fresh entered results.

Now SELECT BACK button to hide the edit pannel.
""")

about.insert(END, '\n10. CONTACT US/ME ===> ', 'h2') 
contactPIC = PhotoImage(file='pics/Mcontact.png')
about.image_create(END, image=contactPIC) 
about.insert(END, """
This APPLICATION also supports sending SMS but only when your computer is connected to internet.

To do this, access the CONTAS US page from the DASHBOARD; it will take you to a page similar to the image above.

 *Required are the NAME, EMAIL, PHONE NO, and the MESSAGE to send.
ADMIN PIN requests can also be sent here for free after paying the ADMIN ACCOUNT fee stated in the manual above.

Your name and Phone number will be captured at signup and will be entered automatically in their fields.
Then hit SEND once all fiels are complete.
""")
about.insert(END, '\n\n11. DEVELOPER PAGE  ===>', 'h2') 
devPIC = PhotoImage(file='pics/Mdev.png')
about.image_create(END, image=devPIC)
about.insert(END, """
To access this page, find the DEVELOPER PAGE button on the dashboard; crutial information is available;
This includes NAMES, UNIVERSITY, EMAIL, PHONE NUMBERS etc.

CONTACT ME USING THE PROVIDED INFORMATION ON THIS PAGE.
FOR FEED BACK MAIL ME TO MY EMAIL ADDRESS.
FOR DONATIONS OR HIRE OR JOB, CALL ME.
  """)

about.insert(END,"""\n\nHope this explains a few features in this APPLICATION; enjoy and share with others.
  FOR GOD AND MY COUNTRY
  OUR GOD REIGNS
  """)
sigPIC = PhotoImage(file='pics/mysign.png')
about.image_create(END, image=sigPIC)
about.insert(END,"""
  MUZOORA BARNABAS
  """)


def clrsms():
  smsName.delete(0, END)
  smsEmail.delete(0, END)
  smsPhone.delete(0, END)
  smsMsg.delete("1.0", END)

def closecontct():
  note.tab(7, state="hidden")
  clrsms()

#--------------------------contact us pages.
contimage = PhotoImage(file="pics/smspng.png")

Button(tab8,command=closecontct, text="x", fg="white", font=("arial", 10, "bold"), bg="red", relief="flat").pack(side=RIGHT, anchor=N)

contF = Frame(tab8, relief=SOLID, bd=1, bg="black")
contF.pack(pady=5, padx=5)

#-minsize, -pad, -uniform, or -weight
Label(contF, image=contimage,).pack(side=LEFT, fill=BOTH,pady=5, padx=5)
CONf = Frame(contF)
CONf.pack(fill=BOTH, pady=5, padx=5)
CONf.rowconfigure(0, weight=1)
CONf.columnconfigure(0, weight=1)
contF.rowconfigure(0, weight=1)
contF.columnconfigure(0, weight=1)
tab8.rowconfigure(0, weight=1)
tab8.columnconfigure(0, weight=1)

Label(CONf, text="SMS INFORMATION.", bg="blue", fg="white", font=('arial', 20, 'bold')).grid(row=0, columnspan=2, sticky=(E+W))
Label(CONf, text="Name", fg="white", bg="blue", font=('arial', 15, 'bold')).grid(row=1, column=0, sticky=(E+W), padx=5, pady=5)
Label(CONf, text="Email", fg="white", bg="blue", font=('arial', 15, 'bold')).grid(row=2, column=0, sticky=(E+W), padx=5, pady=5)
Label(CONf, text="Phone No", fg="white", bg="blue", font=('arial', 15, 'bold')).grid(row=3, column=0, sticky=(E+W), padx=5, pady=5)
Label(CONf, text="Message", fg="white", bg="blue", font=('arial', 15, 'bold')).grid(row=4, column=0, sticky=(E+W+N), padx=5, pady=5)

smsName = Entry(CONf, font=('arial', 15, 'bold'),state="disabled", justify="center", bg="lightgray", relief="solid")
smsName.grid(row=1, column=1, sticky=(E+W), padx=5, pady=5)
tooltip(smsName, ["To change the name, Login again/signup."])

smsEmail = Entry(CONf, font=('arial', 15, 'bold'), justify="center", bg="lightgray", relief="solid")
smsEmail.grid(row=2, column=1, sticky=(E+W), padx=5, pady=5)
tooltip(smsEmail, ["This field is required!"])

smsPhone = Entry(CONf, font=('arial', 15, 'bold'),state="disabled", justify="center", bg="lightgray", relief="solid")
smsPhone.grid(row=3, column=1, sticky=(E+W), padx=5, pady=5)
tooltip(smsPhone, ["This will ease contacting you!"])

txtF=Frame(CONf, relief="solid", bg="lightgray", bd=1)
txtF.grid(row=4, column=1, sticky=(E+W), padx=5, pady=5)
smsMsg = scrolledtext.ScrolledText(txtF, font=('arial', 10, 'bold'), height=11, width=60, bg="lightgray", relief="flat")
smsMsg.grid()
tooltip(smsMsg, ["Your message!"])

smsName.rowconfigure(0, weight=1)
smsName.columnconfigure(0, weight=1)
smsEmail.rowconfigure(0, weight=1)
smsEmail.columnconfigure(0, weight=1)
smsPhone.rowconfigure(0,weight=1)
smsPhone.columnconfigure(0, weight=1)
smsMsg.rowconfigure(0, weight=1)
smsMsg.columnconfigure(0, weight=1)

def change1(*args):
  sendB.config(text="SEND »")
def change(*args):
  sendB.config(text="SEND")
def contct():
  note.select(7)
  try:
    conn = sqlite3.connect('dbs/mjbgpadata.db')
    cursor = conn.cursor()
    sql3 = ('SELECT FIRSTNAME, LASTNAME, PHONE_NO,PIN FROM accounts WHERE LASTNAME=? and PIN=?' )
    valz = (userN.get(), passW.get())
    cursor.execute(sql3, valz)
    value = cursor.fetchall()
    for (FIRSTNAME, LASTNAME, PHONE_NO,PIN) in value:
      pass
    smsName.config(state="normal")
    smsPhone.config(state="normal")
    smsName.delete(0, END)
    smsPhone.delete(0, END)
    smsEmail.delete(0,END)
    smsMsg.delete('1.0', END)
    smsName.insert(0,str(FIRSTNAME+" "+LASTNAME))
    smsPhone.insert(0,str(PHONE_NO))
    smsName.config(state="disabled")
    smsPhone.config(state="disabled")    
  except Exception as e:
    raise e
contP.config(command=contct)
def sendsms():
  if(smsEmail.get()==""):
    smsEmail.config(bg="pink")
    smsEmail.focus()
  elif(smsMsg.get("1.0", "end-1c")==""):
    smsMsg.config(bg="pink")
    smsMsg.focus()
  elif "@" not in smsEmail.get():
    smsEmail.config(bg="pink")
    messagebox.showerror("Email error.",smsEmail.get()+" is not a valid email address.\nEnter a valid address please.")
    smsEmail.focus()
  elif ".com" not in smsEmail.get():
    smsEmail.config(bg="pink")
    messagebox.showerror("Email error.",smsEmail.get()+" is not a valid email address.\nEnter a valid address please.")
    smsEmail.focus()
  elif(len((smsPhone.get()))<10):
    smsPhone.config(state="normal")
    smsPhone.config(bg="pink")
    messagebox.showerror("Phone Number error.","Phone No "+smsPhone.get()+" should have atleast 10 digits.")
    smsPhone.config(state="normal")
    smsPhone.focus()
  else:
    try:
      # Initialize SDK
      username = "mjbgpaapp"    # use 'sandbox' for development in the test environment
      api_key = "384ddab8ed2296c532f605574fe394f955428661463aa6f714e7b84b6cbac602"# use your sandbox app API key for development in the test environment
      africastalking.initialize(username, api_key)


      # Initialize a service e.g. SMS
      sms = africastalking.SMS

      # Or use it asynchronously
      def on_finish(error, response):
          if error is not None:
              messagebox.showerror("SMS SENDING ERROR.", str(error))
          print(response)

      sms.send("MjB GPA APP\n_________________\n"+(str((smsName.get()+"\n"+smsPhone.get()+"\n"+smsEmail.get()+"\nMessage : "+smsMsg.get('1.0', END)))), ["+256750941273"], callback=on_finish)

    except Exception as e:
        messagebox.showerror("SMS SENDING ERROR.", str(e)) 
    else:
      messagebox.showinfo("SMS SENDING SUCCESS.", "Thank you "+smsName.get()+" for contacting MjB SYSTESM.\n We shall inbox you via "+ smsEmail.get()+" or "+smsPhone.get()) 
      clrsms()

def allowsms():
  LASTNAME = "null"
  PASS = "null"
  try:
      conn = sqlite3.connect('dbs/mjbgpadata.db')
      cursor = conn.cursor()
      sql3 = ('SELECT LASTNAME,PIN, UNIVERSITY,FIRSTNAME FROM accounts WHERE LASTNAME=? and PIN=?' )
      valz = (userN.get(), passW.get())
      cursor.execute(sql3, valz)
      value = cursor.fetchall()
      for (LASTNAME,PIN, UNIVERSITY,FIRSTNAME) in value:
        pass
      if(userN.get()==LASTNAME) and passW.get()==PIN:
        contct()
      else:
        messagebox.showerror("MjB-Login error", "Login to contact us please!")     
  except Exception as e:
    print(e)

sendB = Button(CONf, text="SEND", font=('arial', 12, 'bold'), cursor="hand2", bg="blue", relief="solid", bd=1, width=10, fg="white")
sendB.grid(columnspan=2, padx=10, pady=15)
sendB.bind("<Enter>", change1)
sendB.bind("<Leave>", change)
sendB.config(command=sendsms)

def devinfoo():
  note.tab(6, state='normal')
  note.select(6)
devP.config(command=devinfoo)
def aboutmjb():
  messagebox.showinfo('About MjB SYSTEMS','MjB SYSTEMS is an upcoming computer company with \nMuzoora Branabas as the CEO.\nBabeiha Wilson as Developer.\nand Nuwagira Nebert as our Sales and Marketing director.\n\nWe provide services like WEB DESIGNING, SOFTWARE DEVELOPING, SOCIAL MARKETTING FOR BUSINESSES etc.\n\nConnect with us.\nEmail : mjbsystems@gmail.com\nWebste : www.mjbsystems.com')

def abtapp():
  messagebox.showinfo('About MjB-GPA APP', 'This is strictly desktop app that is strictly for use by University Instutions.\n\n1. It helps to find Grade Point for every score.\n2. It also helps to calculate Grade Point Average for    UniversityStudents.\n3. Also helps to calculate CGPA for every year studied.\n4. Helps to inform students about the attained degree. \n5. Finally, helps to save all scores marks and all the above in     a database for reference.\n\nDesigned by MjB SYSTEMS` CEO.')


about.config(state='disabled')
#---------------main menu starts here------------------
menu = Menu(gpa)
gpa.config(menu=menu)
#---------------file menu----------
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit       Alt+F4", command=close)


#---------------accounts-----------
accmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Account Settings", menu=accmenu)
accmenu.add_command(label="Change Pin", command=changePin)
accmenu.add_separator()
accmenu.add_command(label="Forgot Password", command=changePass)
accmenu.add_separator()
accmenu.add_command(label="View User Info", command=viewInfo)
accmenu.add_separator()
accmenu.add_command(label="Logout", command=logout)

#----------------about menu----------
aboutmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="About", menu=aboutmenu)
aboutmenu.add_command(label="MjB GPA APP", command=abtapp)
aboutmenu.add_separator()
aboutmenu.add_command(label="Developer.", command=devinfoo)
aboutmenu.add_separator()
aboutmenu.add_command(label="MjB SYSTEMS", command=aboutmjb)
#-----------------help menu---------------
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="App Manual.", command=appusage)
helpmenu.add_separator()
helpmenu.add_command(label="Contact me.", command=allowsms)

#----------expansion on screen----------


tab1.rowconfigure(0, weight=1)
tab1.columnconfigure(0, weight=1)
tab2.rowconfigure(0, weight=1)
tab2.columnconfigure(0, weight=1)
tab3.rowconfigure(0, weight=1)
tab3.columnconfigure(0, weight=1)
tab4.rowconfigure(0, weight=1)
tab4.columnconfigure(0, weight=1)
tab5.rowconfigure(0, weight=1)
tab5.columnconfigure(0, weight=1)
tab6.rowconfigure(0, weight=1)
tab6.columnconfigure(0, weight=1)
tab7.rowconfigure(0, weight=1)
tab7.columnconfigure(0, weight=1)
tab8.rowconfigure(0, weight=1)
tab8.columnconfigure(0, weight=1)
tab9.rowconfigure(0, weight=1)
tab9.columnconfigure(0, weight=1)
tab10.rowconfigure(0, weight=1)
tab10.columnconfigure(0, weight=1)
mFrame.rowconfigure(0, weight=1)
mFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)
mainFrame.columnconfigure(0, weight=1)
note.rowconfigure(0, weight=1)
note.columnconfigure(0, weight=1)
gpa.rowconfigure(0, weight=1)
gpa.columnconfigure(0, weight=1)
gpa.protocol("WM_DELETE_WINDOW", close)
gpa.mainloop()
#--------------------------code by MUZOORA BARNABAS---------------------
#--------------------------BCS TWO SEMESTER 2 2018---------------------
#--------------------------BSU UNIVERSITY------------------------------