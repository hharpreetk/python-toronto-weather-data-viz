#%%
from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime

path = Path("weather_data/en_climate_daily_ON_6158355_2023_P1D.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract the percipitation.
dates, snows = [], []
for row in reader:
    current_date = datetime.strptime(row[4], "%Y-%m-%d")
    if row[12]:
        snow = int(row[12])
        if snow != 0:
            dates.append(current_date)
            snows.append(snow)

# Create the plot.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(dates, snows)

# Format plot.
ax.set_title("Daily Snow on Ground (cm), From January 1, 2023 to August 16, 2023", fontsize=16)
ax.set_xlabel("Dates (YYYY-MM-DD)")
fig.autofmt_xdate()
plt.ylabel('Snow on Ground (cm)')
plt.tight_layout()

plt.show()
