import os
import json
import time

def main ():
    for i in range(1, 6):
        results = [0, 0]
        print("Running scenario {}".format(i))
        stime = time.time()
        for j in range(0, 1):
            for key, agent in enumerate(["HealthAgent", "SmartHealthAgent"]):
                os.system("python3 disease_simulation.py -s exercise4_maps/scenario{}.scn -H 100 -n 100 -a {} > /dev/null".format(i, agent))
                with open("scenario{}.results.json".format(i)) as json_data:
                    results[key] = json.load(json_data)["average_score"]
            raw_score = max(1, 4 * (1 - (100 - results[1]) / (100 - results[0])))
            print("HealthAgent: {:.2f}\tSmartHealthAgent: {:.2f}\tRaw score: {:.2f}\tScore: {}".format(results[0], results[1], raw_score, round(raw_score)))
        print("Time elapsed: {} seconds".format(time.time() - stime))

if __name__ == "__main__":
    main()