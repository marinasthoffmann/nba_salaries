import pandas as pd
from config import CSV_PATH

class DataProcessor:

    def __init__(self):
        self.df = pd.DataFrame(columns=['Player', 'Salary', 'Year'])

    def add_data(self, player_objects):
        temp_df = pd.DataFrame([
            {'Player': player.name, 'Salary': player.salary, 'Year': player.year}
            for player in player_objects
        ])
        
        self.df = pd.concat([self.df, temp_df], ignore_index=True)

    def clean_data(self):
        self.df['Salary'] = self.df['Salary'].str.replace('$', '').str.replace(',', '')
        self.df['Salary'] = pd.to_numeric(self.df['Salary'])
        self.df['Player'] = self.df['Player'].str.strip()
        self.df['Year'] = pd.to_numeric(self.df['Year'])

    def watch(self):
        print(self.df.size)

    def save_to_csv(self, filename):
        self.df.to_csv(f'{CSV_PATH}/{filename}', index=False)
