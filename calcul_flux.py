from calcul_age import age_exact, decimal_age
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


def dates_flux(date_debut,fractionnement,nb_annees,date_naisssance):
    mois_par_fractions=12//fractionnement 
    nb_periodes= nb_annees *fractionnement
    age_Exact=[]
    age_ENT = []
    dates_fin=[]
    for num_periode in range(nb_periodes):
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

        dates_fin.append(date_fin_periode)
        age_Exact.append(age_exact(date_naisssance,date_fin_periode))
        age_ENT.append(int(age_exact(date_naisssance,date_fin_periode)))
    return (dates_fin , age_ENT, age_Exact)
    


        

print(dates_flux(date_effet_rente, 4, 10, date_naissance_contractant))

