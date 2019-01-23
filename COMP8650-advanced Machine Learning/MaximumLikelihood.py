import cvxpy as cvx
import numpy as np
import pickle
import matplotlib.pyplot as plt
from cvxpy import *

# load data
X = pickle.load(open("asgn5q2.pkl", "rb"))
# get the shape of X
m, n = X.shape
# get the sigmaHat
sigmaHat = np.cov(X, rowvar=0)
# define lambda
lambd = cvx.Parameter(nonneg = True)
# define log space
TRIALS = 50
lambda_vals = np.logspace(-5, 1.3, TRIALS)
# initialize lists to save data
log_likelihood_list = []
obj_list = []
no_zero_list = []
# create one scalar optimization variable.
K = cvx.Variable((n, n), PSD=True)
# create 0 constraints.
constraints = []
# define non-diagonal index
reg_idx = 1 - np.eye(n)
# define the constant
idxConstant = cvx.Constant(reg_idx)
sigmaHatConstant = cvx.Constant(sigmaHat)
# define two expressions and minimize
exp_log = -cvx.log_det(K) + cvx.trace(sigmaHatConstant * K)
exp_regularization = lambd * cvx.sum(cvx.sum(cvx.abs(K) * idxConstant))
obj = cvx.Minimize(exp_log + exp_regularization)
# form the problem.
prob = cvx.Problem(obj, constraints)
for value in lambda_vals:
    # get a lambda value
    lambd.value = value
    # solve the problem
    prob.solve()
    # save data to plot a figure
    log_likelihood_list.append(-exp_log.value)
    obj_list.append(prob.value)
    no_zero_list.append(np.sum(np.sum(K.value > 1e-6)))
# plot a figure and save it
figure = plt.figure()
plt.plot(lambda_vals, obj_list, 'o--',label = 'optimal objective value',
linewidth = 2, color = 'r')
plt.plot(lambda_vals, log_likelihood_list, 'v--',label = 'log-likelihood',
linewidth = 2, color = 'g')
plt.plot(lambda_vals, no_zero_list, '+--',label = 'number of no zero',
linewidth = 2, color = 'b')
plt.grid()
plt.xlabel('lambda')
plt.ylabel('value')
plt.legend()
plt.title('optimal objective value, log-likelihood and number of no zero')
figure.savefig('figure.png')
