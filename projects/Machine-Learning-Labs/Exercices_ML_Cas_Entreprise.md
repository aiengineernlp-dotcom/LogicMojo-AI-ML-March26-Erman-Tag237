# Exercices ML/Statistiques — Cas Entreprise
### Deuxième série (niveau renforcé) — Tensoratech

**Instructions :**
- Même méthode qu'avant : code d'abord, preuve que ça tourne, explication avec tes mots, puis 5+ questions de compréhension.
- Ces cas sont volontairement plus "réalistes" (bruit dans les données, ambiguïtés) — attends-toi à ce que les résultats ne soient jamais parfaits.
- Réfléchis toujours : quel type de problème (régression/classification), quelle distribution, quels pièges potentiels, avant de coder.

---

## Problem 1 : Régression Linéaire Simple — Budget Marketing vs Trafic Site Web

Une startup SaaS a enregistré son budget marketing mensuel (en milliers d'AED) et le nombre de visiteurs uniques sur son site.

| Budget Marketing (k AED) | Visiteurs Uniques |
| --- | --- |
| 5 | 1200 |
| 8 | 1850 |
| 12 | 2600 |
| 15 | 3100 |
| 20 | 4300 |
| 25 | 5000 |

**Tâche :** Entraîne un modèle de régression linéaire simple. Rapporte la pente et l'intercept. Prédis le trafic pour un budget de 30k AED.

**Questions de compréhension :**
1. La pente obtenue — que représente-t-elle concrètement en termes de "visiteurs gagnés par AED de budget supplémentaire" ?
2. Avec 6 points de données, combien de points auras-tu dans X_test avec `test_size=0.2` ? Est-ce suffisant pour évaluer le modèle ?
3. Prédire pour 30k AED, c'est extrapoler au-delà de tes données observées (max = 25k). Pourquoi l'extrapolation est-elle risquée en régression linéaire ?
4. Si l'intercept était négatif, qu'est-ce que ça signifierait concrètement pour un budget de 0 AED — est-ce réaliste ?
5. Le trafic peut-il vraiment continuer à augmenter linéairement indéfiniment avec le budget ? Qu'est-ce que ça suggère sur les limites du modèle linéaire ici ?

---

## Problem 2 : Régression Linéaire Multiple — Prédiction de Salaire

Une entreprise tech veut estimer les salaires selon l'expérience et le niveau de diplôme (encodé en années d'études post-bac).

| Années d'expérience | Années d'études | Salaire (k AED/an) |
| --- | --- | --- |
| 1 | 3 | 60 |
| 3 | 4 | 85 |
| 5 | 5 | 110 |
| 7 | 3 | 105 |
| 10 | 5 | 160 |
| 2 | 5 | 80 |
| 8 | 4 | 130 |

**Tâche :** Entraîne un modèle multiple. Rapporte les coefficients et l'intercept. Prédis le salaire pour 6 ans d'expérience et 4 ans d'études. Attention à l'échelle des features avant d'interpréter les coefficients.

**Questions de compréhension :**
1. Les deux features (expérience, études) ont des échelles différentes (1-10 vs 3-5). Comment ça influence la comparaison directe des coefficients ?
2. Si le coefficient d'expérience est plus grand que celui des études, peux-tu conclure que l'expérience "compte plus" pour le salaire ? Pourquoi (repense à Area/Bedrooms) ?
3. Avec seulement 7 échantillons et 2 features, quel est le risque si tu ajoutais une 3ème feature au modèle ?
4. Que se passerait-il si "années d'études" et "années d'expérience" étaient fortement corrélées entre elles (quelqu'un avec plus d'études a souvent commencé à travailler plus tard) ?
5. Comment vérifierais-tu, avec du code, si ton modèle souffre de data leakage ici ?

---

## Problem 3 : Régression Polynomiale — Rendement d'une Campagne Publicitaire

Une équipe growth observe le revenu généré selon le budget pub investi — avec un effet de rendement décroissant au-delà d'un certain seuil.

| Budget Pub (k AED) | Revenu Généré (k AED) |
| --- | --- |
| 2 | 8 |
| 4 | 18 |
| 6 | 30 |
| 8 | 36 |
| 10 | 38 |
| 12 | 35 |

**Tâche :** Fitte un modèle polynomial degré 2. Interprète la forme de la courbe (est-ce que le rendement croît toujours, ou plafonne/décline ?). Prédis le revenu pour un budget de 14k AED — et discute si cette prédiction te semble fiable.

**Questions de compréhension :**
1. Regarde les données : entre budget=10 et budget=12, le revenu diminue (38→35). Qu'est-ce que ça indique sur la forme de la courbe (parabole vers le haut ou vers le bas) ?
2. Si le coefficient de x² est négatif, qu'est-ce que ça signifie sur le comportement du modèle à très long terme (budget très élevé) ?
3. Pourquoi une prédiction à 14k AED (au-delà du max observé de 12k) est-elle particulièrement risquée ici, plus encore qu'en régression linéaire simple ?
4. Ce dataset a-t-il une relation parfaite comme `y=2x²` (Problem 3 du premier set), ou y a-t-il du bruit ? Comment le vérifier par calcul ?
5. Un "rendement décroissant" en marketing est un phénomène connu (loi des rendements décroissants). Le degré 2 est-il le bon choix pour capter ça, ou faudrait-il envisager un autre modèle ?

