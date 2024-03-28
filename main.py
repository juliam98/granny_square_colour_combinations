from get_colours import crotchet_squares

# Change to "N" if you don't want colours to repeat, and "Y" if you want to allow for repetitions
repeat="N" 

colour_list=[
    'yellow',
    'pink',
    'magenta',
    'burgundy',
    'green',
    'blue',
    'navy',
    'purple'
]

colours_RGB=[
    (0.92549, 0.9098, 0.42353), # yellow
    (0.86667, 0.6902, 0.85882), # pink
    (0.69412, 0.21961, 0.44706), # magenta
    (0.49804, 0.13333, 0.32941), #burgundy
    (0.2, 0.55686, 0.3098), # green
    (0.1451, 0.58824, 0.7451), # blue
    (0.20392, 0.41961, 0.78824), # navy
    (0.33333, 0.27059, 0.57647) # purple
]

# Use this function to generate your squares
crotchet_squares(colour_list=colour_list, colours_RGB=colours_RGB, no_of_squares=5, repeat="N")