import tkinter
from tkinter import *

root = Tk()
root.title("Turoni's Pizza POS")
root.geometry = ("3000x650")
root.resizable(False, False)

#-------------------------Functions--------------------------#
def drink_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    soft_drinks = tkinter.Button(choices, text="Soft Drinks", width=10, font=("Courier", 15),borderwidth=0)
    soft_drinks.grid(row=1, column=0, padx = 10, pady= 10, ipady = 30)

    bottled_beer = tkinter.Button(choices, text="Bottled Beer", width=10, font=("Courier", 15),borderwidth=0)
    bottled_beer.grid(row=1, column=1, padx = 10, pady=10, ipady=30)

    draft = tkinter.Button(choices, text="Draft", width=10, font=("Courier", 15),borderwidth=0)
    draft.grid(row=1, column=2, padx = 10, pady= 10, ipady = 30)

    brew_spcl = tkinter.Button(choices, wraplength= 80, text="Brewery Specials", width=10, font=("Courier", 15),borderwidth=0)
    brew_spcl.grid(row=2, column=0, padx = 10, pady= 10, ipady = 21)

    mixed_drinks = tkinter.Button(choices, text="Mixed Drinks", width=10, font=("Courier", 15),borderwidth=0)
    mixed_drinks.grid(row=2, column=1, padx = 10, pady= 10, ipady = 30)
    

def appetizer_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    garlic_toast = tkinter.Button(choices, text="Garlic Toast", width=10, font=("Courier", 15),borderwidth=0)
    garlic_toast.grid(row=1, column=0, padx = 10, pady= 10, ipady = 30)
    
    breadsticks = tkinter.Button(choices, text="Breadsticks", width=10, font=("Courier", 15),borderwidth=0)
    breadsticks.grid(row=1, column=1, padx = 10, pady=10, ipady=30)

    mozzarella = tkinter.Button(choices, wraplength= 80, text="Mozarella Sticks", width=10, font=("Courier", 15),borderwidth=0)
    mozzarella.grid(row=1, column=2, padx = 10, pady= 10, ipady = 21)

    grilled_cheese = tkinter.Button(choices, wraplength= 80, text="Grilled Cheese", width=10, font=("Courier", 15),borderwidth=0)
    grilled_cheese.grid(row=2, column=0, padx = 10, pady= 10, ipady = 21)

    bruschetta = tkinter.Button(choices, text="Bruschetta", width=10, font=("Courier", 15),borderwidth=0)
    bruschetta.grid(row=2, column=1, padx = 10, pady= 10, ipady = 30)
    
    wings = tkinter.Button(choices, wraplength= 80, text="Bonless Wings", width=10, font=("Courier", 15),borderwidth=0)
    wings.grid(row=2, column=2, padx = 10, pady= 10, ipady = 21)
    
    popper_toast = tkinter.Button(choices, wraplength= 80, text="Popper Toast", width=10, font=("Courier", 15),borderwidth=0)
    popper_toast.grid(row=3, column=0, padx = 10, pady=10, ipady=21)

    jalapeno = tkinter.Button(choices, wraplength= 80, text="Jalapeno Poppers", width=10, font=("Courier", 15),borderwidth=0)
    jalapeno.grid(row=3, column=1, padx = 10, pady= 10, ipady = 21)

    

#-------------------------Widgets--------------------------#
Background_Frame = Frame(root, highlightbackground="Black", highlightthickness=2, background="seashell3")
Background_Frame.grid(row=0, column=0, columnspan=3, rowspan=3, padx=10)

top_menu = Frame(Background_Frame, background="seashell3")
top_menu.grid(row=0, column = 0)

top_choices = Frame(Background_Frame, background="seashell3")
top_choices.grid(row=0, column=1, pady=5)

top_ticket = Frame(Background_Frame, background="seashell3")
top_ticket.grid(row=0, column=2, pady=5)

menu = Frame(Background_Frame, background="seashell3")
menu.grid(row=1, column = 0, padx=10, rowspan=2)

choices = Frame(Background_Frame, highlightbackground="Black", highlightthickness=1, width=300, height=800, background="White")
choices.grid(row=1, column = 1, padx=10, sticky="NS", rowspan=2)

ticket = Frame(Background_Frame, highlightbackground="Black", highlightthickness=1, width=250, background="White")
ticket.grid(row=1, column = 2, padx=10, sticky="NS", rowspan=2)

bottom_menu = Frame(Background_Frame, background="seashell3")
bottom_menu.grid(row=3, column=0)

bottom_choices = Frame(Background_Frame, background="seashell3")
bottom_choices.grid(row=3, column=1, pady=5)

bottom_ticket = Frame(Background_Frame, background="seashell3")
bottom_ticket.grid(row=3, column=2)

#Buttons
#top widgets
menu_items = tkinter.Label(top_menu, text="Menu Items", font=("Courier", 30), borderwidth=0, background="seashell3", foreground="Black")
menu_items.grid(row=0, column=0, ipady=5, columnspan=2)

split= tkinter.Button(top_choices, text="Split", width=15, font=("Courier", 15), borderwidth=0)
split.grid(row=0, column=0, ipady=5, padx=5, pady=5)

