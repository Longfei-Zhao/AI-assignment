from io import open

res = dict()
for line in open('../gov-test-collection/qrels/gov.qrels'):
    index, _, _, relevant = line.split()
    res.setdefault(index, [0,0])
    if relevant == "1":
        res[index][0] += 1
    else:
        res[index][1] += 1
for key, value in res.items():
    print("qrels: " + str(key) + " relevant :" + str(value[0]) + " not relevant: " + str(value[1]))
