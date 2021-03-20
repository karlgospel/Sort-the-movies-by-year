#!/usr/bin/env python3

from tkinter import ttk
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import Listbox
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from os import path
from tkinter import Menu
import tkinter.scrolledtext
import pandas as pd
from pathlib import Path
import random 
from PIL import Image, ImageTk
import easygui as eg

Path('sorting_game.db').touch()
###This code allows to print first name from databsase after clicking on button

def connect():
    conn = sqlite3.connect("sorting_game.db")
    cur = conn.cursor()

    print (pd.read_sql("SELECT * FROM movie_data", conn))
    conn.commit()
    conn.close()



class Leaderboard():
    
    def createLeaderboardTable(self):
    
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        
        #cur.execute("DROP TABLE IF EXISTS jobAndMaterials")
        # cur.execute("CREATE TABLE IF NOT EXISTS leaderboard(ID INTEGER PRIMARY KEY AUTOINCREMENT, name, difficulty, score)")
        
        cur.execute("CREATE TABLE IF NOT EXISTS easyLeaderboard(ID INTEGER PRIMARY KEY AUTOINCREMENT, name, score)")
        cur.execute("CREATE TABLE IF NOT EXISTS intermediateLeaderboard(ID INTEGER PRIMARY KEY AUTOINCREMENT, name, score)")
        cur.execute("CREATE TABLE IF NOT EXISTS hardLeaderboard(ID INTEGER PRIMARY KEY AUTOINCREMENT, name, score)")
        cur.execute("CREATE TABLE IF NOT EXISTS insaneLeaderboard(ID INTEGER PRIMARY KEY AUTOINCREMENT, name, score)")
        cur.execute("CREATE TABLE IF NOT EXISTS impossibleLeaderboard(ID INTEGER PRIMARY KEY AUTOINCREMENT, name, score)")

        conn.commit()
        conn.close()
        
    def refreshLeaderboards(self, user):
        
        #get currently selected difficulty 
        difficulty = q.difficulty
        print("The difficulty is")
        print(difficulty)
        if difficulty == 1:
            self.updateEasyLeaderboard(user)
        elif difficulty == 2:
            self.updateIntermediateLeaderboard(user)
        elif difficulty == 3:
            self.updateHardLeaderboard(user)
        elif difficulty == 4:
            self.updateInsaneLeaderboard(user)
        elif difficulty == 5:
            self.updateImpossibleLeaderboard(user)
        self.populateLeaderboard()
        
    def updateEasyLeaderboard(self, user):
        
        score = q.level
        user_name = user
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()

        details = (user_name, score)
        sql = ''' INSERT INTO easyLeaderboard(name, score)
        VALUES(?,?) '''
        cur.execute(sql, details)
        conn.commit()
        conn.close()
        
        
    def updateIntermediateLeaderboard(self, user):

        score = q.level
        user_name = user
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()

        details = (user_name, score)
        sql = ''' INSERT INTO intermediateLeaderboard(name, score)
        VALUES(?,?) '''
        cur.execute(sql, details)
        conn.commit()
        conn.close()
        
        
    def updateHardLeaderboard(self, user):
        
        #get currently selected difficulty 
        difficulty = q.difficulty
        score = q.level
        user_name = user
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()

        details = (user_name, score)
        sql = ''' INSERT INTO hardLeaderboard(name, score)
        VALUES(?,?) '''
        cur.execute(sql, details)
        conn.commit()
        conn.close()
        
        
    def updateInsaneLeaderboard(self, user):
        #get currently selected difficulty 
        difficulty = q.difficulty
        score = q.level
        user_name = user
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()

        details = (user_name, score)
        sql = ''' INSERT INTO insaneLeaderboard(name, score)
        VALUES(?,?) '''
        cur.execute(sql, details)
        conn.commit()
        conn.close()
        
        
    def updateImpossibleLeaderboard(self,user):
        #get currently selected difficulty 
        difficulty = q.difficulty
        score = q.level
        user_name = user
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()

        details = (user_name, score)
        sql = ''' INSERT INTO impossibleLeaderboard(name, score)
        VALUES(?,?) '''
        cur.execute(sql, details)
        conn.commit()
        conn.close()
        
        
    
    def getEasyLeaderboard(self):
        """ Gets the name and scores of the easy difficulty leaderboard
        
        Returns
        ----------
        List
            A list of leaderboard results
            
        """
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        sql =("SELECT name, score FROM easyLeaderboard")
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit
        conn.close
        return (result)
    
    
    
    def getIntermediateLeaderboard(self):
        """ Gets the name and scores of the intermediate difficulty leaderboard
        
        Returns
        ----------
        List
            A list of leaderboard results
            
        """
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        sql =("SELECT name, score FROM intermediateLeaderboard")
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit
        conn.close
        return (result)
    
    def getHardLeaderboard(self):
        """ Gets the name and scores of the hard difficulty leaderboard
        
        Returns
        ----------
        List
            A list of leaderboard results
            
        """
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        sql =("SELECT name, score FROM hardLeaderboard")
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit
        conn.close
        return (result)
    
    def getInsaneLeaderboard(self):
        """ Gets the name and scores of the insane difficulty leaderboard
        
        Returns
        ----------
        List
            A list of leaderboard results
            
        """
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        sql =("SELECT name, score FROM insaneLeaderboard")
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit
        conn.close
        return (result)
    
    def getImpossibleLeaderboard(self):
        """ Gets the name and scores of the impossible difficulty leaderboard
        
        Returns
        ----------
        List
            A list of leaderboard results
            
        """
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        sql =("SELECT name, score FROM impossibleLeaderboard")
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit
        conn.close
        return (result)

    def populateLeaderboard(self):
        """ Populates the leaderboards"""
        
        easy_scores = self.getEasyLeaderboard()
        easy_leaderboard.delete(*easy_leaderboard.get_children())
        for each in easy_scores:
            easy_leaderboard.insert("",END,values=each)
            
        intermediate_scores = self.getIntermediateLeaderboard()
        intermediate_leaderboard.delete(*intermediate_leaderboard.get_children())
        for each in intermediate_scores:
            intermediate_leaderboard.insert("",END,values=each)
            
        hard_scores = self.getHardLeaderboard()
        hard_leaderboard.delete(*hard_leaderboard.get_children())
        for each in hard_scores:
            hard_leaderboard.insert("",END,values=each)
            
        insane_scores = self.getInsaneLeaderboard()
        insane_leaderboard.delete(*insane_leaderboard.get_children())
        for each in insane_scores:
            insane_leaderboard.insert("",END,values=each)
            
        impossible_scores = self.getImpossibleLeaderboard()
        impossible_leaderboard.delete(*impossible_leaderboard.get_children())
        for each in impossible_scores:
            impossible_leaderboard.insert("",END,values=each)
        
        
