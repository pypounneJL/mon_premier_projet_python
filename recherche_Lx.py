from calcul_age import age_exact, decimal_age, arrondi_excel
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


age_exact_contractant= age_exact(date_naissance_contractant , date_effet_rente)
décimal_age_contractant= decimal_age(date_naissance_contractant)
age_exact_conjoint= age_exact(date_naissance_conjoint, date_effet_rente)
decimal_age_conjoint= decimal_age(date_naissance_conjoint)

print(age_exact_conjoint)
#recuperation de la colonne Lx qui est le nombre de personne en vie restante pour un age donné à une année de naissance donnée 





def recuperation_Lx(date_naissance):
    Lx_collonne = []
    année_naissance=date_naissance.year 
    for age in range(0, 500) :
        
        Lx_collonne.append(table_morta.loc[age , str(année_naissance)])
    return Lx_collonne

    
    
Lx_contractant=recuperation_Lx(date_naissance_contractant)
print(Lx_contractant)
Ly_conjoint= recuperation_Lx(date_naissance_conjoint)

