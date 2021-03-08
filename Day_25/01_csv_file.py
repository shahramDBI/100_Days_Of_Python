# CSV File ####################################
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
###################################################
# Import CSV ###################################
import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)
