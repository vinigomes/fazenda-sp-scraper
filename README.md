# FAZENDA SP Scraper

## Sobre

Cria documentos JSON estruturados com as leis do site da fazenda e planejamento do estado de São Paulo, usando Python e Beautiful Soup 4

## Por que?

_Esse projeto foi desenvolvido com o objetivo de exemplificar como automatizar e fazer o scrap (cópia de dados) de um site.

Encontre no arquivo [legislacao.py](./legislacao.py) a lógica para extração de texto de leis e criação do documento, e no arquivo [scraper.py](./scraper.py) as URLs pedidas que serão passadas para o motor de cópia de dados.

Para criar os documentos JSON de leis, siga esses passos:

1. [Instale Python 3](https://www.python.org/downloads/);
2. Abra um terminal de comandos e instale a biblioteca [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/) executando o seguinte comando: `pip install bs4`;
3. [Instale Git](https://git-scm.com/download/), se ainda não tiver na sua máquina;
4. Clone esse repositório executando `git clone https://github.com/danitrod/ted-talks-scraper.git` e acesse o repositório com `cd ted-talks-scraper`;
5. Execute o programa com `python challenge.py`. Os arquivos JSON serão automaticamente criados na mesma pasta.

Observação: após a extração dos textos do TED Talks, recomendo fortemente que você crie um outro arquivo baseado no [ted.py](./ted.py) e modifique o que for necessário para extração dos textos da Olhar Digital.

## Licença

MIT License

Copyright (c) 2020 Daniel T. Rodrigues
