def get_map_params(coords, spn, q):
    map_params = {
        "ll": coords,
        "spn": spn,
        "l": ['sat', 'map'][q % 2],
    }
    return map_params
