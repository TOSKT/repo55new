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
from bs4 import BeautifulSoup

lb = None

def putlog(str):
    lb.insert(tk.END,str)

def run():
    global lb

    root = tk.Tk()
    root.geometry('880x560')
    root.title('vegitables')
    font = ('Helevetica',14)

    lb = tk.Listbox(
                    root,
                    width=85,
                    height = 30,
                    font = font
                    )

    sb1 = tk.Scrollbar(
                    root,
                    orient = tk.VERTICAL,
                    command = lb.yview
                    )

    sb2 = tk.Scrollbar(
                root,
                orient = tk.HORIZONTAL,
                command = lb.xview
                    )

    lb.configure(yscrollcommand = sb1.set)
    lb.configure(xscrollcommand = sb2.set)
        
    lb.grid(row = 0,column = 0)
    sb1.grid(row = 0,column = 1,sticky = tk.NS)
    sb2.grid(row = 1,column = 0,sticky = tk.EW)

    html = """
    <html><body>
      <p>レタス</p>
      <p>キャベツ</p>
      <p>キュウリ</p>
      <p>トマト</p>
      <p>ナス</p>
    </body></html>
    """
    soup = BeautifulSoup(html,'html.parser')

    p_list = soup.select("p")
    for p in p_list:
        putlog(p.string)


    root.mainloop()

run()