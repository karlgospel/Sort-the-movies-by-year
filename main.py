#!/usr/bin/env python3

from tkinter import ttk
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter.ttk import *
from tkinter import Listbox
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
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
        
    def updateLeaderboards(self, user):
        
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
    
    def resetLeaderboards(self, ):
        
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        sql = '''DELETE FROM easyLeaderboard'''
        cur.execute(sql)
        sql = '''DELETE FROM intermediateLeaderboard'''
        cur.execute(sql)
        sql = '''DELETE FROM hardLeaderboard'''
        cur.execute(sql)
        sql = '''DELETE FROM insaneLeaderboard'''
        cur.execute(sql)
        sql = '''DELETE FROM impossibleLeaderboard'''
        cur.execute(sql)
        conn.commit()
        conn.close()
        self.populateLeaderboard()
        
        
    def resetEasyLeaderboard(self, ):
        
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        sql = '''DELETE FROM easyLeaderboard'''
        cur.execute(sql)
        conn.commit()
        conn.close()
        self.populateLeaderboard()


    def resetIntermediateLeaderboard(self, ):
        
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        sql = '''DELETE FROM intermediateLeaderboard'''
        cur.execute(sql)
        conn.commit()
        conn.close()
        self.populateLeaderboard()


    def resetHardLeaderboard(self, ):
        
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        sql = '''DELETE FROM hardLeaderboard'''
        cur.execute(sql)
        conn.commit()
        conn.close()
        self.populateLeaderboard()


    def resetInsaneLeaderboard(self, ):
        
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        sql = '''DELETE FROM Leaderboard'''
        cur.execute(sql)
        conn.commit()
        conn.close()
        self.populateLeaderboard()
        
    def resetImpossibleLeaderboard(self, ):
        
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        sql = '''DELETE FROM impossibleLeaderboard'''
        cur.execute(sql)
        conn.commit()
        conn.close()
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
        
        
    
    # def getEasyLeaderboard(self):
    #     """ Gets the name and scores of the easy difficulty leaderboard
    #     
    #     Returns
    #     ----------
    #     List
    #         A list of leaderboard results
    #         
    #     """
    #     conn = sqlite3.connect("sorting_game.db")
    #     cur = conn.cursor()
    #     sql =("SELECT rowid, name, score FROM easyLeaderboard ORDER BY score ASC")
    #     cur.execute(sql)
    #     result = cur.fetchall()
    #     conn.commit
    #     conn.close
    #     return (result)
    
    
    def getEasyLeaderboard(self):
        
        conn = sqlite3.connect("sorting_game.db")
        cur = conn.cursor()
        #cur.execute("DROP TABLE easyOrdered")
        cur.execute("CREATE TABLE IF NOT EXISTS easyOrdered (ID INTEGER PRIMARY KEY AUTOINCREMENT, name, score)")
        cur.execute("INSERT INTO easyOrdered (name, score) SELECT name,score FROM easyLeaderboard ORDER BY score DESC")
        
        cur.execute("DROP TABLE easyLeaderboard")
        cur.execute("ALTER TABLE easyOrdered RENAME TO easyLeaderboard")
        sql =("SELECT rowid, name, score FROM easyLeaderboard")
        cur.execute(sql)
        
        result = cur.fetchall()
        #cur.execute("DROP TABLE easyOrdered")
        print(result)
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
        cur.execute("CREATE TABLE IF NOT EXISTS intOrdered (ID INTEGER PRIMARY KEY AUTOINCREMENT, name, score)")
        cur.execute("INSERT INTO intOrdered (name, score) SELECT name,score FROM intermediateLeaderboard ORDER BY score DESC")
    
        cur.execute("DROP TABLE intermediateLeaderboard")
        cur.execute("ALTER TABLE intOrdered RENAME TO intermediateLeaderboard")
        sql =("SELECT rowid, name, score FROM intermediateLeaderboard")
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
        cur.execute("CREATE TABLE IF NOT EXISTS hardOrdered (ID INTEGER PRIMARY KEY AUTOINCREMENT, name, score)")
        cur.execute("INSERT INTO hardOrdered (name, score) SELECT name,score FROM hardLeaderboard ORDER BY score DESC")
    
        cur.execute("DROP TABLE hardLeaderboard")
        cur.execute("ALTER TABLE hardOrdered RENAME TO hardLeaderboard")
        
        sql =("SELECT rowid, name, score FROM hardLeaderboard")
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
        cur.execute("CREATE TABLE IF NOT EXISTS insaneOrdered (ID INTEGER PRIMARY KEY AUTOINCREMENT, name, score)")
        cur.execute("INSERT INTO insaneOrdered (name, score) SELECT name,score FROM insaneLeaderboard ORDER BY score DESC")
    
        cur.execute("DROP TABLE insaneLeaderboard")
        cur.execute("ALTER TABLE insaneOrdered RENAME TO insaneLeaderboard")
        
        sql =("SELECT rowid, name, score FROM insaneLeaderboard")
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
        cur.execute("CREATE TABLE IF NOT EXISTS impOrdered (ID INTEGER PRIMARY KEY AUTOINCREMENT, name, score)")
        cur.execute("INSERT INTO impOrdered (name, score) SELECT name,score FROM impossibleLeaderboard ORDER BY score DESC")
        cur.execute("DROP TABLE impossibleLeaderboard")
        cur.execute("ALTER TABLE impOrdered RENAME TO impossibleLeaderboard")
        
        sql =("SELECT rowid, name, score FROM impossibleLeaderboard")
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit
        conn.close
        return (result)

    def populateLeaderboard(self):
        """ Populates the leaderboards"""
        
        odd_color = widget_color
        even_color = button_color
        leaderboard_font = "Arial"
        leaderboard_font_size = 12
        
        easy_leaderboard.tag_configure('odd', background = even_color, foreground = odd_color, font = (leaderboard_font, leaderboard_font_size))
        easy_leaderboard.tag_configure('even', background= odd_color, foreground = even_color, font = (leaderboard_font, leaderboard_font_size))
        intermediate_leaderboard.tag_configure('odd', background= even_color, foreground = odd_color, font = (leaderboard_font, leaderboard_font_size))
        intermediate_leaderboard.tag_configure('even', background= odd_color, foreground = even_color, font = (leaderboard_font, leaderboard_font_size))
        hard_leaderboard.tag_configure('odd', background= even_color, foreground = odd_color, font = (leaderboard_font, leaderboard_font_size))
        hard_leaderboard.tag_configure('even', background= odd_color, foreground = even_color, font = (leaderboard_font, leaderboard_font_size))
        insane_leaderboard.tag_configure('odd', background= even_color, foreground = odd_color, font = (leaderboard_font, leaderboard_font_size))
        insane_leaderboard.tag_configure('even', background= odd_color, foreground = even_color, font = (leaderboard_font, leaderboard_font_size))
        impossible_leaderboard.tag_configure('odd', background= even_color, foreground = odd_color, font = (leaderboard_font, leaderboard_font_size))
        impossible_leaderboard.tag_configure('even', background= odd_color, foreground = even_color, font = (leaderboard_font, leaderboard_font_size))
        
        easy_scores = self.getEasyLeaderboard()
        easy_leaderboard.delete(*easy_leaderboard.get_children())
        for each in easy_scores:
            if each[0] % 2 == 0:
                easy_leaderboard.insert("",END,values=each, tags = ("even"))
            else:
                easy_leaderboard.insert("",END,values=each, tags = ("odd"))

            
        intermediate_scores = self.getIntermediateLeaderboard()
        intermediate_leaderboard.delete(*intermediate_leaderboard.get_children())
        for each in intermediate_scores:
            if each[0] % 2 == 0:
                intermediate_leaderboard.insert("",END,values=each, tags = ("even"))
            else:
                intermediate_leaderboard.insert("",END,values=each, tags = ("odd"))
                
        hard_scores = self.getHardLeaderboard()
        hard_leaderboard.delete(*hard_leaderboard.get_children())
        for each in hard_scores:
            if each[0] % 2 == 0:
                hard_leaderboard.insert("",END,values=each, tags = ("even"))
            else:
                hard_leaderboard.insert("",END,values=each, tags = ("odd"))
                
        insane_scores = self.getInsaneLeaderboard()
        insane_leaderboard.delete(*insane_leaderboard.get_children())
        for each in insane_scores:
            if each[0] % 2 == 0:
                insane_leaderboard.insert("",END,values=each, tags = ("even"))
            else:
                insane_leaderboard.insert("",END,values=each, tags = ("odd"))
                
        impossible_scores = self.getImpossibleLeaderboard()
        impossible_leaderboard.delete(*impossible_leaderboard.get_children())
        for each in impossible_scores:
            if each[0] % 2 == 0:
                impossible_leaderboard.insert("",END,values=each, tags = ("even"))
            else:
                impossible_leaderboard.insert("",END,values=each, tags = ("odd"))
        
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
            
