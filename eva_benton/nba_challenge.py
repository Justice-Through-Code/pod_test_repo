print("Challenge 2.1:")
jamal_murray_3pts_made = 46
# TODO: Create variable for the number of 3pt shots made by Fred VanVleet
# TODO: Create a variable for the number of 3 pt shots made by James Harden

# creating variables for 3 point shaots made per each player Jamal Murray, Fred Vanvleet, and James Harden

jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37

print()


print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
# TODO: Create print statement here for Fred VanVleet
# TODO: Create print statement here for James Harden

# creating f-string per player indicating 3 point shots

print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")

print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3 point shots")

print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")

print()


print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")

# creating variables per player per 3 pint shot attempts

jamal_murray_3pts_attempts = 93
fred_vanvleet_3pts_attempts = 110
james_harden_3pts_attempts = 109


print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."

# challenge 2.2 statement extended to include 3 point shots per player

print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} "
      f"3 point shots and attempted {jamal_murray_3pts_attempts} 3 point shots")

print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} "
      f"3 point shots and attempted {fred_vanvleet_3pts_attempts} 3 point shots")

print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} "
      f"3 point shots and attempted {james_harden_3pts_attempts} 3 point shots")

print()



print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`

# three point percentage per player
jamal_murray_3pts_percentage = jamal_murray_3pts_made/jamal_murray_3pts_attempts
fred_vanvleet_3pts_percentage = fred_vanvleet_3pts_made/fred_vanvleet_3pts_attempts
james_harden_3pts_percentage = james_harden_3pts_made/james_harden_3pts_attempts

print(f"In the 2020 NBA playoffs, Jamal Murray's 3 point percentage was {jamal_murray_3pts_percentage}")
print(f"In the 2020 NBA playoffs, Fred VanVleet's 3 point percentage was {fred_vanvleet_3pts_percentage}")
print(f"In the 2020 NBA playoffs, James Harden's 3 point percentage was {james_harden_3pts_percentage}")


print('Challenge 3.1')
# paragraph printed out in single sentence per line

print('The Lakers went all in this offseason and swung a deal for former \
Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram,\
Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \
\nThose three have made good developments with the Pelicans, especially \
Brandon Ingram. \nBut the deal is still a huge win for the Lakers as Lebron\
, Davis, and company have put together an incredible season. \nLos Angeles \
has ridden James and Davis, along with a supporting cast built around them, \
to the second-best record in the NBA. \nThe Lakers ended the season atop\
the Western Conference with a record of 49-14. \nThey were narrowly behind \
the Bucks for the best record in the league. \nDavis proved to the final \
piece necessary for the Lakers to rebound from missing the playoffís last \
year. \nLos Angeles was a dominant club on both sides of the ball and are \
in a position to have another successful year next season. ')


print('Challenge 3.2')
# paragraph printed out in single sentence per line

paragraph = 'The Lakers went all in this offseason and swung a deal for former \
Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram,\
Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \
\nThose three have made good developments with the Pelicans, especially \
Brandon Ingram. \nBut the deal is still a huge win for the Lakers as Lebron\
, Davis, and company have put together an incredible season. \nLos Angeles \
has ridden James and Davis, along with a supporting cast built around them, \
to the second-best record in the NBA. \nThe Lakers ended the season atop\
the Western Conference with a record of 49-14. \nThey were narrowly behind \
the Bucks for the best record in the league. \nDavis proved to the final \
piece necessary for the Lakers to rebound from missing the playoffís last \
year. \nLos Angeles was a dominant club on both sides of the ball and are \
in a position to have another successful year next season. '


print(paragraph.upper())



print('Challenge 3.3 Boolean and f-string')
# creating boolean variable
lakers_are_best = False

# creating f-string
print(f'The statement that the Lakers are the best NBA team is \
{lakers_are_best}.')
