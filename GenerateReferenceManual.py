from ColourCode import MAJOR_COLORS, MAJOR_COLORS, color_pair_to_string
def reference_manual_generator():
    pair_number = 1
    reference ={}
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            reference[pair_number] = color_pair_to_string(major_color, minor_color)
            pair_number +=1
            
    return reference 
