print("Challenge: Favourite Restaurants")

print()

print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. 

Go through the dictionary and print out the following 3 pieces of information about the restaurant: 
1. The latitude and longitude of Four Barrel Coffee 
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. 
3. The website of Four Barrel Coffee
'''


restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}


print(restaurant)

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
print(f"{restaurant['latitude']} longitude is {restaurant['longitude']}")
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
print(f"{restaurant['address1']} {restaurant['city']}, {restaurant['state']}, {restaurant['zip_code']}, {restaurant['country']}")
# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print(restaurant['url'])

print()

print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
restaurant_1 = {
        "name" : "parc",
        "address" : '227 s 18th st, pa 19123',
        "favourite_dish" : "stake and eggs"
}

restaurant_2 = {
        'name' : 'jims',
        'address' : '13 s 20th st, pa 19423',
        'favourite_dish' : 'fish and chips'
}

restaurant_3 = {
        'name' : 'kfc',
        'address' : '17 s arch st, pa 19043',
        ' favourite_dish' : 'chicken'
}
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)

# TODO: Print each dictionary

print(restaurant_1)

print(restaurant_2)

print(restaurant_3)
# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich" }
'''

print()

print("Question 3")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there. 
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
restaurant_1.pop("favourite_dish")
print(restaurant_1)
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant

print()

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address. 
Update just this value in that restaurant's dictionary
'''
restaurant_2["address"] = "23th s filbert st pa 19123"
# TODO: Update the address field of 1 restaurant 
print(restaurant_2['address'])
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
# TODO: Print the updated dictionary.
print(restaurant_2)

print()