import search_combos

values = "19157  13184  -1712  71397  17117  99999  77514  83002  -37856  96765  12298  -49214  -39541  -30826   33724  48876  -24915  4641  3255  -28090"
targets =  "96765 306538 200000 42329"

# search all possible combinations, including combined target sums
search_combos.find(values, targets, i_combine_targets=True)

# search only combinations with 3 to 6 items
search_combos.find(values, targets, i_range=range(3, 7))
