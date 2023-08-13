import requests
from bs4 import BeautifulSoup
import mysql.connector
from time import sleep
import re 
import csv
first_car_name = input('''First car name 
ex) bmw or mercedes-benz
Enter : ''')
print('Receiving data from truecar.com please wait ...')

names_data1 = []
price_data1 = []
mile_data1 = []
location_data1 = []
color_data1 = []
model_data1 = []

page = int(input('''How many pages do you want to check?
tip : each page has 33 data
Enter: '''))
print('Wait ...')
for i in range(page):
    url = ('https://www.truecar.com/used-cars-for-sale/listings/%s/?page=%s' % (first_car_name.lower(), i+1))
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_ads = soup.find_all('div', attrs={'class' : 'flex w-full flex-col'})
#get names----------------------------------------------------------------------------------------------------------------------------------------------------  
    for item in all_ads:
        if item.find('span', attrs={'class' : 'truncate'}):
            cars_name1 = item.find('span', attrs={'class' : 'truncate'})
            names_data1.append(cars_name1.text)
#get price-------------------------------------------------------------------------------------------------------------------------------------
    for item in all_ads:
        if item.find('span', attrs={'data-test' : 'vehicleListingPriceAmount'}):
            cars_price1 = item.find('span', attrs={'data-test' : 'vehicleListingPriceAmount'})
            cars_price1n = re.sub(r'\D', '', cars_price1.text)
            price_data1.append(int(cars_price1n))
#get mile-------------------------------------------------------------------------------------------------------------------------------------
    for item in all_ads:
        if item.find('div', attrs={'data-test' : 'vehicleMileage'}):
            cars_mile1 = item.find('div', attrs={'data-test' : 'vehicleMileage'})
            cars_mile1n = re.sub(r'\D', '', cars_mile1.text)
            mile_data1.append(int(cars_mile1n))
#get location-------------------------------------------------------------------------------------------------------------------------------------
    for item in all_ads:
        if item.find('div', attrs={'data-test' : 'vehicleCardLocation'}):
            cars_location1 = item.find('div', attrs={'data-test' : 'vehicleCardLocation'})
            location_data1.append(cars_location1.text)
#get color---------------------------------------------------------------------------------------------------------------------------------------
    for item in all_ads:
        if item.find('div', attrs={'data-test' : 'vehicleCardColors'}):
            cars_color1 = item.find('div', attrs={'data-test' : 'vehicleCardColors'})
            color_data1.append(cars_color1.text)

#get model(year)-------------------------------------------------------------------------------------------------------------------------------------
    for item in all_ads:
        if item.find('span', attrs={'class' : 'vehicle-card-year text-xs'}):
            cars_model1 = item.find('span', attrs={'class' : 'vehicle-card-year text-xs'})
            model_data1.append(int(cars_model1.text))
 
#second car ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
second_car_name = input('''Second car name 
ex) bmw or mercedes-benz
Enter : ''')
print('>>> Receiving data from truecar.com please wait ...')

names_data2 = []
price_data2 = []
mile_data2 = []
location_data2 = []
color_data2 = []
model_data2 = []

page2 = int(input('''How many pages do you want to check?
tip : each page has 33 data
Enter: '''))
print('>>> Wait ...')

for i in range(page2):
    url2 = ('https://www.truecar.com/used-cars-for-sale/listings/%s/?page=%s' % (second_car_name.lower(), i+1))
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    all_ads2 = soup2.find_all('div', attrs={'class' : 'flex w-full flex-col'})
#get names----------------------------------------------------------------------------------------------------------------------------------------------------  
    for item2 in all_ads2:
        if item2.find('span', attrs={'class' : 'truncate'}):
            cars_name2 = item2.find('span', attrs={'class' : 'truncate'})
            names_data2.append(cars_name2.text)
