import sys
import math
import datetime
from itertools import combinations

def find(i_values, i_targets, i_reverse = True, i_range = "reverse", i_combine_targets = False):
    def clr_line():
        sys.stdout.write("\033[K")
        
    values = list(map(int, str(i_values).split()))
    targets = list(map(int, str(i_targets).split()))

    n_values = len(values)
    total_sum = sum(values)

    if i_range == "all":
        loop_range = list(range(1, n_values+1))
    elif i_range == "reverse":
        loop_range = list(reversed(range(1, n_values+1)))
    else:
        loop_range = list(i_range)

    if i_reverse:
        values.reverse()

    n_total = 0
    for i in loop_range:
        n_total += math.comb(n_values, i)

    print(f"*** {n_values} values to combine, {n_total:,} total possible combinations")
    print(f"*** Total sum of input values: {total_sum:,}")
    for target in targets:
        print(f"*** Target sum: {target:,}")

    combo_targets = []
    if i_combine_targets and len(targets) > 1:
        for i in range(2, len(targets)+1):
            for j in combinations(targets, i):
                combo_targets += [sum(j)]
        # Delete duplicates
        combo_targets = list(dict.fromkeys(combo_targets))

        for target in combo_targets:
            print(f"*** Combo target sum: {target:,}")


    n_checked = 0
    start_time = datetime.datetime.now()
    found = False
    for i in loop_range:
        combos = combinations(values, i)
        n = math.comb(n_values, i)

        c = 0
        print()
        for x in combos:
            c += 1
            n_checked += 1
            p = c / n * 100
            total_progress = n_checked / n_total * 100

            now_time = datetime.datetime.now()
            run_time = now_time - start_time
            try:
                remaining_time = run_time / total_progress * 100 - run_time
                if remaining_time.total_seconds() < 0:
                    remaining_time = datetime.timedelta()
            except:
                remaining_time = "-:--:--       "

            clr_line()
            print(now_time.strftime(" %X"),  f"{run_time} {remaining_time} {total_progress:7.3f}% | Checking {n:21,} {i:3} combos: {p:5.1f}%"   , end='\r', flush=True)

            sum_x = sum(x)
            for target in targets:
                if (sum_x == target):
                    found = True
                    clr_line()
                    print('*** Target found', target, x, flush=True)
            
            for target in combo_targets:
                if (sum_x == target):
                    found = True
                    clr_line()
                    print('*** Combo target found', target, x, flush=True)            

    if found:
        print("\n### Finished searching all combos.")
    else:
        print("\n### No combos found.")
        
