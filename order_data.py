from tkinter import *
import pandas as pd

order_data = pd.DataFrame()
order_items = pd.DataFrame()

class OrderData:
    def add_item(self, item_name, price):
        global current_order
    
        #Add to dataframe
        new_item = pd.DataFrame({item_name : [price]})
    
        return pd.concat([order_items, new_item], ignore_index=True)
    
    def close_order(self):
        pass
