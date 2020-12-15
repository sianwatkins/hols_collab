import pandas as pd
import os

import tkinter as tk
from tkinter import filedialog

def hotelbooking():
    hotel = format_table(hotel)
    new_hotel = delete_cancelled(hotel)
    user_date = user_interface()
    hotel2 = select_7days(user_date, new_hotel)
    new = group(user_date)
    file = file()

hotel_booking()
