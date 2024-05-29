from tkinter import *
import requests

root = Tk()
def get_weather():
    city = entercity.get()
    key = "eb2d874646ac2a33fee383722928a247"
    url = "https://openweathermap.org/data/2.5/weather"
    params = {"APPID": key, "q": city, "units": "metric"}
    result = requests.get(url, params=params)
    weather = result.json()
    info["text"] = f'{str(weather["name"])}: {weather["main"]["temp"]}'

root.title("Погода")
root.geometry("300x300")
root.resizable(width=False, height=False)
canvas = Canvas(root, height=300, width=300)
canvas.pack()

frameuser = Frame(root, bg="red")
frameuser.place(relx=0.10, rely=0.10, relwidth=0.8, relheight=0.3)
frameweather = Frame(root, bg="red")
frameweather.place(relx=0.10, rely=0.50, relwidth=0.8, relheight=0.3)

btnweather = Button(frameuser, text="Посмотреть погоду", bg="white", command=get_weather)
btnweather.pack()
entercity = Entry(frameuser, bg="white")
entercity.pack()

info = Label(frameweather, text="Информация о погоде", bg="white", font=40)
info.pack()

root.mainloop()