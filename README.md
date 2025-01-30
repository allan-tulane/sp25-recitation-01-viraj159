[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tqM-lrvp)
# CMPS 2200  Recitation 01

**Name (Team Member 1):**Viraj Choksi
**Name (Team Member 2):**_________________________

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`. All tests are in `test_main.py`.

## Install Python Dependency

We need Python library of "tabulate" to visualize the results in a good shape. Please install it by running 'pip install tabulate' or 'pip install -r requirements.txt' in Shell Tab of Repl.  

## Running and testing your code

- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest test_main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 
For linear_search, the worst case input value of 'key' would be the very last value, since the algorithm would thus have to iterate through the entire list to find the key. For binary_search, the worst case input value of 'key' would be at the position where the depth corresponding to the maximum height of the search tree. This would mean a maximum amount of subdivisions before the algorithm can finally locate the key.

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 
For linear_search, the best case input value of 'key' would be the very first value, as the algorithm would then need only one comparison to find the key. For binary_search, the best case would be the key is the middle element in the list during the first comparison. Since binary_search starts by comparing the key to the middle value, it would thus be done after the first comparison.

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest test_main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:

|        n |   linear |   binary |
|----------|----------|----------|
|       10 |    0.002 |    0.003 |
|      100 |    0.003 |    0.002 |
|     1000 |    0.037 |    0.002 |
|    10000 |    0.628 |    0.006 |
|   100000 |    4.658 |    0.008 |
|  1000000 |   44.912 |    0.012 |
| 10000000 |  465.915 |    0.016 |

- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?
Although there are some discrepencies, like from n=10 to n=100 in linear search, the empirical results largely match the theoretical running times. The reason for the deviations and the times going above the worst-case running times could be limitations in the hardware or caching, however the overrall trend is very close to these times.

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? O(kn)
  + For binary search? Θ(n^2)+O(klog_2(n))
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? Θ(n^2) < O(kn) would have to be true for the above statement to also be true since O(n^2) dominates for large n, and this simplifies to n < k. Thus, when k > n, it is more efficient to first sort and then use binary search. 