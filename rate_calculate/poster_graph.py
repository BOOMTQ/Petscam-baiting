import matplotlib.pyplot as plt
import numpy as np
import json

from secret import MODEL_HISTORY_PATH

# Load the data from the JSON file
with open(MODEL_HISTORY_PATH, 'r') as file:
    data = json.load(file)

# Extract the scam emails data
scam_emails = data['scam_emails']

# Initialize dictionaries to store inbound count and time difference hours
inbound_counts = {}
time_diff_hours = {}

# Loop over each email and aggregate the data
for email, details in scam_emails.items():
    sol = details['sol_used']
    if sol:  # If 'sol_used' is not an empty string
        if sol not in inbound_counts:
            inbound_counts[sol] = []
            time_diff_hours[sol] = []
        inbound_counts[sol].append(details['inbound_count'])
        time_diff_hours[sol].append(details['time_diff_hours'])

# Create arrays for plotting
sol_used = list(inbound_counts.keys())
inbound_counts_min = [min(v) for v in inbound_counts.values()]
inbound_counts_max = [max(v) for v in inbound_counts.values()]
inbound_counts_avg = [np.mean(v) for v in inbound_counts.values()]
time_diff_hours_min = [min(v) for v in time_diff_hours.values()]
time_diff_hours_max = [max(v) for v in time_diff_hours.values()]
time_diff_hours_avg = [np.mean(v) for v in time_diff_hours.values()]

# Set up positions for the bars
positions = np.arange(len(sol_used))

# Plotting the bar charts for Inbound Counts
plt.figure(figsize=(14, 6))
plt.bar(positions - 0.2, inbound_counts_min, width=0.2, label='Min', color='skyblue')
plt.bar(positions, inbound_counts_avg, width=0.2, label='Average', color='seagreen')
plt.bar(positions + 0.2, inbound_counts_max, width=0.2, label='Max', color='sandybrown')
plt.xticks(positions, sol_used, rotation=0, ha='center')
plt.xlabel('Repliers participated')
plt.ylabel('Number of email conversations')
plt.title('Email conversations between repliers and scammers')
plt.legend()
plt.tight_layout()
plt.show()

# Plotting the bar charts for Time Hours
plt.figure(figsize=(14, 6))
plt.bar(positions - 0.2, time_diff_hours_min, width=0.2, label='Min', color='skyblue')
plt.bar(positions, time_diff_hours_avg, width=0.2, label='Average', color='seagreen')
plt.bar(positions + 0.2, time_diff_hours_max, width=0.2, label='Max', color='sandybrown')
plt.xticks(positions, sol_used, rotation=0, ha='center')
plt.xlabel('Repliers participated')
plt.ylabel('Time (Hours)')
plt.title('Time wasted by each replier')
plt.legend()
plt.tight_layout()
plt.show()