---

## Problem 4 : Train-Test Split — Dataset Churn Client

Un dataset de 20 clients d'un service d'abonnement, avec 3 features (ancienneté en mois, nombre de tickets support, note de satisfaction /10) et une cible binaire (churn = 1 quitté, 0 resté).

*(Génère toi-même ce dataset avec `np.random.seed(42)` pour 20 lignes réalistes — ancienneté entre 1-36 mois, tickets entre 0-10, satisfaction entre 1-10, churn corrélé négativement à la satisfaction.)*

**Tâche :** Split 80/20, `random_state=42`. Rapporte les tailles train/test et la shape de X_train. Réfléchis : avec 20 échantillons, est-ce un split plus raisonnable qu'avec 5 ou 15 ?

**Questions de compréhension :**
1. Avec 20 échantillons et test_size=0.2, combien de points auras-tu en test ? Est-ce plus fiable statistiquement que 1 seul point ?
2. La target "churn" est binaire (0/1) — est-ce toujours un problème de régression, ou plutôt de classification ? Qu'est-ce que ça changerait dans le choix du modèle ?
3. Si 18 clients sur 20 n'ont pas churné (classe déséquilibrée), quel risque cela pose-t-il pour l'évaluation du modèle avec un simple split aléatoire ?
4. Pourquoi utilise-t-on `random_state=42` ici aussi, alors que le dataset est déjà généré aléatoirement une fois ?
5. Qu'est-ce qui changerait dans ton approche si, au lieu de prédire churn (0/1), on te demandait de prédire le nombre de mois avant churn (valeur continue) ?

---

## Problem 5 : Statistiques Descriptives — Temps de Réponse Support Client

Temps de réponse (en minutes) pour 12 tickets support résolus cette semaine :

`4, 7, 5, 32, 6, 8, 5, 9, 6, 7, 5, 4`

**Tâche :** Calcule mean, median, mode, variance, écart-type. Compare mean et median — que remarques-tu, et à quoi ça pourrait être dû (regarde bien les valeurs) ?

**Questions de compréhension :**
1. La valeur 32 est très éloignée du reste des données. Comment cette valeur influence-t-elle la moyenne vs la médiane ?
2. Entre mean et median, laquelle est la plus représentative du temps de réponse "typique" ici ? Pourquoi ?
3. Calcule manuellement : si tu retirais la valeur 32 du dataset, la moyenne changerait-elle beaucoup ? Et la médiane ?
4. Le mode ici (valeur la plus fréquente) — est-il proche de la moyenne ou de la médiane ? Qu'est-ce que ça t'indique ?
5. En tant que manager support, quelle statistique choisirais-tu pour communiquer la performance de l'équipe — et pourquoi la moyenne seule pourrait être trompeuse ?

---

## Problem 6 : Z-Score — Détection de Transaction Suspecte

Montants de 10 transactions récentes sur un compte (en AED) :

`120, 95, 150, 110, 130, 105, 140, 4800, 115, 125`

**Tâche :** Calcule le z-score de chaque transaction. Identifie si une transaction dépasse `|z| > 2`. Dans un contexte de détection de fraude, qu'est-ce que ce résultat suggère ?

**Questions de compréhension :**
1. La transaction de 4800 AED va fortement influencer la moyenne et l'écart-type calculés sur ces 10 valeurs — en quoi ça complique la détection par z-score ici ?
2. Si tu recalculais mean/std en excluant la transaction suspecte, les z-scores des autres transactions changeraient-ils ? Dans quel sens ?
3. Un seuil `|z| > 2` correspond à environ quelle proportion de "normalité" attendue (repense à la règle 68-95-99.7) ?
4. En pratique, un système de détection de fraude bancaire se baserait-il uniquement sur 10 transactions historiques pour définir "normal" ? Quelle est la limite ici ?
5. Le z-score suppose une distribution normale des montants de transaction. Est-ce réaliste pour des montants d'achat (qui ne peuvent pas être négatifs) ?

---

## Problem 7 : Corrélation — Temps de Chargement Site vs Taux de Conversion

Une équipe produit a mesuré le temps de chargement moyen (secondes) d'une page et le taux de conversion (%) correspondant sur plusieurs jours.

| Temps de Chargement (s) | Taux de Conversion (%) |
| --- | --- |
| 1.2 | 8.5 |
| 2.0 | 7.1 |
| 2.8 | 5.9 |
| 3.5 | 4.8 |
| 4.2 | 4.0 |
| 5.0 | 3.1 |

**Tâche :** Calcule Pearson. Interprète force et direction. Cette corrélation prouve-t-elle que la lenteur *cause* la baisse de conversion ?

