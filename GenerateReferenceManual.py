from ColourCode import MAJOR_COLORS, MINOR_COLORS, color_pair_to_string, get_pair_number_from_color
def reference_manual_generator():
    reference ={}
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            reference[get_pair_number_from_color(major_color, minor_color)] = color_pair_to_string(major_color, minor_color)
            
    return reference 
