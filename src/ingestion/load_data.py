import pandas as pd
from pathlib import Path


def load_data(file_name: str = "raw/global_inflation_post_covid.csv") -> pd.DataFrame:
    try:
        base_path = Path(__file__).resolve().parents[2]
        data_path = base_path / "dados_Covid" / file_name

        df = pd.read_csv(data_path)
        return df

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {data_path}")

    except Exception as e:
        raise Exception(f"Erro ao carregar dados: {e}")

