def get_map_params(coords, pt_coords, spn, q):
    map_params = {
        "ll": coords,
        "spn": spn,
        "l": ['sat', 'map'][q % 2],
        "pt": pt_coords + ',pm2rdl' if pt_coords else None,
    }
    return map_params
