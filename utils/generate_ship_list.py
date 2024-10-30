from models.ship import Ship
from models.time_period import TimePeriod
import pandas as pd
from constants import DEMO_SHIP_DATA

# read in dataset and return a list of Ship objects
def generate_ship_list():
    df = add_demo_data(pd.read_excel('dataset.xlsx'))
    # Use a dict where the ship name is the key and the val is list of ship objects so 
    # multiple time periods can be supported for each ship
    ships = {} 

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
        ships[ship.name] = ships.get(ship.name, []) + [ship]
    
    return ships

# Give user option to add demo data to dataset to showcase ability to handle 
# multiple periods per ship
def add_demo_data(df):
    acceptable_choices = ['1', '2']
    choice = None
    choice = '1' # auto select 1 for development
    while choice not in acceptable_choices:
        choice = input('\nSelect one of the following options:\n1. Generate chart with original data\n2. Generate chart with demo data, showcasing handling of multiple maintenance/docking periods per ship\n')

    if choice == '1':
        return df
    
    demo_df = pd.DataFrame(DEMO_SHIP_DATA) 

    date_columns = [
        'Maintenance Start Date', 'Maintenance End Date',
        'Docking Start Date', 'Docking End Date'
    ]

    demo_df[date_columns] = demo_df[date_columns].apply(pd.to_datetime)

    return pd.concat([df, demo_df], ignore_index=True)
