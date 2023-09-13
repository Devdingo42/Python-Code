#18. Restaurant Selector
#Write a program that asks whether any members of your party are vegetarian, vegan, or
#gluten-free, to which then displays only the restaurants to which you may take the group.
#Here is an example of the program’s output

#User input
print()
vegetarian = input('Is anyone in your party a vegetarian? ')
print()
vegan = input('Is anyone in your party a vegan? ')
print()
gluten_free = input('Is anyone in your party gluten-free? ')
print()

if vegetarian == 'yes' or vegetarian == 'no':
    if vegetarian == 'yes':
        if vegan == 'yes':
            if gluten_free == 'yes':
                print("You and your friends can go to Corner Café or The Chef's Kitchen.")
        else: 
         if gluten_free == 'yes':
                print("You and your friends can go to Main Street Pizza Company ")
         else:
                if vegan == 'no' and vegetarian == 'yes':
                    print ("You and your freinds can go to Mama's Fine Italian")
    else:
        if vegetarian == 'no' and vegan == 'no' and gluten_free == 'no':
            print("You and your freinds can go eat at Joe's Gourmet Burgers")
else:
    print("Error!, Please Enter 'yes' or 'no'")
print()