import pandas as pd
from visualize import visualize

df = pd.read_excel('gcs_data.xlsx')
shift_numbers = []
average_gcs_values = []

for shift, group in df.groupby('Shift'):
    gcs_values = group['GCS'].tolist()
    avg_gcs = sum(gcs_values) / len(gcs_values)
    shift_numbers.append(shift)
    average_gcs_values.append(avg_gcs)

data = {
    'shift': shift_numbers,
    'avg': average_gcs_values
}

WL1 = 1050  # Warning limit
LCL = 1150  # LCL
UCL = 1350  # UCL
SC1 = 1450  # Stop and contact
SC2 = 1800  # Stop and contact

visualize(data, WL1, LCL, UCL, SC1, SC2)

