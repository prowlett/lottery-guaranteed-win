# lottery-guaranteed-win

The paper '[You need 27 tickets to guarantee a win on the UK National Lottery](https://arxiv.org/abs/2307.12430)' by David Cushing and David I. Stewart presents a list of 27 lottery tickets which will guarantee to match at least two numbers on the UK National Lottery. This code runs all 45,057,474 possible draws against these 27 tickets. 

All draws had between 1 and 9 winning tickets from the set (crucially, none had zero!). Obviously for 27 of the draws one of the winning tickets matched all six numbers, but about 75% of the draws saw a maximum of 2 balls matched by the winning tickets, and a further 23.5% had at most 3 balls matched. This means almost 99% of the time the 27 tickets match just two or three balls, earning prizes which may not exceed the cost of the 27 tickets! (I recommend reading Remark 1.2 in the paper.) 

Last lines of output from guaranteed-win.py

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

