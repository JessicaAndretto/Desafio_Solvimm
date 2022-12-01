def show_movies_avaiable(df_movies):

    """Função reponsável por retornar a quantidade de filmes disponíveis da base de dados de filmes.

    Como foi realizado um tratamento inicial na base de dados, nessa função olhamos a dimensão das linhas do dataframe.
    
    A função recebe como argumento o dataframe df_movies e retorna pelo método shape sua dimensão.

    Método utilizado:
    ----------------

    - df.shape: este método retorna uma tupla com as dimensões do dataframe, (quantidade de linhas, quantidade de colunas).
    Para acessar a quantidade de linhas, foi utilizado o index 0, acessando o primeiro elemento da tupla.

    Return: 
    -------
    
    f'A Netflix possui {total_movies} filmes disponíveis.'
    """

    total_movies = df_movies.shape[0]
    return print(f'A Netflix possui {total_movies} filmes disponíveis.')

def best_rated_movies(df_join_movies_rating):

    """Função reponsável por retornar um dataframe com os 5 filmes com as melhores médias de avaliação.
    
    A função recebe como argumento o dataframe df_join_movies_rating que é o merge dos dois dataframes.
    A função realiza inicialmente um agrupamento pelo nome do filme e a média das avaliações.
    Posteriormente, faz a ordenação do dataframe de forma decrescente pelos valores das médias das avaliações.
    Por fim, apresenta o dataframe com as 5 melhores médias.

    Métodos utilizados:
    -------------------

    - groupby: agrupamento/combinação dos dados
    - mean: média dos valores
    - rename: renomear o nome da coluna de média 
    - sort_values: ordenar os valores

    Return: 
    -------
    
    dataframe com os 5 filmes 
    """
    
    df_groupby_filme = df_join_movies_rating[['Movie_Name', 'Rating']].groupby('Movie_Name').mean('Rating')\
        .rename(columns={'Rating':'Rating_Average'})
    df_groupby_filme.sort_values(['Rating_Average'], ascending=False, inplace=True)
    print('Os 5 filmes com as melhores médias de avaliação são:')
    return df_groupby_filme.reset_index().head()

def years_fewer_movies(df_movies):

    """Função reponsável por retornar um dataframe com os 9 anos que tiveram menor quantidade de lançamentos de filmes.
    
    A função recebe como argumento o dataframe df_movies com as informações de ano de lançamento, nome do filme e identificação.
    A função realiza inicialmente um agrupamento por ano de lançamento com a soma da quantidade de filmes.
    Posteriormente, faz a ordenação do dataframe em ordem crescente da quantidade de filmes.
    Por fim, apresenta um dataframe com os 9 anos com menor quantidade de filmes lançados.

    Métodos utilizados:
    ------------------

    - groupby: agrupamento/combinação dos dados
    - nunique: conta o número de elementos distintos
    - rename: renomear o nome da coluna de quantidade de filmes 
    - sort_values: ordenar os valores

    Return: 
    -------
    
    dataframe com os 9 anos com menor quantidade de filmes lançados
    """

    df_groupby_qtd_filmes_ano = df_movies[['Release_Year','Movie_Id']].groupby('Release_Year')\
        .nunique('Movie_Id').rename(columns={'Movie_Id':'Quantity_Movies'})
    df_groupby_qtd_filmes_ano.sort_values(['Quantity_Movies'], ascending=True, inplace=True)
    print('Os 9 anos que tiveram menor quantidade de lançamentos de filmes foram:')
    return df_groupby_qtd_filmes_ano.reset_index().head(9)

def movies_last_date_rating(df_filter_last_date):

    """Função reponsável por retornar um dataframe com os registros de avaliação média maior ou igual a 4.7, 
    considerando apenas os filmes avaliados na última data de avaliação.
    
    A função recebe como argumento o dataframe df_filter_last_date com apenas as informações da data da última avaliação.
    A função realiza inicialmente um agrupamento pelo nome do filme e a média das avaliações.
    Posteriormente, faz uma filtragem dos dados com média >= 4.7 e atribui a uma variável a quantidade de registros resultantes no dataframe.
    Por fim, apresenta o dataframe filtrado.

    Métodos utilizados:
    -------------------

    - groupby: agrupamento/combinação dos dados
    - mean: média dos valores das avaliações
    - loc: selecionar dados específicos da coluna com os valores das avaliações   
    
    Return: 
    -------
    
    dataframe com os registros de avaliação média maior ou igual a 4.7 na última data de avaliação.
    """

    # Agrupamento do dataframe apenas com os registro da última data, pelo nome do filme e a média das avaliações.
    df_filter_last_date_mean = df_filter_last_date[['Movie_Name', 'Rating']].groupby('Movie_Name').mean('Rating')
    df_filter_last_date_mean_rating = df_filter_last_date_mean.loc[(df_filter_last_date_mean['Rating']>=4.7)]
    return df_filter_last_date_mean_rating

def movies_last_date_rating_asc(df_filter_last_date_mean_rating):

    """Função reponsável por retornar os 10 filmes que tiveram piores notas e quais foram as notas.
    
    A função recebe como argumento o dataframe df_filter_last_date_mean_rating resultante da função movies_last_date_rating().
    A função realiza inicialmente a ordenação do dataframe em ordem crescente dos valores da média das avaliações.
    Por fim, apresenta um dataframe com os 10 filmes tiveram piores notas e quais foram as notas.

    Método utilizado:
    -------------------

    - sort_values: ordenar os valores

    Return: 
    -------
    
    dataframe com os 10 filmes tiveram piores notas e quais foram as notas.
    """

    df_filter_last_date_mean_rating_asc = df_filter_last_date_mean_rating.sort_values(['Rating'], ascending=True)
    print('Os 10 filmes com as piores notas dentre os filmes com notas médias >= 4.7 são:')
    return df_filter_last_date_mean_rating_asc.reset_index().head(10)

def top_rated_customers(df_customers_rating):

    """Função reponsável por retornar um dataframe com os id's dos 5 usuários que mais avaliaram e quantas avaliações cada um fez.
    
    A função recebe como argumento o dataframe df_customers_rating com as informações de avaliações dos usuários.
    A função realiza inicialmente um agrupamento pelo id do cliente e pela soma da quantidade de filmes que ele fez avaliação.
    Posteriormente, faz a ordenação do dataframe em ordem decrescente da quantidade de avaliações.
    Por fim, apresenta um dataframe com os id's dos 5 usuários que mais avaliaram e quantas avaliações cada um fez.

    Métodos utilizados:
    -------------------

    - groupby: agrupamento/combinação dos dados
    - nunique: conta o número de elementos distintos
    - rename: renomear o nome da coluna de quantidade de avaliações

    Return: 
    -------
    
    dataframe com os id's dos 5 usuários que mais avaliaram e quantas avaliações cada um fez.
    """
    
    df_customers_rating_groupby = df_customers_rating[['Cust_Id', 'Movie_Id']].groupby('Cust_Id').nunique('Movie_Id')\
    .rename(columns={'Movie_Id':"Qtd_Avaliacoes"})
    print('Os 5 customers que mais avaliaram filmes foram:')
    return df_customers_rating_groupby.sort_values(['Qtd_Avaliacoes'], ascending=False).reset_index().head()