from pathlib import Path
import pandas as pd 
from datetime import date

today = date.today()
save_path = Path(__file__).resolve().parent.parent / 'data' / 'snapshots'
save_path.mkdir(parents=True, exist_ok=True)

df = pd.read_csv('https://anwendungen.pharmnet-bund.de/lieferengpassmeldungen/public/csv', sep=';',
                 encoding='latin-1')

df = df.drop(['Telefon', 'E-Mail'], axis=1)
df.to_csv(save_path / f'shortages_{today}.csv', index=False)