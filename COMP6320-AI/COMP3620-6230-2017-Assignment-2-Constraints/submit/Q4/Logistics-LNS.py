import argparse
import os
import time

#Get numTruck, numCustomer, curCost from start_solution_filename
#Transfer the table to data structure that I made in the .mzn
#numStep for the amount of the customers that each trucks deliver.
#order for the order of customers for each trucks.
#goods for the units of each truck to each custoemr for two kinds of goods.
def getInput(start_solution_filename):
    with open(start_solution_filename) as f:
        lines = f.readlines()
        numTruck, numCustomer, curCost = lines[0].strip().split(',')
        numTruck = int(numTruck)
        numCustomer = int(numCustomer)
        curCost = float(curCost)
        numStep = [0] * numTruck
        order = [[x for x in range(numCustomer + 1)] for y in range(numTruck)]
        goods = [[[0 for i in range(2)] for j in range(numCustomer + 1)] for k in range(numTruck)]
        for line in lines[1:]:
            tempTruck, tempTime, tempCustomer, tempChilledGoods, tempAmbientGoods = map(int, line.strip().split(','))
            tempTruck = tempTruck - 1
            numStep[tempTruck] = tempTime
            if order[tempTruck][tempTime] != tempCustomer:
                order[tempTruck][order[tempTruck].index(tempCustomer)] = order[tempTruck][tempTime]
                order[tempTruck][tempTime] = tempCustomer
            if tempChilledGoods > 0:
                goods[tempTruck][tempCustomer][0] = tempChilledGoods
            if tempAmbientGoods > 0:
                goods[tempTruck][tempCustomer][1] = tempAmbientGoods
    return numTruck, numCustomer, curCost, numStep, order, goods

# delete two trucks data from numStep, order, goods
# write the data to keep.dzn
def writeToDzn(numStep, order, goods, truckI, truckJ):
    numStep[truckI] = '_'
    numStep[truckJ] = '_'
    order[truckI] = ['_'] * ( numCustomer + 1)
    order[truckJ] = ['_'] * ( numCustomer + 1)
    goods[truckI] = [['_'] * 2] * ( numCustomer + 1)
    goods[truckJ] = [['_'] * 2] * ( numCustomer + 1)
    with open("keep.dzn", 'w') as f:
        f.write("maxSteps = [" + ', '.join(map(str, numStep)) + "];\nsteps = array2d(trucks, customers, [")
        f.write(', '.join(map(str, [j for i in order for j in i]) ) + "]);\nnum = array3d(trucks, customers, goods, [")
        f.write(', '.join(map(str, [k for i in goods for j in i for k in j]) ) + "]);\n")

if __name__ =='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('problem_filename', help='problem file')
    parser.add_argument('start_solution_filename', help='file describing the solution to improve')
    args = parser.parse_args()
    start_solution_filename = args.start_solution_filename
    problem_filename = args.problem_filename

    #Get the input
    numTruck, numCustomer, curCost, numStep, order, goods = getInput(start_solution_filename)
    #Set the output file name
    output_filename = 'solution-Q4-' + str(numTruck) + '-' + str(numCustomer) + '.csv'
    #Set the command
    command = "minizinc Logistics-opt.mzn " + problem_filename + " --soln-sep \"\" --search-complete-msg \"\" > " + output_filename
    #Get the start time
    start_time = time.time()
    while(True):
        for truckI in range(numTruck):
            for truckJ in range(truckI + 1, numTruck):
                writeToDzn(numStep, order, goods, truckI, truckJ)
                os.system(command)
                #Read the output_filename

                with open(output_filename) as f:
                    lines = f.readlines()
                    _, _, tempCost = lines[0].strip().split(',')
                    tempCost = float(tempCost)
                    numStep = [0] * numTruck
                    order = [[x for x in range(numCustomer + 1)] for y in range(numTruck)]
                    goods = [[[0 for i in range(2)] for j in range(numCustomer + 1)] for k in range(numTruck)]
                    for line in lines[1:]:
                        tempTruck, tempTime, tempCustomer, tempChilledGoods, tempAmbientGoods = map(int, line.strip().split(','))
                        tempTruck = tempTruck - 1
                        numStep[tempTruck] = tempTime
                        if order[tempTruck][tempTime] != tempCustomer:
                            order[tempTruck][order[tempTruck].index(tempCustomer)] = order[tempTruck][tempTime]
                            order[tempTruck][tempTime] = tempCustomer
                        if tempChilledGoods > 0:
                            goods[tempTruck][tempCustomer][0] = tempChilledGoods
                        if tempAmbientGoods > 0:
                            goods[tempTruck][tempCustomer][1] = tempAmbientGoods
        if curCost <= tempCost:
            break
        curCost = tempCost
    print("--- %s seconds ---" % (time.time() - start_time))
