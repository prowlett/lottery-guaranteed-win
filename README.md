# lottery-guaranteed-win

The paper '[You need 27 tickets to guarantee a win on the UK National Lottery](https://arxiv.org/abs/2307.12430)' by David Cushing and David I. Stewart presents a list of 27 lottery tickets which will guarantee to match at least two numbers on the UK National Lottery 'Lotto' game. This code runs all 45,057,474 possible draws against these 27 tickets. 

## How many tickets match how many balls?

The program `guaranteed-win.py` runs through all possible lottery combinations of 6 from 59 balls and counts the number of winning tickets among the 27 and the highest number of balls those tickets match.

All draws had between 1 and 9 winning tickets from the set (crucially, none had zero!). Obviously for 27 of the draws one of the winning tickets matched all six numbers, but about 75% of the draws saw a maximum of 2 balls matched by the winning tickets, and a further 23.5% had at most 3 balls matched. This means almost 99% of the time the 27 tickets match just two or three balls, earning prizes which may not exceed the cost of the 27 tickets! (I recommend reading Remark 1.2 in the paper.) 

Last lines of output from `guaranteed-win.py`

```
Draw 45057474: (54, 55, 56, 57, 58, 59)
[0, 5343744, 13241088, 11479880, 11184588, 2217858, 1438332, 133728, 12726, 5530, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 33914033, 10586913, 547927, 8574, 27]
```

| Number of winning tickets | Number of draws | % of draws |
| --- | --- | --- |
| 0 | 0 | 0.0%|
|1 | 5343744 | 11.86%|
|2 | 13241088 | 29.39%|
|3 | 11479880 | 25.48%|
|4 | 11184588 | 24.82%|
|5 | 2217858 | 4.92%|
|6 | 1438332 | 3.19%|
|7 | 133728 | 0.297%|
|8 | 12726 | 0.028%|
|9 | 5530 | 0.012%|
|10 | 0 | 0.0%|
|11 | 0 | 0.0%|
|12 | 0 | 0.0%|
|13 | 0 | 0.0%|
|14 | 0 | 0.0%|
|15 | 0 | 0.0%|
|16 | 0 | 0.0%|
|17 | 0 | 0.0%|
|18 | 0 | 0.0%|
|19 | 0 | 0.0%|
|20 | 0 | 0.0%|
|21 | 0 | 0.0%|
|22 | 0 | 0.0%|
|23 | 0 | 0.0%|
|24 | 0 | 0.0%|
|25 | 0 | 0.0%|
|26 | 0 | 0.0%|
|27 | 0 | 0.0%|

| Max. number of balls matched | Number of draws | % of draws |
| --- | --- | --- |
|0 | 0 | 0.0%|
|1 | 0 | 0.0%|
|2 | 33914033 | 75.27%|
|3 | 10586913 | 23.50%|
|4 | 547927 | 1.22%|
|5 | 8574 | 0.0190%|
|6 | 27 | 0.0000599%|

## What is the expected average return per week?

Tom Briggs asks "[What's the expected average return per week? I assume it to be negative](https://twitter.com/TeaKayB/status/1684354135049601024)".

The program `guaranteed-win-returns.py` is similar to `guaranteed-win.py` but this time it works out the prize money won by the winning tickets and keeps a running total.

### Assumptions

The prize money varies, so some assumptions have been made these are detailed in the table below and its notes. 

| Balls matched | Prize |
| --- | --- |
| 6 | 5000000* |
| 5 | 22158** | 
| 4 | 140 |
| 3 | 30 |
| 2 | 1*** |

\* Assume a jackpot of £10m split between two winners, so a value of £5m, based on recent draw data and a bit of arm-waving.

** Matching 5 numbers gets £1,750, but matching 5 numbers plus the bonus ball is £1m. However, the bonus ball isn't simulated here. Consequently, here we value 5 numbers as 1750 + 1/49 × 1000000 = 22158.

*** Matching 2 balls earns a 'Lucky dip', a randomised ticket in the next lottery. Since 45% of proceeds are paid out in prizes, here we value a 'Lucky dip' ticket (optimistically, and to avoid non-integers) at £1. 

### Results

Last line of output from `guaranteed-win-returns.py`

```
Draw 45057474: (54, 55, 56, 57, 58, 59): 7 tickets won £5000006 (total of £901476513 so far).
```

45,057,474 draws resulted in £901,476,513 in winnings. Dividing the winnings into the number of draws results in an average win per draw of £20.01. 

The cost of buying 27 tickets for a draw is £54, so the cost of buying these tickets would be £2,433,103,596, resulting in a loss of £1,531,627,083. The average loss per draw is therefore £33.99. (Note that, reassuringly, 33.99+20.01=54.)

A standard ticket costs £2 and 45% of proceeds are paid out in prizes, so the expected return might be £0.90. Since £20.01 is 37% of £54, this seems to represent a worse return (given the assumptions made) than buying a single lottery ticket.

There are just 27 tickets that win the jackpot, so the contribution to the prize total from these is £135,000,000. This can be subtracted from the total and replaced by a different figure to change the jackpot size assumption. The assumptions around the bonus ball and 'Lucky dip' are harder to unpick without editing the code.

## How often do you make a profit?

Matt Parker [tweeted](https://twitter.com/standupmaths/status/1685346409652846592) that there is a 1.5% chance of making a profit based on this page, which this page does not say. To answer this question, `guaranteed-win-profit-loss.py` runs through the amount won in each draw and counts when this is a profit cf. £54 to buy 27 tickets. Same assumptions about prize value as above.

Last line of output from `guaranteed-win-profit-loss.py`:

```
Draw 45057474: (54, 55, 56, 57, 58, 59): 7 tickets won £5000006 (profit) (2249125 profits so far).
```

So the 27 tickets make a profit in 2249125 profit draws out of 45057474 - that's 4.99% of draws.
