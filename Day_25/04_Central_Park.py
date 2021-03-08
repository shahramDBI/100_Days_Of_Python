import pandas

data = pandas.read_csv("Central_Park_Squirrel_Census_-_Squirre.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(f"Gray Count: {grey_squirrel_count}")
print(f"Cinnamon Count: {cinnamon_squirrel_count}")
print(f"Black Count: {black_squirrel_count}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
