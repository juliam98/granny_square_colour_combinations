# Granny square colour combinations

This code generates all possible colour combinations for crocheting granny squares. 

## How to use it
The `crotchet_squares` function takes the following input:
- `colour_list`: list of strings, representing the lables of each colour. This variable is used to name the files of each granny square that is generated. Duplicate labels are not allowed (e.g. if you have two shades of yellow and you assign the same label to them), as this will results in files being overwrritten.
- `colours_RGB`: list of tuples, each containing three floats. Each tuple reprersents the RGB value of your colours. The number of tuples in the list has to correspond to the number of labels in `colour_list` variable.
- `no_of_squares`: how many squares form one granny square. The default is 4.
- `repeat`: `"Y"` or `"N"` (default). Indicates if repeating colours are allowed in a single granny square.

In the `main.py` file add your RGB values and update the colour labels.

**Number of colours**: The current version of the code generates images of granny squares which consist of four squares. Therefore provide at least four colours to generate the combinations (if non-repeating). 

## Output:
The output are images representing the possible colour combinations for your granny squares. The pictures will be saved in `./output/repeating_colours/` or `./output/no_repeating_colours/`. 

The output gives you an idea of what your granny sqaures are going to look like:

<p align="center">
  <img src="https://github.com/juliam98/granny_square_colour_combinations/assets/93785710/6ab75e91-cd60-4542-a47e-258755dddf7e"  width="800">
</p>
