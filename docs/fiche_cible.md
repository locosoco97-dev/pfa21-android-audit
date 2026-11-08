# Fiche de cible — EventSchedule

| Champ | Valeur |
|---|---|
| Nom | EventSchedule (application Android interne de consultation du programme d'un événement) |
| Origine | Projet pédagogique **créé par l'équipe** (aucune application tierce) |
| Licence | Code de l'équipe, usage pédagogique (licence à confirmer avec l'encadrant) |
| Package | `ma.emsi.eventschedule` |
| Version | 0.1 (squelette, sans logique métier) |
| SDK | minSdk 24 · targetSdk 34 (déclarés dans `<uses-sdk>` pour être lisibles par le script) |
| Fichier audité | `app/src/main/AndroidManifest.xml` (copie de référence : `manifests/base/`) |
| Environnement | Aucun appareil réel, aucun émulateur, aucune compilation APK (hors MVP) |

## Justification du choix
Contrôle total du manifeste, aucun risque de licence, modification possible sans casser un projet tiers, et cas d'étude réaliste (programme d'événement).

## Composants déclarés
| Composant | Type | `exported` (base) | Rôle |
|---|---|---|---|
| `.MainActivity` | activity | `true` (LAUNCHER, légitime) | Liste du programme |
| `.SessionDetailActivity` | activity | `false` | Détail d'une session |
| `.SyncService` | service | `false` | Synchronisation du programme |
| `.ReminderReceiver` | receiver | `false` | Rappels de sessions |
| `.ScheduleProvider` | provider | `false` | Accès interne aux données |

## Permissions déclarées (base)
`INTERNET`, `ACCESS_NETWORK_STATE`, `POST_NOTIFICATIONS` — toutes justifiées par la consultation en ligne et les rappels.

## État du manifeste de base
Conforme aux 4 contrôles prévus (C1 permissions, C2 composants exportés, C3 `debuggable`/`allowBackup`, C4 trafic en clair) : tous attendus **PASS**.

## Cas d'étude prévu (Sprint 2)
Dérivation d'un manifeste « avant » où `.SyncService` passe à `android:exported="true"` sans permission (C2 en FAIL), puis « après » corrigé.
