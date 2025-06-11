from calcul_age import age_exact, decimal_age,arrondi_excel
from decimal import Decimal, ROUND_HALF_UP
from calcul_flux import dates_flux_liste, age_ENT_contractant_liste, Ly_exact,age_Exact_contractant_liste, age_exact_conjoint_liste, age_ENT_conjoint_liste, Ly_colonne_liste, Ly_plus1_colonne_liste, Lx_colonne_liste, Lxplus1_colonne_liste,Lx_exact,Lx_exact_calcul, dates_flux

from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd 
import calendar
import json 
with open ('param.json','r') as file:
    data=json.load(file)
table_morta= pd.read_csv("Table unisexe.csv",sep= ';',index_col=0)

#lire les dates en python
date_naissance_contractant = datetime.strptime(data['date_naissance_contractant'], "%d/%m/%Y")
date_effet_rente = datetime.strptime(data['date_effet_rente'], "%d/%m/%Y")
date_naissance_conjoint = datetime.strptime(data['date_naissance_conjoint'], "%d/%m/%Y")

def Quotient_Lx (dates_flux_liste, Lx_exact_1 ):
    Quotient_Lx_ex_sur_Lx_ex = []
    
    for indice in range(0,len(Lx_colonne_liste)) :
        if (Lx_exact[indice]==0) : 
            Quotient_Lx_ex_sur_Lx_ex.append(0)
        else :
            Quotient_Lx_ex_sur_Lx_ex.append(arrondi_excel(Lx_exact[indice]/Lx_exact[0],3))
    return(Quotient_Lx_ex_sur_Lx_ex)

Lx_exact_surLx= Quotient_Lx(dates_flux_liste, Lx_exact)
Ly_exact_surLy = Quotient_Lx(dates_flux_liste, Ly_exact)

#print(Lx_exact_surLx)
#print(Ly_exact_surLy)

#print(Lx_exact)