# Organisation du Framework — Config `.env` / Docker / Python

## Principe général

Le framework est **réutilisable tel quel** pour chaque nouveau projet. Une seule partie change d'un projet à l'autre : le fichier `.env`. Tout le reste (Docker, config Python) reste identique et ne doit plus être modifié.

---

## Fichiers qui ne changent JAMAIS (le "squelette" du framework)

```
config/
├── imports.py       ← librairies génériques (pandas, sqlalchemy, etc.)
└── settings.py      ← lit .env, crée l'engine SQLAlchemy
docker-compose.yml   ← lit .env via ${...}
.env.example         ← modèle vide/générique, versionné sur Git
```

### `config/imports.py`

```python
# ── IMPORTS ──────────────────────────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
from pathlib import Path
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')
from sqlalchemy import create_engine
import time
import re
import os

# 1. stop the automatic back to the ligne when display datasets
pd.set_option('display.expand_frame_repr', False)
# 2. display all columns
# pd.set_option('display.max_columns', None)
```

### `config/settings.py`

```python
# ── CONFIGURATION ─────────────────────────────────────
from config.imports import *
import os
from pathlib import Path
from dotenv import load_dotenv

# Remonte à la racine du projet peu importe d'où le script est lancé
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL n'est pas défini dans le fichier .env")

engine = create_engine(DATABASE_URL)


if __name__ == "__main__":
    print(f"DATABASE_URL chargée : {DATABASE_URL}")
    print("Connexion à l'engine créée avec succès ✅")
```

### `docker-compose.yml`

```yaml
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    ports:
      - "${POSTGRES_PORT}:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:                          # volume nommé — les données survivent aux redémarrages
```

### `.env.example` (versionné sur Git, sans vraies valeurs sensibles)

```env
# --- PostgreSQL ---
POSTGRES_DB=nom_de_ta_base
POSTGRES_USER=ton_user
POSTGRES_PASSWORD=ton_mot_de_passe
POSTGRES_PORT=5432

# --- URL complète utilisée par SQLAlchemy (Python) ---
DATABASE_URL=postgresql://ton_user:ton_mot_de_passe@localhost:5432/nom_de_ta_base
```

---

## Le SEUL fichier qui change à chaque projet : `.env`

`.env` n'est **jamais versionné** (protégé par `.gitignore`).

```env
# --- PostgreSQL ---
POSTGRES_DB=nom_du_nouveau_projet
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5554          # un port différent si plusieurs bases tournent en parallèle

# --- URL complète utilisée par SQLAlchemy (Python) ---
DATABASE_URL=postgresql://postgres:postgres@localhost:5554/nom_du_nouveau_projet
```

⚠️ Pas de guillemets, pas d'espaces autour des `=`.

---

## `.gitignore` — vérifier que `.env` est bien protégé

```
.env
```

---

## Workflow pour démarrer un nouveau projet

```bash
# 1. Copier le squelette du framework
cp -r mon_framework/ mon_nouveau_projet/
cd mon_nouveau_projet/

# 2. Modifier UNIQUEMENT le .env avec les nouvelles infos
nano .env

# 3. Lancer Docker avec cette nouvelle config
docker-compose up -d

# 4. Vérifier que tout se connecte bien
python -m config.settings
```

---

## Pourquoi `python -m config.settings` et pas `python config/settings.py`

- `python -m config.settings` exécute le fichier **comme un module à l'intérieur du package** `config` : Python ajoute automatiquement la racine du projet au chemin de recherche, donc `from config.imports import *` fonctionne.
- `python config/settings.py` traite le fichier comme un script isolé : l'import `from config.imports import *` échoue souvent avec `ModuleNotFoundError: No module named 'config'`.

Toujours lancer les commandes **depuis la racine du projet**.

---

## Le gain de cette organisation

- **Un seul point de vérité** : `.env` pilote à la fois Docker et le code Python — plus de risque de désynchronisation entre les deux (ex: mauvais port).
- **Zéro risque de conflit d'`engine`** : un seul `engine` est défini dans `settings.py`, plus de doublons ambigus comme avant.
- **Réutilisabilité immédiate** : chaque nouveau projet ne demande que quelques lignes dans un `.env`, sans toucher à Docker ni au code Python.