class DragDropListbox(tkinter.Listbox):
    """ A Tkinter listbox with drag'n'drop reordering of entries. """
    def __init__(self, master, **kw):
        kw['selectmode'] = tk.SINGLE
        tk.Listbox.__init__(self, master, kw)
        self.bind('<Button-1>', self.setCurrent)
        self.bind('<B1-Motion>', self.shiftSelection)
        self.curIndex = None

    def setCurrent(self, event):
        self.curIndex = self.nearest(event.y)

    def shiftSelection(self, event):
        i = self.nearest(event.y)
        if i < self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i+1, x)
            self.curIndex = i
        elif i > self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i-1, x)
            self.curIndex = i
            
class Questions():
    

    level = 1
    lives = 3
    current_movie_choices = []
    correct_guesses = 0
    difficulty = ""
    player = ""


    def reset_game(self, ):
        #q = Questions()
        score_box.config(state='normal')
        score_box.delete(0,tk.END)
        score_box.insert(0,0)
        score_box.config(state='readonly')
        listbox.delete(0,tk.END)
        level_var.set(1)
        lives_var.set(self.lives)

        # movie_choices = q.start_easy_game()
        
    def new_game(self ):
        answer = messagebox.askyesno("New Game","Are you sure? All current game progress will be lost")
        if answer == True:
            pass
        else:
            return
        q.reset_game()
        # self.level = 1
        # self.lives = 3
        # self.current_movie_choices = []
        # self.correct_guesses = 0
        listbox.delete(0,tk.END)
        level_var.set(1)
        lives_var.set(3)
        level_choice = difficultyVar.get()
        self.difficulty = level_choice
        if level_choice == 1:
         movie_choices = q.start_easy_game()
         for title, year in movie_choices:
           listbox.insert(tk.END, title)
           
        elif level_choice == 2:
         movie_choices = q.start_intermediate_game()
         for title, year in movie_choices:
           listbox.insert(tk.END, title)
           
        elif level_choice == 3:
         movie_choices = q.start_hard_game()
         for title, year in movie_choices:
           listbox.insert(tk.END, title)
           
        elif level_choice == 4:
         movie_choices = q.start_insane_game()
         for title, year in movie_choices:
           listbox.insert(tk.END, title)
           
        elif level_choice == 5:
         movie_choices = q.start_impossible_game()
         for title, year in movie_choices:
           listbox.insert(tk.END, title)
           
        print("----original list of movies----")
        print(movie_choices)
    
    # def reset_game(self ):
    #     # self.level = 1
    #     # self.lives = 3
    #     # self.current_movie_choices = 
    #     # self.correct_guesses = 0
    #     listbox.delete(0,tk.END)
    #     level_var.set(1)
    #     lives_var.set(3)
    #     movie_choices = q.start_easy_game()
    #     q.reset_game()
    # 
    #     for title, year in movie_choices:
    #       listbox.insert(tk.END, title)
    # 
    #     print("----original list of movies----")
    #     print(movie_choices)
    
    def show_movies(self):
       
        listbox.delete(0,tk.END)
        movie_choices = q.start_easy_game()

        for title, year in movie_choices:
          listbox.insert(tk.END, title)

        print("----original list of movies----")
        print(movie_choices)
        # check_answers_button = Button(root, text= 'Submit', command=lambda : Questions.checkAnswers(), width=7)
        # check_answers_button.grid(column=3, row = , padx=0, pady=0)
    
    def getPrediction(self):
        predictions = listbox.get(0,tk.END)
        print("----predictions----")
        print(predictions)
        return predictions
    
    def start_easy_game(self):
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        unique_years = False
        movies = []
        list_length = 0

        while list_length < 5:
          rand_numbers = random.sample(range(1,300), 5)
          cur.execute("SELECT title,year FROM movie_data WHERE id IN (?,?,?,?,?)", rand_numbers)
          movie_choices = cur.fetchall()
          #movie_choices = [('Stardust', 2007), ('Princess Mononoke', 1997), ('L.A. Confidential', 1997), ('Like Stars on Earth', 2007), ('Barton Fink', 1991)]
          # print("The set of movies")
          # print(set(movies))
          for i in movie_choices:
            movies.append(i[1])
          list_length = len(set(movies))
        #print(movie_choices)
        #answers = movie_choices
        self.current_movie_choices = movie_choices
        print("----current movie choices-----")
        print(self.current_movie_choices)
        #answ = cur.fetchall()
        #print(answ)
        # total = total[0]
        conn.commit()
        conn.close()
        return movie_choices
    
    def start_intermediate_game(self):
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        unique_years = False
        movies = []
        list_length = 0

        while list_length < 5:
          rand_numbers = random.sample(range(1,500), 5)
          cur.execute("SELECT title,year FROM movie_data WHERE id IN (?,?,?,?,?)", rand_numbers)
          movie_choices = cur.fetchall()
          #movie_choices = [('Stardust', 2007), ('Princess Mononoke', 1997), ('L.A. Confidential', 1997), ('Like Stars on Earth', 2007), ('Barton Fink', 1991)]
          # print("The set of movies")
          # print(set(movies))
          for i in movie_choices:
            movies.append(i[1])
          list_length = len(set(movies))
        #print(movie_choices)
        #answers = movie_choices
        self.current_movie_choices = movie_choices
        print("----current movie choices-----")
        print(self.current_movie_choices)
        #answ = cur.fetchall()
        #print(answ)
        # total = total[0]
        conn.commit()
        conn.close()
        return movie_choices
       
    def start_hard_game(self):
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        unique_years = False
        movies = []
        list_length = 0

        while list_length < 5:
          rand_numbers = random.sample(range(1,700), 5)
          cur.execute("SELECT title,year FROM movie_data WHERE id IN (?,?,?,?,?)", rand_numbers)
          movie_choices = cur.fetchall()
          #movie_choices = [('Stardust', 2007), ('Princess Mononoke', 1997), ('L.A. Confidential', 1997), ('Like Stars on Earth', 2007), ('Barton Fink', 1991)]
          # print("The set of movies")
          # print(set(movies))
          for i in movie_choices:
            movies.append(i[1])
          list_length = len(set(movies))
        #print(movie_choices)
        #answers = movie_choices
        self.current_movie_choices = movie_choices
        print("----current movie choices-----")
        print(self.current_movie_choices)
        #answ = cur.fetchall()
        #print(answ)
        # total = total[0]
        conn.commit()
        conn.close()
        return movie_choices
       
    def start_insane_game(self):
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        unique_years = False
        movies = []
        list_length = 0

        while list_length < 5:
          rand_numbers = random.sample(range(1,1000), 7)
          cur.execute("SELECT title,year FROM movie_data WHERE id IN (?,?,?,?,?,?,?)", rand_numbers)
          movie_choices = cur.fetchall()
          #movie_choices = [('Stardust', 2007), ('Princess Mononoke', 1997), ('L.A. Confidential', 1997), ('Like Stars on Earth', 2007), ('Barton Fink', 1991)]
          # print("The set of movies")
          # print(set(movies))
          for i in movie_choices:
            movies.append(i[1])
          list_length = len(set(movies))
        #print(movie_choices)
        #answers = movie_choices
        self.current_movie_choices = movie_choices
        print("----current movie choices-----")
        print(self.current_movie_choices)
        #answ = cur.fetchall()
        #print(answ)
        # total = total[0]
        conn.commit()
        conn.close()
        return movie_choices
       
    def start_impossible_game(self):
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        unique_years = False
        movies = []
        list_length = 0

        while list_length < 5:
          rand_numbers = random.sample(range(1,1000), 10)
          cur.execute("SELECT title,year FROM movie_data WHERE id IN (?,?,?,?,?,?,?,?,?,?)", rand_numbers)
          movie_choices = cur.fetchall()
          #movie_choices = [('Stardust', 2007), ('Princess Mononoke', 1997), ('L.A. Confidential', 1997), ('Like Stars on Earth', 2007), ('Barton Fink', 1991)]
          # print("The set of movies")
          # print(set(movies))
          for i in movie_choices:
            movies.append(i[1])
          list_length = len(set(movies))
        #print(movie_choices)
        #answers = movie_choices
        self.current_movie_choices = movie_choices
        print("----current movie choices-----")
        print(self.current_movie_choices)
        #answ = cur.fetchall()
        #print(answ)
        # total = total[0]
        conn.commit()
        conn.close()
        return movie_choices
    
    def getResults(self):
        if self.difficulty == 1 or 2 or 3:
            self.checkAnswers()
        elif self.difficulty == 4:
            self.checkInsaneAnswers()
        elif self.difficulty == 5:
            self.checkImpossibleAnswers()
            
    def checkAnswers(self):
        correct_guesses = 0
        movie_predictions = q.getPrediction()
        print("----user guess----")
        print(movie_predictions)
        correct_order = sorted(self.current_movie_choices, key=lambda x: x[1])
        print("----correct order----")
        print(correct_order)
        for i in correct_order:
            if i[0] == movie_predictions[(correct_order.index(i))]:
              correct_guesses +=1
        if correct_guesses == 5:
          self.level +=1
          level_box.config(state='normal')
          level_box.delete(0,tk.END)
          level_box.insert(0,self.level)
          level_box.config(state='readonly')
          q.show_movies()
        else:
          self.lives -= 1
          lives_box.config(state='normal')
          lives_box.delete(0,tk.END)
          lives_box.insert(0,self.lives)
          lives_box.config(state='readonly')
        if self.lives == 0:
            #tk.messagebox.showinfo("Game Over", "You reached level " + str(self.level))
            msg = "Submit score to leaderboard"
            title = "Game Over"
            field_name = "Name"
            #fieldValues = []  # we start with blanks for the values
            user_name = eg.enterbox(msg,title, field_name)
            self.player = user_name
            lead.refreshLeaderboards(user_name)
            # Leaderboard.getEasyLeaderboard()
            q.reset_game()

    def checkInsaneAnswers(self):
        correct_guesses = 0
        movie_predictions = q.getPrediction()
        print("----user guess----")
        print(movie_predictions)
        correct_order = sorted(self.current_movie_choices, key=lambda x: x[1])
        print("----correct order----")
        print(correct_order)
        for i in correct_order:
            if i[0] == movie_predictions[(correct_order.index(i))]:
              correct_guesses +=1
        if correct_guesses == 7:
          self.level +=1
          level_box.config(state='normal')
          level_box.delete(0,tk.END)
          level_box.insert(0,self.level)
          level_box.config(state='readonly')
          q.show_movies()
        else:
          self.lives -= 1
          lives_box.config(state='normal')
          lives_box.delete(0,tk.END)
          lives_box.insert(0,self.lives)
          lives_box.config(state='readonly')
        if self.lives == 0:
            #tk.messagebox.showinfo("Game Over", "You reached level " + str(self.level))
            msg = "Submit score to leaderboard"
            title = "Game Over"
            field_name = "Name"
            #fieldValues = []  # we start with blanks for the values
            user_name = eg.enterbox(msg,title, field_name)
            self.player = user_name
            lead.refreshLeaderboards(user_name)
            # Leaderboard.getEasyLeaderboard()
            q.reset_game()


    def checkImpossibleAnswers(self):
        correct_guesses = 0
        movie_predictions = q.getPrediction()
        print("----user guess----")
        print(movie_predictions)
        correct_order = sorted(self.current_movie_choices, key=lambda x: x[1])
        print("----correct order----")
        print(correct_order)
        for i in correct_order:
            if i[0] == movie_predictions[(correct_order.index(i))]:
              correct_guesses +=1
        if correct_guesses == 10:
          self.level +=1
          level_box.config(state='normal')
          level_box.delete(0,tk.END)
          level_box.insert(0,self.level)
          level_box.config(state='readonly')
          q.show_movies()
        else:
          self.lives -= 1
          lives_box.config(state='normal')
          lives_box.delete(0,tk.END)
          lives_box.insert(0,self.lives)
          lives_box.config(state='readonly')
        if self.lives == 0:
            #tk.messagebox.showinfo("Game Over", "You reached level " + str(self.level))
            msg = "Submit score to leaderboard"
            title = "Game Over"
            field_name = "Name"
            #fieldValues = []  # we start with blanks for the values
            user_name = eg.enterbox(msg,title, field_name)
            self.player = user_name
            lead.refreshLeaderboards(user_name)
            # Leaderboard.getEasyLeaderboard()
            q.reset_game()
        score_box.config(state='normal')
        score_box.delete(0,tk.END)
        score_box.insert(0,correct_guesses)
        score_box.config(state='readonly')
        print("correct_guesses =  ")
        print(correct_guesses)
        
        

    
