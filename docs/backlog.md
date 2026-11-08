# Backlog du projet PFA-21

Rôles : **A** vérifications/références · **B** correction, automatisation, preuves · (C : réparti entre A et B en binôme).
Statuts : ✅ fait · 🔄 en cours · ⬜ à faire · 🧑 action équipe (non automatisable)

## Sprint 1 — Cadrage et laboratoire
| ID | Tâche | Resp. | Statut |
|---|---|---|---|
| S1-01 | Valider sujet, périmètre et cahier des charges avec l'encadrant | A+B | 🧑 |
| S1-02 | Répartir les rôles A/B (binôme) | A+B | 🧑 |
| S1-03 | Choisir la cible et rédiger la fiche (`docs/fiche_cible.md`) | A | ✅ |
| S1-04 | Créer le dépôt Git, structure, conventions | B | ✅ |
| S1-05 | Dockerfile + `make setup` | B | ✅ |
| S1-06 | Versionner le manifeste de base + tests de sanité | B | ✅ |
| S1-07 | Backlog, risques, planning | A | ✅ |
| S1-08 | `make setup` validé sur le poste de chaque membre (capture) | A+B | 🧑 |
| S1-09 | Pousser le dépôt sur un remote partagé (GitHub/GitLab privé) | B | 🧑 |

## Sprint 2 — Référentiel et grille
| ID | Tâche | Statut |
|---|---|---|
| S2-01 | Étudier la doc Android officielle (permissions, `exported`, backup, trafic en clair) | ⬜ |
| S2-02 | Formaliser les 4 contrôles (risque, règles PASS/WARN/FAIL, remédiation, faux positifs) | ⬜ |
| S2-03 | Recenser et vérifier les références CWE / MASVS | ⬜ |
| S2-04 | Dériver les manifestes « avant » et « après » | ⬜ |
| S2-05 | Faire valider la grille | ⬜ |

## Sprint 3 — Script d'audit
| ID | Tâche | Statut |
|---|---|---|
| S3-01 | Chargement XML sécurisé, espaces de noms | ⬜ |
| S3-02 | Contrôles C1 à C4 (registre de contrôles) | ⬜ |
| S3-03 | Cas limites (`exported` par défaut, LAUNCHER, attributs absents) | ⬜ |
| S3-04 | Sortie console, JSON, codes de sortie 0/1/2 | ⬜ |
| S3-05 | Gestion des erreurs, relecture croisée | ⬜ |

## Sprint 4 — Tests et automatisation
| ID | Tâche | Statut |
|---|---|---|
| S4-01 | Tests pytest par contrôle (PASS/FAIL), cas limites et erreurs | ⬜ |
| S4-02 | Test avant/après et option `--compare` | ⬜ |
| S4-03 | Finaliser setup/start/test/stop + équivalents shell | ⬜ |
| S4-04 | Liste des actions non automatisables, couverture | ⬜ |

## Sprint 5 — Correction et recette
| ID | Tâche | Statut |
|---|---|---|
| S5-01 | Correction du paramètre (commit dédié) | ⬜ |
| S5-02 | Exécution T1/T2/T3 avec preuves | ⬜ |
| S5-03 | Redéploiement et validation sur chaque poste | ⬜ |
| S5-04 | Traitement des anomalies | ⬜ |

## Sprint 6 — Documentation et soutenance
| ID | Tâche | Statut |
|---|---|---|
| S6-01 | Rapport final | ⬜ |
| S6-02 | README + test à froid sur machine propre | ⬜ |
| S6-03 | Extension MobSF (optionnelle, après MVP validé) | ⬜ |
| S6-04 | Démo, support, répétition avec questions croisées | ⬜ |
| S6-05 | Gel de version (tag) et remise | ⬜ |
