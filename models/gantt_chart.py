import plotly.express as px
import plotly.graph_objects as go
from constants import PATTERNS, LEGEND_DATA
from models.user_options import UserOptions
from models.gantt_chart_data import GanttChartData

class GanttChart:
    def __init__(self):
        self.user_options = UserOptions() # Get choices from user
        self.chart_data = GanttChartData(self.user_options.has_demo_data) # Initialize chart data
        self.create_timelines() # Create timeline bars
        self.style_bars() # Style timeline bars
        self.create_overlap_lines() # Create dotted lines for period overlap
        self.create_legend() # Create legend
        self.update_layout() # Set titles and y title tilt

    # Create bars for maintenance/docking timelines 
    def create_timelines(self):
        fig = px.timeline(
            self.chart_data.df,
            x_start='Start',
            x_end='End',
            y='Resource',  
            title='Ship Maintenance and Docking Periods',
            hover_name="Resource_Task",
            hover_data={
                'Resource': False,
                'Start': '|%m-%d-%Y',
                'End': '|%m-%d-%Y',
                'Duration (days)': True,
                'Overlap Start': '|%m-%d-%Y',
                'Overlap End': '|%m-%d-%Y',
                'Overlap Duration (days)': True,
            },
            text='Duration (days)',
        )
        # Set the x tick interval to every 3 months
        fig.update_xaxes(
            dtick='M3',
            tickformat='%b %Y',
        ) 

        self.fig = fig

    # Color/style bars
    def style_bars(self):
        color_palette = self.user_options.color_palette
        df = self.chart_data.df
        self.fig.update_traces(
            # Color each bar based on ship index in color_palette list, cycle through colors if number of ships exceeds number of colors for scalability
            marker_color=[color_palette[row['Ship_Index'] % len(color_palette)] for _, row in df.iterrows() ], 
            marker_pattern_shape=[PATTERNS[row['Task_Index']] for _,row in df.iterrows()], # Style each bar based on odd/even index
        )

    # Add dotted line between each timeline to highlight overlapping maintenance/docking periods
    def create_overlap_lines(self):
        dark_mode = self.user_options.dark_mode
        df = self.chart_data.df
        for _, row in df.iterrows():
            # Skip row if there's no overlap
            if row['Overlap Start'] == 0:
                continue
            # Only create line for maintenance time periods, so there is one line per main/dock pair
            if row['Task_Index'] == 0:
                # Use same y value for each ship, based on index
                y = row['Ship_Index'] * 2 + .5
                self.fig.add_shape(
                    type='line',
                    line_dash='dot',
                    line_color='black' if not dark_mode else 'white',
                    x0=row['Overlap Start'],
                    x1=row['Overlap End'],
                    y0=y,
                    y1=y,
                    legendgroup='Overlap',
                    name='Overlap', 
                )

    # Generate legend from LEGEND_DATA
    def create_legend(self):
        for data in LEGEND_DATA:
            # Change colors if dark mode is selected
            if self.user_options.dark_mode:
                if 'line_color' in data:
                    data['line_color'] = 'white'
                if 'marker' in data:
                    data['marker']['color'] = 'black'
                    data['marker']['line']['color'] = 'white'
                    
            self.fig.add_trace(go.Scatter(data))


    # Set axis titles and yaxis tickangle
    def update_layout(self):
        layout_options = dict(
            xaxis_title='Date',
            yaxis_title='Ship',
            barmode='stack',
            legend_title_text='Legend',
            yaxis_tickangle=-30,
        )
        # Set template to dark mode if chosen by user
        if self.user_options.dark_mode:
            layout_options['template'] = 'plotly_dark'

        self.fig.update_layout(layout_options)
        self.fig.update_yaxes(autorange='reversed') # Reverse rows so most recent periods are at the top

    # Generate and display web interface
    def display(self):
        self.fig.show()
       