#print(Questions.start_easy_game())

# root = tk.Tk()
# listbox = DragDropListbox(root)
# for i,name in enumerate(['name'+str(i) for i in range(10)]):
#   listbox.insert(tk.END, name)
#   if i % 2 == 0:
#     listbox.selection_set(i)
# listbox.pack(fill=tk.BOTH, expand=True)
# root.mainloop()


root = tk.Tk()
root.title("Sort the Movies")
root.state('zoomed')
root.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6,7,8,9), weight=1)
root.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6,7,8,9), weight=1)
widget_color = '#b1070c'

IMAGE_PATH = 'images/cinema_curtains.png'
# WIDTH, HEIGHT = 1280, 700
pad = 3
WIDTH, HEIGHT = root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad
# root.geometry('{}x{}'.format(WIDTH, HEIGHT))
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad))
img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
lbl = tk.Label(root, image=img)
lbl.img = img  # Keep a reference in case this code put is in a function.
lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.



#Create tab control to show leaderboards
    
tabControl = ttk.Notebook(root) 
  
easy_tab = ttk.Frame(tabControl) 
intermediate_tab = ttk.Frame(tabControl) 
hard_tab = ttk.Frame(tabControl) 
insane_tab = ttk.Frame(tabControl) 
impossible_tab = ttk.Frame(tabControl) 

