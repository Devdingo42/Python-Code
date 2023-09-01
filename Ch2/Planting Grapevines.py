#Planting Grapevines
#A vineyard owner is planting several new rows of grapevines, and needs to know how many
#grapevines to plant in each row. She has determined that after measuring the length of a
#future row, she can use the following formula to calculate the number of vines that will fit
#in the row, along with the trellis end-post assemblies that will need to be constructed at
#each end of the row:

#The length of the row, in feet
Length_R = (float(input('Enter the length of the row, in feet.')))

#• The amount of space used by an end-post assembly, in feet
Space_endpost_E = (float(input('Enter the amount of space used by an end-post assembly, in feet.')))

#• The amount of space between the vines, in feet
Space_vines_S = (float(input('Enter the amount of space between the vines, in feet.')))

#Number of grapevines that can fit
Number_Grapevines_Fit = (Length_R - (2 * Space_endpost_E)) / Space_vines_S

#User display
print('The number of grapevines that will fit in the row are', Number_Grapevines_Fit, 'grapevines.')