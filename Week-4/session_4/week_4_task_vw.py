import csv
from collections import namedtuple
import pandas as pd

Car = namedtuple("Car", "model year price transmission mileage fuelType tax mpg engineSize")
cars = []

with open("vw.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)

    for row in reader:
     new_car = Car(*row)
     cars.append(new_car)


#1. What is the most expensive VW car listed?

most_expensive_car = cars[0]
for car in cars:
    if int(car.price) > int(most_expensive_car.price):
        most_expensive_car = car
print(most_expensive_car)

#2 Find all the VW Golf models. What is their average price?

golf_models = 0
golf_total_price = 0

for car in cars:
   if "Golf" in car.model:
      golf_models += 1
      golf_total_price = golf_total_price + int(car.price)
print("The total amount of VW Golf models are " + str(golf_models) + ".")

golf_avg = golf_total_price / golf_models
print("The average price of all VW Golf models is " + str(golf_avg) + ".")

#3. What is the average milage for VW Polo models registered in 2020?

polo_mileage = 0 # will be used to find the total mileage
polo_count = 0 # used to see how many polos are registered in 2020

for car in cars:
   if "Polo" in car.model and car.year == "2020":
      polo_mileage = polo_mileage + int(car.mileage)
      polo_count += 1

#print(polo_count)
#print(polo_mileage)
polo_mileage_avg = polo_mileage/polo_count
print("The average mileage for VW Polo models registered in 2020 is "+ str(polo_mileage_avg) + ".")
