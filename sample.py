import search_combos

# 33 input values take about 15 minutes to process on my MacBook Pro M3

values = "19157  13184  -1712  71397  17117  99999  77514  83002  -37856  96765  12298  -49214  -39541  -30826  -52471  87655  -46677  -68000  -3543  -35217  62241  31166  -55953  59982  8742  77846  -69505  33724  48876  -24915  4641  3255  -28090"
targets =  "306538 242329"

search_combos.find(values, targets)
