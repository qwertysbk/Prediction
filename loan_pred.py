from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import pandas as pd

windows = tk.Tk()
windows.title("PREDICT LOAN")
windows.geometry("680x430")
render=ImageTk.PhotoImage(Image.open('loanpred.jpg'))
img=tk.Label(windows,image=render)
img.place(x=0,y=0)
windows.resizable(False, False)

L1 = tk.Label(windows, text='LOAN PREDICTION...',bg='white' ,fg='black', font=('Times New Roman',25))
L1.place(x=10, y=40)
L1.pack()
L1 = tk.Label(windows, text='Gender', bg='black', fg='white', height=1, width=15, font=('Times New Roman', 12))
L1.place(x=40, y=70)
txt1 = tk.Entry(windows, width=50)
txt1.place(x=170,y=70)
L1 = tk.Label(windows, text='Married', bg='black', fg='white', height=1, width=15, font=('Times New Roman', 12))
L1.place(x=40, y=100)
txt2 = tk.Entry(windows, width=50)
txt2.place(x=170,y=100)
L1 = tk.Label(windows, text='Education', bg='black', fg='white', height=1, width=15, font=('Times New Roman', 12))
L1.place(x=40, y=130)
txt3= tk.Entry(windows, width=50)
txt3.place(x=170,y=130)
L1 = tk.Label(windows, text='Self Employed', bg='black', fg='white', height=1, width=15, font=('Times New Roman', 12))
L1.place(x=40, y=160)
txt4= tk.Entry(windows, width=50)
txt4.place(x=170,y=160)
L1 = tk.Label(windows, text='Applicant Income', bg='black', fg='white', height=1, width=15, font=('Times New Roman', 12))
L1.place(x=40, y=190)
txt5= tk.Entry(windows, width=50)
txt5.place(x=170,y=190)
L1 = tk.Label(windows, text='Loan Amount', bg='black', fg='white', height=1, width=15, font=('Times New Roman', 12))
L1.place(x=40, y=220)
txt6= tk.Entry(windows, width=50)
txt6.place(x=170,y=220)
L1 = tk.Label(windows, text='  Loan Amount Term  ', bg='black', fg='white', height=1, width=15, font=('Times New Roman', 12))
L1.place(x=40, y=250)
txt7= tk.Entry(windows, width=50)
txt7.place(x=170,y=250)
L1 = tk.Label(windows, text='Credit History', bg='black', fg='white', height=1, width=15, font=('Times New Roman', 12))
L1.place(x=40, y=280)
txt8= tk.Entry(windows, width=50)
txt8.place(x=170,y=280)
L1 = tk.Label(windows, text='Propert Area', bg='black', fg='white', height=1, width=15, font=('Times New Roman', 12))
L1.place(x=40, y=310)
txt9= tk.Entry(windows, width=50)
txt9.place(x=170,y=310)

'''menu= StringVar()
menu.set("Select Any Language")
drop= OptionMenu(windows, menu,"C++", "Java","Python","JavaScript","Rust","GoLang")
drop.pack()'''
'''rad1=Radiobutton(windows,text='Gender',value=0)
rad2=Radiobutton(windows,text='Gender',value=1)
rad1.grid(column=230,row=380)
rad2.grid(column=230,row=400)'''


def ok():
    global L5
    df = pd.read_csv('loan_prediction.csv')
    df.head()
    a = int(txt1.get())
    b = int(txt2.get())
    c = int(txt3.get())
    d = int(txt4.get())
    e = int(txt5.get())
    f = int(txt6.get())
    g = int(txt7.get())
    h = int(txt8.get())
    i = int(txt9.get())


    df.isnull().sum()
    df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].mean())
    df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].median())
    df.isnull().sum()
    df.dropna(inplace=True)
    df.isnull().sum()


    df['Loan_Status'].replace('Y',1,inplace=True)
    df['Loan_Status'].replace('N',0,inplace=True)
    df['Loan_Status'].value_counts()
    df.Gender=df.Gender.map({'Male':1,'Female':0})
    df['Gender'].value_counts()
    df.Married=df.Married.map({'Yes':1,'No':0})
    df['Married'].value_counts()
    df.Education=df.Education.map({'Graduate':1,'Not Graduate':0})
    df['Education'].value_counts()
    df.Self_Employed=df.Self_Employed.map({'Yes':1,'No':0})
    df['Self_Employed'].value_counts()
    df.Property_Area=df.Property_Area.map({'Urban':2,'Rural':0,'Semiurban':1})
    df['Property_Area'].value_counts()
    df['Loan_Amount_Term'].value_counts()

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression

    X = df.iloc[:,:-1].values
    y = df.iloc[:,-1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=0)

    model = LogisticRegression()
    model.fit(X_train,y_train)
    s = [[a, b, c, d, e, f, g, h, i]]
    result = model.predict(s)
    if result==0:
        L5 =tk.Label(windows,text='Loan will be approved...',bg='white',fg='black', font=('Times New Roman', 15))
        L5.place(x=200, y=360)
    else:
        L5 =tk.Label(windows,text='Loan will not be approved...',bg='white',fg='black', font=('Times New Roman', 15))
        L5.place(x=200, y=360)
    
def bye():
    '''mb.showinfo('WARNING!!!','The Screen will be closed...')'''
    L5.destroy()
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)
    txt5.delete(0, END)
    txt6.delete(0, END)
    txt7.delete(0, END)
    txt8.delete(0, END)
    txt9.delete(0, END)

def exit():
    windows.destroy()

b1=tk.Button(windows,text='PREDICT',bg='white',fg='black',height=1,width=6,command=ok)
b1.place(x=590, y=200)

b7=tk.Button(windows,text='CLEAR',bg='white',fg='black',height=1,width=7,command=bye)
b7.place(x=590, y=240)

b7=tk.Button(windows,text='EXIT',bg='black',fg='white',height=1,width=7,command=exit)
b7.place(x=590, y=300)

windows.mainloop()