from calcul_age import age_exact, decimal_age,arrondi_excel
from decimal import Decimal, ROUND_HALF_UP
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

def dates_flux(date_debut, fractionnement, date_naissance_cont, date_naissance_conj):
    mois_par_fractions = 12 // fractionnement 
    num_periode = 0
    
    age_Exact_cont = [age_exact(date_naissance_cont, date_debut)]
    age_ENT_cont = [int(age_Exact_cont[0])]
    age_exact_conj = [age_exact(date_naissance_conj, date_debut)]
    age_ENT_conj = [int(age_exact_conj[0])]
    
    annee_naissance_cont = date_naissance_cont.year
    annee_naissance_conj = date_naissance_conj.year 
    
    Lx_colonne = [table_morta.loc[age_ENT_cont[0], str(annee_naissance_cont)]]
    Lxplus1_colonne = [table_morta.loc[age_ENT_cont[0] + 1, str(annee_naissance_cont)]]
    Ly_colonne = [table_morta.loc[age_ENT_conj[0], str(annee_naissance_conj)]]
    Ly_plus1_colonne = [table_morta.loc[age_ENT_conj[0] + 1, str(annee_naissance_conj)]]

    dates_fin = [date_debut]
   
    while age_Exact_cont[num_periode] < 121 and age_exact_conj[num_periode] < 121:
        date_periode = date_debut + relativedelta(months=mois_par_fractions * (num_periode + 1))

        annee = date_periode.year
        mois = date_periode.month
        if mois == 1:
            annee -= 1
            mois = 12
        else:
            mois -= 1

        dernier_jour = calendar.monthrange(annee, mois)[1]
        date_fin_periode = datetime(annee, mois, dernier_jour)

        num_periode += 1
        dates_fin.append(date_fin_periode)

        # Factoriser les calculs d'ages
        age_exact_cont_period = age_exact(date_naissance_cont, date_fin_periode)
        age_ENT_cont_period = int(age_exact_cont_period)

        age_exact_conj_period = age_exact(date_naissance_conj, date_fin_periode)
        age_ENT_conj_period = int(age_exact_conj_period)

        age_Exact_cont.append(age_exact_cont_period)
        age_ENT_cont.append(age_ENT_cont_period)

        age_exact_conj.append(age_exact_conj_period)
        age_ENT_conj.append(age_ENT_conj_period)

        Lxplus1_colonne.append(table_morta.loc[age_ENT_cont_period + 1, str(annee_naissance_cont)])
        Lx_colonne.append(table_morta.loc[age_ENT_cont_period, str(annee_naissance_cont)])

        Ly_colonne.append(table_morta.loc[age_ENT_conj_period, str(annee_naissance_conj)])
        Ly_plus1_colonne.append(table_morta.loc[age_ENT_conj_period + 1, str(annee_naissance_conj)])

    return dates_fin, age_ENT_cont, age_Exact_cont, age_exact_conj, age_ENT_conj, Ly_colonne, Lxplus1_colonne, Lx_colonne, Lxplus1_colonne
    




def Lx_exact_calcul(Lxplu1_liste, Lx_liste,date_naissance, date_flux_liste):
     Lx_exact = []
     
    
     for k in range (len(Lx_liste)):
        
         deci_age = decimal_age(date_naissance,date_flux_liste[k])
         #print(deci_age)
         #print(Lx_liste[k])
       
         Lx_exact.append(((1-deci_age)*Lx_liste[k] + Lxplu1_liste[k]*deci_age))
         

     return Lx_exact 


#print(Lx_exact_0, Ly_exact_0, Ly_colonne_liste[0], Ly_plus1_colonne_liste[0])
#print(age_ENT_liste)
#print(dates_flux_liste)
#print(L_colonne_liste)

#print (decimal_age(date_naissance_contractant, dates_flux_liste[0]))

#print(age_exact(date_naissance_contractant, dates_flux_liste[0]))

#print(Lx_exact)
#print(Lx_colonne_liste)

