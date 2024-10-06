import tkinter
from tkinter import *
import order_data

root = Tk()
root.title("Turoni's Pizza POS")
root.geometry = ("3000x650")
root.resizable(False, False)

#-------------------------Functions--------------------------#

current_order = []
current_subtotal : float = 0.00
current_tax : float = 0.00
current_total : float = 0.00

def add_to_list(item_name : str, price : float):
    #Global var
    global current_order
    
    #Add item to list box
    current_item = [item_name, price]
    current_order.append(current_item)
    order_shown.insert(END, item_name + '\n')
    order_shown.insert(END, "                      $")
    #Format price to 2 decimal places
    price_insert = "{: .2f}".format(float(price))
    order_shown.insert(END, price_insert)
    order_shown.insert(END, '\n')
    
    order_data.OrderData().add_item(item_name, price)
    add_to_total(price)
    
def add_to_total(price):
    #Global vars
    global current_subtotal
    global current_tax
    global current_total
    
    #Calculate subtotal, tax, total (format float for display)
    current_subtotal += price
    subtotal_insert = "{: .2f}".format(float(current_subtotal))
    current_tax += price * .07
    tax_insert = "{: .2f}".format(float(current_tax))
    current_total = current_subtotal + current_tax
    total_insert = "{: .2f}".format(float(current_total))
    
    
    #Delete everything from total textbox and rewrite after each item added
    total.delete("1.0", "end")
    total.insert(END, "Subtotal:                $")
    total.insert(END, subtotal_insert)
    total.insert(END, '\n')
    total.insert(END, "Tax:                     $")
    total.insert(END, tax_insert)
    total.insert(END, '\n')
    total.insert(END, "Total:                   $")
    total.insert(END, total_insert)
    
def sandwich_size(item_name):
    def half(item_name):
        new_name = item_name + " (half)"
        add_to_list(new_name, 6.87)
        size_window.destroy()
                
    def full(item_name):
        new_name = item_name + " (full)"
        add_to_list(new_name, 12.68)
        size_window.destroy()
    
    
    size_window = Toplevel(root)
    #Set window position
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    size_x = root_x + 400
    size_y = root_y + 200
    size_window.geometry(f'+{size_x}+{size_y}')
    
    size_window.title(item_name)
    #size_window.geometry("400x200")
    size_window.resizable(False, False)
    
    size_frame = Frame(size_window, width=380, height=180, background="seashell3", highlightbackground="Black", highlightthickness=2,)
    size_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", rowspan=3, columnspan=2)
    
    sizelbl = Label(size_frame, text="Size?", background="seashell3", fg="Black", font=("Courier", 12))
    sizelbl.grid(row=0, column=0, sticky="nsew", ipadx=167, columnspan=2)
    half_option = Button(size_frame, text="Half", width=10, font=("Courier", 15),borderwidth=0, bg="White", fg="Black", command=lambda: half(item_name))
    half_option.grid(row=1, column=0, ipady=20, pady=10)
    full_option = Button(size_frame, text="Full", width=10, font=("Courier", 15),borderwidth=0, bg="White", fg="Black", command=lambda: full(item_name))
    full_option.grid(row=1, column=1, ipady=20, pady=10)
    cancel = Button(size_frame, text="Cancel", width=5, font=("Courier", 15),borderwidth=0, bg="White", fg="Black")
    cancel.grid(row=2, column=0, ipady=10, pady=10, columnspan=2)
    
    
    

