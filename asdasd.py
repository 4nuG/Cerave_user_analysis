import pandas as pd 


json_data = pd.read_json('cerave_followers.json', lines=True)

csv_data = json_data.to_csv('output3.csv', encoding = 'utf-8', index=False)

