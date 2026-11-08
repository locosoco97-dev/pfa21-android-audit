# Matrice des risques

Probabilité (P) et impact (I) : 1 faible · 3 fort. Criticité = P × I.

| ID | Risque | P | I | Crit. | Parade | Responsable |
|---|---|---|---|---|---|---|
| R1 | Cible inadaptée ou licence floue | 1 | 2 | 2 | Cible créée par l'équipe (EventSchedule) | A |
| R2 | Faux positifs (LAUNCHER, valeurs par défaut de `exported`) | 2 | 3 | 6 | Règles documentées, tests de cas limites (S3/S4) | A |
| R3 | Docker indisponible ou non fonctionnel sur un poste | 2 | 3 | 6 | Scripts `setup.sh`/`setup.ps1`, alternative `venv` Python documentée | B |
| R4 | Environnement non reproductible d'un poste à l'autre | 2 | 3 | 6 | Versions figées dans `requirements.txt`, test à froid en S5 | B |
| R5 | Dérive vers MobSF/APK avant le MVP | 2 | 2 | 4 | Extensions gelées jusqu'à validation du MVP | A+B |
| R6 | Un membre ne maîtrise pas tout le projet | 2 | 3 | 6 | Revues croisées, démonstration individuelle en S6 | A+B |
| R7 | Retard sur le calendrier | 2 | 2 | 4 | Revue de fin de sprint, périmètre MVP prioritaire | A+B |
| R8 | Perte de travail (pas de remote) | 1 | 3 | 3 | Dépôt distant privé + commits quotidiens | B |
