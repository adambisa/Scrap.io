import tkinter as tk
from scrapio import Scraper
import table
from myClasses import Url
import uuid
from time import time



def submit():
    scraper = Scraper()
    url = entry.get()
    price = scraper.scrape_any(url)
    string_var.set(price + 'eur')
    new_url = Url(str(uuid.uuid1()), url, price,'email',time())
    table.add_url(new_url)
    
def preview_saved():
    x = 400
    base_y = 300
    for i in table.view_urls():
        canvas.create_text(x+10,base_y, text=f'link : {i[1]}, price : {i[2]}', fill='white')
        base_y+=15
    #canvas.create_text(x,y, text='')
canvas = tk.Canvas(height=500, width=1000, background='black')
canvas.pack()

canvas.create_text(250, 25, text='PRICE CHECKER',
                   fill='white', font=('Helvetica', '30', 'bold'))

entry = tk.Entry()
entry.place(x=50, y=150)
canvas.create_text(150, 90, text='what do you want to buy?', fill='white')

sender = tk.Button(text='find cheapest product',command=submit)
sender.place(x=250, y=150)

string_var = tk.StringVar()
string_var.set('output')
label = tk.Label(canvas, textvariable=string_var)
label.place(x=290, y=200)

view_all = tk.Button(text='view all products in database', command=preview_saved)
view_all.place(x=250, y=250)
tk.mainloop()
