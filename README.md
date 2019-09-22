### IMDB Movie Ratings

Essa aplicação é faz download do dados do site [IMDb](https://www.imdb.com/interfaces/ "IMDb"), processa os mesmo e faz uma pesquisa.

- Stack
	- Python
	- Docker
	- Docker Compose

# Como rodar
- *docker-compose run app python main.py -w my-word*, irá baixar os dados do site, e pesquisa por  um filter que tem no título a palavra "my-word"

# Rodar testes
- *docker-compose up tests*

# Melhorias
- Menu interativo, onde pudesse fazer várias pesquisas sem ter que iniciar a aplicação como um todo novamente
