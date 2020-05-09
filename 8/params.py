def get_map_params(coords, pt_coords, spn, q):
    map_params = {
        "ll": coords,
        "spn": spn,
        "l": ['sat', 'map'][q % 2],
        "pt": pt_coords + ',pm2rdl' if pt_coords else None,
    }
    return map_params


def get_geocoder_params(coords):
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": ','.join([str(coords[0]), str(coords[1])]),
        "format": "json",
    }
    return geocoder_params