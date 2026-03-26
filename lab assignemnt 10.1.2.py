import pandas as pd

data = {
    "State": ["Maharashtra", "Gujarat", "Rajasthan", "Goa", "Punjab"],
    "Area": [307713, 196024, 342239, 3702, 50362],
    "Population": [124000000, 68000000, 81000000, 1600000, 30000000]
}

df = pd.DataFrame(data)

print("\nComplete Information")
print(df)

largest_area = df.loc[df["Area"].idxmax()]
print("\nState with Largest Area:", largest_area["State"])

largest_population = df.loc[df["Population"].idxmax()]
print("\nState with Largest Population:", largest_population["State"])

df["Density"] = df["Population"] / df["Area"]

print("\nPopulation Density")
print(df[["State", "Density"]])

highest_density = df.loc[df["Density"].idxmax()]
print("\nState with Highest Population Density:", highest_density["State"])