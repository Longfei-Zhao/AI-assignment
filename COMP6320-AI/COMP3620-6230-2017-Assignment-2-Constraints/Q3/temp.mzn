include "alldifferent_except_0.mzn";
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
array[trucks] of int: centsPerKm;         % Cost of running trucks (in cents per km)
array[customers,customers] of int: D;  	  % Distances between customers (including the depot)

var int: tot_cost;	      	   	  % Total cost of the solution

% Insert your other variables and constraints here
array[trucks, times] of var customers : steps;
array[trucks, customers, goods] of var 0..MAXCAP : num;

constraint forall (t in trucks, time in times) (
  steps[t, time] > 0 <-> num[t, steps[t, time], 1] + num[t, steps[t, time], 2] > 0);
  
constraint forall (t in trucks) (
  alldifferent_except_0( [steps[t, time] | time in times])); 
  
constraint forall(t in trucks, c in customers)(
  refrig[t] == false -> num[t, c, 1] = 0);  % If the truck don't have refrigerator, the truck can't deliver chilled goods. 

constraint forall(c in customers)(
  forall(g in goods) (
    sum (t in trucks) (num[t, c, g]) = order[g, c])); % For a certain customer, the number of all trucks deliver is equal to it's order.

constraint forall(t in trucks)(
  sum (c in customers, g in goods) (num[t, c, g]) <= cap[t]); % The number of trucks deliver can not larger than its capacity.

constraint tot_cost = sum (t in trucks, time in 1..C+1 where steps[t, time] > 0) (
  D[steps[t, time-1], steps[t,time]] * centsPerKm[t]);

% In question Q3, we are optimising the total cost
solve minimize tot_cost;

% Write a Minizinc output item to print the solution in the desired format for Q3
output [ show(T) ++ "," ++ show(C) ++ "," ++ show(tot_cost) ++ "\n"];
output [ show(t) ++ "," ++ show(time) ++ "," ++ show(c) ++ "," ++ show(num[t, c, 1]) ++ "," ++ show(num[t, c, 2]) ++ "\n"|
 t in trucks, time in times, c in customers where fix(steps[t, c]) = time /\ (fix(num[t, c, 1]) != 0 \/ fix(num[t, c, 2]) != 0)];