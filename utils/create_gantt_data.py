from utils.generate_ship_list import generate_ship_list
import pandas as pd

# Generate dataframe for use by plotly
def create_gantt_data():
    ships = generate_ship_list()
    data = []

    # Each key in ships dictionary represents a unique ship
    # so i can be used as a unique index for each ship 
    for i, ship_name in enumerate(ships.keys()):

        # Iterate through each ship object in the ships dictionary
        for ship in ships[ship_name]:

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
    df = df.sort_values(by=['Ship_Index', 'Task_Index']).reset_index(drop=True)

    return df



