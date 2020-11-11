# REQUIREMENTS

## High Level Requirements

|ID|Requirements|
|--|-------|
| HH_01 | 0 should be used to represent the blank spaces  |
| HH_02  | Index of empty spaces should be found out first. |
| HH_03  | Backtracking algorithm is used for checking if any repeated number exists in the row, column or grid. |
| HH_04  | GUI should be developed |
| HH_05  | GUI should get updated at every step. |
| HH_06  | Finally, the solved board should be displayed. |

## Low Level Requirements

|ID|Requirements|
|--|-----|
| HH_01_LL_01  | The unsolved board is iterated over by 2 nested loops. |
| HH_02_LL_01  |  Index of all zeros are returned |
| HH_03_TT_01 | Validation and backtracking for rows |
| HH_03_TT_02  | Validation and backtracking for columns |
| HH_03_TT_03 | Validation and backtracking for boxes |
| HH_04_TT_01 | Pygame library is used for GUI development |
| HH_05_TT_01  | Execution of program should start only on a keypress (eventbased) |
