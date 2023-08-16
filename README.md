# Data Visualization Practice Project: Toronto Weather Analysis

## Introduction

This repository contains Python scripts for visualizing weather data from Toronto City, Ontario. The data includes information such as temperature, precipitation, and snowfall for specific dates in the year 2023.

Data Source: [Government of Canada - Historical Climate Data](https://climate.weather.gc.ca/historical_data/search_historic_data_e.html)

## Requirements

- Python 3.x
- Matplotlib

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/toronto-weather-analysis.git
   ```

2. Install the required packages:

   ```bash
   pip install matplotlib
   ```

## Usage

### High and Low Temperatures Visualization

Run the `temps_visual.py` script to visualize the daily high and low temperatures.

```bash
python temps_visual.py
```

This script will generate a plot showing the daily high and low temperatures for the specified date range.

### Mean Temperatures Visualization

Run the `temps_visual.py` script to visualize the daily mean temperatures.

```bash
python temps_visual.py
```

This script will generate a plot showing the daily mean temperatures for the specified date range.

### Snow on Ground Visualization

Run the `snow_visual.py` script to visualize the daily snow on the ground.

```bash
python snow_visual.py
```

This script will generate a plot showing the daily snow on the ground (in centimeters) for the specified date range.

### Precipitation Visualization

Run the `percip_visual.py`` script to visualize the daily total precipitation.

```bash
python percip_visual.py
```
This script will generate a plot showing the daily total precipitation (in millimeters) for the specified date range.


## Data Source

The weather data used for this project is sourced from the [Government of Canada - Historical Climate Data](https://climate.weather.gc.ca/historical_data/search_historic_data_e.html).

## Notes

- This project is for educational purposes and demonstrates basic data visualization techniques using Matplotlib in Python.
- The data used is a subset of the complete dataset available from the provided source.

## License

This project is licensed under the [MIT License](LICENSE).