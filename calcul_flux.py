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


def dates_flux(date_debut,fractionnement,date_naissance_cont, date_naissance_conj):
    mois_par_fractions=12//fractionnement 
    
    num_periode = 0
    
    
    age_Exact_cont = [age_exact(date_naissance_cont,date_debut)]
    age_ENT_cont = [int(age_exact(date_naissance_cont,date_debut))]
    age_exact_conj = [age_exact(date_naissance_conj,date_debut)]
    age_ENT_conj = [int(age_exact(date_naissance_conj,date_debut))]
    
    annee_naissance_cont=date_naissance_cont.year
    annee_naissance_conj = date_naissance_conj.year 
    
    Lx_colonne = [table_morta.loc[int(age_exact(date_naissance_cont,date_debut)) , str(annee_naissance_cont)]]
    Lxplus1_colonne = [table_morta.loc[int(age_exact(date_naissance_cont,date_debut))+1 , str(annee_naissance_cont)]]
    Ly_colonne=[table_morta.loc[int(age_exact(date_naissance_conj,date_debut))+1 , str(annee_naissance_conj)]]
    Ly_plus1_colonne=[table_morta.loc[int(age_exact(date_naissance_conj,date_debut)) , str(annee_naissance_conj)]]

    dates_fin = [date_debut]
   
    
    while age_Exact_cont[num_periode]<121 and age_exact_conj[num_periode] < 121:
        # Calcul de la date de début de la prochaine période
        date_periode = date_debut +relativedelta(months=mois_par_fractions*(num_periode+1))

        # on veut la date de fin du mois précédent la nouvelle période 
        annee = date_periode.year
        mois = date_periode.month
        if mois == 1 :
            annee -= 1
            mois = 12 
        else :
            mois -= 1

        dernier_jour = calendar.monthrange(annee, mois)[1]
        date_fin_periode = datetime (annee, mois, dernier_jour)

        
        
        num_periode +=1
        dates_fin.append(date_fin_periode) #on a la date de fin de periode
       
        age_Exact_cont.append(age_exact(date_naissance_cont,date_fin_periode)) #dessus on clacul l'age exact
        age_ENT_cont.append(int(age_exact(date_naissance_cont,date_fin_periode)))#puis on calcul l'age entier
        
        age_exact_conj.append(age_exact(date_naissance_conj, date_fin_periode))
        age_ENT_conj.append(int(age_exact(date_naissance_conj, date_fin_periode)))
        
        Lxplus1_colonne.append(table_morta.loc[int(age_exact(date_naissance_cont,date_fin_periode)+1) , str(annee_naissance_cont)])
        Lx_colonne.append(table_morta.loc[int(age_exact(date_naissance_cont,date_fin_periode)) , str(annee_naissance_cont)])# de l'age entier on récupère les Lx

        Ly_colonne.append(table_morta.loc[int(age_exact(date_naissance_conj,date_fin_periode)) , str(annee_naissance_conj)])
        Ly_plus1_colonne.append(table_morta.loc[int(age_exact(date_naissance_conj,date_fin_periode)+1) , str(annee_naissance_conj)])

    return dates_fin , age_ENT_cont, age_Exact_cont, age_exact_conj,age_ENT_conj,  Ly_colonne, Lxplus1_colonne, Lx_colonne,Lxplus1_colonne 
    

dates_flux_liste, age_ENT_contractant_liste, age_Exact_contractant_liste, age_exact_conjoint_liste, age_ENT_conjoint_liste, Ly_colonne_liste, Ly_plus1_colonne_liste, Lx_colonne_liste, Lxplus1_colonne_liste = dates_flux(date_effet_rente, 4, date_naissance_contractant,date_naissance_conjoint)


def Lx_exact_calcul(Lxplu1_liste, Lx_liste, n_arrondi,date_naissance, date_flux_liste):
     Lx_exact = []
     
    
     for k in range (len(Lx_colonne_liste)):
        
         deci_age = decimal_age(date_naissance,date_flux_liste[k])
         #print(deci_age)
         #print(Lx_liste[k])
       
         Lx_exact.append(arrondi_excel((1-deci_age)*Lx_liste[k] + Lxplu1_liste[k]*deci_age, n_arrondi))

     return Lx_exact 

Lx_exact = Lx_exact_calcul(Lxplus1_colonne_liste, Lx_colonne_liste, 3, date_naissance_contractant, dates_flux_liste)
Ly_exact = Lx_exact_calcul(Ly_plus1_colonne_liste, Ly_colonne_liste,3, date_naissance_conjoint, dates_flux_liste )
#print(age_ENT_liste)
#print(dates_flux_liste)
#print(Lx_colonne_liste)

#print (decimal_age(date_naissance_contractant, dates_flux_liste[0]))

#print(age_exact(date_naissance_contractant, dates_flux_liste[0]))

#print(Lx_exact)
#print(Lx_colonne_liste)