tabControl.add(easy_tab, text ='Easy') 
tabControl.add(intermediate_tab, text ='Intermediate')
tabControl.add(hard_tab, text ='Hard')
tabControl.add(insane_tab, text ='Insane')
tabControl.add(impossible_tab, text ='Impossible') 
tabControl.grid(column = 9, row = 5) 
  
listbox = DragDropListbox(root, height = 20, width = 60, bd = 6, bg = widget_color)
listbox.grid(column=3, row = 5)
#Create tree view list to show easy leaderboard in easy tab


leaderboard_width = 60
leaderboard_column = 5
leaderboard_row = 5
leaderboard_height = 20

easy_leaderboard= ttk.Treeview(easy_tab, column=("col1", "col2"), show='headings', height=leaderboard_height)
easy_leaderboard.heading("#1", text="Name")
easy_leaderboard.column('#1', stretch=YES, width=240)
easy_leaderboard.heading("#2", text="Level")
easy_leaderboard.column('#2', stretch=YES, width=80)
easy_leaderboard.grid(column=0, row=1, padx = 20,pady=20,rowspan=4, columnspan=2)
#Add scrollbar to jobTree
easy_leaderboard_scrollbar = Scrollbar(easy_tab)
easy_leaderboard_scrollbar.grid(column=2, row=1, sticky = 'NSW',rowspan=4)
easy_leaderboard.config(yscrollcommand = easy_leaderboard_scrollbar.set)
easy_leaderboard_scrollbar.config(command=easy_leaderboard.yview)


