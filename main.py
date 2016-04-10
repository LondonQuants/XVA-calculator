import datetime as dtt
from lsmc import simulate, lsmc

print('hello Git!')

s0 = 900
k = 890
r = 0.05
q = 0.045
sigma = 0.2
t = 0.5
flag = 'call'
t_steps = 100
n_paths = 100000

lamb = 0.75
mu = -0.6
delta = 0.25

starttime = dtt.datetime.now()
strike = 110
s = simulate(s0, r, q, sigma, t, t_steps, n_paths)

V0, V = lsmc(s, t, k, r, t_steps, n_paths, flag, method='laguerre')
print ("{} Option Value {}".format(flag, V0))

endtime = dtt.datetime.now()
print ("Time elapsed: {}\n\
        n of time steps: {}\n\
        n of MC paths: {}".format(endtime - starttime, t_steps, n_paths))