def drink_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    soft_drinks = tkinter.Button(choices, text="Soft Drinks", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Soft Drink", 2.50))
    soft_drinks.grid(row=1, column=0, padx = 10, pady= 10, ipady = 30)

    bottled_beer = tkinter.Button(choices, text="Bottled Beer", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Bottled Beer", 5.00))
    bottled_beer.grid(row=1, column=1, padx = 10, pady=10, ipady=30)

    draft = tkinter.Button(choices, text="Draft", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Draft Pint", 8.00))
    draft.grid(row=1, column=2, padx = 10, pady= 10, ipady = 30)

    brew_spcl = tkinter.Button(choices, wraplength= 80, text="Brewery Specials", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Brew Special", 9.00))
    brew_spcl.grid(row=2, column=0, padx = 10, pady= 10, ipady = 21)

    mixed_drinks = tkinter.Button(choices, text="Mixed Drinks", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Mixed Drink", 10.00))
    mixed_drinks.grid(row=2, column=1, padx = 10, pady= 10, ipady = 30)
    

def appetizer_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    garlic_toast = tkinter.Button(choices, text="Garlic Toast", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Garlic Toast", 5.94))
    garlic_toast.grid(row=1, column=0, padx = 10, pady= 10, ipady = 30)
    
    breadsticks = tkinter.Button(choices, text="Breadsticks", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Breadsticks", 5.94))
    breadsticks.grid(row=1, column=1, padx = 10, pady=10, ipady=30)

    mozzarella = tkinter.Button(choices, wraplength= 82, text="Mozarella Sticks", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Mozzarella Sticks", 9.31))
    mozzarella.grid(row=1, column=2, padx = 10, pady= 10, ipady = 21)

    grilled_cheese = tkinter.Button(choices, wraplength= 80, text="Grilled Cheese", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Grilled Cheez-Eze", 5.94))
    grilled_cheese.grid(row=2, column=0, padx = 10, pady= 10, ipady = 21)

    bruschetta = tkinter.Button(choices, text="Bruschetta", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Bruschetta", 7.93))
    bruschetta.grid(row=2, column=1, padx = 10, pady= 10, ipady = 30)
    
    wings = tkinter.Button(choices, wraplength= 80, text="Boneless Wings", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Boneless Wings", 9.31))
    wings.grid(row=2, column=2, padx = 10, pady= 10, ipady = 21)
    
    popper_toast = tkinter.Button(choices, wraplength= 80, text="Popper Toast", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Popper Toast", 8.27))
    popper_toast.grid(row=3, column=0, padx = 10, pady=10, ipady=21)

    jalapeno = tkinter.Button(choices, wraplength= 80, text="Jalapeno Poppers", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Jalapeno Poppers", 10.49))
    jalapeno.grid(row=3, column=1, padx = 10, pady= 10, ipady = 21)

def salad_options():
    for widget in choices.winfo_children():
        widget.destroy()
        
    italian = tkinter.Button(choices, wraplength= 80, text="Italian Salad", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Italian Salad", 11.41))
    italian.grid(row=1, column=0, padx = 10, pady= 10, ipady = 21)
    
    spinach = tkinter.Button(choices, wraplength= 80, text="Spinach Salad", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Spinach Salad", 10.14))
    spinach.grid(row=1, column=1, padx = 10, pady=10, ipady=21)

    house = tkinter.Button(choices, wraplength= 80, text="House Salad", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("House Salad", 6.29))
    house.grid(row=1, column=2, padx = 10, pady= 10, ipady = 21)

    greek = tkinter.Button(choices, wraplength= 80, text="Greek Salad", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Greek Salad", 10.14))
    greek.grid(row=2, column=0, padx = 10, pady= 10, ipady = 21)
    
def sandwich_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    stromboli = tkinter.Button(choices, text="Stromboli", width=10, font=("Courier", 15),borderwidth=0, command=lambda: sandwich_size("Stromboli"))
    stromboli.grid(row=1, column=0, padx = 10, pady= 10, ipady = 30)
    
    veggie_strom = tkinter.Button(choices, wraplength= 82, text="Veggie Stromboli", width=10, font=("Courier", 15),borderwidth=0, command=lambda: sandwich_size("Veggie Stromboli"))
    veggie_strom.grid(row=1, column=1, padx = 10, pady=10, ipady=21)

    ham_cheese = tkinter.Button(choices, wraplength= 82, text="Ham and Cheese", width=10, font=("Courier", 15),borderwidth=0, command=lambda: sandwich_size("Ham and Cheese"))
    ham_cheese.grid(row=1, column=2, padx = 10, pady= 10, ipady = 21)

    spicy_chk = tkinter.Button(choices, wraplength= 82, text="Spicy Stromboli", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Spicy Stromboli", 12.84))
    spicy_chk.grid(row=2, column=0, padx = 10, pady= 10, ipady = 21)

    vinny = tkinter.Button(choices, wraplength= 82, text="Vinny Burger", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Vinny Burger", 11.77))
    vinny.grid(row=2, column=1, padx = 10, pady= 10, ipady = 21)
    
    steak = tkinter.Button(choices, wraplength= 100, text="Chargrilled Steak", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Chargrilled Steak", 13.99))
    steak.grid(row=2, column=2, padx = 10, pady= 10, ipady = 21)
    
def pizza_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    house_spcl = tkinter.Button(choices, text="House\nSpecial", width=10, font=("Courier", 15),borderwidth=0)
    house_spcl.grid(row=1, column=0, padx = 10, pady= 10, ipady = 21)
    
    strom_pie = tkinter.Button(choices, text="Stromboli\nPie", width=10, font=("Courier", 15),borderwidth=0)
    strom_pie.grid(row=1, column=1, padx = 10, pady=10, ipady=21)

    marg = tkinter.Button(choices, text="Margarita", width=10, font=("Courier", 15),borderwidth=0)
    marg.grid(row=1, column=2, padx = 10, pady= 10, ipady = 30)

    hawaiian = tkinter.Button(choices, text="Hawaiian", width=10, font=("Courier", 15),borderwidth=0)
    hawaiian.grid(row=2, column=0, padx = 10, pady= 10, ipady = 30)

    vinny_p = tkinter.Button(choices, text="Vinny\nSpecial", width=10, font=("Courier", 15),borderwidth=0)
    vinny_p.grid(row=2, column=1, padx = 10, pady= 10, ipady = 21)
    
    iron = tkinter.Button(choices, text="Iron\nMan", width=10, font=("Courier", 15),borderwidth=0)
    iron.grid(row=2, column=2, padx = 10, pady= 10, ipady = 21)
    
    greek_p = tkinter.Button(choices, text="Greek", width=10, font=("Courier", 15),borderwidth=0)
    greek_p.grid(row=3, column=0, padx = 10, pady=10, ipady=30)

    veggie = tkinter.Button(choices, text="Veggie\nSpecial", width=10, font=("Courier", 15),borderwidth=0)
    veggie.grid(row=3, column=1, padx = 10, pady= 10, ipady = 21)
    
    meat = tkinter.Button(choices, text="Lots a\nMeat", width=10, font=("Courier", 15),borderwidth=0)
    meat.grid(row=3, column=2, padx = 10, pady= 10, ipady = 21)
    
    pepper = tkinter.Button(choices, text="Pepper\nPlanet", width=10, font=("Courier", 15),borderwidth=0)
    pepper.grid(row=4, column=0, padx = 10, pady=10, ipady=21)

    buffalo = tkinter.Button(choices, text="Buffalo", width=10, font=("Courier", 15),borderwidth=0)
    buffalo.grid(row=4, column=1, padx = 10, pady= 10, ipady = 30)

    bbq = tkinter.Button(choices, text="BBQ", width=10, font=("Courier", 15),borderwidth=0)
    bbq.grid(row=4, column=2, padx = 10, pady= 10, ipady = 30)
    
def dessert_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    cookies = tkinter.Button(choices, text="Cookies", width=10, font=("Courier", 15),borderwidth=0)
    cookies.grid(row=1, column=0, padx = 10, pady= 10, ipady = 30)
    cheesecake = tkinter.Button(choices, text="Cheesecake", width=10, font=("Courier", 15),borderwidth=0)
    cheesecake.grid(row=1, column=1, padx = 10, pady= 10, ipady = 30)
    ice_cream = tkinter.Button(choices, text="Ice Cream", width=10, font=("Courier", 15),borderwidth=0)
    ice_cream.grid(row=1, column=2, padx = 10, pady= 10, ipady = 30)
    
def cancel_menu():
    for widget in choices.winfo_children():
        widget.destroy()

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

choices = Frame(Background_Frame, highlightbackground="Black", highlightthickness=1, width=428, height=500, background="White")
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

salads = tkinter.Button(menu, text="Salads", width=10, font=("Courier", 15),borderwidth=0, command=lambda: salad_options())
salads.grid(row=2, column=1, padx = 5, pady= 10, ipady = 30)

gourmet = tkinter.Button(menu, wraplength= 80, text="Gourmet Pizzas", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_options())
gourmet.grid(row=3, column=0, padx = 5, pady= 10, ipady = 21)

build = tkinter.Button(menu, wraplength= 80, text="Build Your Own", width=10, font=("Courier", 15),borderwidth=0)
build.grid(row=3, column= 1, padx = 5, pady= 10, ipady = 21)

kiddie = tkinter.Button(menu, text="Kiddie Menu", width=10, font=("Courier", 15),borderwidth=0)
kiddie.grid(row=4, column= 0, padx = 5, pady= 10, ipady = 30)

sandwiches = tkinter.Button(menu, text="Sandwiches", width=10, font=("Courier", 15),borderwidth=0, command=lambda: sandwich_options())
sandwiches.grid(row=4, column= 1, padx = 5, pady= 10, ipady = 30)

desserts = tkinter.Button(menu, text="Desserts", width=10, font=("Courier", 15),borderwidth=0, command=lambda: dessert_options())
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

cancel = tkinter.Button(bottom_menu, text = "Cancel", bg='red', fg='black', font=("Courier", 15),borderwidth=0, command=lambda: cancel_menu())
cancel.grid(row=0, column=0, ipady=5, padx=5)
#-------------------------Images--------------------------#

root.mainloop()
print(current_order)
