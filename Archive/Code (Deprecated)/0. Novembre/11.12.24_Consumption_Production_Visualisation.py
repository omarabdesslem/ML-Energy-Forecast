#Dependencies
#pip install openpyxl matplotlib pandas
#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

file_path = '../../Data/EnergieUebersichtCH-2024.xlsx' 
xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name='Zeitreihen0h15', header=1, nrows=300)
print(df.columns)
# Convert 'Zeitstempel' column to datetime
df['Zeitstempel'] = pd.to_datetime(df['Zeitstempel'], format='%d.%m.%Y %H:%M')
plt.figure(figsize=(10, 6))
plt.plot(df['Zeitstempel'], df['kWh'], label='Total Energy Consumed', color='blue')
plt.plot(df['Zeitstempel'], df['kWh.1'], label='Total Energy Produced', color='red')
plt.xlabel('Timestamp')
plt.ylabel('Energy (kWh)')
plt.title('Energy Consumption vs. Energy Production in Swiss Control Block(SwissGrid)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()