from tkinter import *
def get_weather():
    global scvalue
    lavel.config(text=f"Input Error")
    city_name = city_entry.get()
    api_key = "openweathermap.org"
    base_url = (f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric")

root=Tk()
root.geometry("600x500")
root.title("WEATHER APP")

background_image = PhotoImage(file="Screenshot (24).png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

lavel = Label(root, text="", font=("Arial", 12))
lavel.pack(pady=5)

lavel_1 = Label( text=" TRACK THE WEATHER FORECAST ", font=("Arial", 20))
lavel_1.pack(pady=10)

city =Label(root, text="Enter City Name:", font=("Arial", 14))
city.pack(pady=10)
city_entry =Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

weather_label =Label(root, text="Weather Info will appear here", font=("Arial", 12), wraplength=350)
weather_label.pack(pady=20)

search_button = Button(root, text="Search Weather", font=("Arial", 12),command=get_weather)
search_button.pack(pady=10)

root.mainloop()