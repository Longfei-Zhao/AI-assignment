include "Logistics-Q4.mzn";
solve minimize tot_cost;
output [ show(T) ++ "," ++ show(C) ++ "," ++ show(tot_cost div 100) ++ "." ++ show(tot_cost mod 100) ++ "\n"];
output [ show(t) ++ "," ++ show(time) ++ "," ++ show(steps[t, time]) ++ "," ++ show(num[t, steps[t, time], 1]) ++ "," ++ show(num[t, steps[t, time], 2]) ++ "\n"|
 t in trucks, time in 1..fix(maxSteps[t]) where  fix(num[t, steps[t, time], 1]) != 0 \/ fix(num[t, steps[t, time], 2]) != 0]; 