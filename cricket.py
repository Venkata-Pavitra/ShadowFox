import pandas as pd

data = [
    [1, 1, "Team A", "Player 1", 1, "Slip",
     "Cleanly picked the ball", "Clean Pick", "", 1, 1, "Stadium"],

    [1, 1, "Team A", "Player 2", 2, "Point",
     "Good throw towards wicket", "Good Throw", "Run Out", 0, 1, "Stadium"],

    [1, 1, "Team A", "Player 3", 3, "Mid On",
     "Took a catch", "Catch", "", 0, 1, "Stadium"]
]

columns = [
    "Match No.",
    "Innings",
    "Team",
    "Player Name",
    "Ballcount",
    "Position",
    "Short Description",
    "Pick",
    "Throw",
    "Runs",
    "Overcount",
    "Venue"
]

df = pd.DataFrame(data, columns=columns)
print(df)
df.to_csv("cricket_fielding_analysis.csv", index=False)
print("\nFile created successfully!")