#Create tree view list to show intermediate leaderboard in intermediate tab

intermediate_leaderboard= ttk.Treeview(intermediate_tab, column=("col1", "col2"), show='headings', height=leaderboard_height)
intermediate_leaderboard.heading("#1", text="Name")
intermediate_leaderboard.column('#1', stretch=YES, width=160)
intermediate_leaderboard.heading("#2", text="Level")
intermediate_leaderboard.column('#2', stretch=YES, width=160)
intermediate_leaderboard.grid(column=0, row=1, padx = 20,pady=20,rowspan=4, columnspan=2)
#Add scrollbar to jobTree
intermediate_leaderboard_scrollbar = Scrollbar(intermediate_tab)
intermediate_leaderboard_scrollbar.grid(column=2, row=1, sticky = 'NSW',rowspan=4)
intermediate_leaderboard.config(yscrollcommand = intermediate_leaderboard_scrollbar.set)
intermediate_leaderboard_scrollbar.config(command=intermediate_leaderboard.yview)


#Create tree view list to show hard leaderboard in hard tab

hard_leaderboard= ttk.Treeview(hard_tab, column=("col1", "col2"), show='headings', height=leaderboard_height)
hard_leaderboard.heading("#1", text="Name")
hard_leaderboard.column('#1', stretch=YES, width=160)
hard_leaderboard.heading("#2", text="Level")
hard_leaderboard.column('#2', stretch=YES, width=160)
hard_leaderboard.grid(column=0, row=1, padx = 20,pady=20,rowspan=4, columnspan=2)
#Add scrollbar to jobTree
hard_leaderboard_scrollbar = Scrollbar(hard_tab)
hard_leaderboard_scrollbar.grid(column=2, row=1, sticky = 'NSW',rowspan=4)
hard_leaderboard.config(yscrollcommand = hard_leaderboard_scrollbar.set)
hard_leaderboard_scrollbar.config(command=hard_leaderboard.yview)


