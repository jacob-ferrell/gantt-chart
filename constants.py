# List of colors to be used in order for each bar
COLORS = [
    # red
    '#b91c1c',
    # orange
    '#c2410c',
    # yellow
    '#a16207',
    # lime
    '#4d7c0f',
    # emerald
    '#047857',
    # cyan
    '#0e7490',
    # blue
    '#1d4ed8',
    # violet
    '#6d28d9',
    # fuchsia
    '#a21caf',
    # pink
    '#be185d',
]

PATTERNS = [
    '',
    'x',
]


LEGEND_DATA = [

    # Maintenance legend entry
    dict(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=10, color='white', line=dict(color='black', width=1), symbol='square'),  # White box with black border
        name='Maintenance',
        legendgroup='Maintenance',  
        showlegend=True,
    ),
    # Overlap legend entry
    dict(
        x=[None],  
        y=[None],
        mode='lines',
        line_dash='dot',
        line_color='black',  
        name='Overlap',  
        legendgroup='Overlap',  
        showlegend=True,  
    ),
    # Docking legend entry
    dict(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=10, color='white', line=dict(color='black', width=1), symbol='x'),  # White box with 'x' pattern
        name='Docking',
        legendgroup='Docking',  
        showlegend=True,
    ),
    
]