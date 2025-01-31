import requests
import datetime as dt
import smtplib
MY_LAT=51.507351
MY_LANG=-0.127758
FORMATED=0
def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    print(response)
    if response.status_code==404:
        raise Exception("That resource does not exist")
    elif response.status_code==401:
        raise Exception("You are not authorized to access")
    response.raise_for_status()
    data=response.json()
    iss_latitude=float(data["iss_position"]["latitude"])
    iss_longitude=float(data["iss_position"]["longitude"])
    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LANG-5<=iss_longitude<=MY_LAN:
        return True
from tkinter import *

def get_quote():
    response=requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    quote=response.json()["quote"]
    canvas.itemconfig(quote_text,text=quote)
    #Write your code here.
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
window.mainloop()

def is_night():
    parameters={"lat":MY_LAT,
                "lng":MY_LANG,
                "formatted":FORMATED}
    response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data_1=response.json()
    data=int(data_1["results"]["sunrise"].split("T")[1].split(":")[0])
    data1=int(data_1["results"]["sunset"].split("T")[1].split(":")[0])
    print(data)
    print(data1)
    time_now=dt.datetime.now().hour
    if time_now<=data or time_now>=data1:
        return True
if is_iss_overhead() and is_night():
    with smptlib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="anvyuka  77f",password="aifr'q8 ruf")
        connection.sendmail(from_addr="ajcvkgatfua",to_addrs="kklhzltr7iqyr.qwlfaa",msg="Subject:It is dark")


