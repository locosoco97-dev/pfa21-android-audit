# PFA-21 — Audit statique très ciblé d'une application Android

Projet EMSI (Cybersécurité et Réseaux) — BENLYAMANI Ziad, FERDOUS Larbi Sifeddine — encadrant : Pr. OUAGUID Abdellah.

Audit statique du `AndroidManifest.xml` d'une application de démonstration (**EventSchedule**) : 4 contrôles, détection d'un paramètre permissif, correction, nouvelle vérification.

## Prérequis
Docker (recommandé) **ou** Python 3.11+ ; Git ; `make` (optionnel, scripts équivalents fournis).

## Démarrage rapide
```
make setup     # construit l'image et vérifie l'environnement
make test      # lance les tests (6 tests de sanité au Sprint 1)
make start     # lance l'audit (disponible dès le Sprint 3)
make stop      # nettoie
```
Sans `make` : `scripts/setup.sh` (Linux/macOS) ou `scripts/setup.ps1` (Windows).

Sans Docker :
```
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python scripts/check_env.py && pytest -q
```

## Structure
```
app/                 projet Android pédagogique (manifeste source)
manifests/           base/ (conforme), avant/ et apres/ (Sprint 2)
src/                 script d'audit (Sprint 3)
tests/               tests pytest
scripts/             check_env.py, setup.sh, setup.ps1
docs/                cahier des charges, fiche de cible, backlog, risques, planning, conventions
preuves/             captures, rapports, journaux par sprint
```

## Avancement
- [x] Sprint 1 — Cadrage et laboratoire (voir `docs/backlog.md`)
- [ ] Sprint 2 à 6
