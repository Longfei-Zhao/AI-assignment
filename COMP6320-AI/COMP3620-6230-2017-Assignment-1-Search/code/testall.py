import os

def main ():
    test=[("testAdversarial","12"),
          ("smallAdversarial","2"),
          ("aiAdversarial","10"),
          ("anuAdversarial","8"),
          ("mazeAdversarial","10"),
          ("smallDenseAdversarial","6"),
          ("aiDenseAdversarial","6"),
          ("anuDenseAdversarial","6"),
          ("mazeDenseAdversarial","6")]

    for lay, depth in test:
        #os.system("python3 disease_simulation.py -s exercise4_maps/scenario{}.scn -H 100 -n 100 -a {}".format(i, agent))

        os.system("python3 red_bird.py -p MinimaxAgent -l adv_search_layouts/{}.lay -a depth={} -b GreedyBlackBirdAgent --timeout 60 -c -q >> 1.txt".format(lay,depth))



if __name__ == "__main__":
    main()
