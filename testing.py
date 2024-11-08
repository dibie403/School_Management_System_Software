import tkinter

import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
#from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from customtkinter import *
import calendar
from datetime import datetime
from tkinter import ttk
import pymysql
import pandas as pd
import cryptography
import os


import time
class App:
    def __init__(self):
        #self.login_window=tkinter.Toplevel()
        self.messagebox = None
        self.Splashwindow = tk.Tk()
        self.Splashwindow.title('School Management System')
        self.Splashwindow.geometry('1000x650')

        # Center the window on the screen
        window_width = 700
        window_height = 550
        screen_width = self.Splashwindow.winfo_screenwidth()
        screen_height = self.Splashwindow.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.Splashwindow.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
        self.Splashwindow.config(bg='white')
        #icon photo
        self.image_icon1 = Image.open('images/360_F_238940516_0BihE7YocY9vpgClPDDWuuaLneDwxtWn.jpg')
        self.image_icon1 = ImageTk.PhotoImage(self.image_icon1)
        self.Splashwindow.iconphoto(False, self.image_icon1)
        print("loginwindow() executed successfully.")

        self.image2 = Image.open('images/logo.png')
        self.image2 = ImageTk.PhotoImage(self.image2)
        self.label2 = tk.Label(self.Splashwindow, image=self.image2, bg='white')
        self.label2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.label3 = tk.Label(self.Splashwindow, text='SCHOOL MANAGEMENT SYSTEM',
                               bg='white', fg='forestgreen', font=('Times', 20))
        self.label3.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        #self.Splashwindow.update_idletasks()
        #time.sleep(0.9)
        self.Splashwindow.after(6000,self.loginwindow)
        #self.Splashwindow .after(2000,self.destroy_window())
        #self.loginwindow()
        #self.Splashwindow.update_idletasks()
        #time.sleep(0.8)
        #self.loginwindow()
        #self.login_window=tk.Tk()
        #self.loginwindow()

    def test(self):
        self.Splashwindow.destroy()

        self.login_window = tk.Tk()
        self.login_window.title('School MAnagement System')
        self.login_window.geometry('1000x600')
        self.login_window.config(bg='white')
        # self.login_window.resizable(False, False)
    def loginwindow(self):
        self.switch_window()
        self.Splashwindow.destroy()
        self.clock()
        self.login_window =tk.Tk()
        self.login_window.title('School MAnagement System')
        self.login_window.geometry('1000x600')
        self.login_window.config(bg='white')

        window_width = 1000
        window_height = 600
        screen_width = self.login_window.winfo_screenwidth()
        screen_height = self.login_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.login_window.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
        self.login_window.resizable(False, False)


        self.image_icon2 = Image.open('images/360_F_238940516_0BihE7YocY9vpgClPDDWuuaLneDwxtWn.jpg')
        self.image_icon2 = ImageTk.PhotoImage(self.image_icon2)
        self.login_window.iconphoto(False, self.image_icon2)
        #self.Splashwindow.iconbitmap('free-convert-icon-3213-thumb - Copy.png')
        print("loginwindow() executed successfully.")
        print('i will debug u')

        self.frame1 = ctk.CTkFrame(self.login_window, fg_color='mediumseagreen', width=450,
                                   height=600,corner_radius=10)
        self.frame1.place(relx=0.67, rely=0.1)
        self.frame1.pack(side=tk.RIGHT, padx=10, pady=10)

        print('hello')
        self.image3 = Image.open('images\logo.png')

        self.image3 = ImageTk.PhotoImage(self.image3)
        self.label4 = tk.Label(self.login_window, image=self.image3, bg='white')
        self.label4.pack(side=LEFT, padx=120, pady=10)
        print('hi')
        #creating labels on th frame

        labelwlcm=ctk.CTkLabel(self.frame1, text='Welcome Back!',font=('Italian bold', 30),
                               text_color='white',fg_color='mediumseagreen')
        labelwlcm.place(relx=0.05,rely=0.11)
        labelwlcm2 = ctk.CTkLabel(self.frame1, text='sign into your account', font=('Ariel', 20),
                                 text_color='white', fg_color='mediumseagreen')
        #'#173662'
        labelwlcm2.place(relx=0.05, rely=0.18)
        print('how about here')
        #for padlock
        self.image_padlock = Image.open('images/user (2).png')
        self.image_padlock = ctk.CTkImage(self.image_padlock)
        self.label1F1 = ctk.CTkLabel(self.frame1, text='User_ID:', compound=tk.LEFT, image=self.image_padlock,
                                    fg_color='mediumseagreen', font=('Times bold', 25), text_color='white',padx=1,pady=5)
        self.label1F1.place(relx=0.05,rely=0.3)
        print('okaayyyyy')
        self.padentry=ctk.CTkEntry(self.frame1,placeholder_text='enter user_id',width=350,height=50,
                                   text_color='black',corner_radius=15,
                                   border_color='black',font=('Helvetica',18))
        self.padentry.place(relx=0.05,rely=0.4)
        print('here nko')
        # for password
        self.image_pass = Image.open('images/padlock-check (1).png')
        self.image_pass = ctk.CTkImage(self.image_pass)
        self.label2F1 = ctk.CTkLabel(self.frame1, text='PassWord:', compound=tk.LEFT, image=self.image_pass,
                                    fg_color='mediumseagreen', font=('Times bold', 25), text_color='white', padx=1, pady=5)
        self.label2F1.place(relx=0.05, rely=0.55)
        self.passentry = ctk.CTkEntry(self.frame1, placeholder_text='password', width=350, height=50,
                                     text_color='black', corner_radius=15,
                                     border_color='black', font=('Helvetica', 18),border_width=1)
        self.passentry.place(relx=0.05, rely=0.65)
        print('hope all is well')
        #button
        self.image_but = Image.open('images\sign-in-alt.png')
        button_submit=ctk.CTkButton(self.frame1,text='sign in',corner_radius=32,
                                    text_color= 'blue',border_color='black',border_spacing=2,
                                    fg_color='#c6e2b5',hover_color='grey',command=self.signup,
                                    border_width=2, image=ctk.CTkImage(self.image_but),width=350,height=50,font=('Times',20))
        button_submit.place(relx=0.05,rely=0.85)
    def signup(self):
        userid=self.padentry.get()
        password=self.passentry.get()
        #self.mainwindow()
        #print(userid)
        #if userid and password == "":
            #messagebox.showinfo('error','please fill the form correctly')
        if 'project'not in userid:
            messagebox.showinfo('error', 'Incorrect information')
            return
        elif password !="1234":
             messagebox.showinfo('Opps', 'incorrect information')
             return
        else:
           self.mainwindow()
            ##messagebox.showinfo('error', 'An unknown error')

    def mainwindow(self):
        #self.connectDatabase()
        self.login_window.destroy()
        self.main_window = tk.Tk()
        self.main_window.title('School MAnagement System')
        self.main_window.geometry('1200x650')
        self.main_window.config(bg='#ecebe9')
        window_width = 1200
        window_height = 620
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.main_window.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
        # self.login_window.resizable(False, False)

        self.image_icon3 = Image.open('images/360_F_238940516_0BihE7YocY9vpgClPDDWuuaLneDwxtWn.jpg')
        self.image_icon3 = ImageTk.PhotoImage(self.image_icon3)
        self.main_window.iconphoto(False, self.image_icon3)

        self.frame2 = ctk.CTkFrame(self.main_window, fg_color='mediumseagreen', width=250,
                                   height=680, corner_radius=10)
        self.frame2.place(relx=0.67, rely=0.1)
        self.frame2.pack(side=tk.LEFT, pady=10,padx=20)
        print('check1')
        #top image
        self.image_top = Image.open('images/EMMMA11.png')
        self.image_top = ctk.CTkImage(self.image_top)
        self.label3F1 = ctk.CTkLabel(self.frame2, text='FINAL YEAR PROJECT', compound=tk.LEFT, image=self.image_top,
                                     fg_color='#173662', font=('Italian bold', 15), text_color='white', padx=8, pady=5)
        self.label3F1.place(relx=0.43, rely=0.06,anchor=tk.CENTER)
        #self.label3F1.pack(side=TOP)
        labeltop = ctk.CTkLabel(self.frame2, text='Academics excellence and power', font=('Ariel', 10),
                                  text_color='white', fg_color='#173662')
        labeltop.place(relx=0.13, rely=0.08)

        self.frameline = ctk.CTkFrame(self.frame2, fg_color='white', width=200,
                                   height=5, corner_radius=10)
        self.frameline.place(relx=0.06, rely=0.17,anchor='sw')
        #self.frameline.pack(side=tk.LEFT, padx=10, pady=10)
        print('check2')

        #menu buttons
        self.image_butHome = Image.open('images/home-page-white-icon.png')
        self.button_Home = ctk.CTkButton(self.frame2, text='Home',
                                      text_color='white',state=DISABLED,
                                      fg_color='transparent', hover_color='#276878', command=self.homepage,
                                       image=ctk.CTkImage(self.image_butHome), width=120, height=35,
                                      font=('Times', 18))
        self.button_Home.place(relx=0.05, rely=0.25)


        self.image_butreg = Image.open('images/pencil-2-32.png')
        self.button_register = ctk.CTkButton(self.frame2, text='Registration',
                                    text_color='white',state=DISABLED,
                                    fg_color='transparent', hover_color='#276878', command=self.register,
                                    image=ctk.CTkImage(self.image_butreg), width=120, height=35,
                                    font=('Times', 18))
        self.button_register.place(relx=0.1, rely=0.35)

        self.image_butsearch = Image.open('images/search-9-32.png')
        self.button_search = ctk.CTkButton(self.frame2, text='Search',
                                        text_color='white',state=DISABLED,
                                        fg_color='transparent', hover_color='#276878', command=self.main_SEARCH,
                                        image=ctk.CTkImage(self.image_butsearch), width=120, height=35,
                                        font=('Times', 18))
        self.button_search.place(relx=0.05, rely=0.45)

        self.image_butresult = Image.open('images/book-16-32.png')
        self.button_result= ctk.CTkButton(self.frame2, text='Result',
                                        text_color='white',state=DISABLED,
                                        fg_color='transparent', hover_color='#276878', command=self.result,
                                        image=ctk.CTkImage(self.image_butresult), width=120, height=35,
                                        font=('Times', 18))
        self.button_result.place(relx=0.05, rely=0.55)

        self.image_butrecord = Image.open('images/text-file-32.png')
        self.button_record = ctk.CTkButton(self.frame2, text='Record',
                                      text_color='white',state=DISABLED,
                                      fg_color='transparent', hover_color='#276878', command=self.record,
                                      image=ctk.CTkImage(self.image_butrecord), width=120, height=35,
                                      font=('Times', 18))
        self.button_record.place(relx=0.05, rely=0.65)

        self.image_butbase = Image.open('images/database-32.png')
        self.button_database = ctk.CTkButton(self.frame2, text='Database',
                                      text_color='white',state=DISABLED,
                                      fg_color='transparent', hover_color='#276878', command=self.database_butfunction,
                                      image=ctk.CTkImage(self.image_butbase), width=120, height=35,
                                      font=('Times', 18))
        self.button_database.place(relx=0.05, rely=0.75)

        self.button_logout = ctk.CTkButton(self.frame2, text='LogOut',
                                         text_color='white',
                                         fg_color='transparent', hover_color='#276878', command=self.logout,
                                         image=ctk.CTkImage(self.image_but), width=120, height=35,
                                         font=('Times', 18))
        self.button_logout.place(relx=0.05, rely=0.90)

        # mainfram display
        self.mainframe1 = ctk.CTkFrame(self.main_window, fg_color='#ECEBE9', width=1400,
                                       height=680, corner_radius=10, border_color='#173662',
                                       border_width=0)
        self.mainframe1.place(relx=0.5, rely=0.5)
        self.mainframe1.pack(pady=0, padx=0, fill=BOTH)

        self.display()
        #self.connectDatabase()

    def main_SEARCH(self):


        def okay6():
            self.destroymain1()

            self.smallokay6img = Image.open('images/trophy.png')

            self.smallokay6img = ImageTk.PhotoImage(self.smallokay6img)

            largeframeSmall1 = ctk.CTkFrame(self.mainframe1, fg_color='#ECEBE9', width=1100,
                                            height=680, corner_radius=10, border_color='#173662',
                                            border_width=0)
            largeframeSmall1.place(relx=0.008, rely=0.01)

            Small0 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=500,
                                  height=20, corner_radius=10, border_color='#173662',
                                  border_width=0)
            # Small1.place(relx=0.23, rely=0.01)
            Small0.pack(side=TOP, expand=True, fill=Y)

            Small1 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small1.place(relx=0.23, rely=0.01)
            Small1.pack(padx=270, expand=True, ipadx=20, pady=10)

            Back = CTkButton(largeframeSmall1, text='BACK', fg_color='#173662',
                             text_color='white', height=35, width=80,
                             font=('Ariel', 10, 'bold'), command=self.main_SEARCH)
            Back.place(relx=0.5, rely=0.5)
            Back.pack(side=RIGHT, padx=5, pady=10)

            Small2 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small2.place(relx=0.1, rely=0.04)
            Small2.pack(side=LEFT, padx=10, expand=True, pady=5)

            Small3 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small3.place(relx=0.03, rely=0.04)
            Small3.pack(side=LEFT, padx=45, expand=True, pady=5)

            label1 = tk.Label(Small1, image=self.smallokay6img, bg='#ECEBE9')

            label1.place(relx=0.32, rely=0.01)

            label1head = tk.Label(Small1,
                                  text='DISTINGUISHED PROFESSORS',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label1head.place(relx=0.08, rely=0.25)

            label1a = ctk.CTkLabel(Small1,
                                   text=' Number of Award: 6\nIssued by: ECOWAS\nCategory: International\nYear: 1996,98,99,2005,14,24\nType: Academics Award',
                                   fg_color='white', text_color='#173662', font=('Ariel', 20), corner_radius=5)

            label1a.place(relx=0.1, rely=0.4)

            # smalll2label2 = ctk.CTkLabel(self.smallframe2, text='Lecturers', font=('Ariel', 10),
            # text_color='#242818', fg_color='white', corner_radius=4)
            # smalll2label2.place(relx=0.37, rely=0.1)

            label2 = tk.Label(Small2, image=self.smallokay6img, bg='#ECEBE9')

            label2.place(relx=0.32, rely=0.01)

            label2head = tk.Label(Small2,
                                  text='BEST UNIVERSITY AWARD ',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label2head.place(relx=0.1, rely=0.25)

            label2a = ctk.CTkLabel(Small2,
                                   text=' Number of Award: 4\nIssued by: Academic Board Nigeria\nCategory: National\n Year: 2007,9,15,24\n Type: Academics Award',
                                   fg_color='white', text_color='#173662', font=('Ariel', 20), corner_radius=5)

            label2a.place(relx=0.1, rely=0.4)

            label3 = tk.Label(Small3, image=self.smallokay6img, bg='#ECEBE9')

            label3.place(relx=0.32, rely=0.01)

            label3head = tk.Label(Small3,
                                  text='STAR GOLD MEDAL',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label3head.place(relx=0.1, rely=0.25)

            label3a = ctk.CTkLabel(Small3,
                                   text=' Number of Award: 2\nIssued by: Nigeria Football Federation\nCategory: National\nYear: 2014,15\n Type: Sport Award',
                                   fg_color='white', text_color='#173662', font=('Ariel', 20), corner_radius=5)

            label3a.place(relx=0.1, rely=0.4)

        def okay4():

            top_students = self.get_top_students4()

            for i, student in enumerate(top_students, start=1):
                matric_no, surname, name, dob, department, gender, level, grade, status, faculty, email, phone_no, time, date = student
                if i == 1:
                    surname1 = surname
                    name1 = name
                    grade1 = grade
                    status1 = status
                    matric_no1 = matric_no
                elif i == 2:
                    surname2 = surname
                    name2 = name
                    grade2 = grade
                    status2 = status
                    matric_no2 = matric_no
                elif i == 3:
                    surname3 = surname
                    name3 = name
                    grade3 = grade
                    status3 = status
                    matric_no3 = matric_no

            print(f"{surname1},{status1},it works")
            print(f"{surname2},{status2},it works")
            print(f"{surname3},{status3},it works")
            #self.smallwindow.destroy()
            self.destroymain1()

            largeframeSmall1 = ctk.CTkFrame(self.mainframe1, fg_color='#ECEBE9', width=1100,
                                            height=680, corner_radius=10, border_color='#173662',
                                            border_width=0)
            largeframeSmall1.place(relx=0.008, rely=0.01)

            Small0 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=500,
                                  height=20, corner_radius=10, border_color='#173662',
                                  border_width=0)
            # Small1.place(relx=0.23, rely=0.01)
            Small0.pack(side=TOP, expand=True, fill=Y)

            Small1 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small1.place(relx=0.23, rely=0.01)
            Small1.pack(padx=270, expand=True, ipadx=20, pady=10)

            Back = CTkButton(largeframeSmall1, text='BACK', fg_color='#173662',
                             text_color='white', height=35, width=80,
                             font=('Ariel', 10, 'bold'), command=self.main_SEARCH)
            Back.place(relx=0.5, rely=0.5)
            Back.pack(side=RIGHT, padx=5, pady=10)

            Small2 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small2.place(relx=0.1, rely=0.04)
            Small2.pack(side=LEFT, padx=10, expand=True, pady=5)

            Small3 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small3.place(relx=0.03, rely=0.04)
            Small3.pack(side=LEFT, padx=45, expand=True, pady=5)

            label1 = tk.Label(Small1, image=self.smallframeimage3, bg='#ECEBE9')

            label1.place(relx=0.35, rely=0.1)

            label1head = tk.Label(Small1,
                                  text='FIRST BEST STUDENT',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label1head.place(relx=0.1, rely=0.25)

            label1a = ctk.CTkLabel(Small1,
                                   text=f"Matric_no: {matric_no1}\nSurname: {surname1}\nName: {name1}\nCgpa: {status1}\nGrade: {grade1}",
                                   fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

            label1a.place(relx=0.1, rely=0.4)

            # smalll2label2 = ctk.CTkLabel(self.smallframe2, text='Lecturers', font=('Ariel', 10),
            # text_color='#242818', fg_color='white', corner_radius=4)
            # smalll2label2.place(relx=0.37, rely=0.1)

            label2 = tk.Label(Small2, image=self.smallframeimage3, bg='#ECEBE9')

            label2.place(relx=0.35, rely=0.1)

            label2head = tk.Label(Small2,
                                  text='SECOND BEST STUDENTuuyt',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label2head.place(relx=0.1, rely=0.25)

            label2a = ctk.CTkLabel(Small2,
                                   text=f"Matric_no: {matric_no2}\nSurname: {surname2}\nName: {name2}\nCgpa: {status2}\nGrade: {grade2}",
                                   fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

            label2a.place(relx=0.1, rely=0.4)

            label3 = tk.Label(Small3, image=self.smallframeimage3, bg='#ECEBE9')

            label3.place(relx=0.35, rely=0.1)

            label3head = tk.Label(Small3,
                                  text='THIRD BEST STUDENT',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label3head.place(relx=0.1, rely=0.25)

            label3a = ctk.CTkLabel(Small3,
                                   text=f"Matric_no: {matric_no3}\nSurname: {surname3}\nName: {name3}\nCgpa: {status3}\nGrade: {grade3}",
                                   fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

            label3a.place(relx=0.1, rely=0.4)

        def okay5():
            self.destroymain1()

            self.smallokay5img = Image.open('images/medal-of-honor.png')

            self.smallokay5img = ImageTk.PhotoImage(self.smallokay5img)

            largeframeSmall1 = ctk.CTkFrame(self.mainframe1, fg_color='#ECEBE9', width=1100,
                                            height=680, corner_radius=10, border_color='#173662',
                                            border_width=0)
            largeframeSmall1.place(relx=0.008, rely=0.01)

            Small0 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=500,
                                  height=20, corner_radius=10, border_color='#173662',
                                  border_width=0)
            # Small1.place(relx=0.23, rely=0.01)
            Small0.pack(side=TOP, expand=True, fill=Y)

            Small1 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small1.place(relx=0.23, rely=0.01)
            Small1.pack(padx=270, expand=True, ipadx=20, pady=10)

            Back = CTkButton(largeframeSmall1, text='BACK', fg_color='#173662',
                             text_color='white', height=35, width=80,
                             font=('Ariel', 10, 'bold'), command=self.main_SEARCH)
            Back.place(relx=0.5, rely=0.5)
            Back.pack(side=RIGHT, padx=5, pady=10)

            Small2 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small2.place(relx=0.1, rely=0.04)
            Small2.pack(side=LEFT, padx=10, expand=True, pady=5)

            Small3 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small3.place(relx=0.03, rely=0.04)
            Small3.pack(side=LEFT, padx=45, expand=True, pady=5)

            label1 = tk.Label(Small1, image=self.smallokay5img, bg='#ECEBE9')

            label1.place(relx=0.32, rely=0.01)

            label1head = tk.Label(Small1,
                                  text='TOP ACHEIVER 1',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label1head.place(relx=0.1, rely=0.25)

            label1a = ctk.CTkLabel(Small1,
                                   text=' Matric_no: N/cs/22/4564\nSurname: Kunle\nName: Bola\nCgpa: 4.96\nGrade: Distinction',
                                   fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

            label1a.place(relx=0.1, rely=0.4)

            # smalll2label2 = ctk.CTkLabel(self.smallframe2, text='Lecturers', font=('Ariel', 10),
            # text_color='#242818', fg_color='white', corner_radius=4)
            # smalll2label2.place(relx=0.37, rely=0.1)

            label2 = tk.Label(Small2, image=self.smallokay5img, bg='#ECEBE9')

            label2.place(relx=0.32, rely=0.01)

            label2head = tk.Label(Small2,
                                  text='TOP ACHEIVER 2',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label2head.place(relx=0.1, rely=0.25)

            label2a = ctk.CTkLabel(Small2,
                                   text=' Matric_no: N/cs/22/4564\nSurname: Kunle\nName: Bola\nCgpa: 4.96\nGrade: Distinction',
                                   fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

            label2a.place(relx=0.1, rely=0.4)

            label3 = tk.Label(Small3, image=self.smallokay5img, bg='#ECEBE9')

            label3.place(relx=0.32, rely=0.01)

            label3head = tk.Label(Small3,
                                  text='TOP ACHIEVER 3',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label3head.place(relx=0.1, rely=0.25)

            label3a = ctk.CTkLabel(Small3,
                                   text=' Matric_no: N/cs/22/4564\nSurname: Kunle\nName: Bola\nCgpa: 4.96\nGrade: Distinction',
                                   fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

            label3a.place(relx=0.1, rely=0.4)

        def smallframebut():
            #global comb
            def okay():
                try:
                    self.selected_dept = comboDept1.get()
                    self.selected_level = combolevel.get()
                    #print(f"Selected Department: {self.selected_dept}, Selected Level: {self.selected_level}")
                except Exception as e:
                    #print(f"Error: {str(e)}")
                    messagebox.showinfo('opps😯','data unavailable',parent=self.smallwindow)

                try:
                    top_students = self.get_top_students(self.selected_level , self.selected_dept)

                    for i, student in enumerate(top_students, start=1):
                        matric_no, surname, name, dob, department, gender, level, grade, status, faculty, email, phone_no, time, date = student
                        if i == 1:
                            surname1 = surname
                            name1 = name
                            grade1 = grade
                            status1 = status
                            matric_no1 = matric_no
                        elif i == 2:
                            surname2 = surname
                            name2 = name
                            grade2 = grade
                            status2 = status
                            matric_no2 = matric_no
                        elif i == 3:
                            surname3 = surname
                            name3 = name
                            grade3 = grade
                            status3 = status
                            matric_no3 = matric_no



                    #print(surname1)
                    #print(name2)
                    #print(grade3)



                    self.smallwindow.destroy()
                    self.destroymain1()

                    largeframeSmall1 = ctk.CTkFrame(self.mainframe1, fg_color='#ECEBE9', width=1100,
                                                    height=680, corner_radius=10, border_color='#173662',
                                                    border_width=0)
                    largeframeSmall1.place(relx=0.008, rely=0.01)

                    Small0 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=500,
                                          height=20, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    # Small1.place(relx=0.23, rely=0.01)
                    Small0.pack(side=TOP, expand=True, fill=Y)

                    Small1 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small1.place(relx=0.23, rely=0.01)
                    Small1.pack(padx=270, expand=True, ipadx=20, pady=10)

                    Back = CTkButton(largeframeSmall1, text='BACK', fg_color='#173662',
                                     text_color='white', height=35, width=80,
                                     font=('Ariel', 10, 'bold'), command=self.main_SEARCH)
                    Back.place(relx=0.5, rely=0.5)
                    Back.pack(side=RIGHT, padx=5, pady=10)

                    Small2 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small2.place(relx=0.1, rely=0.04)
                    Small2.pack(side=LEFT, padx=10, expand=True, pady=5)

                    Small3 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small3.place(relx=0.03, rely=0.04)
                    Small3.pack(side=LEFT, padx=45, expand=True, pady=5)

                    label1 = tk.Label(Small1, image=self.smallframeimage3, bg='#ECEBE9')

                    label1.place(relx=0.35, rely=0.1)

                    label1head = tk.Label(Small1,
                                          text='FIRST BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label1head.place(relx=0.1, rely=0.25)

                    label1a = ctk.CTkLabel(Small1,
                                           text=f"Matric_no: {matric_no1}\nSurname: {surname1}\nName: {name1}\nCgpa: {status1}\nGrade: {grade1}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label1a.place(relx=0.1, rely=0.4)

                    # smalll2label2 = ctk.CTkLabel(self.smallframe2, text='Lecturers', font=('Ariel', 10),
                    # text_color='#242818', fg_color='white', corner_radius=4)
                    # smalll2label2.place(relx=0.37, rely=0.1)

                    label2 = tk.Label(Small2, image=self.smallframeimage3, bg='#ECEBE9')

                    label2.place(relx=0.35, rely=0.1)

                    label2head = tk.Label(Small2,
                                          text='SECOND BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label2head.place(relx=0.1, rely=0.25)

                    label2a = ctk.CTkLabel(Small2,
                                           text=f"Matric_no: {matric_no2}\nSurname: {surname2}\nName: {name2}\nCgpa: {status2}\nGrade: {grade2}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label2a.place(relx=0.1, rely=0.4)

                    label3 = tk.Label(Small3, image=self.smallframeimage3, bg='#ECEBE9')

                    label3.place(relx=0.35, rely=0.1)

                    label3head = tk.Label(Small3,
                                          text='THIRD BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label3head.place(relx=0.1, rely=0.25)

                    label3a = ctk.CTkLabel(Small3,
                                           text=f"Matric_no: {matric_no3}\nSurname: {surname3}\nName: {name3}\nCgpa: {status3}\nGrade: {grade3}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label3a.place(relx=0.1, rely=0.4)

                    #print(f"Selected Department: {self.selected_dept}, Selected Level: {self.selected_level}")
                except Exception as e:
                    print(e)

            self.smallwindow = tk.Tk()
            self.smallwindow.grab_set()
            self.smallwindow.title('School MAnagement System')
            self.smallwindow.geometry('400x250+600+200')
            self.smallwindow.config(bg='white')
            self.smallwindow.resizable(False, False)

            checkin =tk.Label(self.smallwindow, text='CHOOSE LEVEL & DEPT?',
                               font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
            checkin.grid(row=0, columnspan=3, padx=50, pady=20)

            deptvalues=['COMPUTER SCIENCE','PUBLIC ADMIN','ACCOUNTING','SLT','BANKING','HMT']
            levelValues=['ND 1','ND 2','HND 1','HND 2']

            deptlabel = tk.Label(self.smallwindow, text='Department:',
                               font=('Ariel', 10,), bg='white', fg='#173662')
            deptlabel.grid(row=1, column=1, padx=10, pady=10)

            comboDept1=ctk.CTkComboBox(self.smallwindow,values=deptvalues)
            comboDept1.set=('select department')
            comboDept1.grid(row=1,column=2)

            levellabel = tk.Label(self.smallwindow, text='level:',
                                 font=('Ariel', 10,), bg='white', fg='#173662')
            levellabel.grid(row=2, column=1, padx=10, pady=10)

            combolevel = ctk.CTkComboBox(self.smallwindow, values=levelValues)
            combolevel.set = ('select level')
            combolevel.grid(row=2, column=2)

            #self.OKbut = tk.Button(smallwindow, text='connect', bg='#173662', fg='white',
                                        #command=okay,
                                       # font=('times new roman', 15, 'bold'))
            #self.OKbut.grid(row=3, columnspan=2, pady=10, padx=10)

            OKbut = CTkButton(self.smallwindow, text='VIEW', fg_color='#173662',
                                          text_color='white', height=35, width=80,
                                          font=('Ariel', 15, 'bold'), command=okay)
            OKbut.grid(row=3, columnspan=4)

        def smallframe2but():
            def okay2():
                try:
                    self.selected_dept2 = comboDept.get()
                    #print(f"Selected Department: {self.selected_dept}, Selected Level: {self.selected_level}")
                except Exception as e:
                    print(f"Error: {str(e)}")
                top_students = self.get_top_students2(self.selected_dept2)
                try:
                    for i, student in enumerate(top_students, start=1):
                        matric_no, surname, name, dob, department, gender, level, grade, status, faculty, email, phone_no, time, date = student
                        if i == 1:
                            surname1 = surname
                            name1 = name
                            grade1 = grade
                            status1 = status
                            matric_no1 = matric_no
                        elif i == 2:
                            surname2 = surname
                            name2 = name
                            grade2 = grade
                            status2 = status
                            matric_no2 = matric_no
                        elif i == 3:
                            surname3 = surname
                            name3 = name
                            grade3 = grade
                            status3 = status
                            matric_no3 = matric_no

                    print(surname1)
                    print(name2)
                    print(grade3)

                    self.smallwindow.destroy()
                    self.destroymain1()

                    largeframeSmall1 = ctk.CTkFrame(self.mainframe1, fg_color='#ECEBE9', width=1100,
                                                    height=680, corner_radius=10, border_color='#173662',
                                                    border_width=0)
                    largeframeSmall1.place(relx=0.008, rely=0.01)

                    Small0 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=500,
                                          height=20, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    # Small1.place(relx=0.23, rely=0.01)
                    Small0.pack(side=TOP, expand=True, fill=Y)

                    Small1 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small1.place(relx=0.23, rely=0.01)
                    Small1.pack(padx=270, expand=True, ipadx=20, pady=10)

                    Back = CTkButton(largeframeSmall1, text='BACK', fg_color='#173662',
                                     text_color='white', height=35, width=80,
                                     font=('Ariel', 10, 'bold'), command=self.main_SEARCH)
                    Back.place(relx=0.5, rely=0.5)
                    Back.pack(side=RIGHT, padx=5, pady=10)

                    Small2 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small2.place(relx=0.1, rely=0.04)
                    Small2.pack(side=LEFT, padx=10, expand=True, pady=5)

                    Small3 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small3.place(relx=0.03, rely=0.04)
                    Small3.pack(side=LEFT, padx=45, expand=True, pady=5)

                    label1 = tk.Label(Small1, image=self.smallframeimage3, bg='#ECEBE9')

                    label1.place(relx=0.35, rely=0.1)

                    label1head = tk.Label(Small1,
                                          text='FIRST BEST STUDENT5555',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label1head.place(relx=0.1, rely=0.25)

                    label1a = ctk.CTkLabel(Small1,
                                           text=f"Matric_no: {matric_no1}\nSurname: {surname1}\nName: {name1}\nCgpa: {status1}\nGrade: {grade1}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label1a.place(relx=0.1, rely=0.4)

                    # smalll2label2 = ctk.CTkLabel(self.smallframe2, text='Lecturers', font=('Ariel', 10),
                    # text_color='#242818', fg_color='white', corner_radius=4)
                    # smalll2label2.place(relx=0.37, rely=0.1)

                    label2 = tk.Label(Small2, image=self.smallframeimage3, bg='#ECEBE9')

                    label2.place(relx=0.35, rely=0.1)

                    label2head = tk.Label(Small2,
                                          text='SECOND BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label2head.place(relx=0.1, rely=0.25)

                    label2a = ctk.CTkLabel(Small2,
                                           text=f"Matric_no: {matric_no2}\nSurname: {surname2}\nName: {name2}\nCgpa: {status2}\nGrade: {grade2}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label2a.place(relx=0.1, rely=0.4)

                    label3 = tk.Label(Small3, image=self.smallframeimage3, bg='#ECEBE9')

                    label3.place(relx=0.35, rely=0.1)

                    label3head = tk.Label(Small3,
                                          text='THIRD BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label3head.place(relx=0.1, rely=0.25)

                    label3a = ctk.CTkLabel(Small3,
                                           text=f"Matric_no: {matric_no3}\nSurname: {surname3}\nName: {name3}\nCgpa: {status3}\nGrade: {grade3}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label3a.place(relx=0.1, rely=0.4)
                except Exception as e:
                   print(e)


            self.smallwindow = tk.Tk()
            self.smallwindow.grab_set()
            self.smallwindow.title('School MAnagement System')
            self.smallwindow.geometry('400x250+600+200')
            self.smallwindow.config(bg='white')
            self.smallwindow.resizable(False, False)

            checkin = tk.Label(self.smallwindow, text='CHOOSE DEPARTMENT?',
                               font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
            checkin.grid(row=0, columnspan=3, padx=50, pady=20)

            deptvalues = ['COMPUTER SCIENCE', 'PUBLIC ADMIN', 'ACCOUNTING', 'SLT', 'BANKING', 'HMT']


            deptlabel = tk.Label(self.smallwindow, text='Department:',
                                 font=('Ariel', 10,), bg='white', fg='#173662')
            deptlabel.grid(row=1, column=1, padx=10, pady=10)

            comboDept = CTkComboBox(self.smallwindow, values=deptvalues)
            comboDept.set = ('select department')
            comboDept.grid(row=1, column=2)

            OKbut = CTkButton(self.smallwindow, text='VIEW', fg_color='#173662',
                              text_color='white', height=35, width=80,
                              font=('Ariel', 15, 'bold'), command=okay2)
            OKbut.grid(row=3, columnspan=4)

        def smallframe3but():
            def okay3():
                try:
                    self.selected_dept3 = comboDept.get()
                    #print(f"Selected Department: {self.selected_dept}, Selected Level: {self.selected_level}")
                except Exception as e:
                    print(f"Error: {str(e)}")

                try:

                    top_students = self.get_top_students3(self.selected_dept3)

                    for i, student in enumerate(top_students, start=1):
                        matric_no, surname, name, dob, department, gender, level, grade, status, faculty, email, phone_no, time, date = student
                        if i == 1:
                            surname1 = surname
                            name1 = name
                            grade1 = grade
                            status1 = status
                            matric_no1 = matric_no
                        elif i == 2:
                            surname2 = surname
                            name2 = name
                            grade2 = grade
                            status2 = status
                            matric_no2 = matric_no
                        elif i == 3:
                            surname3 = surname
                            name3 = name
                            grade3 = grade
                            status3 = status
                            matric_no3 = matric_no

                    self.smallwindow.destroy()
                    self.destroymain1()

                    largeframeSmall1 = ctk.CTkFrame(self.mainframe1, fg_color='#ECEBE9', width=1100,
                                                    height=680, corner_radius=10, border_color='#173662',
                                                    border_width=0)
                    largeframeSmall1.place(relx=0.008, rely=0.01)

                    Small0 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=500,
                                          height=20, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    # Small1.place(relx=0.23, rely=0.01)
                    Small0.pack(side=TOP, expand=True, fill=Y)

                    Small1 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small1.place(relx=0.23, rely=0.01)
                    Small1.pack(padx=270, expand=True, ipadx=20, pady=10)

                    Back = CTkButton(largeframeSmall1, text='BACK', fg_color='#173662',
                                     text_color='white', height=35, width=80,
                                     font=('Ariel', 10, 'bold'), command=self.main_SEARCH)
                    Back.place(relx=0.5, rely=0.5)
                    Back.pack(side=RIGHT, padx=5, pady=10)

                    Small2 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small2.place(relx=0.1, rely=0.04)
                    Small2.pack(side=LEFT, padx=10, expand=True, pady=5)

                    Small3 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small3.place(relx=0.03, rely=0.04)
                    Small3.pack(side=LEFT, padx=45, expand=True, pady=5)

                    label1 = tk.Label(Small1, image=self.smallframeimage3, bg='#ECEBE9')

                    label1.place(relx=0.35, rely=0.1)

                    label1head = tk.Label(Small1,
                                          text='FIRST BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label1head.place(relx=0.1, rely=0.25)

                    label1a = ctk.CTkLabel(Small1,
                                           text=f"Matric_no: {matric_no1}\nSurname: {surname1}\nName: {name1}\nCgpa: {status1}\nGrade: {grade1}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label1a.place(relx=0.1, rely=0.4)

                    # smalll2label2 = ctk.CTkLabel(self.smallframe2, text='Lecturers', font=('Ariel', 10),
                    # text_color='#242818', fg_color='white', corner_radius=4)
                    # smalll2label2.place(relx=0.37, rely=0.1)

                    label2 = tk.Label(Small2, image=self.smallframeimage3, bg='#ECEBE9')

                    label2.place(relx=0.35, rely=0.1)

                    label2head = tk.Label(Small2,
                                          text='SECOND BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label2head.place(relx=0.1, rely=0.25)

                    label2a = ctk.CTkLabel(Small2,
                                           text=f"Matric_no: {matric_no2}\nSurname: {surname2 }\nName: {name2}\nCgpa: {status2}\nGrade: {grade2}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label2a.place(relx=0.1, rely=0.4)

                    label3 = tk.Label(Small3, image=self.smallframeimage3, bg='#ECEBE9')

                    label3.place(relx=0.35, rely=0.1)

                    label3head = tk.Label(Small3,
                                          text='THIRD BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label3head.place(relx=0.1, rely=0.25)

                    label3a = ctk.CTkLabel(Small3,
                                           text=f"Matric_no: {matric_no3}\nSurname: {surname3}\nName: {name3}\nCgpa: {status3}\nGrade: {grade3}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label3a.place(relx=0.1, rely=0.4)
                except Exception as e:
                     print(e)


            self.smallwindow = tk.Tk()
            self.smallwindow.grab_set()
            self.smallwindow.title('School MAnagement System')
            self.smallwindow.geometry('400x250+600+200')
            self.smallwindow.config(bg='white')
            self.smallwindow.resizable(False, False)

            checkin = tk.Label(self.smallwindow, text='CHOOSE FACULTY',
                               font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
            checkin.grid(row=0, columnspan=3, padx=50, pady=20)

            Facvalues = ['APPLIED SCIENCE', 'MANAGEMENT', 'COMMUNICATION', 'COMMERCE', 'ENGINEERING', 'ART']

            Faclabel = tk.Label(self.smallwindow, text='Department:',
                                 font=('Ariel', 10,), bg='white', fg='#173662')
            Faclabel.grid(row=1, column=1, padx=10, pady=10)

            comboDept = CTkComboBox(self.smallwindow, values=Facvalues)
            comboDept.set = ('select faculty')
            comboDept.grid(row=1, column=2)

            OKbut = CTkButton(self.smallwindow, text='VIEW', fg_color='#173662',
                              text_color='white', height=35, width=80,
                              font=('Ariel', 15, 'bold'), command=okay3)
            OKbut.grid(row=3, columnspan=4)



        self.destroymain()
        self.button_search.configure(fg_color='#276878')

        #self.largeframesearch = ctk.CTkFrame(self.mainframe1, fg_color='black', width=1400,
                                             #height=680, corner_radius=10, border_color='#173662',
                                             #border_width=0)
        #self.largeframesearch.place(relx=0.5, rely=0.5, anchor='center')
        #self.largeframesearch.pack(pady=0, padx=0, fill=BOTH)

        self.largeframesearch = ctk.CTkFrame(self.mainframe1, fg_color='#ECEBE9', width=1050,
                                                  height=680, corner_radius=10, border_color='#173662',
                                                  border_width=0)
        self.largeframesearch.place(relx=0.008, rely=0.01)

        self.labelsearching = ctk.CTkLabel(self.largeframesearch, text='MAKE A QUICK SEARCH',
                                      image=ctk.CTkImage(self.image_butreg), compound=tk.LEFT,
                                      fg_color='transparent', font=('Helvetica', 25), text_color='#173662',
                                      corner_radius=10)
        self.labelsearching.grid(row=1,column=1, pady=15,sticky='w')



        smallframe1 = ctk.CTkFrame(self.largeframesearch, fg_color='#CCE0FE', width=320,
                                         height=250, corner_radius=10,
                                         )

        smallframe1.grid(row=2, column=1, pady=20, sticky='w')

        smallframe2 = ctk.CTkFrame(self.largeframesearch, fg_color='#FAE8ED', width=320,
                                   height=250, corner_radius=10,
                                   )

        smallframe2.grid(row=2, column=2, pady=20,padx=30, sticky='w')

        smallframe3 = ctk.CTkFrame(self.largeframesearch, fg_color='#FFF5FD', width=320,
                                   height=250, corner_radius=10,
                                   )

        smallframe3.grid(row=2, column=3, pady=20, sticky='w')

        smallframe4 = ctk.CTkFrame(self.largeframesearch, fg_color='#BCA0DC', width=320,
                                   height=250, corner_radius=10,
                                   )

        smallframe4.grid(row=3, column=1, pady=15, sticky='w')

        smallframe5 = ctk.CTkFrame(self.largeframesearch, fg_color='#f0e2d2', width=320,
                                   height=250, corner_radius=10,
                                   )

        smallframe5.grid(row=3, column=2, pady=15, padx=30, sticky='w')

        smallframe6 = ctk.CTkFrame(self.largeframesearch, fg_color='grey', width=320,
                                   height=250, corner_radius=10,
                                   )

        smallframe6.grid(row=3, column=3, pady=15, sticky='w')

        #LABEL ON FRAME
        smallframe1label = ctk.CTkLabel(smallframe1, text='BEST STUDENT LEVEL',
                                           image=ctk.CTkImage(self.image_butreg), compound=tk.LEFT,
                                           fg_color='transparent', font=('Helvetica', 18,'bold'), text_color='#173662',
                                           corner_radius=10,)
        smallframe1label.place(relx=0.1,rely=0.2)


        smallframe1button=CTkButton(smallframe1,text='VIEW',fg_color='white',
                                    text_color='#173662',height=35,width=80,
                                    font=('Ariel', 10,'bold'),command=smallframebut)
        smallframe1button.place(relx=0.5,rely=0.7)

        smallframe2label = ctk.CTkLabel(smallframe2, text='BEST STUDENT DEPT',
                                        image=ctk.CTkImage(self.image_butreg), compound=tk.LEFT,
                                        fg_color='transparent', font=('Helvetica', 18, 'bold'), text_color='#173662',
                                        corner_radius=10, )
        smallframe2label.place(relx=0.1, rely=0.2)

        smallframe2button = CTkButton(smallframe2, text='VIEW', fg_color='white',
                                      text_color='#173662', height=35, width=80,
                                      font=('Ariel', 10, 'bold'), command=smallframe2but)
        smallframe2button.place(relx=0.5, rely=0.7)

        smallframe3label = ctk.CTkLabel(smallframe3, text='BEST STUDENT FACULTY',
                                        image=ctk.CTkImage(self.image_butreg), compound=tk.LEFT,
                                        fg_color='transparent', font=('Helvetica', 18, 'bold'), text_color='#173662',
                                        corner_radius=10, )
        smallframe3label.place(relx=0.1, rely=0.2)

        smallframe3button = CTkButton(smallframe3, text='VIEW', fg_color='white',
                                      text_color='#173662', height=35, width=80,
                                      font=('Ariel', 10, 'bold'), command=smallframe3but)
        smallframe3button.place(relx=0.5, rely=0.7)

        smallframe4label = ctk.CTkLabel(smallframe4, text='OVERALL BEST IN SCHOOL',
                                        image=ctk.CTkImage(self.image_butreg), compound=tk.LEFT,
                                        fg_color='transparent', font=('Helvetica', 18, 'bold'), text_color='#173662',
                                        corner_radius=10, )
        smallframe4label.place(relx=0.1, rely=0.2)

        smallframe4button = CTkButton(smallframe4, text='VIEW', fg_color='white',
                                      text_color='#173662', height=35, width=80,
                                      font=('Ariel', 10, 'bold'), command=okay4)
        smallframe4button.place(relx=0.5, rely=0.7)

        smallframe5label = ctk.CTkLabel(smallframe5, text='TOP ACHIEVERS',
                                        image=ctk.CTkImage(self.image_butreg), compound=tk.LEFT,
                                        fg_color='transparent', font=('Helvetica', 18, 'bold'), text_color='#173662',
                                        corner_radius=10, )
        smallframe5label.place(relx=0.3, rely=0.2)

        smallframe5button = CTkButton(smallframe5, text='VIEW', fg_color='white',
                                      text_color='#173662', height=35, width=80,
                                      font=('Ariel', 10, 'bold'), command=okay5)
        smallframe5button.place(relx=0.5, rely=0.7)

        smallframe6label = ctk.CTkLabel(smallframe6, text='AWARDS & MERITS',
                                        image=ctk.CTkImage(self.image_butreg), compound=tk.LEFT,
                                        fg_color='transparent', font=('Helvetica', 18, 'bold'), text_color='#173662',
                                        corner_radius=10, )
        smallframe6label.place(relx=0.3, rely=0.2)

        smallframe6button = CTkButton(smallframe6, text='VIEW', fg_color='white',
                                      text_color='#173662', height=35, width=80,
                                      font=('Ariel', 10, 'bold'), command=okay6)
        smallframe6button.place(relx=0.5, rely=0.7)

    def result(self):
        self.destroymain()
        self.button_result.configure(fg_color='#276878')

        self.largeframeresult = ctk.CTkFrame(self.mainframe1, fg_color='#ECEBE9', width=1400,
                                             height=680, corner_radius=10, border_color='#173662',
                                             border_width=0)
        self.largeframeresult.place(relx=0.5, rely=0.5,anchor='center')
        self.largeframeresult.pack(pady=0, padx=0, fill=BOTH)

        Resultlabel = ctk.CTkLabel(self.largeframeresult, text='RESULT NOT AVAILABLE YET',
                                   font=('Helvetica', 50, 'bold'), text_color='#173662',
                                   fg_color='transparent', corner_radius=4)
        Resultlabel.pack(pady=100,expand=True)



    def homepage(self):
        self.destroymain()

        self.button_Home.configure(fg_color='#276878')
        self.largeframe = ctk.CTkFrame(self.mainframe1, fg_color='#ECEBE9', width=1400,
                                       height=680, corner_radius=10, border_color='#173662',
                                       border_width=0)
        self.largeframe.place(relx=0.5, rely=0.5)
        self.largeframe.pack(pady=0, padx=0, fill=BOTH)
        # labeltop2 = ctk.CTkLabel(self.main_window, text='Academics excellence and power', font=('Ariel', 10),
        # text_color='white', fg_color='#173662',corner_radius=4)
        # labeltop2.place(relx=0.55, rely=0.001)
        print('check4')
        # top frame
        self.top_frame = ctk.CTkFrame(self.largeframe, fg_color='white', width=1020,
                                      height=25, corner_radius=5,
                                      )
        self.top_frame.pack(side=TOP, pady=15, ipady=10, fill=X)
        print('chek5')
        # small frames

        self.smallframe1 = ctk.CTkFrame(self.largeframe, fg_color='white', width=200,
                                        height=80, corner_radius=10,
                                        )
        # smallframe1.grid(relx=0.01, rely=0.1)

        self.smallframe2 = ctk.CTkFrame(self.largeframe, fg_color='white', width=200,
                                        height=80, corner_radius=10,
                                        )
        self.smallframe3 = ctk.CTkFrame(self.largeframe, fg_color='white', width=200,
                                        height=80, corner_radius=10,
                                        )
        self.smallframe4 = ctk.CTkFrame(self.largeframe, fg_color='white', width=200,
                                        height=80, corner_radius=10,
                                        )

        self.smallframe1.pack(side=LEFT, padx=0, expand=True, ipadx=10)
        self.smallframe2.pack(side=LEFT, padx=10, expand=True, ipadx=20)
        self.smallframe3.pack(side=LEFT, padx=10, expand=True, ipadx=20)
        self.smallframe4.pack(side=LEFT, padx=0, expand=True, ipadx=10)

        self.largeframe2 = ctk.CTkFrame(self.mainframe1, fg_color='#ecebe9', width=680,
                                        height=600, corner_radius=10, border_color='#173662',
                                        border_width=0)
        self.largeframe2.place(relx=0.26, rely=0.35)
        self.largeframe2.pack(side=LEFT, padx=2, pady=5)

        self.smallframe5A = ctk.CTkFrame(self.largeframe2, fg_color='white', width=320,
                                        height=250, corner_radius=10,
                                        )
        self.smallframe6A = ctk.CTkScrollableFrame(self.mainframe1, fg_color='white', width=370,
                                                   height=500, corner_radius=10, orientation='vertical',
                                                   scrollbar_button_color='#276878',
                                                   scrollbar_button_hover_color='#173662')
        self.smallframe7A = ctk.CTkFrame(self.largeframe2, fg_color='white', width=320,
                                         height=250, corner_radius=10,
                                         )
        self.smallframe8A = ctk.CTkFrame(self.largeframe2, fg_color='white', width=600,
                                         height=250, corner_radius=10,
                                         )

        self.smallframe8A.place(relx=0.01, rely=0.01)
        #smallframe6A.place(relx=0.7, rely=0.01)
        self.smallframe5A.place(relx=0.15, rely=1, anchor='s')
        self.smallframe7A.place(relx=0.4, rely=0.5, anchor='s')

        self.smallframe8A.pack(fill=X, pady=10)
        self.smallframe6A.pack(side=LEFT, padx=8, pady=5)
        # self.scrollbar=ctk.CTkScrollbar(self.smallframe6A)
        # self.scrollbar.pack(side='left', fill='y')
        # self.scrollbar.config(command=self.smallframe6A.yview)
        # self.smallframe6A.configure(yscrollcommand=self.scrollbar.set)
        self.smallframe5A.pack(side=RIGHT, pady=2, padx=5)
        self.smallframe7A.pack(side=RIGHT, pady=0, padx=0, ipadx=20)
        print('check6')
        # labels and widget
        labeltopframe = ctk.CTkLabel(self.top_frame, text='DASHBOARD', font=('Helvetica', 20),
                                     text_color='#173662', fg_color='WHITE', corner_radius=4)
        labeltopframe.place(relx=0.01, rely=0.1)

        self.labeltopframeENTRY = ctk.CTkEntry(self.top_frame, placeholder_text='search for student with matric number',
                                               width=500, height=30,
                                               text_color='#090a06', corner_radius=15,
                                               border_color='#ecebe9', font=('Ariel', 10))
        self.labeltopframeENTRY.place(relx=0.2, rely=0.2)

        self.searchicon = Image.open('images/search1.png')

        # self.searchicon  = ImageTk.PhotoImage(self.searchicon)

        searchtop = ctk.CTkButton(self.top_frame, text='',
                                  fg_color='#ecebe9', command=self.topsearch,
                                  image=ctk.CTkImage(self.image_butsearch), width=20, height=20
                                  )
        searchtop.place(relx=0.62, rely=0.25)

        self.noticon = Image.open('images/notification3.png')

        # self.noticon = ImageTk.PhotoImage(self.noticon)

        notitop = ctk.CTkButton(self.top_frame, text='',
                                fg_color='white', command=self.home,
                                image=ctk.CTkImage(self.noticon), width=25, height=25,
                                )
        notitop.place(relx=0.78, rely=0.1)

        self.topcon = ctk.CTkButton(self.top_frame, text='Connected',
                                    fg_color='green', command=self.home,
                                    width=100, height=40, text_color='white',
                                    )
        self.topcon.place(relx=0.85, rely=0.12)
        # searchtop.pack(side=RIGHT,padx=350)

        # self.labelphotoframe = ctk.CTkFrame(self.top_frame, fg_color='blue', width=50,
        # height=25, corner_radius=30,radius=3
        # )
        # self.labelphotoframe.place(relx=0.9,rely=0.2)
        print('check8')
        # first small frame

        self.smallframeimage1 = Image.open('images/studying1.png')

        self.smallframeimage1 = ImageTk.PhotoImage(self.smallframeimage1)
        self.small1label = tk.Label(self.smallframe1, image=self.smallframeimage1, bg='white')
        self.small1label.place(relx=0.1, rely=0.1)
        smalll1label2 = ctk.CTkLabel(self.smallframe1, text='Students', font=('Ariel', 10),
                                     text_color='#242818', fg_color='white', corner_radius=4)
        smalll1label2.place(relx=0.37, rely=0.1)

        smalll1label3 = ctk.CTkLabel(self.smallframe1, text='12,765', font=('Helvetica', 30),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smalll1label3.place(relx=0.35, rely=0.45)
        print('check9')
        # second small frame
        self.smallframeimage2 = Image.open('images/teacher1.png')

        self.smallframeimage2 = ImageTk.PhotoImage(self.smallframeimage2)
        self.small2label = tk.Label(self.smallframe2, image=self.smallframeimage2, bg='white')
        self.small2label.place(relx=0.1, rely=0.1)
        smalll2label2 = ctk.CTkLabel(self.smallframe2, text='Lecturers', font=('Ariel', 10),
                                     text_color='#242818', fg_color='white', corner_radius=4)
        smalll2label2.place(relx=0.37, rely=0.1)

        smalll1label3 = ctk.CTkLabel(self.smallframe2, text='108', font=('Helvetica', 30),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smalll1label3.place(relx=0.35, rely=0.45)
        print('check10')
        # third frame
        self.smallframeimage3 = Image.open('images/379383_student_icon.png')

        self.smallframeimage3 = ImageTk.PhotoImage(self.smallframeimage3)
        self.small3label = tk.Label(self.smallframe3, image=self.smallframeimage3, bg='white')
        self.small3label.place(relx=0.1, rely=0.1)
        smalll3label2 = ctk.CTkLabel(self.smallframe3, text='Graduates', font=('Ariel', 10),
                                     text_color='#242818', fg_color='white', corner_radius=4)
        smalll3label2.place(relx=0.37, rely=0.1)

        smalll3label3 = ctk.CTkLabel(self.smallframe3, text='32,762', font=('Helvetica', 30),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smalll3label3.place(relx=0.35, rely=0.45)
        print('check11')
        # fourth frame
        self.smallframeimage4 = Image.open('images/books (1).png')

        self.smallframeimage4 = ImageTk.PhotoImage(self.smallframeimage4)
        self.small4label = tk.Label(self.smallframe4, image=self.smallframeimage4, bg='white')
        self.small4label.place(relx=0.1, rely=0.1)
        smalll4label2 = ctk.CTkLabel(self.smallframe4, text='Courses', font=('Ariel', 10),
                                     text_color='#242818', fg_color='white', corner_radius=4)
        smalll4label2.place(relx=0.37, rely=0.1)

        smalll4label3 = ctk.CTkLabel(self.smallframe4, text='620', font=('Helvetica', 30),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smalll4label3.place(relx=0.35, rely=0.45)
        print('check12')
        self.draw_bar_chart()
        print('check13')
        self.draw_pie_chart()
        self.draw_scatter_plot()

        #frame scrollable info

        smalll6label1 = ctk.CTkLabel(self.smallframe6A, text='LIST OF COURSES', font=('Helvetica', 15),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smalll6label1.pack(pady=5)
        self.frameline2 = ctk.CTkFrame(self.smallframe6A, fg_color='#173662', width=300,
                                      height=5, corner_radius=10)
        self.frameline2.pack(pady=15)

        smalll6label2 = ctk.CTkLabel(self.smallframe6A, text='Computer science\nFood technology\nSLT'
                                                             '\nBanking & Finance\nComputer Engineering\nElect Elect'
                                                             '\nAccounting\nHMT\nTaxation\nAgric Technology\nMechatronic\nCivil Engineering\nMass Comm\nMarkerting\ne.t.c', font=('Ariel', 15),
                                     text_color='black', fg_color='white')
        smalll6label2.pack(pady=10,padx=0.1)

        smalll6label3 = ctk.CTkLabel(self.smallframe6A, text='LIST OF FACULTY', font=('Helvetica', 15),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smalll6label3.pack(pady=5)
        self.frameline4 = ctk.CTkFrame(self.smallframe6A, fg_color='#173662', width=300,
                                       height=5, corner_radius=10)
        self.frameline4.pack(pady=15)

        smalll6label5 = ctk.CTkLabel(self.smallframe6A, text='Applied Science\nEngineering\nCommunication'
                                                             '\nART\nManagement\nElect Elect'
                                                             '\nCommerce\nAgriculture\ne.t.c',
                                     font=('Ariel', 15),
                                     text_color='black', fg_color='white')
        smalll6label5.pack(pady=10, padx=0.1)

        smalll6label6 = ctk.CTkLabel(self.smallframe6A, text='NUMBER OF STUENTS', font=('Helvetica', 15),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smalll6label6.pack(pady=5)
        self.frameline3 = ctk.CTkFrame(self.smallframe6A, fg_color='#173662', width=300,
                                       height=5, corner_radius=10)
        self.frameline3.pack(pady=15)

        smalll6label7 = ctk.CTkLabel(self.smallframe6A, text='Computer science: 512\nFood technology: 613\nSLT: 900'
                                                             '\nBanking & Finance: 1023\nComputer Engineering: 2515\nElect Elect: 896'
                                                             '\nAccounting: 1890\nHMT: 654\nTaxation: 432\nAgric Technology: 789\nMechatronic: 321\nCivil Engineering: 657\nMass Comm: 3567\nMarkerting: 761\ne.t.c',
                                     font=('Ariel', 15),
                                     text_color='black', fg_color='white')
        smalll6label7.pack(pady=10, padx=0.1)

    # self.display_calendar()



    def record(self):
        self.destroymain()
        self.button_record.configure(fg_color='#276878')

        self.largeframerecord = ctk.CTkFrame(self.mainframe1, fg_color='#ECEBE9', width=1400,
                                       height=680, corner_radius=10, border_color='#173662',
                                       border_width=0)
        self.largeframerecord.place(relx=0.5, rely=0.5)
        self.largeframerecord.pack(pady=0, padx=0, fill=BOTH)

        self.treeframe2 = tk.Frame(self.largeframerecord, bg='black', width=100,
                                  height=680)
        self.treeframe2.pack(pady=5, padx=10, side=RIGHT)

        scrollbarX = tk.Scrollbar(self.treeframe2, orient=HORIZONTAL)
        scrollbarY = tk.Scrollbar(self.treeframe2, orient=VERTICAL)

        style = ttk.Style(self.treeframe2)
        style.theme_use('clam')
        style.configure('Treeview', font=('Arial', 10), foreground='#173662', background='white',
                        fieldbackground='white')
        style.map('Treeview', background=[('selected', 'mediumseagreen')])

        style.configure('Treeview.Heading', font=('Arial', 10,), background='mediumseagreen', foreground='white')

        # Create Treeview widget
        self.tree2 = ttk.Treeview(self.treeframe2, height=30, xscrollcommand=scrollbarX.set,
                                 yscrollcommand=scrollbarY.set,
                                 columns=('Matric', 'Surname', 'Name', 'DOB', 'Department', 'Gender', 'Level',
                                          'Grade', 'Cgpa', 'Faculty', 'Email',
                                          'Phone_No', 'Time', 'Date'), show='headings')
        self.tree2.column('#0', width=100)

        scrollbarX.configure(command=self.tree2.xview)
        scrollbarY.configure(command=self.tree2.yview)
        scrollbarX.pack(side=BOTTOM, fill=X)
        scrollbarY.pack(side=RIGHT, fill=Y)
        self.tree2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Define columns and set their properties
        columns = ['Matric', 'Surname', 'Name', 'DOB', 'Department', 'Gender', 'Level',
                   'Grade', 'Cgpa', 'Faculty', 'Email',
                   'Phone_No', 'Time', 'Date']
        for col in columns:
            self.tree2.heading(col, text=col, )
            self.tree2.column(col, width=150, anchor='center')

        query = 'select *from student'
        self.mycursor.execute(query)
        self.fecthed_data = self.mycursor.fetchall()
        self.tree2.delete(*self.tree2.get_children())
        for data in self.fecthed_data:
            datalist = list(data)
            self.tree2.insert('', END, values=datalist)



    def register(self):

        def reggister():
            if self.Matric2entry.get() == '' or self.Surname2entry.get() == '' or self.Name2entry.get() == '' or self.DOB2entry.get() == '' or self.Dept2entry.get() == '' or self.Gender2entry.get() == '' or self.Level2entry.get() == '' or self.Grade2entry.get() == '' or self.Status2entry.get() == '' or self.Fac2entry.get() == '' or self.Email2entry.get() == '' or self.phone2entry.get() == '':
                messagebox.showerror('Error', 'no field should be left empty')

            else:
                try:
                    query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    self.mycursor.execute(query, (
                    self.Matric2entry.get(), self.Surname2entry.get(), self.Name2entry.get(), self.DOB2entry.get(), self.Dept2entry.get(),
                    self.Gender2entry.get(),
                    self.Level2entry.get(), self.Grade2entry.get(), self.Status2entry.get(), self.Fac2entry.get(), self.Email2entry.get(),
                    self.phone2entry.get(), self.currenttime, self.date))

                    self.con.commit()

                    result = messagebox.askyesno('Data added sucessfully', 'do you want to clean the form')
                    if result:
                        self.Matric2entry.delete(0, END)
                        self.Surname2entry.delete(0, END)
                        self.Name2entry.delete(0, END)
                        self.DOB2entry.delete(0, END)
                        self.Dept2entry.delete(0, END)
                        self.Grade2entry.delete(0, END)
                        self.Level2entry.delete(0, END)
                        self.Email2entry.delete(0, END)
                        self.Gender2entry.delete(0, END)
                        self.phone2entry.delete(0, END)
                        self.Fac2entry.delete(0, END)
                        self.Status2entry.delete(0, END)
                    else:
                        pass

                except:
                    messagebox.showerror('Error', 'Matric number already exist!')
                    return





        self.destroymain()
        self.button_register.configure(fg_color='#276878')
        self.largeframe2 = ctk.CTkScrollableFrame(self.mainframe1, fg_color='#ECEBE9', width=1000,
                                       height=650, corner_radius=10, border_color='#173662',
                                       border_width=0,orientation='vertical')
        self.largeframe2.place(relx=0.01, rely=0.01)

        self.labelregg = ctk.CTkLabel(self.largeframe2, text='REGISTER NEW STUDENT',image=ctk.CTkImage(self.image_butreg),compound=tk.LEFT,
                                         fg_color='blue', font=('Times', 25), text_color='white',
                                      corner_radius=10)
        self.labelregg.grid(row=0,columnspan=3,padx=20,pady=15)

        self.labelMatric2 = ctk.CTkLabel(self.largeframe2, text='Matric_No:',
                                         fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelMatric2.grid(row=1,column=0,padx=10, pady=15,sticky='w')

        self.Matric2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Matric_no', width=500, height=35,
                                         text_color='black', corner_radius=10,
                                         border_color='black', font=('Helvetica', 18), border_width=1)
        self.Matric2entry.grid(row=1,column=1,sticky='w',padx=10)

        self.labelSurname2 = ctk.CTkLabel(self.largeframe2, text='Surname:',
                                         fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelSurname2.grid(row=2, column=0, padx=10, pady=15, sticky='w')

        self.Surname2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Surname', width=500, height=35,
                                         text_color='black', corner_radius=10,
                                         border_color='black', font=('Helvetica', 18), border_width=1)
        self.Surname2entry.grid(row=2, column=1, sticky='w', padx=10)

        self.labelName2 = ctk.CTkLabel(self.largeframe2, text='Name:',
                                          fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelName2.grid(row=3, column=0, padx=10, pady=15, sticky='w')

        self.Name2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Name', width=500, height=35,
                                          text_color='black', corner_radius=10,
                                          border_color='black', font=('Helvetica', 18), border_width=1)
        self.Name2entry.grid(row=3, column=1, sticky='w', padx=10)

        self.labelDOB2 = ctk.CTkLabel(self.largeframe2, text='DOB:',
                                       fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelDOB2.grid(row=4, column=0, padx=10, pady=15, sticky='w')

        self.DOB2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your DOB', width=500, height=35,
                                       text_color='black', corner_radius=10,
                                       border_color='black', font=('Helvetica', 18), border_width=1)
        self.DOB2entry.grid(row=4, column=1, sticky='w', padx=10)

        self.labelDept2 = ctk.CTkLabel(self.largeframe2, text='Department:',
                                      fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelDept2.grid(row=5, column=0, padx=10, pady=15, sticky='w')

        self.Dept2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Department', width=500, height=35,
                                      text_color='black', corner_radius=10,
                                      border_color='black', font=('Helvetica', 18), border_width=1)
        self.Dept2entry.grid(row=5, column=1, sticky='w', padx=10)

        self.labelGender2 = ctk.CTkLabel(self.largeframe2, text='Gender:',
                                       fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelGender2.grid(row=6, column=0, padx=10, pady=15, sticky='w')

        self.Gender2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your gender', width=500, height=35,
                                       text_color='black', corner_radius=10,
                                       border_color='black', font=('Helvetica', 18), border_width=1)
        self.Gender2entry.grid(row=6, column=1, sticky='w', padx=10)

        self.labelLevel2 = ctk.CTkLabel(self.largeframe2, text='Level:',
                                         fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelLevel2.grid(row=7, column=0, padx=10, pady=15, sticky='w')

        self.Level2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Level', width=500, height=35,
                                         text_color='black', corner_radius=10,
                                         border_color='black', font=('Helvetica', 18), border_width=1)
        self.Level2entry.grid(row=7, column=1, sticky='w', padx=10)

        self.labelGrade2 = ctk.CTkLabel(self.largeframe2, text='Grade:',
                                        fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelGrade2.grid(row=8, column=0, padx=10, pady=15, sticky='w')

        self.Grade2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Level', width=500, height=35,
                                        text_color='black', corner_radius=10,
                                        border_color='black', font=('Helvetica', 18), border_width=1)
        self.Grade2entry.grid(row=8, column=1, sticky='w', padx=10)

        self.labelStatus2 = ctk.CTkLabel(self.largeframe2, text='Cgpa:',
                                      fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelStatus2.grid(row=9, column=0, padx=10, pady=15, sticky='w')

        self.Status2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your cgpa', width=500, height=35,
                                        text_color='black', corner_radius=10,
                                        border_color='black', font=('Helvetica', 18), border_width=1)
        self.Status2entry.grid(row=9, column=1, sticky='w', padx=10)


        self.labelFac2 = ctk.CTkLabel(self.largeframe2, text='Faculty:',
                                       fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelFac2.grid(row=10, column=0, padx=10, pady=15, sticky='w')

        self.Fac2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Faculty', width=500, height=35,
                                        text_color='black', corner_radius=10,
                                        border_color='black', font=('Helvetica', 18), border_width=1)
        self.Fac2entry.grid(row=10, column=1, sticky='w', padx=10)

        self.labelEmail2 = ctk.CTkLabel(self.largeframe2, text='Email:',
                                      fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelEmail2.grid(row=11, column=0, padx=10, pady=15, sticky='w')

        self.Email2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Email', width=500, height=35,
                                      text_color='black', corner_radius=10,
                                      border_color='black', font=('Helvetica', 18), border_width=1)
        self.Email2entry.grid(row=11, column=1, sticky='w', padx=10)

        self.labelphone2 = ctk.CTkLabel(self.largeframe2, text='Phone_no:',
                                        fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelphone2.grid(row=12, column=0, padx=10, pady=15, sticky='w')

        self.phone2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your phone_no', width=500, height=35,
                                        text_color='black', corner_radius=10,
                                        border_color='black', font=('Helvetica', 18), border_width=1)
        self.phone2entry.grid(row=12, column=1, sticky='w', padx=10)

        self.registernew = ctk.CTkButton(self.largeframe2, text='Register', corner_radius=32,
                                         text_color='white', border_color='black', border_spacing=2,
                                         fg_color='#173662', hover_color='#276878', command=reggister,
                                         border_width=2, image=ctk.CTkImage(self.image_but), width=200, height=50,
                                         font=('Times', 20))
        self.registernew.grid(row=13,columnspan=3)

        #self.largeframe2.pack(pady=0, padx=0, fill=BOTH)
        #self.largeframe2=ctk.CTkScrollbar(self.largeframe2)


        #self.labelsurname.pack()
        #self.surnameentry.pack()
        #self.labelname.pack()
        #self.nameentry.pack()
        #self.labelmatric.pack()
        #self.matricentry.pack()
        #self.labellevel.pack()
        #self.levelentry.pack()
        #self.labelDob.pack()
        #self.Dobentry.pack()
        #self.labeldept.pack()
        #self.deptentry.pack()
        #self.labelcgp.pack()
        #self.cgpentry.pack()
        #self.labelstatus.pack()
        #self.statusentry.pack()
        #self.labelfac.pack()
        #self.facentry.pack()

    def RegisterNew(self):
        pass
    def draw_bar_chart(self):
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        # Sample data
        categories = ['Com-Sci', 'SLT', 'Mass-Com','Food-Nut',
                      'Com-Eng', 'Elect-Elect','Civil-Eng','Accounting',
                      'Bank&Fin','Architecture','Machanical','Mechatronic']
        values = [85, 90, 80, 50, 75,80,80,70,75,72,80,65]
        #colors = ['red', 'green', 'blue', 'orange', 'purple']
        fig, ax = plt.subplots(figsize=(5, 3), dpi=100)
        ax.bar(categories, values)
        #ax.set_xlabel('Courses',color='#173662')
        ax.set_ylabel('Percentage',color='#173662')
        ax.set_title('Course competitiveness')
        plt.xticks(rotation=10, ha='right',fontsize=5)

        canvas = FigureCanvasTkAgg(fig, master=self.smallframe8A)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def draw_pie_chart(self):

        # Sample data (replace with your actual data)
        male_count = 450
        female_count = 550

        # Calculate percentages
        total_count = male_count + female_count
        male_percentage = (male_count / total_count) * 100
        female_percentage = (female_count / total_count) * 100

        # Create labels and sizes for the pie chart
        labels = ['Male', 'Female']
        sizes = [male_percentage, female_percentage]
        colors = ['lightblue', 'lightcoral']

        # Create the pie chart
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.set_title('Percentage of Boys to Girls',fontsize=7)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Embed the plot in a Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.smallframe7A)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.5, rely=1, anchor=tk.CENTER)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        #canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=tk.CENTER)



    def display_calendar(self):

        # Get the current date
        now = datetime.now()
        year = now.year
        month = now.month

        # Create a Calendar object
        cal = calendar.Calendar()

        # Get the calendar for the current month
        month_calendar = cal.monthdatescalendar(year, month)

        # Create a Tkinter Treeview widget to display the calendar
        tree = ttk.Treeview(self.smallframe5A, columns=list(range(7)), show="headings")

        # Define the headings for the columns
        for i, day in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]):
            tree.heading(i, text=day)

        # Insert the dates into the Treeview widget
        for week in month_calendar:
            tree.insert("", "end", values=week)

        # Pack the Treeview widget into the frame
        tree.pack(padx=0, pady=0, fill=tk.BOTH, expand=True)


    def destroymain(self):
        for frame in self.mainframe1.winfo_children():
            frame.destroy()
        for button in self.frame2.winfo_children():
            button.configure(fg_color='transparent')

        self.frameline.configure(fg_color='white')

    def destroymain1(self):
        for frame in self.mainframe1.winfo_children():
            frame.destroy()


    def database_butfunction(self):
        self.destroymain()
        self.button_database.configure(fg_color='#276878')

        self.largeframe3= ctk.CTkFrame(self.mainframe1, fg_color='#ecebe9', width=1400,
                                        height=680, corner_radius=10, border_color='#173662',
                                        border_width=0)
        self.largeframe3.place(relx=0.5, rely=0.5)
        self.largeframe3.pack(pady=0, padx=0)

        self.framebutton=ctk.CTkFrame(self.largeframe3, fg_color='#ecebe9', width=250,
                                        height=500, corner_radius=10, border_color='#173662',
                                        border_width=0)
        self.framebutton.place(relx=0.001, rely=0.01,anchor='n')
        self.framebutton.pack(side=LEFT,expand=True,fill=Y)

        self.labeldata = ctk.CTkLabel(self.framebutton, text='DATABASE',
                             fg_color='#ecebe9', font=('helvatica', 25), text_color='#173662', corner_radius=10,pady=20)
        #self.labeldata.place(relx=0.01, rely=0.05)
        self.labeldata.grid(row=0,column=0)

        self.add_but = ctk.CTkButton(self.framebutton, text='Add Student',
                                         text_color='blue',state=DISABLED,
                                         fg_color='transparent', hover_color='#276878', command=self.addstudent,
                                        width=120, height=35,
                                         font=('Times', 18))
        self.add_but.grid(row=1,column=0,pady=20)

        self.search2_but = ctk.CTkButton(self.framebutton, text='Search Student',
                                     text_color='blue',state=DISABLED,
                                     fg_color='transparent', hover_color='#276878', command=self.search_student,
                                     width=120, height=35,
                                     font=('Times', 18))
        self.search2_but.grid(row=2, column=0, pady=20)

        self.delete_but = ctk.CTkButton(self.framebutton, text='Delete Student',
                                         text_color='blue',state=DISABLED,
                                         fg_color='transparent', hover_color='#276878', command=self.delete_student,
                                         width=120, height=35,
                                         font=('Times', 18))
        self.delete_but.grid(row=3, column=0, pady=20)

        self.update_but = ctk.CTkButton(self.framebutton, text='Update Student',
                                         text_color='blue',state=DISABLED,
                                         fg_color='transparent', hover_color='#276878', command=self.update,
                                         width=120, height=35,
                                         font=('Times', 18))
        self.update_but.grid(row=4, column=0, pady=20)

        self.show_but = ctk.CTkButton(self.framebutton, text='Show Student',
                                         text_color='blue',state=DISABLED,
                                         fg_color='transparent', hover_color='#276878', command=self.showstudent,
                                         width=120, height=35,
                                         font=('Times', 18))
        self.show_but.grid(row=5, column=0, pady=20)

        self.export_but = ctk.CTkButton(self.framebutton, text='Export Data',
                                         text_color='blue',state=DISABLED,
                                         fg_color='transparent', hover_color='#276878', command=self.export,
                                         width=120, height=35,
                                         font=('Times', 18))
        self.export_but.grid(row=6, column=0, pady=20)

        self.treeframe =tk.Frame(self.largeframe3 , bg='black', width=100,
                                       height=680)
        self.treeframe.pack(pady=5, padx=10,side=RIGHT)

        scrollbarX=tk.Scrollbar(self.treeframe,orient=HORIZONTAL)
        scrollbarY = tk.Scrollbar(self.treeframe, orient=VERTICAL)

        #self.tree=ttk.Treeview(self.treeframe,height=650,columns=('Surname','Name','Matric','Level',
                                                     #'Gender','D.O.B','DEPT','CGPA',
                                                      # 'Status','Falculty'))
        #style = ttk.Style()
        #style.configure('TreeView.Heading', background='blue', forground='red')
        #self.tree.place(relx=0.1,rely=0.1)
        #self.tree.pack(side=LEFT,fill=Y,expand=1)

        #self.tree.heading('Surname',text='Surname')
        #self.tree.config(show='headings')

        style = ttk.Style(self.treeframe)
        style.theme_use('clam')
        style.configure('Treeview', font=('Arial', 10), foreground='#173662', background='white', fieldbackground='white')
        style.map('Treeview', background=[('selected', 'mediumseagreen')])

        style.configure('Treeview.Heading', font=('Arial', 10,), background='mediumseagreen', foreground='white')


        # Create Treeview widget
        self.tree = ttk.Treeview(self.treeframe, height=30,xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set, columns=('Matric', 'Surname', 'Name', 'DOB', 'Department', 'Gender', 'Level',
                                                                     'Grade', 'Cgpa', 'Faculty', 'Email',
                                                                     'Phone_No', 'Time', 'Date'), show='headings')
        self.tree.column('#0',width=100)

        scrollbarX.configure(command=self.tree.xview)
        scrollbarY.configure(command=self.tree.yview)
        scrollbarX.pack(side=BOTTOM, fill=X)
        scrollbarY.pack(side=RIGHT, fill=Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Define columns and set their properties
        columns = ['Matric','Surname', 'Name', 'DOB', 'Department', 'Gender', 'Level',
                                                                     'Grade', 'Cgpa', 'Faculty', 'Email',
                                                                     'Phone_No','Time','Date']
        for col in columns:
            self.tree.heading(col, text=col, )
            self.tree.column(col, width=150, anchor='center')
            #self.tree.configure(column='Email', width=350,anchor='center')

        # Sample data
       # sample_data = [
           # ("Smith", "John", "12345", "3", "M", "01-01-2000", "CSE", "3.5", "Active", "Engineering"),
           # ("Doe", "Jane", "67890", "2", "F", "05-15-1999", "ECE", "3.8", "Active", "Engineering"),
            #("Brown", "Charlie", "54321", "4", "M", "07-22-1998", "EEE", "3.2", "Graduated", "Engineering")
       # ]

        #for item in sample_data:
            #self.tree.insert("", tk.END, values=item)

        self.firstcon = ctk.CTkButton(self.framebutton, text='connect',
                                      text_color='white',
                                      fg_color='blue', hover_color='#276878', command=self.confirm,
                                      width=100, height=35,
                                      font=('Times', 18))
        self.firstcon.grid(row=8,column=0)

    def logout(self):
        def yes():
            self.main_window.destroy()
        def no():
            self.main_window1.destroy()

        self.main_window1 = tk.Toplevel()
        self.main_window1.grab_set()
        self.main_window1.title('School MAnagement System')
        self.main_window1.geometry('400x150+600+200')
        self.main_window1.config(bg='white')
        self.main_window1.resizable(False, False)

        labellogout=tk.Label(self.main_window1,text='Do You Want To Exit?',
                             font=('Ariel',15,'bold'),bg='white',fg='#173662')
        labellogout.grid(row=0,column=0,padx=20,pady=20)

        butyes=ctk.CTkButton(self.main_window1 , text='YES',
                                         text_color='white',
                                         fg_color='red', hover_color='#276878', command=yes,
                                         width=90, height=35,
                                         font=('Times', 18))


        butno = ctk.CTkButton(self.main_window1, text='N0',
                               text_color='white',
                               fg_color='green', hover_color='#276878', command=no,
                               width=90, height=35,
                               font=('Times', 18))

        butyes.grid(row=1, column=0)
        butno.grid(row=1, column=1)


    def connectDatabase1(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='1234')
            self.mycursor=con.cursor()
        except:
            messagebox.showinfo('error','couldnt connect to the database')
            return

        try:
            query = 'create database StudentManagementSystem'
            self.mycursor.execute(query)

            #query='create table Student(Matric_no varchar(20) not null primary key,Surname varchar(20),Name varchar(20),D.O.B varchar(20),Department varchar(30),Gender varchar(20),Level varchar(10),Grade varchar(20),Status varChar(20),Falculty varchar(50),Email varchar(30),Phone_No varchar(20),Time varchar(10),Date varchar(10))'
            #self.mycursor.execute(query)

            #query='create table information(key varchar(50),value varchar(100),description TEXT,primary key(key,value))'
            #self.mycursor.execute(query)

            query = 'create database StudentManagementSystem'
            self.mycursor.execute(query)

            query = '''create table Student(
                Matric_no varchar(20) not null primary key,
                Surname varchar(20),
                Name varchar(20),
                D.O.B varchar(20),
                Department varchar(30),
                Gender varchar(20),
                Level varchar(10),
                Grade varchar(20),
                Status varChar(20),
                Falculty varchar(50),
                Email varchar(30),
                Phone_No varchar(20),
                Time varchar(10),
                Date varchar(10))'''
            self.mycursor.execute(query)

            query = '''create table information(
                key varchar(50),
                value varchar(100),
                description TEXT,
                primary key(key,value))'''
            self.mycursor.execute(query)

        except:
            query='use StudentManagementSystem'
            self.mycursor(query)

            query='use informationSchool'
            self.mycursor.execute(query)

        messagebox.showinfo('success','database successfully connected')

    import pymysql
    from tkinter import messagebox

    def connectDatabase(self):
        try:
            self.con = pymysql.connect(
                host='localhost',  # typically 'localhost' or an IP address
                user='root',  # correct parameter name is 'user', not 'role'
                password='1234'
            )
            self.mycursor = self.con.cursor()
        except pymysql.MySQLError as e:
            messagebox.showinfo('error', f"Couldn't connect to the database: {e}")
            print(e)
            return

        try:
            self.mycursor.execute('CREATE DATABASE IF NOT EXISTS StudentManagementSystem')
            self.mycursor.execute('USE StudentManagementSystem')

            self.mycursor.execute('''CREATE TABLE IF NOT EXISTS Student(
                Matric_no VARCHAR(20) NOT NULL PRIMARY KEY,
                Surname VARCHAR(20),
                Name VARCHAR(20),
                DOB VARCHAR(20),                # Changed D.O.B to DOB
                Department VARCHAR(20),
                Gender VARCHAR(20),
                Level VARCHAR(10),
                Grade VARCHAR(20),
                Status DECIMAL(10,2),
                Faculty VARCHAR(50),            # Changed Falculty to Faculty
                Email VARCHAR(30),
                Phone_No VARCHAR(20),
                Time VARCHAR(10),
                Date VARCHAR(10)
            )''')

            # Correcting table definition for information
            self.mycursor.execute('''CREATE TABLE IF NOT EXISTS Studentinformation(
                `key` VARCHAR(50),
                `value` VARCHAR(100),
                description TEXT,
                PRIMARY KEY(`key`, `value`)
            )''')
        except pymysql.MySQLError as e:
            messagebox.showinfo('error', f"An error occurred while creating tables: {e}")
            return

        messagebox.showinfo('success', 'Database successfully connected')
        self.topcon.configure(fg_color='green',text="Connected")
        self.button_Home.configure(state=NORMAL)
        self.button_register.configure(state=NORMAL)
        self.button_record.configure(state=NORMAL)
        self.button_result.configure(state=NORMAL)
        self.button_search.configure(state=NORMAL)
        self.button_database.configure(state=NORMAL)
        self.homepage()

    def home(self):
        pass
    def destroy_window(self):
        self.Splashwindow.destroy()
        self.loginwindow()

    def start(self):
        self.Splashwindow.mainloop()

    def start2(self):
        self.login_window.mainloop()

    def new_start(self):
        self.start2()

    def switch_window(self):
        self.Splashwindow.withdraw()
        #self.login_window.deiconify()

    def showstudent(self):
        print('hello')
        query = 'select *from student'
        self.mycursor.execute(query)
        self.fecthed_data = self.mycursor.fetchall()
        self.tree.delete(*self.tree.get_children())
        for data in self.fecthed_data:
            datalist = list(data)
            self.tree.insert('', END, values=datalist)

    def update(self):
        global status_value

        def update_student():
            query = '''
            UPDATE student 
            SET Surname=%s, Name=%s, DOB=%s, Department=%s, Gender=%s, Level=%s, Grade=%s, Status=%s, Faculty=%s, Email=%s, Phone_No=%s, Time=%s, Date=%s 
            WHERE Matric_no=%s
            '''

            # Fetching and converting the status entry to string to ensure proper format
            status_value = str(Statusentry.get())

            self.mycursor.execute(query, (
                Surnameentry.get(),
                Nameentry.get(),
                DOBentry.get(),
                Departmententry.get(),
                Genderentry.get(),
                Levelentry.get(),
                Gradeentry.get(),
                status_value,
                Facultyentry.get(),
                Emailentry.get(),
                phoneentry.get(),
                self.currenttime,
                self.date,
                matricentry.get()
            ))

            self.con.commit()
            messagebox.showinfo('Success', f"{matricentry.get()} has been modified")
            self.upadate_window.destroy()
            self.showstudent()

        self.upadate_window = tk.Toplevel(self.treeframe)
        self.upadate_window.title('Update STUDENT')
        self.upadate_window.grab_set()

        matriclabel = tk.Label(self.upadate_window, text='Matric No', font=('times new roman', 15, 'bold'))
        matriclabel.grid(padx=10, pady=10)
        matricentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        matricentry.grid(row=0, column=1, padx=10, pady=10)

        Surnamelabel = tk.Label(self.upadate_window, text='Surname', font=('times new roman', 15, 'bold'))
        Surnamelabel.grid(row=1, column=0, padx=10, pady=10)
        Surnameentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Surnameentry.grid(row=1, column=1, padx=10, pady=10)

        Namelabel = tk.Label(self.upadate_window, text='Name', font=('times new roman', 15, 'bold'))
        Namelabel.grid(row=2, column=0, padx=10, pady=10)
        Nameentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Nameentry.grid(row=2, column=1, padx=10, pady=10)

        DOBlabel = tk.Label(self.upadate_window, text='DOB', font=('times new roman', 15, 'bold'))
        DOBlabel.grid(row=3, column=0, padx=10, pady=10)
        DOBentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        DOBentry.grid(row=3, column=1, padx=10, pady=10)

        Departmentlabel = tk.Label(self.upadate_window, text='Department', font=('times new roman', 15, 'bold'))
        Departmentlabel.grid(row=4, column=0, padx=10, pady=10)
        Departmententry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Departmententry.grid(row=4, column=1, padx=10, pady=10)

        Genderlabel = tk.Label(self.upadate_window, text='Gender', font=('times new roman', 15, 'bold'))
        Genderlabel.grid(row=5, column=0, padx=10, pady=10)
        Genderentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Genderentry.grid(row=5, column=1, padx=10, pady=10)

        Levellabel = tk.Label(self.upadate_window, text='Level', font=('times new roman', 15, 'bold'))
        Levellabel.grid(row=6, column=0, padx=10, pady=10)
        Levelentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Levelentry.grid(row=6, column=1, padx=10, pady=10)

        Gradelabel = tk.Label(self.upadate_window, text='Grade', font=('times new roman', 15, 'bold'))
        Gradelabel.grid(row=7, column=0, padx=10, pady=10)
        Gradeentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Gradeentry.grid(row=7, column=1, padx=10, pady=10)

        Statuslabel = tk.Label(self.upadate_window, text='Cgpa', font=('times new roman', 15, 'bold'))
        Statuslabel.grid(row=8, column=0, padx=10, pady=10)
        Statusentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Statusentry.grid(row=8, column=1, padx=10, pady=10)

        Facultylabel = tk.Label(self.upadate_window, text='Faculty', font=('times new roman', 15, 'bold'))
        Facultylabel.grid(row=9, column=0, padx=10, pady=10)
        Facultyentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Facultyentry.grid(row=9, column=1, padx=10, pady=10)

        Emaillabel = tk.Label(self.upadate_window, text='Email', font=('times new roman', 15, 'bold'))
        Emaillabel.grid(row=10, column=0, padx=10, pady=10)
        Emailentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Emailentry.grid(row=10, column=1, padx=10, pady=10)

        phonelabel = tk.Label(self.upadate_window, text='phone', font=('times new roman', 15, 'bold'))
        phonelabel.grid(row=11, column=0, padx=10, pady=10)
        phoneentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        phoneentry.grid(row=11, column=1, padx=10, pady=10)

        buttonaddstudent = tk.Button(self.upadate_window, text='Update Student', bg='#173662', fg='white',
                                     command=update_student, font=('times new roman', 15, 'bold'))
        buttonaddstudent.grid(row=13, columnspan=3, pady=10, padx=10)

        index = self.tree.focus()
        content = self.tree.item(index)
        data = content['values']

        matricentry.insert(0, data[0])
        Surnameentry.insert(0, data[1])
        Nameentry.insert(0, data[2])
        DOBentry.insert(0, data[3])
        Departmententry.insert(0, data[4])
        Genderentry.insert(0, data[5])
        Levelentry.insert(0, data[6])
        Gradeentry.insert(0, data[7])
        Statusentry.insert(0, data[8])
        Facultyentry.insert(0, data[9])
        Emailentry.insert(0, data[10])
        phoneentry.insert(0, data[11])

        # Initialize status_value and ensure currenttime and date are set
        status_value = str(Statusentry.get())
        self.currenttime = self.currenttime  # Replace with actual time logic
        self.date = self.date  # Replace with actual date logic

    def addstudent(self):

        def add():

               if matricentry.get()=='' or Surnameentry.get()=='' or Nameentry.get()=='' or DOBentry.get()=='' or Departmententry.get()=='' or  Genderentry.get()=='' or Levelentry.get()=='' or Gradeentry.get()=='' or Statusentry.get()=='' or Facultyentry.get()=='' or Emailentry.get()=='' or phoneentry.get()=='':
                  messagebox.showerror('Error','no field should be left empty',parent=self.treeframe)

               else:
                   try:
                         query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                         self.mycursor.execute(query,(matricentry.get(),Surnameentry.get(),Nameentry.get(),DOBentry.get(),Departmententry.get(),Genderentry.get(),
                                                     Levelentry.get(),Gradeentry.get(),Statusentry.get(),Facultyentry.get(),Emailentry.get(),phoneentry.get(),self.currenttime,self.date))
                         print(matricentry.get())
                         self.con.commit()

                         result=messagebox.askyesno('Data added sucessfully','do you want to clean the form')
                         if result:
                             matricentry.delete(0,END)
                             Surnameentry.delete(0,END)
                             Nameentry.delete(0, END)
                             DOBentry.delete(0, END)
                             Departmententry.delete(0, END)
                             Gradeentry.delete(0, END)
                             Levelentry.delete(0, END)
                             Emailentry.delete(0, END)
                             Genderentry.delete(0, END)
                             phoneentry.delete(0, END)
                             Facultyentry.delete(0, END)
                             Statusentry.delete(0, END)
                         else:
                             pass
                   except:
                       messagebox.showerror('Error','Matric number already exist!')
                       return
               query='select *from student'
               self.mycursor.execute(query)
               self.fecthed_data=self.mycursor.fetchall()
               self.tree.delete(*self.tree.get_children())
               for data in self.fecthed_data:
                   datalist=list(data)
                   self.tree.insert('',END,values=datalist)








        #self.addstudent_window=tk.Toplevel(self.main_window)
        self.addstudent_window=tk.Toplevel(self.treeframe)
        self.addstudent_window.title('ADD STUDENT')
        #self.addstudent_window.place(relx=0.001,rely=0.01)

        self.addstudent_window.grab_set()
        matriclabel=tk.Label(self.addstudent_window,text='Matric No',font=('times new roman',15,'bold'))
        matriclabel.grid(padx=10,pady=10)
        matricentry=tk.Entry(self.addstudent_window,width=25,font=('times new roman',15,'bold'))
        matricentry.grid(row=0,column=1,padx=10,pady=10)

        Surnamelabel = tk.Label(self.addstudent_window, text='Surname', font=('times new roman', 15, 'bold'))
        Surnamelabel.grid(row=1,column=0,padx=10, pady=10)
        Surnameentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Surnameentry.grid(row=1, column=1, padx=10, pady=10)

        Namelabel = tk.Label(self.addstudent_window, text='Name', font=('times new roman', 15, 'bold'))
        Namelabel.grid(row=2, column=0, padx=10, pady=10)
        Nameentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Nameentry.grid(row=2, column=1, padx=10, pady=10)

        DOBlabel = tk.Label(self.addstudent_window, text='DOB', font=('times new roman', 15, 'bold'))
        DOBlabel.grid(row=3, column=0, padx=10, pady=10)
        DOBentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        DOBentry.grid(row=3, column=1, padx=10, pady=10)

        Departmentlabel = tk.Label(self.addstudent_window, text='Department', font=('times new roman', 15, 'bold'))
        Departmentlabel.grid(row=4, column=0, padx=10, pady=10)
        Departmententry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Departmententry.grid(row=4, column=1, padx=10, pady=10)

        Genderlabel = tk.Label(self.addstudent_window, text='Gender', font=('times new roman', 15, 'bold'))
        Genderlabel.grid(row=5, column=0, padx=10, pady=10)
        Genderentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Genderentry.grid(row=5, column=1, padx=10, pady=10)

        Levellabel = tk.Label(self.addstudent_window, text='Level', font=('times new roman', 15, 'bold'))
        Levellabel.grid(row=6, column=0, padx=10, pady=10)
        Levelentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Levelentry.grid(row=6, column=1, padx=10, pady=10)

        Gradelabel = tk.Label(self.addstudent_window, text='Grade', font=('times new roman', 15, 'bold'))
        Gradelabel.grid(row=7, column=0, padx=10, pady=10)
        Gradeentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Gradeentry.grid(row=7, column=1, padx=10, pady=10)

        Statuslabel = tk.Label(self.addstudent_window, text='Cgpa', font=('times new roman', 15, 'bold'))
        Statuslabel.grid(row=8, column=0, padx=10, pady=10)
        Statusentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Statusentry.grid(row=8, column=1, padx=10, pady=10)

        Facultylabel = tk.Label(self.addstudent_window, text='Faculty', font=('times new roman', 15, 'bold'))
        Facultylabel.grid(row=9, column=0, padx=10, pady=10)
        Facultyentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Facultyentry.grid(row=9, column=1, padx=10, pady=10)

        Emaillabel = tk.Label(self.addstudent_window, text='Email', font=('times new roman', 15, 'bold'))
        Emaillabel.grid(row=10, column=0, padx=10, pady=10)
        Emailentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Emailentry.grid(row=10, column=1, padx=10, pady=10)

        phonelabel = tk.Label(self.addstudent_window, text='phone', font=('times new roman', 15, 'bold'))
        phonelabel.grid(row=11, column=0, padx=10, pady=10)
        phoneentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        phoneentry.grid(row=11, column=1, padx=10, pady=10)

        buttonaddstudent=tk.Button(self.addstudent_window, text='Add Student',bg='#173662',fg='white',command=add,font=('times new roman', 15, 'bold'))
        buttonaddstudent.grid(row=13,columnspan=3,pady=10,padx=10)

        #self.addstudent_window.grid(padx=50,pady=50)

    def search_student(self):

        def searchStd():

            query='select *from student where Matric_no=%s or Surname=%s or Name=%s or DOB=%s or Department=%s or Gender=%s or Level=%s or Grade=%s or Status=%s or Faculty=%s or Email=%s or Phone_No=%s'
            self.mycursor.execute(query,(matricentry.get(),Surnameentry.get(),Nameentry.get(),DOBentry.get(),Departmententry.get(),Genderentry.get(),Levelentry.get(),Gradeentry.get(),Statusentry.get(),Facultyentry.get(),Emailentry.get(),phoneentry.get()))
            self.tree.delete(*self.tree.get_children())
            fetched_data=self.mycursor.fetchall()
            print(fetched_data)
            if self.mycursor.fetchall() is None:
                messagebox.showinfo('Opps','No Data Found')
            else:
                for data in fetched_data:
                    datalist = list(data)
                    self.tree.insert('', END, values=datalist)




        self.searchstudent_window = tk.Toplevel(self.treeframe)
        self.searchstudent_window.title('SEARCH STUDENT')
        # self.searchstudent_window.place(relx=0.001,rely=0.01)

        self.searchstudent_window.grab_set()
        matriclabel = tk.Label(self.searchstudent_window, text='Matric No', font=('times new roman', 15, 'bold'))
        matriclabel.grid(padx=10, pady=10)
        matricentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        matricentry.grid(row=0, column=1, padx=10, pady=10)

        Surnamelabel = tk.Label(self.searchstudent_window, text='Surname', font=('times new roman', 15, 'bold'))
        Surnamelabel.grid(row=1, column=0, padx=10, pady=10)
        Surnameentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Surnameentry.grid(row=1, column=1, padx=10, pady=10)

        Namelabel = tk.Label(self.searchstudent_window, text='Name', font=('times new roman', 15, 'bold'))
        Namelabel.grid(row=2, column=0, padx=10, pady=10)
        Nameentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Nameentry.grid(row=2, column=1, padx=10, pady=10)

        DOBlabel = tk.Label(self.searchstudent_window, text='DOB', font=('times new roman', 15, 'bold'))
        DOBlabel.grid(row=3, column=0, padx=10, pady=10)
        DOBentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        DOBentry.grid(row=3, column=1, padx=10, pady=10)

        Departmentlabel = tk.Label(self.searchstudent_window, text='Department', font=('times new roman', 15, 'bold'))
        Departmentlabel.grid(row=4, column=0, padx=10, pady=10)
        Departmententry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Departmententry.grid(row=4, column=1, padx=10, pady=10)

        Genderlabel = tk.Label(self.searchstudent_window, text='Gender', font=('times new roman', 15, 'bold'))
        Genderlabel.grid(row=5, column=0, padx=10, pady=10)
        Genderentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Genderentry.grid(row=5, column=1, padx=10, pady=10)

        Levellabel = tk.Label(self.searchstudent_window, text='Level', font=('times new roman', 15, 'bold'))
        Levellabel.grid(row=6, column=0, padx=10, pady=10)
        Levelentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Levelentry.grid(row=6, column=1, padx=10, pady=10)

        Gradelabel = tk.Label(self.searchstudent_window, text='Grade', font=('times new roman', 15, 'bold'))
        Gradelabel.grid(row=7, column=0, padx=10, pady=10)
        Gradeentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Gradeentry.grid(row=7, column=1, padx=10, pady=10)

        statuslabel = tk.Label(self.searchstudent_window, text='Cgpa', font=('times new roman', 15, 'bold'))
        statuslabel.grid(row=8, column=0, padx=10, pady=10)
        Statusentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Statusentry.grid(row=8, column=1, padx=10, pady=10)

        Facultylabel = tk.Label(self.searchstudent_window, text='Faculty', font=('times new roman', 15, 'bold'))
        Facultylabel.grid(row=9, column=0, padx=10, pady=10)
        Facultyentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Facultyentry.grid(row=9, column=1, padx=10, pady=10)

        Emaillabel = tk.Label(self.searchstudent_window, text='Email', font=('times new roman', 15, 'bold'))
        Emaillabel.grid(row=10, column=0, padx=10, pady=10)
        Emailentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Emailentry.grid(row=10, column=1, padx=10, pady=10)

        phonelabel = tk.Label(self.searchstudent_window, text='phone', font=('times new roman', 15, 'bold'))
        phonelabel.grid(row=11, column=0, padx=10, pady=10)
        phoneentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        phoneentry.grid(row=11, column=1, padx=10, pady=10)

        buttonsearchstudent = tk.Button(self.searchstudent_window, text='Search', bg='#173662', fg='white',command=searchStd,
                                     font=('times new roman', 15, 'bold'))
        buttonsearchstudent.grid(row=13, columnspan=3, pady=10, padx=10)


    def clock(self):
        self.date=time.strftime('%d/%m/%Y')
        self.currenttime=time.strftime('%H:%M:%S')
        print(self.currenttime,self.date)

    def confirm(self):
        def confirmation():
            try:
                while self.userentry.get()!='project' or self.password1entry.get()!='1234':
                    messagebox.showerror('INVALID INPUT','ACCESS DENIED!')
                    self.main_window2.destroy()
                    return
                else:
                    self.main_window2.destroy()

                    self.add_but.configure(state=NORMAL)
                    self.search2_but.configure(state=NORMAL)
                    self.delete_but.configure(state=NORMAL)
                    self.update_but.configure(state=NORMAL)
                    self.show_but.configure(state=NORMAL)
                    self.export_but.configure(state=NORMAL)
                    self.firstcon.configure(text='connected', fg_color='green',command=self.home)
                    messagebox.showinfo('SUCCESS','ACCESS GRANTED')

                    query = 'select *from student'
                    self.mycursor.execute(query)
                    self.fecthed_data = self.mycursor.fetchall()
                    self.tree.delete(*self.tree.get_children())
                    for data in self.fecthed_data:
                        datalist = list(data)
                        self.tree.insert('', END, values=datalist)
            except:
                   messagebox.showerror('error', 'invalid input')




        self.main_window2 = tk.Tk()
        self.main_window2.grab_set()
        self.main_window2.title('School MAnagement System')
        self.main_window2.geometry('500x270+600+200')
        self.main_window2.config(bg='white')
        self.main_window2.resizable(False, False)

        checkin = tk.Label(self.main_window2, text='ARE YOU AN ADMIN?',
                           font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
        checkin.grid(row=0, columnspan=3, padx=50, pady=20)

        self.userlabel = tk.Label(self.main_window2, text='USER_ID', bg='white', font=('times new roman', 15, 'bold'))
        self.userlabel.grid(row=1, column=0, padx=10, pady=10)
        self.userentry = tk.Entry(self.main_window2, width=25, font=('times new roman', 15, 'bold'))
        self.userentry.grid(row=1, column=1, padx=10, pady=10)

        self.password1label = tk.Label(self.main_window2, text='PIN', bg='white',
                                      font=('times new roman', 15, 'bold'))
        self.password1label.grid(row=2, column=0, padx=10, pady=10)
        self.password1entry = tk.Entry(self.main_window2, width=25, font=('times new roman', 15, 'bold'))
        self.password1entry.grid(row=2, column=1, padx=10, pady=10)

        self.comfirmbut = tk.Button(self.main_window2 , text='connect', bg='#173662', fg='white', command=confirmation,
                                     font=('times new roman', 15, 'bold'))
        self.comfirmbut.grid(row=3, columnspan=4, pady=10, padx=10)


    def display(self):
        self.destroymain()

        #self.button_Home.configure(fg_color='#276878')
        self.largeframe = ctk.CTkFrame(self.mainframe1, fg_color='#ECEBE9', width=1400,
                                       height=680, corner_radius=10, border_color='#173662',
                                       border_width=0)
        self.largeframe.place(relx=0.5, rely=0.5)
        self.largeframe.pack(pady=0, padx=0, fill=BOTH)
        # labeltop2 = ctk.CTkLabel(self.main_window, text='Academics excellence and power', font=('Ariel', 10),
        # text_color='white', fg_color='#173662',corner_radius=4)
        # labeltop2.place(relx=0.55, rely=0.001)
        print('check4')
        # top frame
        self.top_frame = ctk.CTkFrame(self.largeframe, fg_color='white', width=1020,
                                      height=25, corner_radius=5,
                                      )
        self.top_frame.pack(side=TOP, pady=15, ipady=10, fill=X)
        print('chek5')
        # small frames

        self.smallframe1 = ctk.CTkFrame(self.largeframe, fg_color='white', width=200,
                                        height=80, corner_radius=10,
                                        )
        # smallframe1.grid(relx=0.01, rely=0.1)

        self.smallframe2 = ctk.CTkFrame(self.largeframe, fg_color='white', width=200,
                                        height=80, corner_radius=10,
                                        )
        self.smallframe3 = ctk.CTkFrame(self.largeframe, fg_color='white', width=200,
                                        height=80, corner_radius=10,
                                        )
        self.smallframe4 = ctk.CTkFrame(self.largeframe, fg_color='white', width=200,
                                        height=80, corner_radius=10,
                                        )


        self.smallframe1.pack(side=LEFT, padx=0, expand=True, ipadx=10)
        self.smallframe2.pack(side=LEFT, padx=10, expand=True, ipadx=20)
        self.smallframe3.pack(side=LEFT, padx=10, expand=True, ipadx=20)
        self.smallframe4.pack(side=LEFT, padx=0, expand=True, ipadx=10)

        self.largeframe2 = ctk.CTkFrame(self.mainframe1, fg_color='#ecebe9', width=680,
                                        height=600, corner_radius=10, border_color='#173662',
                                        border_width=0)
        self.largeframe2.place(relx=0.26, rely=0.35)
        self.largeframe2.pack(side=LEFT, padx=2, pady=5)

        self.smallframe5A = ctk.CTkFrame(self.largeframe2, fg_color='white', width=320,
                                         height=250, corner_radius=10,
                                         )
        self.smallframe6A = ctk.CTkScrollableFrame(self.mainframe1, fg_color='white', width=370,
                                                   height=500, corner_radius=10, orientation='vertical',
                                                   scrollbar_button_color='#276878',
                                                   scrollbar_button_hover_color='#173662')
        self.smallframe7A = ctk.CTkFrame(self.largeframe2, fg_color='white', width=320,
                                         height=250, corner_radius=10,
                                         )
        self.smallframe8A = ctk.CTkFrame(self.largeframe2, fg_color='white', width=600,
                                         height=250, corner_radius=10,
                                         )

        self.smallframe8A.place(relx=0.01, rely=0.01)
        # smallframe6A.place(relx=0.7, rely=0.01)
        self.smallframe5A.place(relx=0.15, rely=1, anchor='s')
        self.smallframe7A.place(relx=0.4, rely=0.5, anchor='s')

        self.smallframe8A.pack(fill=X, pady=10)
        self.smallframe6A.pack(side=LEFT, padx=8, pady=5)
        # self.scrollbar=ctk.CTkScrollbar(self.smallframe6A)
        # self.scrollbar.pack(side='left', fill='y')
        # self.scrollbar.config(command=self.smallframe6A.yview)
        # self.smallframe6A.configure(yscrollcommand=self.scrollbar.set)
        self.smallframe5A.pack(side=RIGHT, pady=2, padx=5)
        self.smallframe7A.pack(side=RIGHT, pady=0, padx=0, ipadx=20)
        print('check6')
        # labels and widget
        labeltopframe = ctk.CTkLabel(self.top_frame, text='DASHBOARD', font=('Helvetica', 20),
                                     text_color='#173662', fg_color='WHITE', corner_radius=4)
        labeltopframe.place(relx=0.01, rely=0.1)

        self.labeltopframeENTRY = ctk.CTkEntry(self.top_frame, placeholder_text='search for student with matric number',
                                               width=500, height=30,
                                               text_color='#090a06', corner_radius=15,
                                               border_color='#ecebe9', font=('Ariel', 10))
        self.labeltopframeENTRY.place(relx=0.2, rely=0.2)

        self.searchicon = Image.open('images/search1.png')

        # self.searchicon  = ImageTk.PhotoImage(self.searchicon)

        searchtop = ctk.CTkButton(self.top_frame, text='',
                                  fg_color='#ecebe9', command=self.home,
                                  image=ctk.CTkImage(self.image_butsearch), width=20, height=20
                                  )
        searchtop.place(relx=0.62, rely=0.25)

        self.noticon = Image.open('images/notification3.png')

        # self.noticon = ImageTk.PhotoImage(self.noticon)

        notitop = ctk.CTkButton(self.top_frame, text='',
                                fg_color='white', command=self.home,
                                image=ctk.CTkImage(self.noticon), width=25, height=25,
                                )
        notitop.place(relx=0.78, rely=0.1)

        self.topcon = ctk.CTkButton(self.top_frame, text='Connect',
                               fg_color='#173662', command=self.connectDatabase,
                               width=100, height=40, text_color= 'white',
                               )
        self.topcon.place(relx=0.85, rely=0.12)
        #the correct command=self.self.connectDatabase

        # searchtop.pack(side=RIGHT,padx=350)

        # self.labelphotoframe = ctk.CTkFrame(self.top_frame, fg_color='blue', width=50,
        # height=25, corner_radius=30,radius=3
        # )
        # self.labelphotoframe.place(relx=0.9,rely=0.2)
        print('check8')
        # first small frame

        self.smallframeimage1 = Image.open('images/studying1.png')

        self.smallframeimage1 = ImageTk.PhotoImage(self.smallframeimage1)
        self.small1label = tk.Label(self.smallframe1, image=self.smallframeimage1, bg='white')
        self.small1label.place(relx=0.1, rely=0.1)
        smalll1label2 = ctk.CTkLabel(self.smallframe1, text='Students', font=('Ariel', 10),
                                     text_color='#242818', fg_color='white', corner_radius=4)
        smalll1label2.place(relx=0.37, rely=0.1)

        smalll1label3 = ctk.CTkLabel(self.smallframe1, text='12,765', font=('Helvetica', 30),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smalll1label3.place(relx=0.35, rely=0.45)
        print('check9')
        # second small frame
        self.smallframeimage2 = Image.open('images/teacher1.png')

        self.smallframeimage2 = ImageTk.PhotoImage(self.smallframeimage2)
        self.small2label = tk.Label(self.smallframe2, image=self.smallframeimage2, bg='white')
        self.small2label.place(relx=0.1, rely=0.1)
        smalll2label2 = ctk.CTkLabel(self.smallframe2, text='Lecturers', font=('Ariel', 10),
                                     text_color='#242818', fg_color='white', corner_radius=4)
        smalll2label2.place(relx=0.37, rely=0.1)

        smalll1label3 = ctk.CTkLabel(self.smallframe2, text='108', font=('Helvetica', 30),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smalll1label3.place(relx=0.35, rely=0.45)
        print('check10')
        # third frame
        self.smallframeimage3 = Image.open('images/379383_student_icon.png')

        self.smallframeimage3 = ImageTk.PhotoImage(self.smallframeimage3)
        self.small3label = tk.Label(self.smallframe3, image=self.smallframeimage3, bg='white')
        self.small3label.place(relx=0.1, rely=0.1)
        smalll3label2 = ctk.CTkLabel(self.smallframe3, text='Graduates', font=('Ariel', 10),
                                     text_color='#242818', fg_color='white', corner_radius=4)
        smalll3label2.place(relx=0.37, rely=0.1)

        smalll3label3 = ctk.CTkLabel(self.smallframe3, text='32,762', font=('Helvetica', 30),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smalll3label3.place(relx=0.35, rely=0.45)
        print('check11')
        # fourth frame
        self.smallframeimage4 = Image.open('images/books (1).png')

        self.smallframeimage4 = ImageTk.PhotoImage(self.smallframeimage4)
        self.small4label = tk.Label(self.smallframe4, image=self.smallframeimage4, bg='white')
        self.small4label.place(relx=0.1, rely=0.1)
        smalll4label2 = ctk.CTkLabel(self.smallframe4, text='Courses', font=('Ariel', 10),
                                     text_color='#242818', fg_color='white', corner_radius=4)
        smalll4label2.place(relx=0.37, rely=0.1)

        smalll4label3 = ctk.CTkLabel(self.smallframe4, text='620', font=('Helvetica', 30),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smalll4label3.place(relx=0.35, rely=0.45)
        print('check12')
        #self.draw_bar_chart()
        print('check13')
        #self.draw_pie_chart()

       # self.display_calendar()

    def changeThis(self):
        messagebox.showerror('Error','database connection disrupted x1bxx000cggi000sllchg')
    def get_top_students(self, level, department, top_n=3):

        # Define the query to fetch the top 3 students by CGPA in the specified level and department
        query = """
                       SELECT * FROM student
                       WHERE Level = %s AND Department = %s
                       ORDER BY Status DESC
                       LIMIT %s
                       """

        # Execute the query with the given level and department
        self.mycursor.execute(query, (level, department, top_n))

        # Fetch the results
        top_students = self.mycursor.fetchall()
        print('did you execute up to here')
        if len(top_students) < 3:
            messagebox.showinfo('Error','Data not Available')
            self.smallwindow.destroy()
        else:
           return top_students

    def get_top_students2(self,department, top_n=3):

        # Define the query to fetch the top 3 students by CGPA in the specified level and department
        query = """
                       SELECT * FROM student
                       WHERE  Department = %s
                       ORDER BY Status DESC
                       LIMIT %s
                       """

        # Execute the query with the given level and department
        self.mycursor.execute(query, ( department, top_n))

        # Fetch the results
        top_students = self.mycursor.fetchall()
        #print('did you execute up to here')
        if len(top_students) < 3:
            messagebox.showinfo('Error', 'Data not Available')
            self.smallwindow.destroy()
        else:
            return top_students


    def get_top_students3(self, faculty, top_n=3):

        # Define the query to fetch the top 3 students by CGPA in the specified level and department
        query = """
                       SELECT * FROM student
                       WHERE Faculty = %s
                       ORDER BY Status DESC
                       LIMIT %s
                       """

        # Execute the query with the given level and department
        self.mycursor.execute(query, (faculty,top_n))

        # Fetch the results
        top_students = self.mycursor.fetchall()
        print('did you execute up to here')
        if len(top_students) < 3:
            messagebox.showinfo('Error', 'Data not Available')
            self.smallwindow.destroy()
        else:
            return top_students

    def get_top_students4(self, top_n=3):

        # Define the query to fetch the top 3 students by CGPA in the specified level and department
        query = """
                       SELECT * FROM student
                       ORDER BY Status DESC
                       LIMIT %s
                       """

        # Execute the query with the given level and department
        self.mycursor.execute(query, (top_n))

        # Fetch the results
        top_students = self.mycursor.fetchall()
        print('did you execute up to here')

        return top_students

    # Output the full information of the top 3 students
    def display_students(self, students):
        # Display the full information of the students
        print('why are you not working')
        for i, student in enumerate(students, start=1):
            print(f"Top {i} Student:")
            for field, value in zip([column[0] for column in self.mycursor.description], student):
                print(f"{field}: {value}")
            print()

    def display_students1(self, students):
        # Display the full information of the students
        for i, student in enumerate(students, start=1):
            print(f"Top {i} Student:")
            matric_no, surname, name, dob, department, gender, level, grade, status, faculty, email, phone_no, time, date = student
            print(f"Matric_no: {matric_no}")
            print(f"Surname: {surname}")
            print(f"Name: {name}")
            print(f"DOB: {dob}")
            print(f"Department: {department}")
            print(f"Gender: {gender}")
            print(f"Level: {level}")
            print(f"Grade: {grade}")
            print(f"Status: {status}")
            print(f"Faculty: {faculty}")
            print(f"Email: {email}")
            print(f"Phone_No: {phone_no}")
            print(f"Time: {time}")
            print(f"Date: {date}")
            print()

    def topsearch(self):
        def okay():
            self.labeltopframeENTRY.delete(0,END)
            self.smallwindow.destroy()

        query = 'select *from student where Matric_no=%s'
        self.mycursor.execute(query,
        self.labeltopframeENTRY.get())
        fetched_data = self.mycursor.fetchall()
        print(fetched_data)
        if self.mycursor.fetchall() is NONE:
            messagebox.showinfo('Opps', 'No Data Found')
        else:
            for data in fetched_data:
                datalist = list(data)
                #self.tree.insert('', END, values=datalist)
                print(datalist)
                surname=datalist[1]
                name = datalist[2]
                dept=datalist[4]
                level = datalist[6]
                grade = datalist[7]
                cgpa = datalist[8]
                faculty=datalist[9]
                email=datalist[10]
                number=datalist[11]
        self.smallwindow = tk.Tk()
        self.smallwindow.grab_set()
        self.smallwindow.title('School MAnagement System')
        self.smallwindow.geometry('400x550+600+100')
        self.smallwindow.config(bg='white')
        self.smallwindow.resizable(False, False)

        show = tk.Label(self.smallwindow, text='STUDENT INFORMATION',
                           font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
        show.grid(row=0, columnspan=3, padx=50, pady=10)

        surname = tk.Label(self.smallwindow, text=f"SURNAME:   {surname}",
                        font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
        surname.grid(row=1, columnspan=2, padx=20, pady=5,sticky='w')

        name = tk.Label(self.smallwindow, text=f"NAME:   {name}",
                           font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
        name.grid(row=2, columnspan=2, padx=20, pady=5,sticky='w')

        dept= tk.Label(self.smallwindow, text=f"DEPT:   {dept}",
                        font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
        dept.grid(row=3, columnspan=2, padx=20, pady=5,sticky='w')

        level = tk.Label(self.smallwindow, text=f"LEVEL:   {level}",
                        font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
        level.grid(row=4, columnspan=2, padx=20, pady=10,sticky='w')

        status = tk.Label(self.smallwindow, text=f"CGPA:   {cgpa}",
                         font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
        status.grid(row=5, columnspan=2, padx=20, pady=10,sticky='w')

        cgpa = tk.Label(self.smallwindow, text=f"Grade:   {grade}",
                        font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
        cgpa.grid(row=6, columnspan=2, padx=20, pady=5,sticky='w')

        FACULTY = tk.Label(self.smallwindow, text=f"Faculty:   {faculty}",
                        font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
        FACULTY.grid(row=7, columnspan=2, padx=20, pady=5, sticky='w')

        email = tk.Label(self.smallwindow, text=f"Email:   {email}",
                           font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
        email.grid(row=8, columnspan=2, padx=20, pady=5, sticky='w')

        number = tk.Label(self.smallwindow, text=f"Phone_no:   {number}",
                         font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
        number.grid(row=9, columnspan=2, padx=20, pady=20, sticky='w')

        okayseen = tk.Button(self.smallwindow, text='OK', bg='GREEN', fg='white',
                                        command=okay,
                                        font=('times new roman', 15, 'bold'))
        okayseen.grid(row=10, columnspan=3, padx=20, pady=5,)

    def delete_student(self):
        index=self.tree.focus()
        content=self.tree.item(index)
        data_matric=content['values'][0]
        print(data_matric)

        query='DELETE FROM student WHERE Matric_no=%s'
        self.mycursor.execute(query,data_matric)

        result=messagebox.askyesno('Comfirmation','Are You Sure You Want To Delete')
        if result:
            self.con.commit()
            messagebox.showinfo('Success','Data Successfully deleted!')
            self.showstudent()
        else:
            pass


    def export(self):
        url = filedialog.asksaveasfilename(defaultextension='.csv')
        print(url)
        indexing = self.tree.get_children()
        newList = []
        for index in indexing:
            content = self.tree.item(index)['values']
            newList.append(content)
        print(newList)
        # Create a DataFrame
        columns = ['Matric_no', 'Surname', 'Name', 'DOB', 'Department', 'Gender', 'Level', 'Grade', 'Status', 'Faculty',
                   'Email', 'Phone_No', 'Time', 'Date']
        df = pd.DataFrame(newList, columns=columns)
        print(df)
        # Save to CSV without the index
        df.to_csv(url, index=False)

        # Show success message
        messagebox.showinfo('success', 'Data Successfully Saved')

    def draw_scatter_plot(self):



        # Fetch data from the student table
        self.mycursor.execute("SELECT Matric_no, Status FROM student")
        data = self.mycursor.fetchall()



        # Extract matric numbers and CGPA from the fetched data
        matric_no = [row[0] for row in data]
        cgpa = [row[1] for row in data]

        # Create a scatter plot
        fig, ax = plt.subplots(figsize=(4, 2.5))
        ax.scatter(matric_no, cgpa, color='blue')
        ax.set_title('Scatter Plot of Students vs CGPA')
        ax.set_xlabel('Students')
        ax.set_ylabel('CGPA')

        ax.set_xticks([])

        # Embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.smallframe5A)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)



if __name__ == "__main__":
    app = App()
    app.start()

