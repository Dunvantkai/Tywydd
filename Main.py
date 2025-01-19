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
    pWindTXT.config(text=ServerResponse['wind']['speed'])
    pHumidityTXT.config(text=ServerResponse['main']['humidity'])
    pLongitudeTXT.config(text=ServerResponse['coord']['lon'])
    pLatitudeTXT.config(text=ServerResponse['coord']['lat'])

def GetCityCountry():
    Town = pTownEntry.get()
    Country = pCountryEntry.get()
    ServerResponse = GetWether(Town + "," + Country)
    PrintWether(ServerResponse)

# 
root = tk.Tk()
root.title('Tywydd')
pTownLabel = tk.Label(root, text="Town/City:")
pTownEntry = tk.Entry(root)
pCountryLabel = tk.Label(root, text="Country:")
pCountryEntry = tk.Entry(root)
pSearch = tk.Button(root, text="Search", command=GetCityCountry)
# labels
pWetherLabel = tk.Label(root, text="Weather:")
pTempLabel = tk.Label(root, text="Temperature °C:")
pWindLabel = tk.Label(root, text="Wind Speed m/s:")
pHumidityLabel = tk.Label(root, text="Humidity %:")
pLongitudeLabel = tk.Label(root,text="Longitude:")
pLatitudeLabel = tk.Label(root, text="Latitude:")
pServerLabel= tk.Message(root, text="Server API Data", bg="lightgray", fg="black")
# texts
pWetherTXT = tk.Message(root, bg="lightgray", fg="black")
pTempTXT = tk.Message(root, bg="lightgray", fg="black")
pWindTXT = tk.Message(root, bg="lightgray", fg="black")
pHumidityTXT = tk.Message(root, bg="lightgray", fg="black")
pLongitudeTXT = tk.Message(root, bg="lightgray", fg="black")
pLatitudeTXT = tk.Message(root, bg="lightgray", fg="black")
pSeverTxt = tk.Message(root, bg="lightgray", fg="black")
# prints
pTownLabel.grid(row=0, column=0, padx=60, pady=10)
pTownEntry.grid(row=0, column=1)
pCountryLabel.grid(row=1, column=0, padx=60)
pCountryEntry.grid(row=1, column=1)
pSearch.grid(row=2, column=1, pady=10)
pWetherLabel.grid(row=3, column=0, pady=10)
pWetherTXT.grid(row=3, column=1, pady=10)
pTempLabel.grid(row=4, column=0, pady=10)
pTempTXT.grid(row=4, column=1, pady=10)
pWindLabel.grid(row=5, column=0, pady=10)
pWindTXT.grid(row=5, column=1, pady=10)
pHumidityLabel.grid(row=6, column=0, pady=10)
pHumidityTXT.grid(row=6, column=1, pady=10)
pLongitudeLabel.grid(row=8, column=0, pady=10)
pLongitudeTXT.grid(row=8, column=1, pady=10)
pLatitudeLabel.grid(row=7, column=0, pady=10)
pLatitudeTXT.grid(row=7, column=1, pady=10)
pServerLabel.place(x=60, y=550)
pSeverTxt.place(x=60, y=600)
root.geometry("400x800")
root.mainloop()