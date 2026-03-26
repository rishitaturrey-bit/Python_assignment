import pandas as pd

df = pd.read_csv("books.csv")

print("\nComplete Report")
print(df)

author = input("\nEnter Author Name: ")
print(df[df["Author"] == author])

publisher = input("\nEnter Publisher Name: ")
print(df[df["Publisher"] == publisher])

cheap = df.loc[df["Price"].idxmin()]
costly = df.loc[df["Price"].idxmax()]

print("\nCheapest Book")
print(cheap["Title"])

print("\nCostliest Book")
print(costly["Title"])

sorted_df = df.sort_values(by="Year")
print("\nBooks Sorted by Year")
print(sorted_df)