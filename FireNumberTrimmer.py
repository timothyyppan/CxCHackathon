#Trims fire_number until there is just the first letter that represents a region
def trim_fire_number(fire_number):
    trimmed_fire_number = []
    for num in fire_number:
        trimmed_fire_number.append(num[:1])
    
    return trimmed_fire_number
