import sqlalchemy as sql
import pandas as pd
from datetime import datetime
engine = sql.create_engine('mysql+pymysql://simplon:simplon@localhost/ASSURAUTO')

CL_ID = pd.read_sql_query('SELECT max(CL_ID) as max FROM CLIENTS;' , engine)['max'].values
CL_ID = CL_ID[0]+1
CO_CLIENTS_FK = CL_ID
CL_PRENOM = input('Entrez le prenom : ')
CL_NOM = input('Entrez le nom : ').upper()
CL_ADRESSE = input("Entrez l'adresse : ")
CL_POSTALE ='' 
while len(CL_POSTALE) == 0 :
    CL_POSTALE = input('Entrez le code postale : ')

    if (CL_POSTALE.isdigit()): 
        CL_POSTALE = CL_POSTALE

    else:
        print("ERRROR")
        CL_POSTALE = ''

CL_VILLE = input('Entrez la ville : ')
CL_COORDONNEES = input('Entrez les coordonnees : ')

engine.execute('INSERT INTO CLIENTS (CL_ID, CL_PRENOM, CL_NOM, CL_ADRESSE, CL_POSTALE, CL_VILLE, CL_COORDONNEES) values (%s,"%s","%s","%s",%s,"%s",%s);' %(CL_ID, CL_PRENOM, CL_NOM, CL_ADRESSE, CL_POSTALE, CL_VILLE, CL_COORDONNEES))


CO_CATEGORIE = input('Entrez la categorie : ')
CO_BONUS_MALUS = input('Entrez le bonus/malus : ')

engine.execute('INSERT INTO CONTRAT (CO_NUM, CO_DATE, CO_CATEGORIE, CO_BONUS_MALUS, CO_CLIENTS_FK) values ((SELECT max(CO_NUM)+1 from CONTRAT as CO), CURDATE(),"%s",%s,%s);' %( CO_CATEGORIE, CO_BONUS_MALUS,CO_CLIENTS_FK))