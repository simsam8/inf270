# Problem 1 

## b)


| Iteration | $x_1$ | $x_2$ | $x_3$ | $x_4$ |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| initial | 1/10 | 1/100 | 1/1000 | 1/10000 |
| 1. | 9/10 | 9/100 | 9/1000 | 9/10000 |
| 2. | 9/10 | 91/100 | 91/1000 | 91/10000 |
| 3. | 1/10 | 99/100 | 99/1000 | 99/10000 |
| 4. | 1/10 | 99/100 | 901/1000 | 820/9101 |
| 5. | 9/10 | 91/100 | 909/1000 | 908/9989 |
| 6. | 9/10 | 0 | 1 | 1/10 |
| 7. | 9/10 | 0 | 1 | 451/501 |
| 8. | 9/10 | 5 | 1/2 | 477/502 |
| 9. | 9/10 | 9/100 | 9/1000 | 1 |
| 10. | 1/10 | 1/100 | 1/1000 | 1 |

It took 10 iterations in Phase 2 to find the optimal solution.


## c) 

The worst case of the simplex algorithm is exponential as the number of 
edges between intersection increases exponentially by the number of variables.
Since the worst case would be to visit all intersections before 
finding the optimal solution, the algorithm grows exponentially.


## d)

The value of $x_1$ only changes when the kth pivot is col 1.
