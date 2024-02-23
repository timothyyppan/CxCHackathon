#Maps a letter to a region
def get_region_from_letter(letter):
    title_mapping = { 
        'C' : 'Calgary',
        'E' : 'Edson',
        'H' : 'High Level',
        'G' : 'Grande Prairie',
        'L' : 'Lac La Biche',
        'M' : 'Fort McMurray',
        'P' : 'Peace River',
        'R' : 'Rocky',
        'S' : 'Slave Lake',
        'W' : 'Whitecourt'
    }

    if letter in title_mapping:
        name = title_mapping[letter]

    return name