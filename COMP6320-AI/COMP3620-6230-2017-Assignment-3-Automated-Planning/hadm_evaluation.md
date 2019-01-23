# hadm evaluation

I use the relaxation framework provided and follow the slides to build a basic hmax for Q4.

## Blocks (astar)
| Task Name | With hadm | Run-Time | Node Expansion | Plan Length |   
| --- | --- | --- | --- | --- |
| Task01 | YES | 0.023 | 151 | 6 |
| | NO | 0.0021 | 178 | 6 |
| Task02 | YES | 0.0017 | 107 | 10 |
| | NO | 0.016 | 102 | 10 |
| Task03 | YES | 0.018 | 112 | 6 |
| | NO | 0.0016 | 104 | 6 |
| Task04 | YES | 0.24 | 1224 | 12 |
| | NO | 0.016 | 939 | 12 |
| Task05 | YES | 0.21 | 1035 | 10 |
| | NO | 0.016 | 886 | 10 |
| Task06 | YES | 0.29 | 1846 | 16 |
| | NO | 0.027 | 1714 | 16 |
| Task07 | YES | 1.4 | 4089 | 12 |
| | NO | 0.091 | 4195 | 12 |
| Task08 | YES | 3.0 | 9111 | 10 |
| | NO | 0.17 | 8875 | 10 |
| Task09 | YES | 4.2 | 17032 | 20 |
| | NO | 0.25 | 16936 | 20 |
| Task10 | YES | 3.5e+01 | 93359 | 20 |
| | NO | 2.1 | 89198 | 20 |
| Task11 | YES | 5.1e+01 | 180240 | 22 |
| | NO | 3.9 | 180192 | 22 |
| Task12 | YES | 4.8e+01 | 164509 | 20 |
| | NO |3.8 | 160979 | 20 |
| Task13 | YES | 6.7e+02 | 1436274 | 18 |
| | NO | 5.5e+01 | 1396798 | 18 |
| Task14 | YES |   |  |  |
| | NO | 7.7e+01 | 1848904 | 20 |
| Task15 | YES | 6e+02 |1199843 | 16 |
| | NO | 3.9e+01 | 1071291 | 16 |

## pegsol (astar)

| Task Name | With hadm |Run-Time | Node Expansion | Plan Length |   
| --- | --- | --- | --- | --- |
| Task01 | YES | 0.01 | 13 | 5 |
| | NO | 0.00084 | 12 | 5 |
| Task02 | YES | 0.084 | 111 | 9 |
| | NO | 0.0049 | 111 | 9 |
| Task03 | YES | 0.24 | 305 | 9 |
| | NO | 0.013 | 295 | 9 |
| Task04 | YES | 0.25 | 331 | 10 |
| | NO | 0.013 | 350 | 10 |
| Task05 | YES | 0.38 | 457 | 11 |
| | NO | 0.019 | 455 | 11 |
| Task06 | YES | 1.9 | 2450 | 12 |
| | NO | 0.11 | 2469 | 12 |
| Task07 | YES | 0.57 | 648 | 12 |
| | NO | 0.027 | 646 | 12 |
| Task08 | YES | 5e+01 | 65019 | 16 |
| | NO | 2.6 | 64917 | 16 |
| Task09 | YES | 5.4 | 7071 | 15 |
| | NO | 0.28 | 7078 | 15 |
| Task10 | YES | 5.8e+01 | 78854 | 17 |
| | NO | 3.1 | 78472 | 17 |
| Task11 | YES | 1.9e+01 | 25271 | 18 |
| | NO | 1.0 | 25267 | 18 |
| Task12 | YES | 5.3e+01 | 76535 | 20 |
| | NO | 3.2 | 76514 | 20 |
| Task13 | YES | 4.9e+01 | 59077 | 21 |
| | NO | 2.6 | 59093 | 21 |
| Task14 | YES | 9.1e+01 | 123655 | 20 |
| | NO | 5.4 | 123568 | 20 |
| Task15 | YES | 1.1e+02 | 151051 | 21 |
| | NO | 5.9 | 150772 | 21 |