#Create tree view list to show insane leaderboard in insane tab

insane_leaderboard= ttk.Treeview(insane_tab, column=("col1", "col2"), show='headings', height=leaderboard_height)
insane_leaderboard.heading("#1", text="Name")
insane_leaderboard.column('#1', stretch=YES, width=160)
insane_leaderboard.heading("#2", text="Level")
insane_leaderboard.column('#2', stretch=YES, width=160)
insane_leaderboard.grid(column=0, row=1, padx = 20,pady=20,rowspan=4, columnspan=2)
#Add scrollbar to jobTree
insane_leaderboard_scrollbar = Scrollbar(insane_tab)
insane_leaderboard_scrollbar.grid(column=2, row=1, sticky = 'NSW',rowspan=4)
insane_leaderboard.config(yscrollcommand = insane_leaderboard_scrollbar.set)
insane_leaderboard_scrollbar.config(command=insane_leaderboard.yview)


#Create tree view list to show impossible leaderboard in impossible tab

impossible_leaderboard= ttk.Treeview(impossible_tab, column=("col1", "col2"), show='headings', height=leaderboard_height)
impossible_leaderboard.heading("#1", text="Name")
impossible_leaderboard.column('#1', stretch=YES, width=160)
impossible_leaderboard.heading("#2", text="Level")
impossible_leaderboard.column('#2', stretch=YES, width=160)
impossible_leaderboard.grid(column=0, row=1, padx = 20,pady=20,rowspan=4, columnspan=2)
#Add scrollbar to jobTree
impossible_leaderboard_scrollbar = Scrollbar(impossible_tab)
impossible_leaderboard_scrollbar.grid(column=2, row=1, sticky = 'NSW',rowspan=4)
impossible_leaderboard.config(yscrollcommand = impossible_leaderboard_scrollbar.set)
impossible_leaderboard_scrollbar.config(command=impossible_leaderboard.yview)

