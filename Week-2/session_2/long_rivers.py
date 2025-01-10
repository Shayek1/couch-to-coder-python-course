#list of dicts for week 2 tasks
rivers = [
 {"name": "Nile", "length": 4157},
 {"name": "Yangtze", "length": 3434},
 {"name": "Murray-Darling", "length": 2310},
 {"name": "Volga", "length": 2290},
 {"name": "Mississippi", "length": 2540},
 {"name": "Amazon", "length": 3915}
]

#task 1 - printing out each river's name
for river in rivers:
    print(river["name"])

#task 2
total_length_river = 0
for river in rivers:
    total_length_river += river["length"]
print("The total river length is " + str(total_length_river) + ".")

#Extension 1
for river in rivers:
    if river["name"].startswith("M"):
     print(river["name"])


#Extension 2
for river in rivers:
    river_km = river["length"] * 1.6
    print(river_km)