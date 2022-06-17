# Knapsacks
## Introduction
- <b><i>Knapsack problems</i></b>
is one kind of problem in combinatorial optimization in which you 
need to find a set of items, with given value and size (such as weights 
and volumes), packed into a container with a maximum capacity in order to
achieve the highest value.

- In this repo, the demonstration of knapsack problems solving is given in several methods.
Initialy, it includes solving knapsacks demo in 
<b>Linear Programmming</b> 
and
<b>Meta Heuristic Algorithm</b>.

- In each method's folder, there are further analysis which help you to understand more detail 
the related features.
<br>

## List of Included Methods
- [Simplex Method for Linear Programming](/LinearProgramming)
- [Harmony Search Algorithm](/HarmonySearch)

## Example used
A manufacturing company needs to solve a logistic problem with its delivery process, 
in which they have to pack different crates of post-production components into a container 
and then distribute them to different assembly factories.<br>

Each crate has its weight, volume and value, 
it is required to find a solution for optimizing the capacity while achieving the highest value.<br>

The factory can provide at most 20 waiting-for-deliver similar crates at one delivery.<br>
<br><br>
<code>N = 10</code><br>
<code>W = 1500</code><br>
<code> V = 2500</code><br>
<code>List Value = [90, 36, 54, 108, 45, 18, 50, 80, 210, 150]</code><br>
<code>List Weight = [10, 4, 6, 12, 5, 2, 7, 9, 18, 15]</code><br>
<code>List Volume = [9, 3, 9, 10, 6, 2, 5, 6, 25, 12]</code><br>
<pre>
            Value   Weight  Volume
  Item 1:    90      10        9       
  Item 2:    36       4        3
  Item 3:    54       6        9
  Item 4:   108      12       10
  Item 5:    45       5        6
  Item 6:    18       2        2
  Item 7:    50       7        5
  Item 8:    80       9        6
  Item 9:   210      18       25
  Item 10:  150      15       12
  
</pre>

## List of Programming Language Used
> Python<br>
> C++ (Demo pending)

## Note
> Check out my final report here -> [Final_report](/AdvancedAlgorithms_final_rp.pdf)