#Radio buttons to select difficulty

level_difficulty_pane = ttk.Panedwindow(root, orient=tk.VERTICAL)

level_difficulty_frame = ttk.Labelframe(level_difficulty_pane, text='1. Invoice Type')
level_difficulty_pane.add(level_difficulty_frame, weight = 6)

level_difficulty_pane.grid(column = 1, row = 3, padx=5, pady=5, columnspan = 1, rowspan=4)
difficultyVar = tk.IntVar()
easyRadioButton = Radiobutton(level_difficulty_pane, text="Easy", variable=difficultyVar, value=1)
intermediateRadioButton = Radiobutton(level_difficulty_pane, text="Intermediate", variable=difficultyVar, value=2)
hardRadioButton = Radiobutton(level_difficulty_pane, text="Hard", variable=difficultyVar, value=3)
insaneRadioButton = Radiobutton(level_difficulty_pane, text="Insane", variable=difficultyVar, value=4)
impossibleRadioButton = Radiobutton(level_difficulty_pane, text="Impossible", variable=difficultyVar, value=5)


# level_difficulty_pane.add(quoteRadioButton)
# level_difficulty_pane.add(interimRadioButton)
# level_difficulty_pane.add(finalRadioButton)
# level_difficulty_pane.add(salesRadioButton)
# level_difficulty_pane.add(recurringRadioButton)

easyRadioButton.grid(column=0, row=1, padx=20, pady=(15,0))
intermediateRadioButton.grid(column=0, row=2, padx=5, pady=2) 
hardRadioButton.grid(column=0, row=3, padx=10, pady=2) 
insaneRadioButton.grid(column=0, row=4, padx=5, pady=2) 
impossibleRadioButton.grid(column=0, row=5, padx=5, pady=2) 

# Button to start a new game
new_game_button = tk.Button(root, text= 'New Game', command=lambda: q.new_game(), width=2, bg = widget_color)
new_game_button.grid(column=1, row = 6, padx=0, pady=10, sticky='nesw')

#Button to confirm guess
submit_button = tk.Button(root, text= 'Submit', command=lambda: q.checkAnswers(), width=2, bg = widget_color)
submit_button.grid(column=3, row = 6, padx=0, pady=10, sticky='nesw')


score_box_label = tk.Label(root, text = "Correct Guesses ", font = ('Arial', 12), bg = widget_color)
score_box_label.grid(column = 2, row = 3, padx=10, pady=10)
 
score_var = tk.IntVar()
score_box = tk.Entry(root, textvariable=score_var, font = ('Arial', 20), width = 16, bg = widget_color)
score_box.grid(column=3, row = 3, padx=0, pady=10, sticky='nesw')
score_box.config(state='readonly')




lives_var = tk.IntVar()  
lives_box = tk.Entry(root, textvariable=lives_var, font = ('Arial', 20), width = 16, bg = widget_color)
lives_box.grid(column=9, row = 0, padx=0, pady=10, sticky='nesw')
lives_box.config(state='readonly')

lives_label = tk.Label(root, text = "Lives  " , font = ('Arial', 12), bg = widget_color)
lives_label.grid(column = 8, row = 0, padx=10, pady=10)

level_label = tk.Label(root, text = "Level  ", font = ('Arial', 12), bg = widget_color)
level_label.grid(column = 2, row = 2, padx=10, pady=10)

level_var = tk.IntVar()
level_box = tk.Entry(root, textvariable=level_var, font = ('Arial', 20), width = 16, bg = widget_color)
level_box.grid(column=3, row = 2, padx=0, pady=10, sticky='nesw')
level_box.config(state='readonly')

listbox = DragDropListbox(root, height = 20, width = 60, bd = 6, bg = widget_color)
listbox.grid(column=3, row = 5)

#Populate leaderboard
q = Questions()
lead = Leaderboard()
lead.populateLeaderboard()
lead.createLeaderboardTable()

root.mainloop()


