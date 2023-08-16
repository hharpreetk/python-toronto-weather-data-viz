# %%
from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime
#%%
path = Path("weather_data/en_climate_daily_ON_6158355_2023_P1D.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# Extract the dates and temperatures
dates, highs, lows, means = [], [], [], []
for row in reader:
    current_date = datetime.strptime(row[4], "%Y-%m-%d")
    high = float(row[8])
    low = float(row[9])
    mean = float(row[10])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)
    means.append(mean)
#%%
# Plot the High and Low Temperatures (°C)
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily High and Low Temperatures (°C), From January 1, 2023 to August 16, 2023", fontsize=16)
ax.set_xlabel("Dates (YYYY-MM-DD)")
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)")
plt.tight_layout()

# Show the plot.
plt.show()
#%%
# Plot the Mean Temperatures (°C)
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(dates, means, color='green')

# Format plot.
ax.set_title("Daily Mean Temperatures (°C), From January 1, 2023 to August 16, 2023", fontsize=16)
ax.set_xlabel("Dates (YYYY-MM-DD)")
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)")
plt.tight_layout()

plt.show()
#%%
