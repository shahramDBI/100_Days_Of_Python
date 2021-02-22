# LIST
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
#Print List
print(states_of_america)
#First Index
print(states_of_america[0])
#Last Index
print(states_of_america[-1])
#Input
states_of_america[1] = "Penny"
print(states_of_america)
#Add
states_of_america.append("Shahramland")
print(states_of_america)
#Add
states_of_america.extend("Hiland", "Byeland")
print(states_of_america)
## Who's Paying
#Write your code below this line 👇
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
nam_item = len(names)
random_choice = random.randint(0, nam_item - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " Is goinig to buy the meal today")