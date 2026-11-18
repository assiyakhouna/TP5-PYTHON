
class CsvException(Exception):
    pass


class FichierIntrouvableException(CsvException):
    pass


class LigneInvalideException(CsvException):
    pass


class PrixNegatifException(CsvException):
    pass

import csv
import os


def charger_csv(chemin):
    # 1. Vérifier si le fichier existe
    if not os.path.exists(chemin):
        raise FichierIntrouvableException(
            f"Le fichier '{chemin}' est introuvable."
        )

    articles = []

    # 2. Ouvrir et lire le fichier CSV
    with open(chemin, "r", encoding="utf-8") as fichier:
        lecteur = csv.reader(fichier, delimiter=";")

        # Ignorer l'en-tête
        next(lecteur, None)

        for numero, ligne in enumerate(lecteur, start=2):

            # Ignorer les lignes vides
            if not ligne:
                continue

            # 3. Vérifier le nombre de colonnes
            if len(ligne) != 3:
                raise LigneInvalideException(
                    f"Ligne {numero} : exactement 3 colonnes sont attendues."
                )

            identifiant, nom, prix = ligne

            # 4. Vérifier que le prix est numérique
            try:
                prix = float(prix)
            except ValueError:
                raise LigneInvalideException(
                    f"Ligne {numero} : le prix doit être numérique."
                )

            # 5. Vérifier que le prix est positif
            if prix <= 0:
                raise PrixNegatifException(
                    f"Ligne {numero} : le prix doit être supérieur à zéro."
                )

            # 6. Ajouter l'article
            articles.append({
                "id": identifiant,
                "nom": nom,
                "prix": prix
            })

    return articles
