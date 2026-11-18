
from csv_reader import charger_csv

try:
    articles = charger_csv("articles.csv")

    print("Importation réussie !")
    print("Liste des articles :")

    for article in articles:
        print(article)

except Exception as e:
    print("Erreur :", e)
