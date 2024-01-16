from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/gigabyte-geforce-rtx-4070-ti-gv-n407tgaming-oc-12gd/p/N82E16814932580?Item=N82E16814932580&SoldByNewegg=1&quicklink=true"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.findAll(string = "$")
print(prices[0].parent.find("strong").string)

print()