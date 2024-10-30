# Gantt Chart

### Description
This project is a gantt chart designed to display the docking/maintenance periods for a list of ships.

### Design
- This project was designed using an object oriented approach.  While the project could be completed without the use of classes, the implementation of some object oriented design principles supports clean, modular, organized, and maintainable code
- Plotly was chosen to generate the graph for its enhanced interactivity over other libraries such as matplotlib
- Pandas was chosen for its simple data processing capabilities and seamless compatibility with Plotly

### Languages and Libraries
- Python programming language
- Pandas, Plotly, Openpyxl

### Features
- Maintenance and docking periods are grouped by ship with maintenance bar directly above the docking bar
- Dotted lines showing periods of overlap, if any, are inbetween each ship's periods
- Periods are color-coded based on their ship
- Maintenance/docking periods are differentiated by style, with maintenance periods having no style and docking periods having a cross-hatched style overlayed on the bar.
- The duration, in days, of each period is displayed within each bar
- Hovering over each bar will display data such as ship name, period type, start date, end date, duration in days, overlap start date, overlap end date, and overlap duration in days
- A legend to clarify what the different styles represent
- For scalability, the program supports datasets where there are multiple rows (multiple maintenance/docking periods) for each ship 
- Users can chooce between light/dark mode, a selection of different color palettes, 

### Challenges
- Using plotly express' timelines to display both the docking and maintenance periods, with docking below maintenance, was the first challenge as this is not natively supported by the timelines object.  This was overcome by giving each period its own row in the dataframe with a Ship_Index indicating which ship it belonged to and a Task_Index indicating which kind of period it was. All rows with a Task_Index indicative of being a docking period were given Y-axis titles of whitespace with length equivalent to the ship's index.  The dataframe was then sorted by Ship_Index and Task_Index.
- Coloring the bars was challenging, as using the 'color' option for plotly timelines disrupted the original order of the dataframe.  I was able to overcome this by using the 'marker_color' option in the update_traces method to set the color of each bar based on its ship index, which corresponded to a list I created with hard-coded colors for each ship.  A similar approach was used to style the periods.

### Installation



