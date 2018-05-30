from scipy import stats

import numpy as np

x=[-0.018,-0.008,0.011,0.017,-0.008,-0.002]

y=[-0.006,-0.001,0.015,0.017,-0.0019,-0.005]

gradient,intercept,r_value,p_value,std_err=stats.linregress(x,y)

print ("Gradient and intercept",gradient,intercept)

print ("R-squared",r_value**2)