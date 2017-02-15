import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.patches import Circle, Rectangle, Arc

df = pd.read_csv("C:/Users/andrewp/Dropbox/Spatial Jam/NBL/shotData/2016-17/combinedShotsNBL.csv")

######

def draw_court(ax=None, color='grey', lw=2, outer_lines=False):
	if ax is None:
		ax = plt.gca()

	hoop = Circle((50, 12), radius=2, linewidth=lw, color=color, fill=False)

	court_elements = [hoop]

	for element in court_elements:
		ax.add_patch(element)

	return ax
######

player = (df.loc[df['Player'] == 'C. Gliddon'])

sns.set_style("white")

x2 = player.X * 2

color = sns.cubehelix_palette(8, light=1, as_cmap=True)

shotChart = sns.jointplot(player.Y, x2, kind='kde', space=0, ratio=8, bins='log', cmap = "Blues_d", size = 10, shade=False)

ax = shotChart.ax_joint
ax.scatter(player.Y, x2, color = "grey", s = 30, linewidth=1, marker="+")
draw_court(ax)

ax.set_xlim(0,100)
ax.set_ylim(0,100)

ax.set_xlabel('')
ax.set_ylabel('')
ax.tick_params(labelbottom='off', labelleft='off')

plt.show()