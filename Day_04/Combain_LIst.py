#Combain Lists
even_list = [2, 4, 6, 8]
odd_list = [1, 3, 5, 7, 9]
thierd_list = [even_list, odd_list]
print(thierd_list)
#########################################################################
## Treasure Map
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizonal = int(position[0])
vertical = int(position[1])
map[vertical - 1] [horizonal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")