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
array[trucks] of int: centsPerKm;         % Cost of running trucks (in cents per km)
array[customers,customers] of int: D;  	  % Distances between customers (including the depot)

var int: tot_cost;	      	   	  % Total cost of the solution

% Insert your other variables and constraints here
array[trucks] of var times : maxSteps;
array[trucks, times] of var customers : steps;
array[trucks, customers, goods] of var 0..MAXCAP : num;

constraint forall (t in trucks) (
  maxSteps[t] = sum (c in customers) (bool2int(num[t, c, 1] + num[t, c, 2] >0))); % Get the sum of steps for each trucks

constraint forall (t in trucks) (steps[t, 0] = 0); % steps[t, 0] is depot
   
constraint forall (t in trucks) (
  alldifferent([steps[t, time] | time in 0..C])); % truck can't go to a customer twice
  
constraint forall (t in trucks, time in 1..maxSteps[t]) (
  num[t, steps[t, time], 1] + num[t, steps[t, time], 2] > 0); % if the truck deliver to the customer, the step[t, c] will in 1..maxSteps[t]
  
constraint forall(t in trucks, c in customers)(
  refrig[t] == false -> num[t, c, 1] = 0);  % If the truck don't have refrigerator, the truck can't deliver chilled goods. 

constraint forall(c in customers)(
  forall(g in goods) (
    sum (t in trucks) (num[t, c, g]) = order[g, c])); % For a certain customer, the number of all trucks deliver is equal to it's order.

constraint forall(t in trucks)(
  sum (c in customers, g in goods) (num[t, c, g]) <= cap[t]); % The number of trucks deliver can not larger than its capacity.

constraint tot_cost = sum (t in trucks, time in 0..maxSteps[t]-1) (
  D[steps[t, time], steps[t,time+1]] * centsPerKm[t]) + sum(t in trucks)(D[steps[t, maxSteps[t]], steps[t, 0]] * centsPerKm[t]); % Calculating the costs

% In question Q3, we are optimising the total cost
solve minimize tot_cost;

% Write a Minizinc output item to print the solution in the desired format for Q3
output [ show(T) ++ "," ++ show(C) ++ "," ++ show(tot_cost div 100) ++ "." ++ show(tot_cost mod 100) ++ "\n"];
output [ show(t) ++ "," ++ show(time) ++ "," ++ show(steps[t, time]) ++ "," ++ show(num[t, steps[t, time], 1]) ++ "," ++ show(num[t, steps[t, time], 2]) ++ "\n"|
 t in trucks, time in 1..fix(maxSteps[t]) where  fix(num[t, steps[t, time], 1]) != 0 \/ fix(num[t, steps[t, time], 2]) != 0]; 