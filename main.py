# Import necessary packages
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import earthpy as et

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

sns.set(font_scale=1.5, style="whitegrid")


os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))
# Date fictive pentru totalul de emisii pe an pentru câteva țări
emissions_data = {
    'Area': ['Afghanistan','Afghanistan' ,'Afghanistan',  'Afghanistan', 'Afghanistan'],
    'Item': ['Crop Residues', 'Crop Residues', 'Crop Residues', 'Crop Residues', 'Crop Residues'],
    'Element': ['Direct emissions ', 'Indirect emissions ', 'Emissions ', 'Emissions ', 'Emissions '],
    'Unit': ['kilotonnes', 'kilotonnes' ,'kilotonnes', 'kilotonnes', 'kilotonnes'],
    '2000': [0.52, 0.117, 0.637, 168.807, 168.807]

}

# Convertirea datelor într-un DataFrame pandas
df = pd.DataFrame(emissions_data)

# Afișarea tabelului
print(df)
