# List of colors to be used in order for each bar
COLORS = (
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
)

PATTERNS = (
    '',
    'x',
)


LEGEND_DATA = (

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
    
)

DEMO_SHIP_DATA = {
    'Ship Name': (
        'USS George Washington', 'USS John Adams', 'USS Thomas Jefferson',
        'USS James Madison', 'USS James Monroe', 'USS John Qunicy Adams',
        'USS Andrew Jackson', 'USS Martin Van Buren', 'USS Germantown',
        'USS John Tyler'
    ),
    'Maintenance Start Date': (
        '10/1/2025', '10/1/2025', '4/1/2026', 
        '4/1/2027', '7/1/2027', '10/1/2027',
        '4/1/2028', '4/1/2028', '7/1/2028', 
        '4/20/2029'
    ),
    'Maintenance End Date': (
        '1/1/2026', '1/1/2026', '7/1/2026',
        '7/1/2027', '10/1/2027', '1/1/2028',
        '7/1/2028', '7/1/2028', '10/1/2028',
        '8/20/2029'
    ),
    'Docking Start Date': (
        '10/1/2025', '10/1/2025', '4/1/2026',
        '4/1/2027', '7/1/2027', '11/16/2027',
        '4/16/2028', '4/1/2028', '7/16/2028',
        '4/20/2029'
    ),
    'Docking End Date': (
        '11/1/2025', '12/15/2025', '4/30/2026',
        '5/1/2027', '9/1/2027', '12/15/2027',
        '6/1/2028', '6/15/2028', '8/31/2028',
        '7/30/2029'
    ),
}