class App():
    

    level = 1
    lives = 3
    current_movie_choices = []
    correct_guesses = 0
    difficulty = ""
    player = ""


    def reset_game(self, ):
        #q = App()
        score_box.config(state='normal')
        score_box.delete(0,tk.END)
        score_box.insert(0,0)
        score_box.config(state='readonly')
        listbox.delete(0,tk.END)
        level_var.set(1)
        lives_var.set(self.lives)
        self.level = 1
        self.lives = 3
        self.correct_guesses = 0
        self.difficulty = ""
        self.player = ""

        # movie_choices = q.start_easy_game()
        
    def new_game(self ):
        # print(difficultyVar.get())
        if difficultyVar.get() == 0:
            tk.messagebox.showinfo("Oops","Please choose a difficulty setting")
            return
        else:
            pass
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
        #lives_var.set(3)
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
    
    def show_easy_movies(self):
       
        listbox.delete(0,tk.END)
        movie_choices = q.start_easy_game()

        for title, year in movie_choices:
          listbox.insert(tk.END, title)

        print("----original list of movies----")
        print(movie_choices)

    def show_intermediate_movies(self):
       
        listbox.delete(0,tk.END)
        movie_choices = q.start_intermediate_game()

        for title, year in movie_choices:
          listbox.insert(tk.END, title)

        print("----original list of movies----")
        print(movie_choices)
        
        
    def show_hard_movies(self):
       
        listbox.delete(0,tk.END)
        movie_choices = q.start_hard_game()

        for title, year in movie_choices:
          listbox.insert(tk.END, title)

        print("----original list of movies----")
        print(movie_choices)
        
        
    def show_insane_movies(self):
       
        listbox.delete(0,tk.END)
        movie_choices = q.start_insane_game()

        for title, year in movie_choices:
          listbox.insert(tk.END, title)

        print("----original list of movies----")
        print(movie_choices)
        
        
    def show_impossible_movies(self):
       
        listbox.delete(0,tk.END)
        movie_choices = q.start_impossible_game()

        for title, year in movie_choices:
          listbox.insert(tk.END, title)

        print("----original list of movies----")
        print(movie_choices)
        
        
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
        lives_var.set(10)
        self.lives = 10
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
        lives_var.set(8)
        self.lives = 8
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
        lives_var.set(5)
        self.lives = 5
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
        lives_var.set(5)
        self.lives = 5
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
        lives_var.set(5)
        self.lives = 5
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
        self.correct_guesses = 0
        movie_predictions = q.getPrediction()
        print("----user guess----")
        print(movie_predictions)
        correct_order = sorted(self.current_movie_choices, key=lambda x: x[1])
        print("----correct order----")
        print(correct_order)
        for i in correct_order:
            if i[0] == movie_predictions[(correct_order.index(i))]:
              self.correct_guesses +=1
        if self.correct_guesses == 5:
          self.level +=1
          level_box.config(state='normal')
          level_box.delete(0,tk.END)
          level_box.insert(0,self.level)
          level_box.config(state='readonly')
          self.correct_guesses = 0
          q.show_easy_movies()

        else:
          self.lives -= 1
          lives_box.config(state='normal')
          lives_box.delete(0,tk.END)
          lives_box.insert(0,self.lives)
          lives_box.config(state='readonly')
        if self.lives == 0:
            user_name = self.getName()
            lead.updateLeaderboards(user_name)
            q.reset_game()
            return
        
        score_box.config(state='normal')
        score_box.delete(0,tk.END)
        score_box.insert(0,self.correct_guesses)
        score_box.config(state='readonly')
        
        
    def checkInsaneAnswers(self):
        self.correct_guesses = 0
        movie_predictions = q.getPrediction()
        print("----user guess----")
        print(movie_predictions)
        correct_order = sorted(self.current_movie_choices, key=lambda x: x[1])
        print("----correct order----")
        print(correct_order)
        for i in correct_order:
            if i[0] == movie_predictions[(correct_order.index(i))]:
              self.correct_guesses +=1
        if self.correct_guesses == 7:
          self.level +=1
          level_box.config(state='normal')
          level_box.delete(0,tk.END)
          level_box.insert(0,self.level)
          level_box.config(state='readonly')
          self.correct_guesses = 0
          q.show_insane_movies()
        else:
          self.lives -= 1
          lives_box.config(state='normal')
          lives_box.delete(0,tk.END)
          lives_box.insert(0,self.lives)
          lives_box.config(state='readonly')
        if self.lives == 0:
            user_name = self.getName()
            lead.updateLeaderboards(user_name)
            q.reset_game()
            
        score_box.config(state='normal')
        score_box.delete(0,tk.END)
        score_box.insert(0,self.correct_guesses)
        score_box.config(state='readonly')

    def checkImpossibleAnswers(self):
        self.correct_guesses = 0
        movie_predictions = q.getPrediction()
        print("----user guess----")
        print(movie_predictions)
        correct_order = sorted(self.current_movie_choices, key=lambda x: x[1])
        print("----correct order----")
        print(correct_order)
        for i in correct_order:
            if i[0] == movie_predictions[(correct_order.index(i))]:
              self.correct_guesses +=1
        if self.correct_guesses == 10:
          self.level +=1
          level_box.config(state='normal')
          level_box.delete(0,tk.END)
          level_box.insert(0,self.level)
          level_box.config(state='readonly')
          self.correct_guesses = 0
          q.show_impossible_movies()
        else:
          self.lives -= 1
          lives_box.config(state='normal')
          lives_box.delete(0,tk.END)
          lives_box.insert(0,self.lives)
          lives_box.config(state='readonly')
        if self.lives == 0:
            user_name = self.getName()
            lead.updateLeaderboards(user_name)
            q.reset_game()
        score_box.config(state='normal')
        score_box.delete(0,tk.END)
        score_box.insert(0,self.correct_guesses)
        score_box.config(state='readonly')
        print("correct_guesses =  ")
        print(self.correct_guesses)
    
    
    def answer_checker(self, ):
        
        difficulty = q.difficulty
        if difficulty in [1,2,3]:
            self.checkAnswers()
        elif difficulty == 4:
            self.checkInsaneAnswers()
        elif difficulty == 5:
            self.checkImpossibleAnswers()



    
    def getName(self ):
        '''Asks for user's name with a popup dialog box. Max 20 characters

            Returns:
                    name (str): String containing user's name 
    '''
        correct = False
        while correct == False:
            name = simpledialog.askstring("Game Over","Submit score to Leaderboard", parent = root)
            if len(name) > 0 and len(name) < 21:
                correct == True
                break
            if len(name) > 20:
                tk.messagebox.showerror("Sorry", "Oops, That looks a little bit too long")
            if len(name) == 0:
                answer = tk.messagebox.askyesno("Are You Sure?", "Did you mean to enter no name?")
                if answer == True:
                    correct = True
        return (name)

    
    def SetCheckButton(self, ):
        '''
        

        '''
        selection = str(difficultyVar.get())
        print(selection)
        print("hello")
        if selection == 1:
            easyRadioButton.config(borderwidth = 12)
    
        

    def openHelp(self):
        '''
        Opens a message box with information on how to play the game
        '''
        tk.messagebox.showinfo("How To Play", "1. Choose a difficulty \n\n2. Sort the movies by their release date. Oldest movies at the top, newest at the bottom \n\n3. Submit your guess \n\n4. The number of correct guesses is how many movies you have in the correct position \n\n5. Keep guessing until you get the right solution, or you're out of lives \n\n6. Submit your score to the leaderboard \n\n7. Keep playing and beat your high score \n\n8. Have Fun!!! ")
    


