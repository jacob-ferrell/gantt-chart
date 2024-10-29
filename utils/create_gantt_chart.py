import plotly.express as px
from utils.create_gantt_data import create_gantt_data
from constants import COLORS

# create the gantt chart from the processed data
def create_gantt_chart():
    # Generate the DataFrame
    df = create_gantt_data()


    
    # Plot the Gantt chart
    fig = px.timeline(
        df,
        x_start='Start',
        x_end='End',
        y='Resource',  
        title='Ship Maintenance and Docking Periods',
        hover_name="Resource_Task",

    )
    
    # Update layout to show only ship names in the specified order
    fig.update_layout(
        xaxis_title='Date',
        yaxis=dict({
            'categoryorder': 'array',
            'categoryarray': df.index
        }),
        yaxis_title='Ships',
        barmode='overlay',
        legend_title_text='Task Type',
        #template='plotly_dark',
    )

    fig.update_yaxes(autorange='reversed')
    
    # Color each bar based on index in COLORS list 
    fig.update_traces(
        marker_color=[COLORS[i] for i, _ in df.iterrows() ]
    )

    fig.show()