#!/bin/bash
size=15
# blocks pegsol
problem=blocks
# hadm hff hgoal
h=hff
# astar gbf
s=astar
# settings above
fileName=${h}_${s}_evaluation_${problem}.md
echo "|${problem}+$s|heuristic|node expansion|time|plan length|" > $fileName
echo "|------------:|----|----------|-------------|-----------|" >> $fileName
for ((j=1;j<=$size;++j))
do
    x=`printf %02d $j`
    y=`python3 pddl_planner.py ../benchmarks/$problem/task${x}.pddl -H $h -s $s`
    e=0
    t=0
    l=0
    i=1
    expansion="--"
    time="--"
    length="--"
    for z in $y
    do
      if [[ $i == $e ]]; then
        expansion=$z
      fi
      if [[ $i == $t ]]; then
        time=$z
      fi
      if [[ $i == $l ]]; then
        length=$z
      fi
      ((i++))
      if [[ $z == "expansion:" ]]; then
        e=$i
      fi
      if [[ $z == "time:" ]]; then
        t=$i
      fi
      if [ $z == "length:" ]; then
        l=$i
      fi
    done
    echo "|"${x}"|"$h"|"${expansion}"|"${time}"|"${length}"|">>$fileName
done
