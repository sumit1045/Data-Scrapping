import requests
from bs4 import BeautifulSoup
import pandas as pd

data = pd.read_csv("sheet.csv")

print(data.columns)
print(data['Unnamed: 1'])

addressed_found = []

try:
    for place in data['Unnamed: 1']:
        # Send a GET request to the URL and get the HTML response
        response = requests.get(place)
        html = response.content

        # Use BeautifulSoup to parse the HTML and extract the address
        soup = BeautifulSoup(html, "html.parser")

        address = soup.find("div", class_="address")
        address_extracted = []

        if address == None:
            address = soup.find("div", id ="address")
            if address != None:
                for para in address.find_all("p"):
                    #print(para.get_text())
                    address_extracted.append(para.get_text())


        # Print the extracted address
        print(" ".join(address_extracted))
        addressed_found.append(" ".join(address_extracted))

except:
    print("Exception occured")


df = pd.DataFrame(addressed_found)
df.to_csv(index=False)
