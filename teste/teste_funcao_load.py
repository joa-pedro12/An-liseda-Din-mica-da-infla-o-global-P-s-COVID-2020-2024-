import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ingestion.load_data import load_data

df = load_data("raw/global_inflation_post_covid.csv")
print(df.head)