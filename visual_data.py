import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import imageio

'''
import dataframes
'''
fert = pd.read_csv(
    'data/gapminder_total_fertility.csv', 
    index_col=0
)
life = pd.read_excel(
    'data/gapminder_lifeexpectancy.xlsx', 
    index_col=0, 
    nrows=260
)
population = pd.read_excel(
    'data/gapminder_population.xlsx', 
    index_col=0
)
continents = pd.read_csv(
    'data/continents.csv', 
    index_col=0, 
    sep=';'
)

'''
set column names as integer
'''
fert.columns = fert.columns.astype(int)
life.columns = life.columns.astype(int)
population.columns = population.columns.astype(int)

'''
define index name
'''
fert.index.name = 'country'
life.index.name = 'country'
population.index.name = 'country'
continents.index.name = 'continents'

'''
reset indexes
'''
fert = fert.reset_index()
life = life.reset_index()
population = population.reset_index()
continents = continents.reset_index()

'''
transform dataframes from wide to long format
'''
fert = fert.melt(
    id_vars='country', 
    var_name='year', 
    value_name='fertility_rate'
)
life = life.melt(
    id_vars='country', 
    var_name='year', 
    value_name='life_expectancy'
)
population = population.melt(
    id_vars='country', 
    var_name='year', 
    value_name='population'
)

'''
merge all dataframes
'''
df = fert.merge(
    population
)
df = df.merge(
    life
)
df = df.merge(
    continents
)

'''
show a plot of a subset(datas from year 2000)
'''
df_subset = df.loc[
    df['year'] == 2000
]
sns.scatterplot(
    x='life_expectancy', 
    y='fertility_rate', 
    data=df_subset, 
    alpha=0.6
)
# plt.show()

'''
plot and save as images through years 1960-2016
'''
for year in range(1960, 2016):
    fig, ax = plt.subplots(
        figsize = (12, 7)
    )
    data = df[df['year'] == year]

    sns.scatterplot(
        x=data['life_expectancy'], 
        y=data['fertility_rate'], 
        size=data['population'], 
        sizes=(80, 10000), 
        hue=data['continents'], 
        palette='pastel', 
        alpha=0.7
    )

    ax.set_xlabel('Life Expectancy')
    ax.set_ylabel('Fertility Rate')
    ax.set_title((f'Year {year}'))
    ax.set_xlim(20, 90)
    ax.set_ylim(0, 10)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(
        handles=handles[1:7], 
        labels=labels[1:7], 
        loc='upper right', 
        frameon=False, 
        framealpha=0.7
    )

    plt.savefig(f'plots/lifeexp_{year}.png')
    plt.close()

'''
create and save a gif with all the plots
'''
images = []
for i in range(1960, 2016):
    filename = f'plots/lifeexp_{i}.png'
    images.append(imageio.imread(filename))

imageio.mimsave(
    'gif/output.gif', 
    images, 
    fps=7
)