root = tk.Tk()
root.title("CineSort")
root.state('zoomed')
root.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6,7,8,9, 10,11,12), weight=1)
root.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6,7,8,9,10,11), weight=1)
#root.config(bg="#330000")
#widget_color = '#b1070c'

#Set color scheme
widget_color = "#BF0404"
button_color = "#F29F05"

border_width_size = 4


#Add image as background and set to full size
IMAGE_PATH = 'images/red_border.png'
# WIDTH, HEIGHT = 1280, 700
pad = 80
WIDTH, HEIGHT = root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad
# root.geometry('{}x{}'.format(WIDTH, HEIGHT))
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad))
img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
lbl = tk.Label(root, image=img)
lbl.img = img  # Keep a reference in case this code put is in a function.
lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.

# Fonts and colour variables
widget_font = "Ebrima"
font_color = "#FFC000"


# Title of game

title_label = tk.Label(root, text = "CineSort", font = ('Arial', 42), bg = 'white', fg = widget_color)
title_label.grid(column =0, row = 3, columnspan = 12, rowspan = 1)

#Create tab control to show leaderboards with style
style = ttk.Style()                     
#current_theme =style.theme_use()
# style.theme_settings(current_theme, {"TNotebook.Tab": {"configure": {"padding": [10, 5], "selected": button_color, "background": "white"  }}})
mygreen = "#d2ffd2"
myred = "#dd0202"