combine= tkinter.Button(top_choices, text="Combine", width=15, font=("Courier", 15), borderwidth=0)
combine.grid(row=0, column=1, ipady=5, padx=5, pady=5)

void = tkinter.Button(top_ticket, text="void", font=("Courier", 15), borderwidth=0)
void.grid(row=0, column=0,ipady=5, pady=5, padx=5)

checks = tkinter.Button(top_ticket, text="Checks",width = 10, font=("Courier", 15), borderwidth=0)
checks.grid(row=0, column=1, ipady=5, pady=5, padx=5)

printer = tkinter.Button(top_ticket, text = "print", font=("Courier", 15), borderwidth=0)
printer.grid(row=0, column=2, ipady=5, pady=5, padx=5)


#Menu Buttons
drinks = tkinter.Button(menu, text="Drinks", width=10, font=("Courier", 15), borderwidth=0, command=lambda: drink_options())
drinks.grid(row=1, column=0, padx = 2, pady= 10, ipady = 30)

appetizers = tkinter.Button(menu, text="Appetizers", width=10, font=("Courier", 15),borderwidth=0, command=lambda: appetizer_options())
appetizers.grid(row=1, column=1, padx = 5, pady=10, ipady=30)

lunch_spcl = tkinter.Button(menu, wraplength= 80, text="Lunch Specials", width=10, font=("Courier", 15),borderwidth=0)
lunch_spcl.grid(row=2, column=0, padx = 5, pady= 10, ipady = 21)

salads = tkinter.Button(menu, text="Salads", width=10, font=("Courier", 15),borderwidth=0)
salads.grid(row=2, column=1, padx = 5, pady= 10, ipady = 30)

gourmet = tkinter.Button(menu, wraplength= 80, text="Gourmet Pizza's", width=10, font=("Courier", 15),borderwidth=0)
gourmet.grid(row=3, column=0, padx = 5, pady= 10, ipady = 21)

build = tkinter.Button(menu, wraplength= 80, text="Build Your Own", width=10, font=("Courier", 15),borderwidth=0)
build.grid(row=3, column= 1, padx = 5, pady= 10, ipady = 21)

kiddie = tkinter.Button(menu, text="Kiddie Menu", width=10, font=("Courier", 15),borderwidth=0)
kiddie.grid(row=4, column= 0, padx = 5, pady= 10, ipady = 30)

sandwiches = tkinter.Button(menu, text="Sandwiches", width=10, font=("Courier", 15),borderwidth=0)
sandwiches.grid(row=4, column= 1, padx = 5, pady= 10, ipady = 30)

desserts = tkinter.Button(menu, text="Desserts", width=10, font=("Courier", 15),borderwidth=0)
desserts.grid(row=5, column= 0, padx = 5, pady= 10, ipady = 30)

sides = tkinter.Button(menu, text="Side Items", width=10, font=("Courier", 15),borderwidth=0)
sides.grid(row=5, column= 1, padx = 5, pady= 10, ipady = 30)

catering = tkinter.Button(menu, text="Catering", width = 25, font=("Courier", 15),borderwidth=0)
catering.grid(row=6, column=0, pady = 5, ipady=20, columnspan=2)


#Choices Buttons


#Ticket Buttons
order= tkinter.Label(ticket, text="Order", bg="White", fg="Black", font=("Courier", 15),borderwidth=0)
order.grid(row = 0, column=1, columnspan=3, ipadx=121, ipady=5)

order_shown = Text(ticket, width=30, height= 30, highlightcolor="Black", highlightbackground="Black", highlightthickness=1, fg='Black', bg='White', font=("Courier", 15),borderwidth=0)
order_shown.grid(row=1, column= 1, ipadx=10)

total = Text(ticket, width=30, height= 5, fg='Black', bg='White', font=("Courier", 15), highlightcolor="Black", highlightbackground="Black", highlightthickness=1)
total.grid(row=2, column= 1, ipadx=10, padx=5, pady=5)


#bottom Widgets
table= tkinter.Button(bottom_choices, text="table", width=15,font=("Courier", 15),borderwidth=0)
table.grid(row=0, column=0, ipady=5, padx=5, pady=5)

discounts= tkinter.Button(bottom_choices, text="discounts", width=15, font=("Courier", 15),borderwidth=0, background="seashell3")
discounts.grid(row=0, column=1, ipady=5, padx=5, pady=5)

chain = tkinter.Button(bottom_ticket, text="Chain", font=("Courier", 15),borderwidth=0)
chain.grid(row=0, column=0,ipady=5, pady=5, padx=5)

pay = tkinter.Button(bottom_ticket, text="Staff Bank",width = 10, font=("Courier", 15),borderwidth=0)
pay.grid(row=0, column=1, ipady=5, pady=5, padx=5)

finish = tkinter.Button(bottom_ticket, text = "Done", font=("Courier", 15),borderwidth=0)
finish.grid(row=0, column=2, ipady=5, pady=5, padx=5)

cancel = tkinter.Button(bottom_menu, text = "Cancel", bg='red', fg='black', font=("Courier", 15),borderwidth=0)
cancel.grid(row=0, column=0, ipady=5, padx=5)
#-------------------------Images--------------------------#

root.mainloop()
