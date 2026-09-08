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


# sns.set_theme(style="whitegrid", font_scale=1.05)
# plt.rcParams.update({
#     'figure.facecolor': 'white',
#     'axes.spines.top': False,
#     'axes.spines.right': False,
#
# })

# Cela cible la racine du projet (le parent du dossier config)
# BASE_DIR = Path(__file__).resolve().parent.parent
# OUTPUT_DIR = BASE_DIR/"output"/"charts"
# OUTPUT_DIR.mkdir(parents= True, exist_ok=True)
# PALETTE = {
#     "primary": "#2980b9",
#     "secondary": "#e74c3c",
#     "success": "#2ecc71",
#     "warning": "#f39c12",
#     "purple": "#8e44ad",
#     "dark": "#2c3e50",
# }


# def save_fig(name: str) -> None:
#     plt.savefig(OUTPUT_DIR / f"{name}.png", dpi=150, bbox_inches='tight', facecolor='white')
#     plt.close()
#     print(f"Save: {name}.png")

if __name__ == "__main__":
    print(f"DATABASE_URL chargée : {DATABASE_URL}")
    print("Connexion à l'engine créée avec succès ✅")
    #python -m config.settings
    '''
        # -m dit à Python : "traite cet argument comme un nom de module (pas un chemin de fichier), et lance-le comme 
        si c'était le point d'entrée"
    '''
