import tkinter
from timeit import default_timer as timer
import random


def speed_test():
   speed_test_sentences = [
       'This is a random sentence to check speed.',
       'Speed, I am lightning mcqueen.'
   ]

   sentence = random.choice(speed_test_sentences)
   start = timer()
   main_window = tkinter.Tk()
   main_window.geometry('600x400')

   label_1 = tkinter.Label(main_window, text=sentence, font='times 20')
   label_1.place(x=150, y=10)

   label_2 = tkinter.Label(main_window, text='Start Typing', font='times 20')
   label_2.place(x=10, y=50)

   entry = tkinter.Entry(main_window)
   entry.place(x=280, y=55)

   def check_result():
       if entry.get() == sentence:
           end = timer()
           label_3.configure(text=f'Time: {round((end-start), 4)}s')
       else:
           label_3.configure(text='Wrong Input')
