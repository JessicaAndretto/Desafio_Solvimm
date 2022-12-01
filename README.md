# **Desafio Estágio Solvimm**
Desafio Técnico para vaga de estágio na área de Data Engineer

### **Contexto do desafio**

Um novo aplicativo de streaming "5GFlix" está com o desafio de fazer um estudo de mercado para formular a estratégia de negócio que irão adotar. Como parte do estudo de mercado, a "5GFlix" precisa realizar análises em cima de filmes e séries que estão disponíveis na Netflix, a sua concorrente direta.

Para auxiliar no desafio da "5GFlix", seu CTO Alan Turing, entrou em contato com a Solvimm para construir uma estrutura lógica que possibilite o time de BI da "5GFlix" a responder várias perguntas de negócio relacionadas aos dados na Netflix, sendo elas:

1. Quantos filmes estão disponíveis no dataset?
2. Qual é o nome dos 5 filmes com melhor média de avaliação?
3. Quais os 9 anos com menos lançamentos de filmes?
4. Quantos filmes que possuem avaliação maior ou igual a 4.7, considerando apenas os filmes avaliados na última data de avaliação do dataset?
5. Dos filmes encontrados na questão anterior, quais são os 10 filmes com as piores notas e quais as notas?
6. Quais os id's dos 5 customer que mais avaliaram filmes e quantas avaliações cada um fez?


### **Base de dados da Netflix**

Base1: https://drive.google.com/file/d/1gLsCjaMrL91ECdThq58cZAzB9tPxG18g/view?usp=sharing

Base2: https://drive.google.com/file/d/1C_T1w8fc7Oa8MeTo4LMTEcv90IfEOS-6/view?usp=sharing


### **Informações contidas na base de dados**

**Base 1:**
1. ID do filme
2. título e ano de lançamento

**Base 2:**
1. Cust_Id: ID do customer que fez a avaliação
2. Rating: avaliação (nota)
3. Date: data da avaliação
4. Movie_Id: ID do filme

### **Entendendo o código**

Para realizar o estudo de mercado solicitado pela 5Gflix, foram utilizados as duas bases de dados da sua principal concorrente direta, a Netflix. Para um efetivo trabalho de análise, foi realizado inicialmente uma visualização do banco para entender melhor os dados existentes. Logo após, foi realizado um tratamento e limpeza dos dados, verificando valores ausentes, registros duplicados, o tipo de dado de cada coluna e as modificações necessárias, alterações nos nomes das colunas, fatiamento de informações de uma coluna com a criação novas e combinação de banco de dados (merge).
Com os bancos de dados tratados, ou seja, prontos para uso, foram definidas funções que respondessem os questionamentos realizados pela 5Gflix. Por fim, apresentou-se grande parte dos resultados no formato de tabela para melhor visualização. Visando a melhor compreensão, no decorrer dos comandos executados dentro do código (codigo_completo.ipynb) foram realizadas as explicações de cada processo.

### **Informações importantes para executar o código em uma IDE**

1. O código foi desenvolvido pelo Visual Studio Code com a extensão do Jupyter Notebook;
2. Foi criado um ambiente virtual em python no VS Code, visando evitar problemas na execução do código em outro computador. As configurações (pacotes e suas dependências) utilizadas dentro do ambiente virtual encontra-se dentro do arquivo requirements.txt;
3. Para executar o código é importante a instalação dos pacotes conforme utilizado no desenvolvimento do código;
4. A pasta com os arquivos encontra-se no seguinte link do google drive: https://drive.google.com/drive/folders/1rH-5MaO1HBfe2cA6bUcBi70h4qx5QavW?usp=sharing
5. É importante que seja mantida a mesma organização dos arquivos conforme encontra-se no drive;
6. O arquivo codigo_completo.ipynb possui todo o código de processamento, tratamento e análise dos dados;
7. Dentro da pasta html possui um arquivo .html com a documentação das funções utilizadas.

**Passo a passo para executar o código:**
1. Baixar a pasta com os arquivos no drive e descompactar no local de preferência;
2. Abrir a pasta do arquivo dentro da IDE de sua preferência (recomenda-se utilizar o Visual Studio Code);
3. Abrir o terminal pela sua IDE e verifique se o local está dentro da pasta com o código (caso não esteja, é preciso navegar até a pasta);
4. Execute o comando abaixo no terminal para instalar todos os pacotes e suas dependências:
```bash
pip install -r requeriments.txt
```
5. Com as instalações realizadas, o código está pronto para execução.


### **Informações importantes para executar o código no Google Colaboratory**

O código também possui sua versão no notebook Google Colaboratory. Para executar o código, é necessário que as duas bases de dados estejam dentro do drive do e-mail que será utilizado para rodar o código. Como estamos tratando de uma base de dados com muitos registros, o código faz uma conexão direta com o drive para fazer a leitura dos dados.

**Passo a passo para executar o código no Google Colaboratory:**
1. Acessar a conta do gmail que será utilizada para executar o código;
2. Acessar o drive da conta e criar uma pasta com o nome: base_dados_netflix;
3. Anexar dentro da pasta base_dados_netflix as duas base de dados, movies.csv e customers_rating;
4. Abrir o link do código;
5. Executar a primeira linha do código;
```python
from google.colab import drive
drive.mount('/content/drive')
```
6. Após executar a linha acima será solicitado a permissão para acessar o drive, é necessário permitir o acesso. Essa permissão será importante para que o código consiga realizar a leitura das bases;
7. Por fim, o código está pronto para ser executado por inteiro.

Link (leitor): https://colab.research.google.com/drive/1URsyM4EvCvhAYyWpU2r0HlxUUuSqT5ru?usp=sharing
Link (editor): https://colab.research.google.com/drive/1fM1AehmGU11L4awt3OVEoaJZgnaExEDw?usp=sharing

### **Código no repositório do github**

Link: https://github.com/JessicaAndretto/Desafio_Solvimm.git

Importante: caso o download dos arquivos seja realizado pelo github, é importante colocar na mesma pasta do código os arquivos da base de dados, movies.csv e customers_rating.