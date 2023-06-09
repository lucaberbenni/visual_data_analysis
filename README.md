# visual_data_analysis
visual data analysis of world wide life expectancy and fertility rate from 1960 to 2016.

1. **Data Import:**
   The code imports several data files in different formats, such as CSV and Excel, using pandas. The data includes information on total fertility rates, life expectancy, population, and continents.

2. **Data Preparation:**
   The column names in the fertility, life expectancy, and population dataframes are converted to integers. The index names of the dataframes are also set appropriately. Additionally, the dataframes are transformed from wide to long format using the melt function, resulting in a merged dataframe that combines all the relevant data.

3. **Data Visualization:**
   The code generates data visualizations to explore the relationships between life expectancy, fertility rates, population, and continents. It starts by creating a scatter plot for a subset of data from the year 2000, showing the relationship between life expectancy and fertility rate. The plot is generated using the seaborn library.

4. **Plot Generation and Animation:**
   The code generates and saves scatter plots for each year from 1960 to 2016. Each plot represents the relationship between life expectancy, fertility rate, and population, with different continents indicated by colors. The plots are saved as individual PNG image files. Subsequently, the code combines these images into a GIF using the imageio library. The resulting GIF file, named "output.gif", showcases the visual evolution of the data over the years.
