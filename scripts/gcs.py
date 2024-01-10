import pandas as pd
from visualize import visualize

WL1 = 1050
LCL = 1150
UCL = 1350
SC1 = 1450
SC2 = 1800

data = pd.read_excel("../data/gcs_data.xlsx")
df = pd.DataFrame(data)
target_date = '30-05-2023'
visualize(df, target_date, WL1, LCL, UCL, SC1, SC2)