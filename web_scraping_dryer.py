from bs4 import BeautifulSoup
import requests

URL = "https://bazzar.hr/p/DEVEZQD-koncar-susilica-rublja-sr8vt2"

response = requests.get(URL)
# print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

name = soup.find("h1", attrs={"class": "h2 font-weight-bold mb-2"})
product_name = name.text.strip() if name else "N/A"

price = soup.find("div", attrs={"class": "h3 mb-0 text-primary font-weight-bold mr-2"})
product_price = price.get_text(strip=True) if price else "N/A"

low_price = soup.find("dd", attrs={"class": "col-7 col-sm-7 col-lg-8"})
lowest_price = low_price.text  # type: ignore


print(
    f"""
      *******************************************************
      Current price of product {product_name}         
      is {product_price},and the lowest price
      in the last 30 days was {lowest_price}.     
      ******************************************************* 
"""
)

