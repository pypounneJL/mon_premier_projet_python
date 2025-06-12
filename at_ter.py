
import time 
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime

from dateutil.relativedelta import relativedelta
import pandas as pd 
import calendar









def calcul_at_ter(prorata_deces,probabilité_décès_desDeux,Lx_exact_surLx,annuite_garantie,fractionnement,taux_technique,taux_rev, arreage_deces,terme):
    at_ter=[]
    
    for indice in range(min(len(prorata_deces),len(probabilité_décès_desDeux),len(Lx_exact_surLx), len(annuite_garantie))) :
        if terme == "avance" or arreage_deces == "annulé" :
            C=0
        else : 
            if arreage_deces == "entier" :
                C = prorata_deces[indice] * 1

            else : 
                C = prorata_deces[indice]*(0.5*1/(1+taux_technique)**(0.5/fractionnement))

        at_ter.append((Lx_exact_surLx[indice] + taux_rev*probabilité_décès_desDeux[indice] + C)*annuite_garantie[indice]*1)
    return at_ter   


#print (Lx_exact_surLx[2], probabilité_décès_desDeux[2] ,annuite_garantie[2],prorata_deces[2])
#print(at_ter)

def calcul_at_bis(at_ter,fractionnement,annuité_gar,majoration,pourcentage_majo,annuite_garantie ):
    at_bis= []

    for indice in range(len(at_ter)) :
        if indice/fractionnement < annuité_gar +1/fractionnement :
            at_bis.append(annuite_garantie[indice])
        elif indice/fractionnement < majoration +1/fractionnement:
            at_bis.append(at_ter[indice])
        else :
            at_bis.append(at_ter[indice]*(1+pourcentage_majo))
    return at_bis

#print(at_bis)

def calcul_ax (terme,at_bis,fractionnement,cc):

    if terme=="echu" :
        somme = sum(at_bis[1:])
    else : 
        somme = sum(at_bis)
    ax= somme/fractionnement
    rente_brut = cc/ax 
    print(ax, rente_brut)
    


