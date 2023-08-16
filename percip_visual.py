# %%
from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime

path = Path("weather_data/en_climate_daily_ON_6158355_2023_P1D.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract the percipitation.
dates, percips = [], []
for row in reader:
    current_date = datetime.strptime(row[4], "%Y-%m-%d")
    percip = float(row[11])
    if percip != 0:
        dates.append(current_date)
        percips.append(percip)

# Plot the Total Precipitation (mm).
# The sum of the total rainfall and the water equivalent of the total snowfall in millimetres (mm), observed at the location during a specified time interval.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(dates, percips, color='green')

# Format plot.
ax.set_title("Daily Total Perciptations (mm), From January 1, 2023 to August 16, 2023", fontsize=16)
ax.set_xlabel("Dates (YYYY-MM-DD)")
fig.autofmt_xdate()
plt.ylabel('Total Precipitation (mm)')
plt.tight_layout()

plt.show()