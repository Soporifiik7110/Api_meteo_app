from tkinter import *
from api_test import vue_distance ,temp_fahrenheit, temp_celsius,feels_like_fahrenheit, feels_like_celsius, city, humidity, sunset_time, sunrise_time, weather1, wind_speed, humidity, description
import datetime as dt


print(f"Température a {city}: {temp_celsius:.2f}°C ou {temp_fahrenheit:.2f}°F")
print(f"Température a {city} ressentie: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
print(f"Température a {city}: {temp_celsius:.2f}°C ou {temp_fahrenheit:.2f}°F")
print(f"L'humiditée de {city}: {humidity:.2f}%")
print(f"la vitesse du vent: {wind_speed*3.6:.2f} km/h ou {wind_speed:.2f} m/s")
print(f'Description général de {city}: {description}')
print(f"Levée du soleil à {city} a {sunrise_time} heure local.")
print(f"Couché du soleil a {sunset_time} heure local")
print(f"la météo: {weather1}")
print(f"la description: {description}")
print(f"La vue: {vue_distance/1000:.2f} Kms")

mainf = Tk()
mainf.title("Météo")
mainf.geometry("1500x800")
#pour la vitesse du vent
Vitesse_vent = Label(mainf, text=f"Vitesse du vent: {wind_speed * 3.6:.2f} Km/h", font=("arial", 15), fg="blue")
Vitesse_vent.place(x=20, y=80)
#pour l'humiditée
humide = Label(mainf, text=f"Le taux d'humiditée: {humidity} %", font=("arial", 15), fg="blue")
humide.place(x=20, y=110)
#pour la ville le nom
ville = Label(mainf, text=f"{city}",  font=("arial", 30),  fg="black")
ville.place(x=600, y=5)
#pour image de fond de la visibilitée
photo1 = PhotoImage(file="vue.png")
nb = Label(mainf, image=photo1)
nb.place(x=1360, y=600)
#label pour la visibilitée
visible = Label(mainf, text=f"Visibilitée à: {vue_distance/1000:.2f} Km",  font=("arial", 15),  fg="black")
visible.place(x=1290, y=570)
mainloop()