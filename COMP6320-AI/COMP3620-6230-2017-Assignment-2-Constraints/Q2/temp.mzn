include "alldifferent.mzn";

int: C;					  % Number of customers
int: T;                     		  % Number of trucks
int: G;                     		  % Number of goods types 
int: MAXCAP;                		  % Upper bound on truck capacity

set of int: trucks = 1..T;    	     	  % Set of trucks
set of int: customers = 0..C;        	  % Set of customers. Includes depot as customer 0
set of int: goods = 1..G;            	  % Set of goods types
int: chilled = 1;  int: ambient = 2; 	  % Good types
set of int: times = 0..C+1;            	  % Enough times to visit each customer once and depot twice if needed

array[trucks] of int: cap;	     	  % Capacity of trucks
array[trucks] of bool: refrig;	     	  % Whether or not trucks are refrigerated
array[goods,customers] of int: order;	  % Number of units of goods types ordered by customers

% Insert your other variables and constraints here
array[trucks] of var times : maxSteps;
array[trucks, times] of var customers : steps;
array[trucks, customers, goods] of var 0..MAXCAP : num;

constraint forall (t in trucks) (
  maxSteps[t] = sum (c in customers) (bool2int(num[t, c, 1] + num[t, c, 2] >0))); % Get the sum of steps for each trucks

constraint forall (t in trucks) (steps[t, 0] = 0);
   
constraint forall (t in trucks) (
  alldifferent([steps[t, time] | time in 0..C])); 
  
constraint forall (t in trucks, time in 1..maxSteps[t]) (
  num[t, steps[t, time], 1] + num[t, steps[t, time], 2] > 0); 
  
constraint forall(t in trucks, c in customers)(
  refrig[t] == false -> num[t, c, 1] = 0);  % If the truck don't have refrigerator, the truck can't deliver chilled goods. 

constraint forall(c in customers)(
  forall(g in goods) (
    sum (t in trucks) (num[t, c, g]) = order[g, c])); % For a certain customer, the number of all trucks deliver is equal to it's order.

constraint forall(t in trucks)(
  sum (c in customers, g in goods) (num[t, c, g]) <= cap[t]); % The number of trucks deliver can not larger than its capacity.

% In question Q2, we are only finding a satisfying solution
solve satisfy;

% Write a Minizinc output item to print the solution in the desired format for Q2
output [ show(T) ++ "," ++ show(C) ++ "\n"];
output [ show(t) ++ "," ++ show(time) ++ "," ++ show(steps[t, time]) ++ "," ++ show(num[t, steps[t, time], 1]) ++ "," ++ show(num[t, steps[t, time], 2]) ++ "\n"|
 t in trucks, time in 1..fix(maxSteps[t]) where fix(num[t, steps[t, time], 1]) != 0 \/ fix(num[t, steps[t, time], 2]) != 0];