#Import requred libraries:
from selectorlib import Extractor
import requests 
import json
import csv
import mysql.connector

#Open a file with "w' (write) mode
f = open("data_output.csv", "w")

#Init our writer obj
writer = csv.writer(f)

#Writer our first row (for headers)
writer.writerow(["asin", "title", "rating", "totalReviews", "prices"])

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('page_selectors.yml')

#Define a user agent (the browser the website will see)
user_agent= 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'

#user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
headers = {'User-Agent': user_agent}

# Download the page using requests
r = requests.get("https://www.amazon.com/Xiaomi-128GB-6GB-RAM-Resolution/dp/B07R5ZYR77", headers=headers)

# Pass the HTML of the page and create an extract based on YML template
data = e.extract(r.text)
# Assign data to vars
asin = str(data['asin'])
title = str(data['title'])
rating = str(data['rating']).split(" ")[0]
totalReviews = str(data['totalReviews']).split(" ")[0]
prices = str(data["prices"])

#Create a connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Jaskat416"
)

print(mydb)

mycursor = mydb.cursor()

print(totalReviews)

#Update statement
sql = "UPDATE amazoncellphone.items SET asin = '"+asin+"', title = '"+title+"', rating='"+rating+"', totalReviews='"+totalReviews+"', prices='"+prices+"'  WHERE asin = '"+asin+"'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

#Write data to CSV
#writer.writerow([str(asin), str(title), str(rating), str(totalReviews), str(prices)])

print("Done.")

f.close()
