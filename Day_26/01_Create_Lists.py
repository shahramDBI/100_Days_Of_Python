name = "Shahram"
letters_list = [letter for letter in name]
print(letters_list)
# Ressult# ['S', 'h', 'a', 'h', 'r', 'a', 'm'] ######
####################################################
names = ["Shahram", "Sara", "Angela", "Bahar", "Caroline"]
short_names = [name for name in names if len(name) < 5]
long_name = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(long_name)
# Ressult# ['Sara'] ######
# Ressult# ['SHAHRAM', 'ANGELA', 'CAROLINE'] ######
#####################################################