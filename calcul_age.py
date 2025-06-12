from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd 
import calendar
import json 


def arrondi_excel(valeur, nb_decimales):
    facteur = Decimal('1.' + '0'*nb_decimales)
    return float(Decimal(str(valeur)).quantize(facteur, rounding=ROUND_HALF_UP))




def age_exact(date_naissance, date_effet_rente) :
    """on rentre en argument la date de naissance et la date d'effet de la rente ATTENTION elle doivent eêtre au format date de python """

        # --- Fraction du premier mois ---
    # Dernier jour du mois de naissance
    dernier_jour_mois_naissance = calendar.monthrange(date_naissance.year, date_naissance.month)[1]

    fraction_premier_mois = arrondi_excel(
        (dernier_jour_mois_naissance - date_naissance.day + 1) / dernier_jour_mois_naissance, 3
    )
    # --- Nombre de mois pleins entre naissance et mois précédent contrat ---
    # Date du mois précédent contrat
    mois_precedent_contrat = date_effet_rente - relativedelta(months=1)

    nb_annees = mois_precedent_contrat.year - date_naissance.year
    nb_mois = mois_precedent_contrat.month - date_naissance.month

    total_mois = nb_annees * 12 + nb_mois
    # comme les contrats commencent le 01/m/n on a fini car on a la fractions de mois entre la naissance et la fin du mois de naissance
    dernier_jour_mois_contrat = calendar.monthrange(date_effet_rente.year, date_effet_rente.month)[1]

    fraction_dernier_mois = round((date_effet_rente.day - 1) / dernier_jour_mois_contrat, 3)

        # --- Calcul final ---
    age_exact = arrondi_excel((fraction_premier_mois + total_mois + fraction_dernier_mois) / 12, 3)
    
    
    return age_exact




def decimal_age(date_naissance, date_flux):
    return arrondi_excel((age_exact(date_naissance , date_flux))-int(age_exact(date_naissance, date_flux)), 3) 

#print(decimal_age(date_naissance_contractant, date_effet_rente))
#print(age_exact(date_naissance_contractant, date_effet_rente))