style.theme_create( "tabControl", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": "white", "foreground": "black", "fontsize": 16, "font": widget_font},
            "map":       {"background": [("selected", myred)],
                          "expand": [("selected", [3, 3, 3, 0])] } } } )

tabControl = ttk.Notebook(root) 


style.theme_use("tabControl")
  
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
tabControl.grid(column = 9, row = 5, padx=10, pady=10, columnspan = 3) 
  


#Create tree view list to show easy leaderboard in easy tab


leaderboard_width = 60
leaderboard_column = 5
leaderboard_row = 5
leaderboard_height = 20
rank_width = 40
name_width = 180
level_width = 40

easy_leaderboard= ttk.Treeview(easy_tab, column=("col1", "col2", "col3"), show='headings', height=leaderboard_height)
easy_leaderboard.heading("#1", text="Rank")
easy_leaderboard.column('#1', stretch=YES, width=rank_width)
easy_leaderboard.heading("#2", text="Name")
easy_leaderboard.column('#2', stretch=YES, width=name_width)
easy_leaderboard.heading("#3", text="Level")
easy_leaderboard.column('#3', stretch=YES, width=level_width)
easy_leaderboard.grid(column=0, row=1, padx = 20,pady=20,rowspan=4, columnspan=2)
#Add scrollbar to jobTree
easy_leaderboard_scrollbar = Scrollbar(easy_tab)
easy_leaderboard_scrollbar.grid(column=3, row=1, sticky = 'NSW',rowspan=4)
easy_leaderboard.config(yscrollcommand = easy_leaderboard_scrollbar.set)
easy_leaderboard_scrollbar.config(command=easy_leaderboard.yview)


