
print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()
for m in range(len(meats)):
    meats[m] = meats[m].capitalize()
for c in range(len(cheeses)):
    meats[m] = cheeses[m].capitalize()
print(meats)

print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []
for meat in meats:
    for cheese in cheeses:
        sandwiches.append(f'{meat} & {cheese}')
print(sandwiches)

print('Question 3')


# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'

yourorder = input('What kind of sandwich would you like?')


for sandwich in sandwiches:
    if yourorder == sandwich:
        print(f'Great choice! 1 {yourorder} coming right up!')
        break