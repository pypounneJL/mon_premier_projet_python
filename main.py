from datetime import datetime
import pandas as pd 
import numpy as np
import json 
import time 
from at_ter import calcul_at_ter,calcul_at_bis,calcul_ax
from calcul_annexe import probas_deces,calcul_annuite_garantie
from calcul_age import arrondi_excel, age_exact, decimal_age 
from prorata_deces import calcul_prorata_deces 
from calcul_flux import dates_flux, Lx_exact_calcul
from quotien import Quotient_Lx

with open ('param.json','r') as file:
    data=json.load(file)
a=time.time()
date_naissance_contractant = datetime.strptime(data['date_naissance_contractant'], "%d/%m/%Y")
date_effet_rente = datetime.strptime(data['date_effet_rente'], "%d/%m/%Y")
date_naissance_conjoint = datetime.strptime(data['date_naissance_conjoint'], "%d/%m/%Y")
date_calcul = datetime.strptime(data['date_de_calcul'], "%d/%m/%Y")
table_morta= pd.read_csv("Table unisexe.csv",sep= ';',index_col=0)

taux_technique = data['taux_technique']
fractionnement = 4
terme = "echu"
arreage_deces = "annulé"
majoration = 0
pourcentage_majo=0
annuité_gar = 0
taux_reversion=0

dates_flux_liste, age_ENT_contractant_liste, age_Exact_contractant_liste, age_exact_conjoint_liste, age_ENT_conjoint_liste, Ly_colonne_liste, Ly_plus1_colonne_liste, Lx_colonne_liste, Lxplus1_colonne_liste = dates_flux(date_effet_rente, fractionnement, date_naissance_contractant,date_naissance_conjoint)

Lx_exact = Lx_exact_calcul(Lxplus1_colonne_liste, Lx_colonne_liste, date_naissance_contractant, dates_flux_liste)
Ly_exact = Lx_exact_calcul(Ly_plus1_colonne_liste, Ly_colonne_liste, date_naissance_conjoint, dates_flux_liste )

Lx_exact_0 = arrondi_excel((1-decimal_age(date_naissance_contractant,date_calcul))*Lx_colonne_liste[0]+decimal_age(date_naissance_contractant,date_calcul)*Lxplus1_colonne_liste[0],3)
Ly_exact_0 = arrondi_excel((1-decimal_age(date_naissance_conjoint,date_calcul))*Ly_colonne_liste[0]+decimal_age(date_naissance_conjoint,date_calcul)*Ly_plus1_colonne_liste[0],3)

prorata_deces = calcul_prorata_deces(Lx_exact,Ly_exact,taux_reversion,Lx_exact_0,Ly_exact_0)
probas_deces_des_deux=probas_deces(Lx_colonne_liste, Ly_colonne_liste,Lx_exact_0,Ly_exact_0)
annuite_garantie = calcul_annuite_garantie(age_exact_conjoint_liste,taux_technique)
Lx_exact_surLx = Quotient_Lx(dates_flux_liste, Lx_exact)


at_ter=calcul_at_ter(prorata_deces,probas_deces_des_deux,Lx_exact_surLx,annuite_garantie,fractionnement,taux_technique,taux_reversion, arreage_deces,terme)
at_bis=calcul_at_bis(at_ter,fractionnement,annuité_gar,majoration,pourcentage_majo,annuite_garantie)


print (calcul_ax(terme,at_bis,fractionnement))
print(time.time()-a)





