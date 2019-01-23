include "Logistics-Q4.mzn";
solve satisfy;
output [ show(T) ++ "," ++ show(C) ++ "," ++ show(tot_cost div 100) ++ "." ++ show(tot_cost mod 100) ++ "\n"];
output [ show(t) ++ "," ++ show(time) ++ "," ++ show(c) ++ "," ++ show(num[t, c, 1]) ++ "," ++ show(num[t, c, 2]) ++ "\n"|
 t in trucks, time in times, c in customers where fix(steps[t, c]) = time /\ (fix(num[t, c, 1]) != 0 \/ fix(num[t, c, 2]) != 0)];