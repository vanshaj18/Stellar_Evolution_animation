# data.py

tracks = {
    "1 M☉": {
        "temp": [5800, 5000, 4000, 3000],
        "lum": [1, 10, 100, 0.01],
        "stages": ["Main Sequence", "Subgiant", "Red Giant", "White Dwarf"]
    },
    "5 M☉": {
        "temp": [15000, 10000, 6000, 3000],
        "lum": [500, 1000, 3000, 1],
        "stages": ["Main Sequence", "Red Giant", "Supergiant", "White Dwarf"]
    },
    "15 M☉": {
        "temp": [30000, 20000, 10000, 5000],
        "lum": [10000, 20000, 100000, 100],
        "stages": ["Main Sequence", "Giant", "Supernova", "Neutron Star"]
    },
    "30 M☉": {
        "temp": [40000, 30000, 20000, 10000],
        "lum": [50000, 100000, 500000, 1000],
        "stages": ["Main Sequence", "Supergiant", "Supernova", "Black Hole"]
    }
}
