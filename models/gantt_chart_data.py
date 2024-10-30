import pandas as pd
from constants import DEMO_SHIP_DATA
from models.ship import Ship
from models.time_period import TimePeriod


class GanttChartData:

    def __init__(self, has_demo_data):
        self.has_demo_data = has_demo_data 
        self.create_chart_data()


    # read in dataset and create a dictionary of Ship objects
    def generate_ship_list(self):
        df = pd.read_excel('dataset.xlsx')
        
        # Add demo data if chosen by user
        if self.has_demo_data:
            df = self.add_demo_data(df)
        
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
        
        self.ships =  ships
    
    # Add demo data to dataset to showcase ability to handle 
    # multiple periods per ship
    def add_demo_data(self, df):
       
        demo_df = pd.DataFrame(DEMO_SHIP_DATA) 

        date_columns = [
            'Maintenance Start Date', 'Maintenance End Date',
            'Docking Start Date', 'Docking End Date'
        ]
        # Convert date fields to same timestamp objects as original dataset
        demo_df[date_columns] = demo_df[date_columns].apply(pd.to_datetime)

        # concat original dataset with formatted demo dataset
        return pd.concat([df, demo_df], ignore_index=True)

    # Generate the dataframe to be used for generating the chart
    def create_chart_data(self):
        self.generate_ship_list()
        data = []

        # Each key in ships dictionary represents a unique ship
        # so i can be used as a unique index for each ship 
        for i, ship_name in enumerate(self.ships.keys()):
            # Iterate through each ship object in the ships dictionary
            for ship in self.ships[ship_name]:
                # Add maintenance and docking data with j used as an index 
                # to signify task type
                for j, task in enumerate(['maintenance', 'docking']):
                    period = getattr(ship, task)
                    overlap = ship.overlap # Get overlap period, if any, for highlighting
                    data.append({
                        'Task': task.capitalize(),
                        'Start': period.start,
                        'End': period.end,
                        'Overlap Start': overlap.start if overlap else 0,
                        'Overlap End': overlap.end if overlap else 0,
                        'Overlap Duration (days)': overlap.duration.days if overlap else 0,
                        'Duration (days)': period.duration.days,
                        'Resource': ship.name if not j else ' ' * i, # Change resource to whitespace for docking bar to avoid cluttering y axes
                        'Resource_Task': f'{ship.name} - {task.capitalize()}', # Combine ship name and task for labeling
                        'Ship_Index': i,
                        'Task_Index': j,
                    })

        df = pd.DataFrame(data)

        # Sort dataframe by ship index, then when those are the same by task index
        self.df = df.sort_values(by=['Ship_Index', 'Task_Index']).reset_index(drop=True)