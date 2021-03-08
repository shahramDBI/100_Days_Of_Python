import pandas

data = pandas.read_csv("weather_data.csv")
# Print CSV ################################
# print(data)
# Print Temp Only ##########################
# print(data["temp"])
# Print Type ###############################
# print(type(data))
# Print Type [] ############################
# print(type(data["temp"]))
# Change To Dict ###########################
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(f"temp_list is: {temp_list}")
# print(len(temp_list))
# Average Of temperatures ###################
# average = sum(temp_list) / len(temp_list)
# print(f"Average temperatures: {average}")
# print(data["temp"].mean())
# Max Of temperatures ###################
# print(data["temp"].max())
# Get Data in Columns #######################
# print(data["condition"])
# print(data.condition)
# Get Data in Row #########################
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# Print Temp F #########################################
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(f"Monday temperatures F: {monday_temp_F}")
# # Create a Dataframe from scratch ####################
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")
