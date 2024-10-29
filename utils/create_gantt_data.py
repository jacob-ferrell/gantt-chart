from utils.generate_ship_list import generate_ship_list
import pandas as pd

# generate dataframe for use by plotly
def create_gantt_data():
    ships = generate_ship_list()
    data = []
    
    for i, ship in enumerate(ships):

        # add maintenance and docking data
        for j, task in enumerate(['maintenance', 'docking']):
            period = getattr(ship, task)
            data.append({
                'Task': task.capitalize(),
                'Start': period.start,
                'End': period.end,
                'Duration': period.duration,
                'Resource': ship.name if not j else ' ' * i,
                'Resource_Task': f'{ship.name} - {task.capitalize()}',
                'Ship_Index': i,
                'Task_Index': j,
                'Index': len(data)
            })

    df = pd.DataFrame(data)
    df = df.sort_values(by=['Ship_Index', 'Task_Index']).reset_index(drop=True)
    
    return df



    


