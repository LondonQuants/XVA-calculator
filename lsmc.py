import numpy.random as npr
import datetime as dtt
import numpy as np

s0 = 900
k = 890
r = 0.05
q = 0.045
sigma = 0.2
t = 0.5
flag = 'call'
t_steps = 1000
n_paths = 10000

lamb = 0.75
mu = -0.6
delta = 0.25
    

def simulate(t):
    np.random.seed(123456)
    dt = t / t_steps
    s = np.zeros((t_steps+1, n_paths))
    s[0] = s0
    sn1 = npr.standard_normal((t_steps+1, n_paths))
    for t in range(1, t_steps+1, 1):
        s[t] = s[t-1] * (np.exp((r - q - 0.5*sigma**2) * dt + sigma * np.sqrt(dt) * sn1[t]))
    return s

  
def simulate_j(t):
    np.random.seed(123456)
    dt = t / t_steps
    rj = lamb * (np.exp(mu + 0.5*delta**2) - 1)
    s = np.zeros((t_steps+1, n_paths))
    s[0] = s0
    sn1 = npr.standard_normal((t_steps+1, n_paths))
    sn2 = npr.standard_normal((t_steps+1, n_paths))
    poi = npr.poisson(lamb*dt, (t_steps+1, n_paths))
    for t in range(1, t_steps+1, 1):
        s[t] = s[t-1] * (np.exp((r - rj - 0.5*sigma**2) * dt + sigma * np.sqrt(dt) * sn1[t])\
        +(np.exp(mu + delta*sn2[t]) - 1) * poi[t])
    return s

  
def lsmc(s, t, k, r, flag, method='poly'):
    m = 1 if flag == 'call' else -1
    h = np.maximum(m*(s-k), 0)  # inner values for put option
    v = np.zeros_like(h)  # value matrix
    v[-1] = h[-1]
    dt = t / t_steps
    df = np.exp(-r * dt)
    # Valuation by LSM
    for t in range(t_steps - 1, 0, -1):
        if method == 'laguerre':
            rg = np.polynomial.laguerre.lagfit(s[t, :], v[t+1, :]*df, 4)
            c = np.polynomial.laguerre.lagval(s[t, :], rg) 
        else:
            rg = np.polyfit(s[t, :], v[t + 1, :] * df, 5)  # regression
            c = np.polyval(rg, s[t, :])  # evaluation of regression
        v[t, :] = np.where(h[t, :] > c, h[t, :], v[t + 1, :] * df)  # exercise decision/optimization
    v0 = np.sum(v[1, :] * df) / n_paths  # LSM estimator
    
    return v0, v[1,:]


starttime = dtt.datetime.now()
strike = 110
s = simulate(t)

V0, V = lsmc(s, t, k, r, flag, method='laguerre')
print ("{} Option Value {}".format(flag, V0))

endtime = dtt.datetime.now()
print ("Time elapsed: {}\n\
        n of time steps: {}\n\
        n of MC paths: {}".format(endtime - starttime, t_steps, n_paths))