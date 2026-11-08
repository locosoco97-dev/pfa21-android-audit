# Conventions Git et travail d'équipe

## Branches
- `main` : toujours stable, correspond aux jalons de sprint (tags `sprint1-done`, `sprint2-done`, …).
- `develop` : intégration courante.
- `feature/sN-description` : une branche par tâche (ex. `feature/s3-controle-c2`).

## Commits
Format : `type(portée): message court` — types : `feat`, `fix`, `docs`, `test`, `chore`.
Exemples : `docs(cible): ajout fiche de cible`, `test(c2): cas exported implicite`.

## Règles
- Merge dans `develop` après relecture par l'autre membre.
- Aucun secret, aucune donnée personnelle, aucun APK tiers dans le dépôt.
- Preuves : `preuves/sprintN/` avec nom explicite (`T1_console_poste-A.png`).
- Toute commande documentée doit avoir été exécutée à froid par l'autre membre.
