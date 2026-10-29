# CONVERSATION.md : échanges avec l'IA (Claude)

## Contexte
Examen final, session 8 : Campaign Audit Quiz. Fichier de données : `campaigns_A.csv`.
J'ai utilisé Claude comme assistant. Claude a écrit la première version de `campaign_audit.py`,
puis je l'ai relue, testée et expliquée fonction par fonction pour la comprendre.

## 1. Ask : ce que j'ai demandé
J'ai donné à Claude le sujet de l'examen (PDF) et mon fichier `campaigns_A.csv`, et je lui ai demandé
d'écrire le programme : lire le CSV, calculer CTR / CPA / ROAS, poser 5 questions, donner le score,
écrire `result.csv`.

## 2. Read : ce que Claude a trouvé dans le fichier (il n'est pas propre)
- Séparateur `;` et non `,`.
- Un caractère invisible au début du fichier (BOM) -> lecture avec `utf-8-sig`.
- Une colonne vide entre `Conversions` et `Revenue (€)` -> lecture des colonnes par leur nom.
- Virgule décimale (`11088,60`) -> remplacée par un point avant `float()`.
- Une campagne sans impressions (Monthly Newsletter) -> exclue de tous les calculs.
- Deux campagnes à 0 conversion (Black Friday, App Install) -> pas de CPA (None), mais
  gardées pour les autres calculs. Cela évite l'erreur `ZeroDivisionError`.

## 3. Adapt : ce qu'il a fallu adapter à MON fichier
- Les noms de colonnes exacts : `Cost (€)`, `Revenue (€)`, `Conversions`.
- Question 5 : l'énoncé ne dit pas si le CTR moyen est en ratio ou en pourcentage.
  J'ai choisi le pourcentage (2,60 %). Si le prof attend le ratio, il suffit de changer une ligne dans `main()`.

## 4. Check : vérification à la main
J'ai recalculé les valeurs avec un petit script indépendant. Résultats identiques à ceux du programme :
- Meilleur CTR : Aurora Launch (4,07 %)
- CPA le plus élevé : Blog Traffic (49,36 €)
- Campagnes avec ROAS > 3 : 7
- Canal avec le plus de conversions : YouTube Ads (4125)
- CTR moyen : 2,60 %

## 5. Erreurs et points difficiles
- Risque d'erreur principal : diviser par 0 quand une campagne a 0 conversion. Corrigé avec
  `if c["conversions"]:` avant la division.
- Risque 2 : case vide ou texte illisible dans le CSV. Corrigé avec `parse_number`, qui renvoie `None`
  au lieu de planter.
- Un test avec des réponses fausses a bien produit un score de 0/5 sans plantage et a écrit `result.csv`.

## 6. Ce que j'ai compris
(À compléter avec mes propres mots.)
