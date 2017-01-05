planet_list = ["Mercury", "Mars"]
print(planet_list)

# Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)

# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
planet_list2 = ["Neptune", "Uranus"]
planet_list.extend(planet_list2)
print(planet_list)

# Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
print(planet_list)

# Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")
print(planet_list)

# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
rocky_planets = planet_list[0:4]
print(rocky_planets)

# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del planet_list[8]
print(planet_list)

# Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Jupiter')).

# spacecraft = tuple()
spacecraft = [('Cassini', 'Jupiter'),('Voyager I', 'Saturn'),('Mariner 10', 'Mercury'),('Pioneer', 'Mercury')]
print(spacecraft)

# Iterate over your list of planets and inside that loop, iterate over the list of tuples. Print, for each planet, which sattelites have visited.

for planet in planet_list:
    for craft in spacecraft:
        if craft[1] == planet:
            print("{} visited {}".format(craft[0], planet))
            print(planet, " was visited by ", craft[0])

