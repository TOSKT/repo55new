"""
MIT License

Copyright (c) 2018 TOSKT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import tkinter as tk
import random

entry = None
lb = None
n_name = 'talkbox:'
y_name = 'you:'

def putlog(str):

    lb.insert(tk.END,str)

def push():
    inp = entry.get()
    putlog(y_name + inp)
    lis = ['はい','そうですね','そうでもないですよ']
    if not inp:
        putlog(n_name + ' ?')
    elif   inp == '元気？':
            putlog(n_name + random.choice(lis))
            entry.delete(0,tk.END)
    elif   inp == 'おはよう':
            putlog(n_name + 'おはようございます')
            entry.delete(0,tk.END)
    elif   inp == 'こんにちは':
            putlog(n_name + 'こんにちは')
            entry.delete(0,tk.END)
    elif   inp == 'こんばんは':
            putlog(n_name + 'こんばんは')
            entry.delete(0,tk.END)
    elif   inp == 'フルーツリスト':
            putlog(n_name +'フルーツリストですね')
            import fruitslist      
    elif   inp == 'やさいリスト':
            putlog(n_name +'やさいリストですね')
            import vegitableslist
    elif   inp == 'おみくじ':
            putlog(n_name + 'おみくじですね')
            entry.delete(0,tk.END)
            omikuji()
    else:
        putlog(n_name + ' ?')
        entry.delete(0,tk.END)

def omikuji():
        putlog(n_name+'おみくじを開始いたします')
        lis = ['大吉','中吉','小吉','凶','大凶']
        putlog(n_name+random.choice(lis))


def run():
    global entry,lb

    root = tk.Tk()
    root.geometry('880x560')
    root.title('talkbox')
    font = ('Helevetica',14)

    display = tk.Label(
                root,
                width = 20,
                height = 23,
                font = font,
                bg = 'gray',
                text = '対応単語：\n元気？\nおはよう\nこんばんは\nこんにちは\nやさいリスト\nフルーツリスト\nおみくじ'
                        )
    display.place(x=650,y=20)


    frame = tk.Frame(root)
    frame.place(x=30,y=520)

    entry = tk.Entry(
                frame,
                width = 70,
                font = font
                )
    entry.pack(side = tk.LEFT)
    entry.focus_set()

    button = tk.Button(
                frame,
                width = 15,
                text = 'push',
                command = push
                )
    button.pack(side = tk.LEFT)

    button2 = tk.Button(
                root,
                width = 15,
                text = 'おみくじ',
                command = omikuji
                )
    button2.place(x=690,y=340)

    lb = tk.Listbox(
                root,
                width = 60,
                height = 24,
                font = font
                )

    sb1 = tk.Scrollbar(
                root,
                orient = tk.VERTICAL,
                command = lb.yview
                )

    lb.configure(yscrollcommand = sb1.set)
    
    lb.grid(row = 0,column = 0)
    sb1.grid(row = 0,column = 1,sticky = tk.NS)

    root.mainloop()

run()