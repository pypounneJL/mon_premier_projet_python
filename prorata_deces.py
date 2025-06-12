from calcul_age import age_exact, decimal_age, arrondi_excel
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd 
import calendar
import numpy as np





def calcul_prorata_deces(Lx_ex_liste, Ly_ex_liste, taux_rev, Lx_exact_0, Ly_exact_0):
    Lx = np.array(Lx_ex_liste)
    Ly = np.array(Ly_ex_liste)
    
    # On fait les différences entre éléments consécutifs
    term1 = (Lx[:-1] - Lx[1:]) / Lx_exact_0 * (1 - taux_rev * Ly[1:] / Ly_exact_0)
    term2 = (Ly[:-1] - Ly[1:]) / Ly_exact_0 * (1 - Lx[:-1] / Lx_exact_0) * taux_rev
    
    # On met 0 en première position comme dans ta version originale
    prorata = np.concatenate(([0], term1 + term2))
    
    return prorata









#print(prorata_deces)