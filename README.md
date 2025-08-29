# 🛒 Bazzar.hr Product Price Scraper

A simple Python script that scrapes **product name**, **current price**, and **lowest price in the last 30 days** from [Bazzar.hr](https://bazzar.hr) using `Requests` and `BeautifulSoup4`.

---

## 📦 Features

- ✅ Fetches product name  
- ✅ Fetches current product price  
- ✅ Fetches the lowest price in the last 30 days  
- ✅ Prints results in a clean formatted output  

---
## 🎯 Real-Life Use Case

This project was created out of a **real need**: while searching for an **air dryer (sušilica)** to buy, I wanted a quick way to check the **current price** and compare it with the **lowest price in the last 30 days** directly from Bazzar.hr.  
Instead of manually checking the page each time, the script provides the info instantly in the terminal.  


## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/bazzar-price-scraper.git
cd bazzar-price-scraper
```

### 2. Install dependencies

Make sure you have Python 3 and install the required packages:
```
pip install -r requirements.txt
```
### 3. Run the script
```
python scraper.py
```
Example output:
```
*******************************************************
Current price of product Končar dryer SR8VT2
is 399.00 €, and the lowest price
in the last 30 days was 349.00 €.
*******************************************************
```
🛠️ Customize

You can change the product URL in the script:
```
URL = "https://bazzar.hr/p/DEVEZQD-koncar-susilica-rublja-sr8vt2"
```

Replace it with any other product page from Bazzar.hr to scrape different products.

📄 License

MIT – free to use, modify, and distribute.

Made with ❤️ by VR

