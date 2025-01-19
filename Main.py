import tkinter as tk

import requests
API_KEY="a90edca8f5371093d13956fe80ba21cc"
BaseURL="http://api.openweathermap.org/data/2.5/weather"

def GetWether(CityName):
    print(CityName)
    url= f"{BaseURL}?q={CityName}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    # print(response)
    return response

def PrintWether(ServerResponse):
    pSeverTxt.config(text=ServerResponse)
    pWetherTXT.config(text=ServerResponse['weather'][0]['description'])
    pTempTXT.config(text=ServerResponse['main']['temp'])

def GetCityCountry():
    Town = pTownEntry.get()
    Country = pCountryEntry.get()
    ServerResponse = GetWether(Town + "," + Country)
    PrintWether(ServerResponse)


root = tk.Tk()
root.title('Tywydd')

pTownLabel = tk.Label(root, text="Town/City:")
pTownEntry = tk.Entry(root)
pCountryLabel = tk.Label(root, text="Country:")
pCountryEntry = tk.Entry(root)
pSearch = tk.Button(root, text="Search", command=GetCityCountry)

pWetherLabel = tk.Label(root, text="Weather:")
pTempLabel = tk.Label(root, text="Temperature °C:")
pServerLabel= tk.Message(root, text="Server API Data", bg="lightgray", fg="black")

pWetherTXT = tk.Message(root, bg="lightgray", fg="black")
pTempTXT = tk.Message(root, bg="lightgray", fg="black")
pSeverTxt = tk.Message(root, bg="lightgray", fg="black")

pTownLabel.grid(row=0, column=0, padx=60, pady=10)
pTownEntry.grid(row=0, column=1)
pCountryLabel.grid(row=1, column=0, padx=60)
pCountryEntry.grid(row=1, column=1)
pSearch.grid(row=2, column=1, pady=10)
pWetherLabel.grid(row=3, column=0, pady=10)
pWetherTXT.grid(row=3, column=1, pady=10)

pTempLabel.grid(row=4, column=0, pady=10)
pTempTXT.grid(row=4, column=1, pady=10)

pServerLabel.place(x=60, y=550)
pSeverTxt.place(x=60, y=600)
root.geometry("400x800")
root.mainloop()