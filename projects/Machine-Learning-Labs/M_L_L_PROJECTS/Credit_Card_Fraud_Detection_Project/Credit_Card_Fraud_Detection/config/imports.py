# ── IMPORTS ──────────────────────────────────────────
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
from pathlib import Path
from datetime import datetime,timedelta
import warnings
warnings.filterwarnings('ignore')
from sqlalchemy import create_engine
import time
import re
import os
# # 1. stop the automatic back to the ligne when display datasets
pd.set_option('display.expand_frame_repr', False)
# 2. display all columns
# pd.set_option('display.max_columns', None)

