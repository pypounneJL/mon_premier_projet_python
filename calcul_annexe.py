
from decimal import Decimal, ROUND_HALF_UP
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd 
import calendar



def probas_deces(Lx_ex_liste, Ly_ex_liste, Lx_exact_0, Ly_exact_0):
    # Conversion en numpy arrays
    Lx_ex = np.array(Lx_ex_liste)
    Ly_ex = np.array(Ly_ex_liste)
    
    # Calcul vectorisé
    proba_deces = (1 - Lx_ex / Lx_exact_0) * (Ly_ex / Ly_exact_0)
    
    return proba_deces

#recuperation de la colonne Lx qui est le nombre de personne en vie restante pour un age donné à une année de naissance donnée 

#def probas_deces (Lx_ex_liste,Ly_ex_liste,Lx_exact_0,Ly_exact_0) :
    #longueur = max(len(Lx_ex_liste), len(Ly_ex_liste))
    #proba_deces=[]
    #for indice in range(longueur) :
     #   proba_deces.append((1-Lx_ex_liste[indice]/Lx_exact_0)*(Ly_ex_liste[indice]/Ly_exact_0))

    
    #return proba_deces


#print(Ly_exact)

#print (probabilité_décès_desDeux)
def calcul_annuite_garantie(age_ex_liste, taux_tech):
    age_ex = np.array(age_ex_liste)
    
    Annuite_garantie = (1 / (1 + taux_tech)) ** (age_ex - age_ex[0])
    
    return Annuite_garantie




#print(annuité_garantie(age_Exact_contractant_liste, taux_technique))








        






