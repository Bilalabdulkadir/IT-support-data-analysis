import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# IT Support Ticket Analysis
# Author: Bilal Abdulkadir Muhammed
# -------------------------------

def analyze_tickets(file_path="tickets.csv"):
    data = pd.read_csv(file_path)

    # Clean data
    data = data.dropna(subset=["ResolutionTime", "IssueType"])

    # Metrics
    avg_time = data["ResolutionTime"].mean()
    median_time = data["ResolutionTime"].median()
    issue_counts = data["IssueType"].value_counts()

    # Save summary report
    with open("analysis_summary.txt", "w") as f:
        f.write("IT Support Analysis Report\n\n")
        f.write(f"Average Resolution Time: {avg_time:.2f} minutes\n")
        f.write(f"Median Resolution Time: {median_time:.2f} minutes\n\n")
        f.write("Issue Type Counts:\n")
        f.write(issue_counts.to_string())

    # Visualization
    plt.figure(figsize=(8,6))
    issue_counts.plot(kind='bar')
    plt.title("IT Support Tickets by Issue Type")
    plt.xlabel("Issue Type")
    plt.ylabel("Number of Tickets")
    plt.tight_layout()
    plt.savefig("issue_type_chart.png")

    return avg_time, median_time, issue_counts


# Run analysis
if __name__ == "__main__":
    analyze_tickets()