from time import sleep
from legislacao import main
from utils import get_formatted_date_from_url
from zipfile import ZipFile
import glob


def scrap_atos():
    # Nesse array você pode adicionar quantas URLs quiser
    urls = ['https://legislacao.fazenda.sp.gov.br/Paginas/Atos.aspx?Tipo=Leis&StartDate=2020-01-01&EndDate=2020-12-31',
            'https://legislacao.fazenda.sp.gov.br/Paginas/Atos.aspx?Tipo=Leis&StartDate=2019-01-01&EndDate=2019-12-31',
            'https://legislacao.fazenda.sp.gov.br/Paginas/Atos.aspx?Tipo=Leis&StartDate=2018-01-01&EndDate=2018-12-31'
            ]

    print('=======================================================')
    for url in urls:
        startDate = get_formatted_date_from_url(url, 'StartDate')
        endDate = get_formatted_date_from_url(url, 'EndDate')
        print('EXTRAINDO OS ATOS DE ' + startDate + ' ATÉ ' + endDate)
        main(url)
        print('=======================================================')
        sleep(1)

    zipobj = ZipFile('files/leis.zip', 'w')
    files = glob.glob("files/*.json")
    for f in files:
        zipobj.write(f)
    zipobj.close()
