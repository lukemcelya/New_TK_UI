from tkinter import *
import pandas as pd

temp_order = []
order_data_list = []
order_names = []
order_prices = []
order_df = pd.DataFrame()

class OrderData:
    def add_item(self, item_name, price):
        global order_items
        global order_names
        global order_prices

        order_names.append(item_name)
        order_prices.append(price)
    
    def close_order(self):
        global order_names
        global order_prices
        global order_data_list
        global temp_order
        
        tempdict = dict(zip(order_names, order_prices))
        temp_order = tempdict
        order_data_list.append(tempdict)
        order_names.clear()
        order_prices.clear()
        print(order_data_list)
            
    def add_order_to_df(self, subtotal, tax, total):
        global order_data_list
        global temp_order
        global order_df
        
        n_items : int = 0
        for items in temp_order:
            n_items += 1
        
        dictionary = {'Number of Items' : n_items, 'Subtotal' : subtotal, 'Tax' : tax, 'Total' : total}
        
        
        return pd.concat([order_df, dictionary], ignore_index=True)
        
        