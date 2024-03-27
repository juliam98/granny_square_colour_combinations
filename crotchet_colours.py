import itertools
import pandas as pd


repeat="Y" # Change to "N" if you don't want colours to repeat

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

if repeat==True:
    output_folder='output/repeating_colours/'
    # Generate all possible four-element combinations of the list using itertools.combinations_with_replacement with repeating colours
    combinations = pd.DataFrame(data=itertools.combinations_with_replacement(colours_RGB, 4))
elif repeat==False:
    # Generate all possible four-element combinations of the list using itertools.combinations with no repeating colours
    combinations = pd.DataFrame(data=itertools.combinations(colours_RGB, 4))
    output_folder='output/no_repeating_colours/'
else:
    raise ValueError(f"{repeat} is not a valid answer. Please reply with Y or N")

combinations.columns=('colour1','colour2','colour3','colour4')

colour_names=[]
for RGB_code in range(len(combinations)):
    # row in this iteration- pd.Series with frou RGB codes
    current_row=combinations.iloc[RGB_code]
    colours_each_row=[]
    # iterate over each column
    for column in range(len(current_row.index)):
        index_each_row=list(colours_RGB).index(current_row[column])
        name_of_colour=colour_list[index_each_row]
        colours_each_row.append(name_of_colour)
    colours_each_row_str = (colours_each_row[0]+'_'+colours_each_row[1]+'_'+colours_each_row[2]+'_'+colours_each_row[3])
    colour_names.append(colours_each_row_str)

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

for a in range(len(combinations)):

    #define Matplotlib figure and axis
    fig, ax = plt.subplots()
    plt.axis('off')

    #create simple line plot
    ax.set(xlim=(0, 10), ylim=(0, 10), aspect="equal")

    #add rectangle 1 to plot
    ax.add_patch(Rectangle((0, 0), 10, 10,
                facecolor = combinations['colour1'][a],
                fill=True,
                lw=5))

    #add rectangle 2 to plot
    ax.add_patch(Rectangle((1, 1), 8, 8,
                facecolor = combinations['colour2'][a],
                fill=True,
                lw=5))

    #add rectangle 3 to plot
    ax.add_patch(Rectangle((2, 2), 6, 6,
                facecolor = combinations['colour3'][a],
                fill=True,
                lw=5))

    #add rectangle 3 to plot
    ax.add_patch(Rectangle((3, 3), 4, 4,
                facecolor = combinations['colour4'][a],
                fill=True,
                lw=5))

    #save plot
    plt.savefig(fname=output_folder+colour_names[a]+'.png',bbox_inches='tight')
    plt.close()