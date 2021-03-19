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
from os import path
from tkinter import Menu
import tkinter.scrolledtext
import pandas as pd
from pathlib import Path
import random 
from PIL import Image, ImageTk

Path('sorting_game.db').touch()
###This code allows to print first name from databsase after clicking on button

def connect():
    conn = sqlite3.connect("sorting_game.db")
    cur = conn.cursor()

    print (pd.read_sql("SELECT * FROM movie_data", conn))
    conn.commit()
    conn.close()

 

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
            messagebox.showinfo("Game Over", "You reached level " + str(self.level))
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

q = Questions()

tabControl = ttk.Notebook(root) 
  
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
  
tabControl.add(tab1, text ='Tab 1') 
tabControl.add(tab2, text ='Tab 2') 
tabControl.grid(column = 8, row = 3) 
  
ttk.Label(tab1, text ="Welcome to GeeksForGeeks").grid(column = 0,  row = 0, padx = 30, pady = 30)   
ttk.Label(tab2, text ="Lets dive into the world of computers").grid(column = 0, row = 0, padx = 30, pady = 30) 
 # # # # #  TO DO - -- - sort out radio buttons, put them in their own pane, assign to game

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
root.mainloop()


