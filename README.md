Challenges:
- using plotly express timelines to display two different timelines per ship was the first major challenge.  plotly express timelines does not natively support this, so I created individual rows for each docking/maintenance period for each ship with the y axis title for the docking period being a string of whitespace with length equivalent to the ships index.  I then sorted the dataframe by ship index and task index.

- coloring the bars was the next challenge, as using the 'color' option for plotly timelines disrupted the original order of the dataframe.  I was able to overcome this by using the 'marker_color' option in the update_traces method to set the color of each bar based on its ship index, which corresponded to a list I created with hard-coded colors for each ship.

- Using different styling for maintenance/docking periods was the next challenge, which was solved similarly to the coloring, by applying style to each bar based on whether its index in the dataframe was odd/even

