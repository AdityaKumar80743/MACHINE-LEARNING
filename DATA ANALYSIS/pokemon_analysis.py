import pandas as pd 
import matplotlib.pyplot as plt 

# read dataset
df = pd.read_csv("Pokemon.csv")

# print(df.isnull().sum())
# no data clening needed all imprant values are filled


# --------- visualisation
# 1: legendary vs non legendary
# extract stat info 
pokemon_type = df.groupby("Legendary")[['Attack','HP','Defense','Sp. Atk','Sp. Def','Speed']].mean()

pokemon_type.plot(kind='bar', figsize=(8,5))
plt.title('Legendary VS non-Legendary stats')
plt.xlabel('Type')
plt.ylabel('Average values')

plt.xticks(ticks=[0,1], labels=['Non-Legendary', 'Legendary'], rotation=0)
plt.legend(title='stats')

plt.tight_layout()
# save graph
plt.savefig("legendary_vs_nonLegendary.png",dpi=300)
# plt.show()


# total stats
pokemon_total = df.groupby("Legendary")[['Total']].mean()

pokemon_total.plot(kind='bar', figsize=(8,5))
plt.title('Legendary VS non-Legendary total stats')
plt.xlabel('stats')
plt.ylabel('type')

plt.xticks(ticks=[0,1], labels=['Non-Legendary', 'Legendary'], rotation=0)
plt.legend(title='stats')

plt.tight_layout()
plt.savefig("legendary_vs_nonLegendary_total.png",dpi=300)
# plt.show()

# insight
print("LEGENDARY are stronger than normal pokemon in all aspects")



# 2: comparison based on pokemon type and speed
pokemon_speed = df.groupby('Type 1')[['Speed']].mean()

plt.figure(figsize=(12,7))
plt.bar(pokemon_speed.index, pokemon_speed['Speed'])

plt.title('Comparison of speed of different Types')
plt.xlabel('Type')
plt.ylabel('Average Speed')

plt.tight_layout()
plt.savefig("pokemon_speed_vs.png",dpi=300)
# plt.show()

# insight
print("Flying type pokemon are the fastest")



# 3: comparison based on pokemon type and total power
pokemon_total = df.groupby('Type 1')[['Total']].mean()

plt.figure(figsize=(12,7))
plt.bar(pokemon_total.index, pokemon_total['Total'])

plt.title('Comparison of Total of different Types')
plt.xlabel('Type')
plt.ylabel('Average Total')

plt.tight_layout()
plt.savefig("pokemon_total_vs.png",dpi=300)
plt.show()

# insight
print("Dragon type pokemon have highest total power")
