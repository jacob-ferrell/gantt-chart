from utils.generate_ship_list import generate_ship_list
import pandas as pd
from utils.find_overlap import find_overlap

# Generate dataframe for use by plotly
def create_gantt_data():
    ships = generate_ship_list()
    data = []
    
    for i, ship in enumerate(ships):

        # Add maintenance and docking data
        for j, task in enumerate(['maintenance', 'docking']):
            period = getattr(ship, task)
            # Get overlap period, if any, for highlighting
            overlap = ship.overlap
            data.append({
                'Task': task.capitalize(),
                'Start': period.start,
                'End': period.end,
                'Overlap_Start': overlap.start if overlap else None,
                'Overlap_End': overlap.end if overlap else None,
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



    