#Create tree view list to show intermediate leaderboard in intermediate tab

intermediate_leaderboard= ttk.Treeview(intermediate_tab, column=("col1", "col2", "col3"), show='headings', height=leaderboard_height)
intermediate_leaderboard.heading("#1", text="Rank")
intermediate_leaderboard.column('#1', stretch=YES, width=rank_width)
intermediate_leaderboard.heading("#2", text="Name")
intermediate_leaderboard.column('#2', stretch=YES, width=name_width)
intermediate_leaderboard.heading("#3", text="Level")
intermediate_leaderboard.column('#3', stretch=YES, width=level_width)
intermediate_leaderboard.grid(column=0, row=1, padx = 20,pady=20,rowspan=4, columnspan=2)
#Add scrollbar to jobTree
intermediate_leaderboard_scrollbar = Scrollbar(intermediate_tab)
intermediate_leaderboard_scrollbar.grid(column=3, row=1, sticky = 'NSW',rowspan=4)
intermediate_leaderboard.config(yscrollcommand = intermediate_leaderboard_scrollbar.set)
intermediate_leaderboard_scrollbar.config(command=intermediate_leaderboard.yview)


#Create tree view list to show hard leaderboard in hard tab

hard_leaderboard= ttk.Treeview(hard_tab, column=("col1", "col2", "col3"), show='headings', height=leaderboard_height)
hard_leaderboard.heading("#1", text="Rank")
hard_leaderboard.column('#1', stretch=YES, width=rank_width)
hard_leaderboard.heading("#2", text="Name")
hard_leaderboard.column('#2', stretch=YES, width=name_width)
hard_leaderboard.heading("#3", text="Level")
hard_leaderboard.column('#3', stretch=YES, width=level_width)
hard_leaderboard.grid(column=0, row=1, padx = 20,pady=20,rowspan=4, columnspan=2)
#Add scrollbar to jobTree
hard_leaderboard_scrollbar = Scrollbar(hard_tab)
hard_leaderboard_scrollbar.grid(column=3, row=1, sticky = 'NSW',rowspan=4)
hard_leaderboard.config(yscrollcommand = hard_leaderboard_scrollbar.set)
hard_leaderboard_scrollbar.config(command=hard_leaderboard.yview)


