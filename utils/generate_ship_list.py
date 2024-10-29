from models.ship import Ship
from models.time_period import TimePeriod
import pandas as pd
import os

# read in dataset and return a list of Ship objects
def generate_ship_list():
    print("cur directory: ", os.getcwd())
    df = pd.read_excel('dataset.xlsx')
    ships = []

    for _, row in df.iterrows():
        ship = Ship(
            name=row['Ship Name'],
            maintenance=TimePeriod(
                start=row['Maintenance Start Date'],
                end=row['Maintenance End Date']
            ),
            docking=TimePeriod(
                start=row['Docking Start Date'],
                end=row['Docking End Date']
            )  
        )

        ships.append(ship)

    return ships