"""
using lists,
Print different areas 
of the house , using variables
"""
# whole data for different areas of house
areas = ["kitchen" , 7.88, "dining room", 13.0, 
        "terrace", 20.34,"toilet", 6.55,"room1", 7.98,
         "room2", 12, "hallway", 4.23]
#Print the second element         
print(areas[1])
#Print the last item
print(areas[-1])
#Print the area of the terrace
print(areas[5])
#Print from the first element to the third element
print(areas[0:2])
#Print from the third element to the last
print(areas[-3])
#Print the total area of the two rooms
print(areas[-3+-5])
#Modify the toilet area and print the new list area
