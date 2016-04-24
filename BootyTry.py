# Here I'm just trying out the bootstrapper

from Bootstrapper.py import BootstrapYieldCurve

yield_curve = BootstrapYieldCurve()
yield_curve.add_instrument(100, 0.25, 0., 97.5)
yield_curve.add_instrument(100, 0.5, 0., 94.9)
yield_curve.add_instrument(100, 1.0, 0., 90.)
yield_curve.add_instrument(100, 1.5, 8, 96., 2)
yield_curve.add_instrument(100, 2., 12, 101.6, 2)
    
#y =import matplotlib.pyplot as plt
#plt.plot(x, y)
#plt.title("Zero Curve")
#plt.ylabel("Zero Rate (%)")
#plt.xlabel("Maturity in Years")
#plt.show() yield_curve.get_zero_rates()
#x = yield_curve.get_maturities()
    
    