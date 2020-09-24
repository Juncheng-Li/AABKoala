import tkinter as tk
import requests
from LocalProgram.config import host
from LocalProgram.config import port
from LocalProgram.config import authorization
import pandas as pd
import json
import http.client
import mimetypes
from pandas import json_normalize
from LocalProgram.config import *
from datetime import datetime
import time
import math
import LocalProgram.resultRequest as rr
import LocalProgram.graphRequest as gr

HEIGHT = 500
WIDTH = 600
conn = http.client.HTTPConnection(host, port)

def test_function(entry):
    print("This is the entry:", entry)


# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

# def format_response(weather):
#     try:
#         name = weather['name']
#         desc = weather['weather'][0]['description']
#         temp = weather['main']['temp']
#
#         final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
#     except:
#         final_str = 'There was a problem retrieving that information'
#
#     return final_str
#
#
# def get_weather(city):
#     weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
#     url = 'https://api.openweathermap.org/data/2.5/weather'
#     params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
#     response = requests.get(url, params=params)
#     weather = response.json()
#
#     label['text'] = format_response(weather)


def retrieveResultWithID(resultID):
    payload = ''
    headers = {
        'Authorization': authorization,
    }
    conn.request("GET", "/graphs/results/" + resultID + "/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    content = bytes.decode(data, 'utf-8')
    df = json_normalize(json.loads(content))
    df.to_excel("download/" + "retrive" + resultID + datetime.now().strftime("%Y%m%d%H%H%S") + ".xlsx")
    print(data.decode("utf-8"))
    label['text'] = 'where is the data?'


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: rr.resultRequest().retrieveResultWithID(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='black', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)
# label.pack()
root.mainloop()
