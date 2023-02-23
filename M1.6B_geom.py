import math
from scipy.optimize import minimize
from scipy.optimize import Bounds


def ngeomLL(par, data):
    llsum = 0
    for t in range(1,len(data)):
        llsum += (data[t-1]-data[t])*math.log(par*(1-par)**(t-1))
    llsum += data[len(data)-1]*math.log((1-par)**(len(data)-1))
    return -llsum

data = [1000, 869, 743, 653, 593, 551, 517, 491]

bnds = Bounds(0.0001,0.9999)
res = minimize(ngeomLL, 0.2, (data), method="nelder-mead",
               options={'xatol': 1e-08, 'disp': True},bounds=bnds)


print('MLE for theta is', res.x, 'and LL is',-ngeomLL(res.x,data))
