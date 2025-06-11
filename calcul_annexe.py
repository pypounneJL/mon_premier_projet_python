from calcul_age import age_exact, decimal_age, arrondi_excel
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd 
import calendar
from calcul_flux import dates_flux_liste, age_ENT_contractant_liste, Ly_exact,age_Exact_contractant_liste, age_exact_conjoint_liste, age_ENT_conjoint_liste, Ly_colonne_liste, Ly_plus1_colonne_liste, Lx_colonne_liste, Lxplus1_colonne_liste,Lx_exact,Lx_exact_calcul, dates_flux
from quotien import Ly_exact_surLy, Lx_exact_surLx
import json 
with open ('param.json','r') as file:
    data=json.load(file)
table_morta= pd.read_csv("Table unisexe.csv",sep= ';',index_col=0)

#lire les dates en python
date_naissance_contractant = datetime.strptime(data['date_naissance_contractant'], "%d/%m/%Y")
date_effet_rente = datetime.strptime(data['date_effet_rente'], "%d/%m/%Y")
date_naissance_conjoint = datetime.strptime(data['date_naissance_conjoint'], "%d/%m/%Y")
taux_technique = data['taux_technique']




#recuperation de la colonne Lx qui est le nombre de personne en vie restante pour un age donné à une année de naissance donnée 

def probas_deces (Lx_ex_liste,Ly_ex_liste,) :
    longueur = max(len(Lx_ex_liste), len(Ly_ex_liste))
    proba_deces=[]
    for indice in range(longueur) :
        proba_deces.append(arrondi_excel((1-Lx_ex_liste[indice]/Lx_ex_liste[0])*(Ly_ex_liste[indice]/Ly_ex_liste[0]), 3))

    
    return proba_deces

probabilité_décès_desDeux = probas_deces(Lx_exact,Ly_exact) 

#print (probabilité_décès_desDeux)

def annuité_garantie(age_ex_liste, taux_tech, ) : 
    Annuite_garantie=[]
    for indice in range(len(age_ex_liste)): 
        Annuite_garantie.append(pow(1/(1+taux_tech),(age_ex_liste[indice]-age_ex_liste[0])))
    return Annuite_garantie 

print(annuité_garantie(age_Exact_contractant_liste, taux_technique))







        






