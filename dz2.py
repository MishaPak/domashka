import pandas as pd
from pandas import pivot_table
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
df = pd.read_csv('trainingData_tabular_chunk1.csv')

matchup = pivot_table(df,
                      index = 'player.hero_card_id',
                      columns = 'opponent.hero_card_id',
                      values = 'decision',
                      aggfunc = 'mean')
print(matchup)

a = df[(df['player.deck_count'] > 5)&(df['decision'] == 1)]
average_turn = a.groupby(a['player.hero_card_id'])['turn'].mean()
matchup = pd.merge(matchup, average_turn, on='player.hero_card_id')
print(matchup)

df['player_sustainability'] = df['player.armor']+df['player.hp']
graph = df.groupby(df['player_sustainability'])[['decision', 'player_sustainability']].mean()
print(graph)
fig, ax = plt.subplots()
ax.plot(graph['player_sustainability'], graph['decision'])
ax.set_xlabel("Player's hp+armor")
ax.set_ylabel('Average decision')
plt.show()
