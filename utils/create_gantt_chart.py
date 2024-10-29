import plotly.express as px
from utils.create_gantt_data import create_gantt_data

# create the gantt chart from the processed data
def create_gantt_chart():
  # Generate the DataFrame
    df = create_gantt_data()
    
    # Extract the unique ship names in the original order
    unique_ships = df['Resource'].unique()
    
    # Plot the Gantt chart
    fig = px.timeline(
        df,
        x_start='Start',
        x_end='End',
        y='Y',  # Use numeric y values to allow stacking
        color='Task',
        title='Ship Docking and Maintenance Periods',
        hover_name="Resource"
    )
    
    # Update layout to show only ship names in the specified order
    fig.update_layout(
        xaxis_title='Date',
        barmode='overlay',
        yaxis=dict(
            title='Ships',
            tickvals=[i * 2 for i in range(len(unique_ships))],  # Sets spacing for Y labels
            ticktext=unique_ships,  # Ship names as labels
        ),
        legend_title_text='Task Type'
    )

    fig.show()