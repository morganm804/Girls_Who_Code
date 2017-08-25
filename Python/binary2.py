####### BINARY SEARCH #######
import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')
length = len(countries)

# Prompt user to enter a city - Pay attention the the lower/higher case letters
print("What country are you looking for?:")
searchKey = input('')
Key=searchKey.capitalize()
# Initialize variables
foundCity = ""
notfound = True
firstPoint = 0
lastPoint = len(countries)-1
# Loop thru the citiesList by updating the midPoint
while (notfound and firstPoint<=lastPoint):
    midPoint = int((firstPoint + lastPoint) / 2)
    # If the city found
    if (Key==countries[midPoint]):  # ADD YOUR CODE HERE
        notfound=False
        foundCity=Key
        break
   # Else if the city is less than the citiesList midPoint in an alphabetic order
    elif (Key<countries[midPoint]):  # ADD YOUR CODE HERE
        lastPoint=midPoint-1
   # Else if the city is greater than the citiesList midPoint in an alphabetic order
    elif (Key>countries[midPoint]):  # ADD YOUR CODE HERE
        firstPoint=midPoint+1

# If the city is found, then print the city name. Else, print an error message
if (notfound == False):
    print("Your country is in the country list. It is %s." % foundCity)
else:
    print("Your country is not in the country list!")
