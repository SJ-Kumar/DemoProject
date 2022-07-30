import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Loading data

col_names = ['Player'] + [f'Hole {i}' for i in range(1, 17)]

df = pd.read_excel('Investment1.xls', header=None, index_col=0, names=col_names)

df_cumsum = df.cumsum(axis=1)
df_cumsum

fig, ax = plt.subplots(figsize=(16, 9))

bar_width = .4
index = np.arange(df.shape[1])
xticks = index - ((df.index.size * bar_width) / 2)

for i, player in enumerate(df.index):
    ax.bar(
        xticks + (i * bar_width),
        df.loc[player],
        width=bar_width,
        label=player,
        align='edge',
        joinstyle='round'
    )


ax.set_xticks(index)
ax.set_xticklabels(df.columns.tolist())
ax.grid(color='gray', linestyle='-', linewidth=1, alpha=.3)
ax.set_axisbelow(True)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.legend()
ax.set_ylabel('Strokes')
ax.set_yticks(np.arange(15));

## Plotting cumulative strokes

fig, ax = plt.subplots(figsize=(16, 9))
xticks = df_cumsum.columns.tolist()
ax.grid(color='gray', linestyle='-', linewidth=1, alpha=.3)
ax.set_axisbelow(True)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for player in df_cumsum.index.tolist():
    ax.plot(xticks, df_cumsum.loc[player], label=player, linewidth=3, marker='o')
ax.legend()
ax.set_ylabel('Strokes')
ax.set_yticks(np.arange(0, 100, 5));

## Calculating mean values

df.mean(axis=1)

## The mean number of strokes per hole:
df_meanperholes = df.mean()
fig, ax = plt.subplots(figsize=(16, 9))
ax.grid(color='gray', linestyle='-', linewidth=1, alpha=.3)
ax.set_axisbelow(True)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.set_ylabel('Mean number of strokes')
ax.set_yticks(np.arange(0, 15));
ax.bar(df_meanperholes.index, df_meanperholes);

plt.show()

