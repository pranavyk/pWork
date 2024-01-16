import requests
from bs4 import BeautifulSoup

# Define the URL of the balance check page
url = "https://www.costco.com/costco-shop-card"

# Prompt the user to enter the card number and PIN
card_number = input("Enter the card number: ")
pin = input("Enter the PIN: ")

# Make an HTTP GET request to the balance check page
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
contents = BeautifulSoup(response.content, "html.parser")

# Find the form on the page and extract the CSRF token from it
form = contents.find("form", {"id": "costco-shop-card-form"})
csrf_token = form.find("input", {"name": "_csrf"})["value"]

# Construct the data to be submitted in the POST request
data = {
    "_csrf": csrf_token,
    "cardNumber": card_number,
    "cardPin": pin
}

# Make an HTTP POST request to submit the form data and retrieve the balance information
response = requests.post(url, data=data)

# Parse the HTML content of the response using BeautifulSoup
contents = BeautifulSoup(response.content, "html.parser")

# Find the element that contains the balance information and extract its text content
balance_element = contents.find("div", {"class": "card-value"})
balance = balance_element.text.strip()

# Print the balance information to the console
print("Card balance:", balance)