#Create tree view list to show insane leaderboard in insane tab

insane_leaderboard= ttk.Treeview(insane_tab, column=("col1", "col2", "col3"), show='headings', height=leaderboard_height)
insane_leaderboard.heading("#1", text="Rank")
insane_leaderboard.column('#1', stretch=YES, width=rank_width)
insane_leaderboard.heading("#2", text="Name")
insane_leaderboard.column('#2', stretch=YES, width=name_width)
insane_leaderboard.heading("#3", text="Level")
insane_leaderboard.column('#3', stretch=YES, width=level_width)
insane_leaderboard.grid(column=0, row=1, padx = 20,pady=20,rowspan=4, columnspan=2)
#Add scrollbar to jobTree
insane_leaderboard_scrollbar = Scrollbar(insane_tab)
insane_leaderboard_scrollbar.grid(column=3, row=1, sticky = 'NSW',rowspan=4)
insane_leaderboard.config(yscrollcommand = insane_leaderboard_scrollbar.set)
insane_leaderboard_scrollbar.config(command=insane_leaderboard.yview)


#Create tree view list to show impossible leaderboard in impossible tab

impossible_leaderboard= ttk.Treeview(impossible_tab, column=("col1", "col2", "col3"), show='headings', height=leaderboard_height)
impossible_leaderboard.heading("#1", text="Rank")
impossible_leaderboard.column('#1', stretch=YES, width=rank_width)
impossible_leaderboard.heading("#2", text="Name")
impossible_leaderboard.column('#2', stretch=YES, width=name_width)
impossible_leaderboard.heading("#3", text="Level")
impossible_leaderboard.column('#3', stretch=YES, width=level_width)
impossible_leaderboard.grid(column=0, row=1, padx = 20,pady=20,rowspan=4, columnspan=2)
#Add scrollbar to jobTree
impossible_leaderboard_scrollbar = Scrollbar(impossible_tab)
impossible_leaderboard_scrollbar.grid(column=3, row=1, sticky = 'NSW',rowspan=4)
impossible_leaderboard.config(yscrollcommand = impossible_leaderboard_scrollbar.set)
impossible_leaderboard_scrollbar.config(command=impossible_leaderboard.yview)



