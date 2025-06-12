
from decimal import Decimal, ROUND_HALF_UP
import numpy as np 
from dateutil.relativedelta import relativedelta
import pandas as pd 
import calendar

def Quotient_Lx(dates_flux_liste, Lx_exact):
    Lx_exact = np.array(Lx_exact)  # on convertit en array numpy
    
    Quotient_Lx_ex_sur_Lx_ex = np.where(Lx_exact == 0, 0, Lx_exact / Lx_exact[0])
    
    return Quotient_Lx_ex_sur_Lx_ex









#print(Ly_exact[0],Ly_exact[1], Ly_exact_surLy[1])
#print(Lx_exact_surLx)
#print(Ly_exact_surLy)

#print(Lx_exact)