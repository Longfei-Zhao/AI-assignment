# hff evaluation

I create a list of facts to hold all facts that we need to get and a list of actions that we want to have.
Firstly, put all goals in this list.
Then, pop a fact in this list and get its cheapest action. If this action we already have, do nothing. If not, we push this action to the action list and get all its precondition to the facts list.

## Blocks (GS)

| Task Name | With hff | Run-Time | Node Expansion | Plan Length |   
| --- | --- | --- | --- | --- |
| Task01 | YES | 0.0096 | 30 | 10 |
|  | NO | 0.0019 | 151 | 6 |
| Task02 | YES | 0.0059 | 18 | 10 |
|  | NO | 0.0016 | 111 | 10 |
| Task03 | YES | 0.0047 | 10 | 6 |
|  | NO | 0.0012 | 79 | 6 |
| Task04 | YES | 0.014 | 33 | 12 |
|  | NO | 0.016 | 1050 | 12 |
| Task05 | YES | 0.021 | 44 | 10 |
|  | NO | 0.015 | 940 | 10 |
| Task06 | YES | 0.044 | 96 | 24 |
|  | NO | 0.025 | 1721 | 16 |
| Task07 | YES | 0.26 | 515 | 34 |
|  | NO | 0.086 | 3640 | 12 |
| Task08 | YES | 0.08 | 121 | 18 |
|  | NO | 0.22 | 10615 | 10 |
| Task09 | YES | 0.25 | 486 | 32 |
|  | NO | 0.26 | 16933 | 20 |
| Task10 | YES| 0.056 | 47 | 22 |
|  | NO | 2.0 | 91123 | 20 |
| Task11 | YES | 0.42 | 615 | 40 |
|  | NO | 3.3 | 176855 | 22 |
| Task12 | YES | 0.26 | 346 | 38 |
|  | NO | 3.1 | 163598 | 20 |
| Task13 | YES | 0.98 | 144 | 34 |
|  | NO | 4.3e+01 | 1260378 | 18 |
| Task14 | YES | 1.4 | 1295 | 54 |
| Task14 | NO | 6.9e+01 | 1808216 | 20 |
| Task15 | YES | 0.25 | 267 | 30 |
|  | NO | 4.1e+01 | 1153379 | 16 |


## pegsol (GS)

| Task Name | With hff | Run-Time | Node Expansion | Plan Length |   
| --- | --- | --- | --- | --- |
| Task01 | YES | 0.0031 | 5 | 5 |
|  | NO | 0.00096 | 12 | 5 |
| Task02 | YES | 0.023 | 26 | 9 |
|  | NO | 0.0052 | 109 | 9 |
| Task03 | YES | 0.02 | 13 | 9 |
|  | NO | 0.012 | 297 | 9 |
| Task04 | YES | 0.065 | 185 | 11 |
|  | NO | 0.013 | 344 | 10 |
| Task05 | YES | 0.016 | 17 | 12 |
|  | NO | 0.019 | 454 | 11 |
| Task06 | YES | 0.1 | 88 | 15 |
|  | NO | 0.11 | 2396 | 12 |
| Task07 | YES | 0.017 | 14 | 13 |
|  | NO | 0.027 | 645 | 12 |
| Task08 | YES | 0.49 | 353 | 20 |
|  | NO | 3.1 | 64416 | 16 |
| Task09 | YES | 0.58 | 711 | 17 |
|  | NO | 0.29 | 7069 | 15 |
| Task10 | YES | 0.5 | 419 | 21 |
|  | NO | 3.5 | 78189 | 17 |
| Task11 | YES | 0.96 | 1074 | 22 |
|  | NO | 1.1 | 25276 | 18 |
| Task12 | YES | 0.08 | 55 | 22 |
|  | NO | 3.5 | 76500 | 20 |
| Task13 | YES | 0.62 | 543 | 23 |
|  | NO | 2.6 | 59095 | 21 |
| Task14 | YES | 8.3 | 8022 | 23 |
|  | NO | 5.3 | 123953 | 20 |
| Task15 | YES | 1.4 | 1262 | 25 |
|  | NO | 6.8 | 151308 | 21 |
