import pandas as pd

from scripts.xbar_rbar import spc_analysis
from visualize import visualize

WL1 = 1050
LCL = 1150
UCL = 1350
SC1 = 1450
SC2 = 1800

data = pd.read_excel("../data/gcs_data.xlsx")
df = pd.DataFrame(data)
df['DateTime'] = pd.to_datetime(df['Date'].dt.strftime('%d-%m-%Y') + ' ' + df['Time'].astype(str), format='%d-%m-%Y %H:%M:%S')
target_date = '30-05-2023'
target_date2 = '31-05-2023'
visualize(df, target_date, target_date2, WL1, LCL, UCL, SC1, SC2)
spc_analysis(df, target_date, target_date2, UCL, LCL)
