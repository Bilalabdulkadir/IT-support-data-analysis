import pandas as pd

data = pd.read_csv("tickets.csv")

print("Average Resolution Time:", data["ResolutionTime"].mean())
print("\nIssue Counts:\n", data["IssueType"].value_counts())