**Questions de compréhension :**
1. Le coefficient de Pearson ici devrait être négatif — pourquoi (regarde le sens de variation des deux colonnes) ?
2. Cite un facteur externe (variable cachée) qui pourrait expliquer à la fois un temps de chargement lent ET une conversion basse, sans lien de causalité direct.
3. Si la relation réelle entre temps de chargement et conversion était en forme de "coude" (chute brutale après un seuil, puis stable), Pearson capterait-il bien cette relation ? Pourquoi ?
4. Avec seulement 6 points, quelle est la fiabilité de cette corrélation pour orienter une décision produit coûteuse (comme refaire l'infrastructure) ?
5. Si on voulait prouver la causalité (pas juste la corrélation), quel type d'expérience faudrait-il mettre en place ?

---

## Problem 8 : Probabilité Binomiale — Taux de Conversion Publicitaire

Une publicité en ligne a un taux de clic historique (CTR) de 4%. Sur 20 impressions montrées à des utilisateurs différents.

**Tâche :** Calcule la probabilité d'obtenir exactement 2 clics. Puis calcule la probabilité d'obtenir **au moins 1 clic** (utilise la logique 1 - P(0 clic), pas juste `pmf`).

**Questions de compréhension :**
1. Quelles sont les 3 conditions qui justifient l'usage d'une binomiale ici (n, p, indépendance) — sont-elles vraiment respectées dans un vrai système publicitaire ?
2. Pourquoi calcule-t-on "au moins 1 clic" via `1 - P(0 clic)` plutôt que d'additionner P(1)+P(2)+...+P(20) directement ?
3. Si le CTR réel variait selon l'heure de la journée (pas constant à 4%), quelle condition de la binomiale serait violée ?
4. Avec CTR=4% et 20 impressions, quel est, selon toi, le nombre de clics le plus probable (sans calculer, juste intuition) ? Vérifie ensuite avec le code.
5. En marketing digital, pourquoi la binomiale est-elle utile pour définir si une campagne "sous-performe" statistiquement, plutôt que de juger sur un seul jour de résultats ?

---

## Problem 9 : Distribution Normale — Temps de Livraison

Les temps de livraison d'un service de livraison suivent (approximativement) une distribution normale, moyenne de 35 minutes, écart-type de 6 minutes.

**Tâche :** (a) Quel % de livraisons arrivent entre 29 et 41 minutes ? (b) Quelle est la probabilité qu'une livraison prenne plus de 50 minutes ? (c) Ce dernier résultat te semble-t-il cohérent avec la règle 68-95-99.7, ou est-ce un cas plus extrême — pourquoi ?

**Questions de compréhension :**
1. L'intervalle [29,41] correspond à combien d'écarts-types autour de la moyenne ? Quel % attendu selon la règle 68-95-99.7 ?
2. 50 minutes correspond à combien d'écarts-types au-dessus de la moyenne ? Cette probabilité devrait-elle être petite ou grande ?
3. Pourquoi utilise-t-on `1 - norm.cdf(50, mu, sigma)` plutôt que `norm.cdf(50, mu, sigma)` directement pour la question (b) ?
4. Un temps de livraison ne peut jamais être négatif — pourtant la distribution normale théorique s'étend jusqu'à -∞. Pourquoi ce n'est généralement pas un problème pratique ici (regarde la valeur de μ-3σ) ?
5. Si un client se plaint d'avoir attendu 55 minutes, est-ce un cas "normal" selon ce modèle, ou plutôt une anomalie à investiguer ?

---

## Problem 10 : Test t Apparié — Impact d'un Redesign UI sur le Taux de Conversion

Une équipe produit a testé un redesign de page checkout sur 8 jours, en comparant le taux de conversion (%) de l'ancienne version vs la nouvelle version, mesuré sur les mêmes segments d'utilisateurs.

| Jour | Conversion Avant (%) | Conversion Après (%) |
| --- | --- | --- |
| 1 | 3.2 | 3.5 |
| 2 | 2.9 | 3.1 |
| 3 | 3.5 | 3.4 |
| 4 | 3.0 | 3.6 |
| 5 | 3.3 | 3.8 |
| 6 | 2.8 | 3.0 |
| 7 | 3.1 | 3.3 |
| 8 | 3.4 | 3.7 |

**Tâche :** Formule H0/H1. Effectue un test t apparié à 5% de signification. Conclus. Avec des différences aussi petites, la significativité statistique garantit-elle un impact *business* important ?

**Questions de compréhension :**
1. Pourquoi un test t apparié est-il adapté ici plutôt qu'un test indépendant (même segments d'utilisateurs mesurés 2 fois) ?
2. Si le p_value obtenu est < 0.05, que conclus-tu sur H0 et H1 ?
3. Les différences jour par jour sont petites (souvent <0.5 point de %). Un résultat statistiquement significatif est-il automatiquement significatif *business* (ex: rentabilise le coût du redesign) ? Distingue les deux notions.
4. Si tu avais seulement 3 jours de données au lieu de 8, la conclusion serait-elle aussi fiable ? Pourquoi ?
5. Quelle serait la conséquence de tester `ttest_rel(avant, après)` au lieu de `ttest_rel(après, avant)` sur l'interprétation du signe du t_stat ?

---

*Fin du set. Même méthode que d'habitude : on avance un problème à la fois, code → preuve → explication → questions.*
