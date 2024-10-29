from utils.generate_ship_list import generate_ship_list
import pandas as pd

# generate dataframe for use by plotly
def create_gantt_data():
    ships = generate_ship_list()
    data = []
    
    for i, ship in enumerate(ships):
        # create unique y value for ship, leaving space for value for maint/dock
        ship_y_value = i * 2

        # add maintenance and docking data
        for j, task in enumerate(['maintenance', 'docking']):
            period = getattr(ship, task)
            data.append({
                'Task': task.capitalize(),
                'Start': period.start,
                'End': period.end,
                'Duration': period.duration,
                'Resource': ship.name,
                'Y': ship_y_value - (j * 1.5) #if j == 1 else ship_y_value + (j * 2.75)
            })

    df = pd.DataFrame(data)


    return df.sort_values(by=['Resource', 'Task'])
    


