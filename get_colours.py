import itertools
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def crotchet_squares(colour_list:list[str], colours_RGB:list[tuple[float]], no_of_squares:int=4, repeat:str="N"):
    """
    Generate schematic representation of granny squares to crotchet.

    no_of_squares: How many squares form one granny square. Default value is 4.
    repeat: Y, N - whether the colour combinations should repeat the same colour in one granny square. Default is N - no colour repetitions in a square. If Y is chosen, colour repetitions are allowed. 
    """

    # Check if variables provieded are correct:
    if len(colour_list)!=len(colours_RGB): #All colours should have corresponding labels
        raise Exception("The number of colour labels provided has to correspond to the number of RBG colour values.")

    if len(colour_list)!=len(set(colour_list)): #Labels should not have any repetitions
        raise Exception("The colour labels have to be unique, otherwise files will get overwritten!")

    if repeat=="Y":
        output_folder='output/repeating_colours/'
        # Generate all possible four-element combinations of the list using itertools.combinations_with_replacement with repeating colours
        combinations = pd.DataFrame(data=itertools.combinations_with_replacement(colours_RGB, no_of_squares))
    elif repeat=="N":
        # Generate all possible four-element combinations of the list using itertools.combinations with no repeating colours
        combinations = pd.DataFrame(data=itertools.combinations(colours_RGB, no_of_squares))
        output_folder='output/no_repeating_colours/'
    else:
        raise ValueError(f"{repeat} is not a valid answer. Please reply with Y or N")
    
    
    # Create the output folder if doesn't already exists
    try:
        os.mkdir(output_folder)
    except FileExistsError:
        pass

    combinations = pd.DataFrame(data=itertools.combinations(colours_RGB, no_of_squares))
    combinations.columns = ['colour{}'.format(i) for i in range(1, no_of_squares + 1)]

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
        colours_each_row_str = '_'.join(colours_each_row)
        # colours_each_row_str = (colours_each_row[0]+'_'+colours_each_row[1]+'_'+colours_each_row[2]+'_'+colours_each_row[3])
        colour_names.append(colours_each_row_str)

    x, y = 0, 0
    width, height = no_of_squares*2+2, no_of_squares*2+2
    # print(len(colour_names) + "number of colour names")
    for a in range(len(combinations)):
        # corrent row- each has a set of colours for one square
        current_row=combinations.iloc[a]
        #define Matplotlib figure and axis
        fig, ax = plt.subplots()
        plt.axis('off')
        #create simple line plot
        ax.set(xlim=(0, width), ylim=(0, height), aspect="equal")

        for i in range(no_of_squares):
            # add rectangle
            ax.add_patch(Rectangle((x+i, y+i), width-(i*2), height-(i*2),
                    facecolor = current_row[i],
                    fill=True,
                    lw=5))
            
        #save plot
        plt.savefig(fname=output_folder+colour_names[a]+'.png',bbox_inches='tight', pad_inches=0.0)
        plt.close()

    print(f"{len(combinations)} squares were created! I have saved them in this path: {output_folder}\nHappy crocheting!")