import numpy as np
import pandas as pd
import pyodbc

# Établir une connexion à la base de données SQL Server
conn_str = (
    'DRIVER={SQL Server};'
    'SERVER=STG-ERP-4;'
    'DATABASE=Vente_Retail;'
)

# Requête SQL pour sélectionner les données pertinentes pour la prévision
query = '''
    SELECT fo.Item_Number,
       AVG(Distinct CONVERT(INT,r.AverageTemperature))*1.5 as AverageTemperature,
       AVG(Distinct p.CatalogPrice)*2 AS CatalogPrice,
       AVG(DISTINCT p.QualRating)*3 AS QualRating,
       AVG(fo.UnitPrice)*1.5 AS AvgUnitPrice,
       SUM(fo.SalesQty)*2 AS TotalSalesQty,
       SUM(fo.Sales)*2 AS TotalSales,
       MIN(fo.Order_Date) AS MinOrderDate,
       MAX(fo.Order_Date) AS MaxOrderDate,
       COUNT(fo.Customer_Number)*3 AS Customer_Number,
       -AVG(CONVERT(FLOAT, fo.number_of_Days_Late))*3 AS AverageLate
FROM Fact_Order fo
INNER JOIN Product p ON fo.Item_Number = p.Number
INNER JOIN Dim_Region r ON r.Id_Region = fo.Id_Region
GROUP BY fo.Item_Number

'''

# Se connecter à la base de données et récupérer les données
with pyodbc.connect(conn_str) as conn:
    data = pd.read_sql_query(query, conn)

# Convertir les colonnes appropriées en nombres
numeric_columns = ['CatalogPrice', 'QualRating','AverageTemperature', 'Customer_Number','AvgUnitPrice', 'TotalSalesQty', 'TotalSales', 'AverageLate']
for column in numeric_columns:
    data[column] = pd.to_numeric(data[column], errors='coerce')

# Combiner les colonnes en une seule colonne
data['Combined_Columns'] = data[numeric_columns].sum(axis=1)

# Calculer la durée de prévision pour chaque groupe de produits
data['Forecast_Duration'] = (data['MaxOrderDate'] - data['MinOrderDate']).dt.days

# Appliquer le lissage exponentiel à la colonne combinée
alpha = 0.2  # Ajustez ce paramètre en fonction de vos besoins
data['Smoothed_Combined'] = data.groupby('Item_Number')['Combined_Columns'].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

# Calculer l'indicateur de prévision de demande entre 1 et 10
min_smoothed_combined = data['Smoothed_Combined'].min()
max_smoothed_combined = data['Smoothed_Combined'].max()
data['Indicateur_demande'] = ((data['Smoothed_Combined'] - min_smoothed_combined) / (max_smoothed_combined - min_smoothed_combined) * 9 + 1).round(2)

# Appliquer le lissage exponentiel à la durée de prévision
data['Duree_demande'] = data.groupby('Item_Number')['Forecast_Duration'].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

# Afficher les données prévues pour les produits de la dimension produit
product_data = data[['Item_Number', 'CatalogPrice', 'QualRating','AverageTemperature', 'AvgUnitPrice', 'TotalSalesQty', 'TotalSales', 'Indicateur_demande', 'Duree_demande']]
print(product_data)

# Enregistrer les données dans un fichier Excel
product_data.to_excel("product_prediction_BI.xlsx", index=False)