# Pane to select level difficulty
#Radio buttons to select difficulty

level_difficulty_pane = ttk.Panedwindow(root, orient=tk.VERTICAL)

level_difficulty_frame = ttk.Frame(level_difficulty_pane)
level_difficulty_pane.add(level_difficulty_frame, weight = 6)

button_padding_y = 4
button_padding_x = 20
radio_button_size = 20

level_difficulty_pane.grid(column = 4, row = 3, padx=5, pady=5, columnspan = 2, rowspan=4)
difficultyVar = tk.IntVar()
easyRadioButton = tk.Radiobutton(level_difficulty_pane, text="Easy", variable=difficultyVar, value=1, borderwidth = border_width_size, width = 10, relief = RAISED, font = (widget_font, radio_button_size), bg = widget_color, fg = font_color, justify = LEFT, selectcolor = widget_color, activeforeground = "white", command = lambda: q.SetCheckButton)
intermediateRadioButton = tk.Radiobutton(level_difficulty_pane, text="Intermediate", variable=difficultyVar, value=2, borderwidth = border_width_size, width = 10, relief = RAISED, font = (widget_font, radio_button_size), bg = widget_color, fg = font_color, justify = CENTER, selectcolor = widget_color)
hardRadioButton = tk.Radiobutton(level_difficulty_pane, text="Hard", variable=difficultyVar, value=3, borderwidth = border_width_size, width = 10, relief = RAISED, font = (widget_font, radio_button_size), bg = widget_color, fg = font_color, justify = CENTER, selectcolor = widget_color)
insaneRadioButton = tk.Radiobutton(level_difficulty_pane, text="Insane", variable=difficultyVar, value=4, borderwidth = border_width_size, width = 10, relief = RAISED, font = (widget_font, radio_button_size), bg = widget_color, fg = font_color, justify = CENTER, selectcolor = widget_color)
impossibleRadioButton = tk.Radiobutton(level_difficulty_pane, text="Impossible", variable=difficultyVar, value=5, borderwidth = border_width_size, width = 10, relief = RAISED, font = (widget_font, radio_button_size), bg = widget_color, fg = font_color, justify = CENTER, selectcolor = widget_color)


easyRadioButton.grid(column=0, row=1, padx=button_padding_x, pady=button_padding_y)
intermediateRadioButton.grid(column=0, row=2, padx=button_padding_x, pady=button_padding_y) 
hardRadioButton.grid(column=0, row=3, padx=button_padding_x, pady=button_padding_y) 
insaneRadioButton.grid(column=0, row=4, padx=button_padding_x, pady=button_padding_y) 
impossibleRadioButton.grid(column=0, row=5, padx=button_padding_x, pady=button_padding_y) 


BUTTON_IMAGE_PATH = 'images/red_rectangle.png'
HELP_BUTTON_PATH = 'images/help.png'
# SETTINGS_PATH = 'images/settings.png'
# WIDTH, HEIGHT = 1280, 700

submit_btn_img = ImageTk.PhotoImage(Image.open(BUTTON_IMAGE_PATH).resize((300, 100), Image.ANTIALIAS))
#submit_btn_img = ImageTk.PhotoImage(Image.open(BUTTON_IMAGE_PATH))

newgame_btn_img = ImageTk.PhotoImage(Image.open(BUTTON_IMAGE_PATH).resize((200, 100), Image.ANTIALIAS))
help_btn_img = ImageTk.PhotoImage(Image.open(HELP_BUTTON_PATH))
# settings_btn_img = ImageTk.PhotoImage(Image.open(SETTINGS_PATH))

#img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))


# Button to start a new game
new_game_button = tk.Button(root, text= 'New Game', command=lambda: q.new_game(), image = newgame_btn_img,  bg = "white", relief = FLAT, compound = 'center', bd = 0, activebackground = "white", font = ("Century",16), width = 20, height = 20, fg = font_color)
new_game_button.grid(column=4, row = 6, sticky='nesw', columnspan = 2)

