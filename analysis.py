import pandas as pd
import matplotlib.pyplot as plt

print("Starting IT Support Data Analysis...")

# Load data
data = pd.read_csv("tickets.csv")

# --- Basic Analysis ---
avg_time = data["ResolutionTime"].mean()
issue_counts = data["IssueType"].value_counts()

print("\nAverage Resolution Time:", avg_time)
print("\nIssue Counts:\n", issue_counts)

# --- Chart 1: Issue Type Count ---
plt.figure()
issue_counts.plot(kind='bar')
plt.title("Number of Tickets by Issue Type")
plt.xlabel("Issue Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("issue_type_chart.png")
plt.close()

# --- Chart 2: Resolution Time Distribution ---
plt.figure()
data["ResolutionTime"].plot(kind='hist', bins=5)
plt.title("Resolution Time Distribution")
plt.xlabel("Minutes")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("resolution_time_chart.png")
plt.close()

print("\nCharts created successfully!")