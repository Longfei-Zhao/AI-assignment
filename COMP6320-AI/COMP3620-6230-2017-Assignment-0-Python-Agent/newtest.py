import os
import json
import time

def main ():
    total_score = 0
    for i in range(1, 6):
        print("Scenario {} - ".format(i), end = '')

        results = [0, 0]
        stime   = time.time()

        for key, agent in enumerate(["HealthAgent", "SmartHealthAgent"]):
            os.system("python3 disease_simulation.py -s exercise4_maps/scenario{}.scn -H 100 -n 100 -a {} > /dev/null".format(i, agent))
            with open("scenario{}.results.json".format(i)) as json_data:
                results[key] = json.load(json_data)["average_score"]

        raw_score    = max(1, 4 * (1 - (100 - results[1]) / (100 - results[0])))
        total_score += raw_score

        print(("HealthAgent: {:.2f}  " +
               "SmartHealthAgent: {:.2f}  " +
               "Raw mark: {:.2f}  " +
               "Time elapsed: {:.4f} seconds").format(results[0], results[1], raw_score, time.time() - stime))

    print("Raw mark:   {:.2f}".format(total_score))
    print("Total mark: {}".format(round(total_score)))

if __name__ == "__main__":
    main()