# Button to confirm guess
#submit_button = tk.Button(root, text= 'Submit', command=lambda: q.answer_checker(), width=1, bg = button_color, relief = RAISED)
submit_button = tk.Button(root, text= 'Submit', command=lambda: q.answer_checker(), image = submit_btn_img,  bg = "white", relief = FLAT, compound = 'center', bd = 0, activebackground = "white",width = 20, height = 20, font = ("Century",16), fg = font_color)
submit_button.grid(column=7, row = 6, sticky='nesw', columnspan=1)

#Button to reset leaderboards
help_button = tk.Button(root, command=lambda: q.openHelp(), image = help_btn_img,  bg = "white", relief = GROOVE, compound = 'center', bd = 0, activebackground = "white", width = 1)
help_button.grid(column=10, row = 6, sticky='nesw', columnspan = 1)

#settings_button = tk.Button(root, command=lambda: q.openHelp(), image = settings_btn_img,  bg = "white", relief = GROOVE, compound = 'center', bd = 0, activebackground = "white", width = 1)
# settings_button.grid(column=11, row = 6, sticky='nesw')

# Create style for frames

# Initialize style
s = ttk.Style()
# Create style used by default for all Frames
s.configure('TFrame', background = widget_color)

# Create style for the first frame
s.configure('level_difficulty_frame.TFrame', background= 'white')
# # Use created style in this frame
# tab1 = ttk.Frame(mainframe, style='Frame1.TFrame')
# mainframe.add(tab1, text="Tab1")


# Create pane to show score, level, and lives info

game_info_pane = ttk.Panedwindow(root, orient=tk.VERTICAL)
game_info_frame = ttk.Frame(game_info_pane, width = 30)
game_info_pane.add(game_info_frame, weight = 12)
game_info_pane.grid(column = 6, row = 4, columnspan = 3, rowspan=1, sticky = 's')
#game_info_frame.grid(column = 3, row = 4, columnspan = 8, rowspan=1, sticky = 's')

level_label = tk.Label(game_info_frame, text = "Level  ", font = (widget_font, 16), bg = widget_color, fg = button_color)
level_label.grid(column =5, row = 2, padx=10, pady=10)

level_var = tk.IntVar()
level_box = tk.Entry(game_info_frame, textvariable=level_var, font = (widget_font, 20), width = 3, bg = widget_color)
level_box.grid(column=6, row = 2, padx=10, pady=10, sticky='nesw')
level_box.config(state='readonly')

#Box to display the number of correct guesses
score_box_label = tk.Label(game_info_frame, text = "Correct Guesses ", font = (widget_font, 16), bg = widget_color, fg = button_color)
score_box_label.grid(column = 3, row = 2, padx=10, pady=10)
 
score_var = tk.IntVar()
score_box = tk.Entry(game_info_frame, textvariable=score_var, font = (widget_font, 20), width = 3, bg = widget_color)
score_box.grid(column=4, row = 2, padx=10, pady=10, sticky='nesw')
score_box.config(state='readonly')


lives_label = tk.Label(game_info_frame, text = "Lives  " , font = (widget_font, 16), bg = widget_color, fg = button_color)
lives_label.grid(column = 7, row = 2, padx=10, pady=10)

lives_var = tk.IntVar()  
lives_box = tk.Entry(game_info_frame, textvariable=lives_var, font = (widget_font, 20), width = 3, bg = widget_color)
lives_box.grid(column=8, row = 2, padx=10, pady=10, sticky='nesw')
lives_box.config(state='readonly')





listbox = DragDropListbox(root, height = 10, width = 38, bd = 2, bg = button_color, font = (widget_font, 28), fg = widget_color, relief = GROOVE, cursor = "double_arrow", selectbackground = button_color, justify=CENTER)
listbox.grid(column=6, row = 5, padx=10, pady=10, columnspan = 3)

#Populate leaderboard
q = App()
lead = Leaderboard()
lead.populateLeaderboard()
lead.createLeaderboardTable()
# lead.resetLeaderboards()

root.mainloop()


