from itertools import combinations
comb_list = list(combinations(range(1, 60), 6))
start_index = comb_list.index((1, 2, 3, 4, 5, 6))
counter = 0

tickets = ((1, 2, 3, 4, 5, 6 ),(1, 2, 3, 4, 7, 8 ),(1, 2, 5, 6, 7, 8 ),(9, 10, 11, 12, 13, 14),(9, 10, 11, 15, 16, 17),(12, 13, 14, 15, 16, 17),(18, 19, 20, 21, 26, 27),(18, 19, 22, 23, 30, 31),(18, 19, 24, 25, 28, 29),(20, 21, 22, 23, 28, 29),(20, 21, 24, 25, 30, 31),(22, 23, 24, 25, 26, 27),(26, 27, 28, 29, 30, 31),(32, 33, 34, 35, 40, 41),(32, 33, 36, 37, 44, 45),(32, 33, 38, 39, 42, 43),(34, 35, 36, 37, 42, 43),(34, 35, 38, 39, 44, 45),(36, 37, 38, 39, 40, 41),(40, 41, 42, 43, 44, 45),(46, 47, 48, 49, 54, 55),(46, 47, 50, 51, 58, 59),(46, 47, 52, 53, 56, 57),(48, 49, 50, 51, 56, 57),(48, 49, 52, 53, 58, 59),(50, 51, 52, 53, 54, 55),(54, 55, 56, 57, 58, 59))

profit_times = 0

for i, comb in enumerate(comb_list[start_index:]):
    print(f"Draw {i+1}: {comb}", end="")
    counter += 1
    
    this_prize_total = 0
    this_winning_tickets = 0
    for ticket in tickets:
        matches = len(set(comb).intersection(ticket))
        # print("matches for this ticket: {} - {}".format(ticket,matches))
        if matches > 1:
            this_winning_tickets += 1
            if matches == 2:
                this_prize_total += 1
            elif matches == 3:
                this_prize_total += 30
            elif matches == 4:
                this_prize_total += 140
            elif matches == 5:
                this_prize_total += 22158
            elif matches == 6:
                this_prize_total += 5000000
    label = "loss"
    if this_prize_total > 54:
        profit_times += 1
        label = "profit"
    print(": {} tickets won £{} ({}) ({} profits so far).".format(this_winning_tickets,this_prize_total,label,profit_times))
