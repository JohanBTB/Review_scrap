import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from csv_exploring.csv_utils import top_movies_by_genre
from csv_exploring.csv_utils import segmenting_dates


current_directory = os.getcwd()
users_path = os.path.join(current_directory, "csv_cleaning", "csv_files","users.csv")
reviews_path = os.path.join(current_directory, "csv_cleaning", "csv_files","reviews.csv")
movies_path = os.path.join(current_directory, "csv_cleaning", "csv_files","movies.csv")



# --------------------------- Exploring users ---------------------------------
# users = pd.read_csv(users_path, index_col = 'users_id')



# --------------------------- Exploring reviews -------------------------------

# reviews = pd.read_csv(reviews_path, index_col = 'reviews_id')


# counting_reviews = reviews.groupby('name', as_index = False).count().sample(10)
# plt.figure(figsize=(11,9))
# sns.barplot(x='name', y='movie', data = counting_reviews)
# plt.xlabel("Nombre de usuario")
# plt.ylabel("N° de comentarios")
# plt.title('Numero de comentarios por usuario')
# plt.show()

# counting_scores = reviews.groupby('score', as_index = False).count()
# sns.scatterplot(data = counting_scores, x = 'score',y='name')
# plt.xlabel("Calificacion")
# plt.ylabel("N° de ocurrencias")
# plt.title('Numero de ocurrencias por califiacion')
# plt.show()

# measuring_scores = reviews.groupby('name', as_index = False).mean().sample(10)
# sns.barplot(data = measuring_scores, x = 'name',y='score')
# plt.xlabel("Nombre de usuario")
# plt.ylabel("Promedio de califiacion")
# plt.title('Promedio de califiacion por usuario')
# plt.show()



# --------------------------- Exploring movies -------------------------------

movies = pd.read_csv(movies_path, index_col = 'movies_id', parse_dates=['Release Date'])



# Printing top movies by genre
# selected_genres = list(movies.iloc[:,5:].columns)
# top_movies_by_genre(movies, selected_genres)


# Pie plot of movies by year
# movies_dates = movies.copy()
# movies_dates['Release Date'] = movies_dates['Release Date'].apply((segmenting_dates))
# movies_dates['Release Date'] = movies_dates['Release Date'].apply(lambda x: f"{x.year} - {x.replace(year = x.year + 5 ).year}")
# movies_dates = movies_dates.groupby('Release Date').count()
# movies_dates.plot( kind = 'pie', x='Release Year', y = 'name',legend = True, ylabel = '',
#                   xlabel = 'hola', title = 'Peliculas emitidos  por periodos de años',
#                   colormap = plt.get_cmap('cool'), figsize=(10,13), shadow = True, autopct = "%1.1f%%",
#                   fontsize=12)
# plt.legend(loc='right')


# Box plot of score vs release date AND runtime vs release date
# fig, axs = plt.subplots(1,2, figsize = (15,8), dpi=200)
# movies_dates = movies.copy().loc[:,['Release Date','score','Runtime']]
# movies_dates['Release Date'] = movies_dates['Release Date'].apply((segmenting_dates))
# movies_dates['Release Date'] = movies_dates['Release Date'].apply(lambda x: f"{x.year} - {x.replace(year = x.year + 5 ).year}")
# sns.boxplot(x = 'score', y = "Release Date", data = movies_dates,ax = axs[0])
# axs[0].title.set_text('Calificacion vs Tiempo')
# sns.boxplot(x = 'Runtime', y = "Release Date", data = movies_dates,ax = axs[1])
# axs[1].title.set_text('Duracion vs Tiempo')


# movies = movies.astype({'score':'int16' })

# score critic_score

