from utils.create_gantt_data import create_gantt_data
import plotly.express as px
import plotly.graph_objects as go
from constants import COLORS, PATTERNS, LEGEND_DATA

class GanttChart:
    def __init__(self):
        self.df = create_gantt_data() # Create dataframe
        self.fig = self.create_timelines() # Create timeline bars
        self.style_bars() # Style timeline bars
        self.create_overlap_lines() # Create dotted lines for period overlap
        self.create_legend() # Create legend
        self.update_layout() # Set titles and y title tilt
        self.fig.update_yaxes(autorange='reversed') # Reverse rows so most recent periods are at the top

    # Create bars for maintenance/docking timelines 
    def create_timelines(self):
        return px.timeline(
            self.df,
            x_start='Start',
            x_end='End',
            y='Resource',  
            title='Ship Maintenance and Docking Periods',
            hover_name="Resource_Task",
            hover_data={
                'Resource': False,
                'Start': True,
                'End': True,
                'Duration (days)': True,
            },
            text='Duration (days)',
        )

    # Color/style bars
    def style_bars(self):
        self.fig.update_traces(
            # Color each bar based on ship index in COLORS list, cycle through colors if number of ships exceeds number of colors for scalability
            marker_color=[COLORS[int(row['Ship_Index']) % len(COLORS)] for _, row in self.df.iterrows() ], 
            marker_pattern_shape=[PATTERNS[i % 2] for i, _ in self.df.iterrows()], # Style each bar based on odd/even index
        )

    # Add dotted line between each timeline to highlight overlapping maintenance/docking periods
    def create_overlap_lines(self):
        for i, row in self.df.iterrows():
            if not i % 2:
                self.fig.add_shape(
                    type='line',
                    line_dash='dot',
                    line_color='black',
                    x0=row['Overlap_Start'],
                    x1=row['Overlap_End'],
                    y0=i + .5,
                    y1=i + .5,
                    legendgroup='Overlap',
                    name='Overlap', 
                )

    # Generate legend from LEGEND_DATA
    def create_legend(self):
        for data in LEGEND_DATA:
            self.fig.add_trace(go.Scatter(data))


    # Set axis titles and yaxis tickangle
    def update_layout(self):
        self.fig.update_layout(
            xaxis_title='Date',
            yaxis_title='Ships',
            barmode='stack',
            legend_title_text='',
            yaxis_tickangle=-30,
            #template='plotly_dark',
        )

    def display(self):
        self.fig.show()
       