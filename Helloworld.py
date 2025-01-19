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

ServerResponse = GetWether("Cambridge, NZ")
root = tk.Tk()
root.title('Tywydd')

pTownLabel = tk.Label(root, text="Town/City:")
pTownEntry = tk.Entry(root)
pCountryLabel = tk.Label(root, text="Country:")
pCountryEntry = tk.Entry(root)
pSearch = tk.Button(root, text="Search")
pSeverTxt = tk.Message(root, text=ServerResponse, bg="lightgray", fg="black")

pTownLabel.grid(row=0, column=0, padx=60, pady=10)
pTownEntry.grid(row=0, column=1)
pCountryLabel.grid(row=1, column=0, padx=60)
pCountryEntry.grid(row=1, column=1)
pSearch.grid(row=2, column=1, pady=10)
pSeverTxt.place(x=60, y=600)
root.geometry("400x800")
root.mainloop()