#get price-------------------------------------------------------------------------------------------------------------------------------------
    for item2 in all_ads2:
        if item2.find('span', attrs={'data-test' : 'vehicleListingPriceAmount'}):
            cars_price2 = item2.find('span', attrs={'data-test' : 'vehicleListingPriceAmount'})
            cars_price2n = re.sub(r'\D', '', cars_price2.text)
            price_data2.append(int(cars_price2n))
#get mile-------------------------------------------------------------------------------------------------------------------------------------
    for item2 in all_ads2:
        if item2.find('div', attrs={'data-test' : 'vehicleMileage'}):
            cars_mile2 = item2.find('div', attrs={'data-test' : 'vehicleMileage'})
            cars_mile2n = re.sub(r'\D', '', cars_mile2.text)
            mile_data2.append(int(cars_mile2n))
#get location-------------------------------------------------------------------------------------------------------------------------------------
    for item2 in all_ads2:
        if item2.find('div', attrs={'data-test' : 'vehicleCardLocation'}):
            cars_location2 = item2.find('div', attrs={'data-test' : 'vehicleCardLocation'})
            location_data2.append(cars_location2.text)
#get color---------------------------------------------------------------------------------------------------------------------------------------
    for item2 in all_ads2:
        if item2.find('div', attrs={'data-test' : 'vehicleCardColors'}):
            cars_color2 = item2.find('div', attrs={'data-test' : 'vehicleCardColors'})
            color_data2.append(cars_color2.text)

#get model(year)-------------------------------------------------------------------------------------------------------------------------------------
    for item2 in all_ads2:
        if item2.find('span', attrs={'class' : 'vehicle-card-year text-xs'}):
            cars_model2 = item2.find('span', attrs={'class' : 'vehicle-card-year text-xs'})
            model_data2.append(int(cars_model2.text))

#All data readed from website !

cnx = mysql.connector.connect(
    host='',
    user='root',
    password='',
    database='myproject'
)
while True:
    print('>>> Connecting to database ...')
    sleep(1)
    break
print(">>> Connected!")
#                                   +-------+-------------+------+-----+---------+-------+
#                                   | Field | Type        | Null | Key | Default | Extra |
#                                   +-------+-------------+------+-----+---------+-------+
#                                   | name  | varchar(50) | YES  |     | NULL    |       |
#                                   | price | int(50)     | YES  |     | NULL    |       |
# My tables(firstcar,secondcar) >   | mile  | int(50)     | YES  |     | NULL    |       |
#                                   | loc   | varchar(50) | YES  |     | NULL    |       |
#                                   | color | varchar(50) | YES  |     | NULL    |       |
#                                   | model | int(50)     | YES  |     | NULL    |       |
#                                   +-------+-------------+------+-----+---------+-------+
cursor = cnx.cursor()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
cursor.execute('DELETE FROM firstcar')
cursor.execute('DELETE FROM secondcar')
#Old data deleted!---------------------------------------------------------------------------------------------------------------------------------------------------------------
for name,price,mile,location,color,model in zip(names_data1,price_data1,mile_data1,location_data1,color_data1,model_data1):
    cursor.execute("INSERT INTO firstcar VALUES ('%s', '%i', '%i', '%s', '%s', '%i')" % (name, price, mile, location, color, model))
for name,price,mile,location,color,model in zip(names_data2,price_data2,mile_data2,location_data2,color_data2,model_data2):
    cursor.execute("INSERT INTO secondcar VALUES (\'%s\', '%i', '%i', \'%s\', \'%s\', '%i')" % (name,price,mile,location,color,model))

cnx.commit()
while True:
    print('>>> Saving data to database ... ')
    sleep(1)
    break
while True:
    print('>>> Reading data from database ... ')
    sleep(1)
    break
cursor.execute('SELECT * FROM firstcar ORDER BY model')
print('%s sorted by model :' % first_car_name)
for i in cursor:
    print(i)

cursor.execute('SELECT * FROM secondcar ORDER BY model')
print('%s sorted by model :' % second_car_name)
for i in cursor:
    print(i)

