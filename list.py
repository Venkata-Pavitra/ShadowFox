justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

#Question 1
print("Number of members:", len(justice_league))
print(justice_league)

#Question 2
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding members:")
print(justice_league)

#Question 3
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman leader:")
print(justice_league)

#Question 4
justice_league.remove("Superman")
aquaman_position = justice_league.index("Aquaman")
justice_league.insert(aquaman_position + 1, "Superman")
print("After moving Superman:")
print(justice_league)

#Question 5
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]
print("New Justice League:")
print(justice_league)

#Question 6
justice_league.sort()
print("Alphabetically sorted:")
print(justice_league)
print("New leader:", justice_league[0])