#writing data in CSV
with open('Firstcar.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['LIST OF %s:' % first_car_name.upper()])
    writer.writerow(['Name | price | mile | location | color | model'])
    writer.writerow([])
    cursor.execute('select * from firstcar where model>2018 order by model desc')
    writer.writerow(["------------ Newer car sorted by model(year): ------------"])
    for row in cursor:
        writer.writerow(row)
    
    cursor.execute('select * from firstcar where model<=2018 order by model desc')
    writer.writerow([])
    writer.writerow(["------------ Older car sorted by model(year): ------------"])
    for row in cursor:
        writer.writerow(row)
    
    cursor.execute('select * from firstcar order by price desc limit 1')
    writer.writerow([])
    writer.writerow(['------------ The most expensive car: ------------'])
    for i in cursor:
        writer.writerow(i)

    cursor.execute('SELECT * FROM firstcar ORDER BY price ASC LIMIT 1')
    writer.writerow([])
    writer.writerow(['------------ The cheapest car: ------------'])
    for i in cursor:
        writer.writerow(i)
    
    cursor.execute('select avg(price) from firstcar')
    writer.writerow([])
    writer.writerow(['------------ Average of prices : ------------'])
    for i in cursor:
        writer.writerow(['%.0f$' % i])

    cursor.execute('select avg(mile) from firstcar')
    writer.writerow([])
    writer.writerow(['------------ Average of miles : ------------'])
    for i in cursor:
        writer.writerow(['%i miles' % i ])
    
    writer.writerow([])
    cursor.execute('SELECT * FROM firstcar ORDER BY mile DESC LIMIT 1 ')
    writer.writerow(['------------ Most used car : ------------'])
    for i in cursor:
        writer.writerow(i)
    
    writer.writerow([])    
    cursor.execute('SELECT * FROM firstcar ORDER BY mile ASC LIMIT 1 ')
    writer.writerow(['------------ Less used car : ------------'])
    for i in cursor:
        writer.writerow(i)

#write second car info 

cursor.execute('select * from secondcar where model>2018 order by model desc')
with open('Secondcar.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['LIST OF %s' % second_car_name.upper() ])
    writer.writerow(['Name | price | mile | location | color | model'])
    writer.writerow([])
    writer.writerow(["------------ Newer car sorted by model(year): ------------"])
    for row in cursor:
        writer.writerow(row)
    cursor.execute('select * from secondcar where model<=2018 order by model desc')
    writer.writerow([])
    writer.writerow(["------------ Older car sorted by model(year): ------------"])
    for row in cursor:
        writer.writerow(row)
    cursor.execute('select * from secondcar order by price desc limit 1')
    writer.writerow([])
    writer.writerow(['------------ The most expensive car: ------------'])
    
    for i in cursor:
        writer.writerow(i)

    cursor.execute('SELECT * FROM secondcar ORDER BY price ASC LIMIT 1')
    writer.writerow([])
    writer.writerow(['------------ The cheapest car: ------------'])
    for i in cursor:
        writer.writerow(i)
    
    cursor.execute('select avg(price) from secondcar')
    writer.writerow([])
    writer.writerow(['------------ Average of prices : ------------'])
    for i in cursor:
        writer.writerow(['%.0f$' % i])

    cursor.execute('select avg(mile) from secondcar')
    writer.writerow([])
    writer.writerow(['------------ Average of miles : ------------'])
    for i in cursor:
        writer.writerow(['%i miles' % i ])
    
    cursor.execute('SELECT * FROM secondcar ORDER BY mile DESC LIMIT 1 ')
    writer.writerow([])
    writer.writerow(['------------ Most used car : ------------'])
    for i in cursor:
        writer.writerow(i)
    writer.writerow([])    
    cursor.execute('SELECT * FROM secondcar ORDER BY mile ASC LIMIT 1 ')
    writer.writerow(['------------ Less used car : ------------'])
    for i in cursor:
        writer.writerow(i)

print('>>> Check csv files for more information')
print('Program done!')






































