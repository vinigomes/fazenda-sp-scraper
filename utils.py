import urllib.parse as urlparse
from urllib.parse import parse_qs
import datetime


def get_formatted_date_from_url(url, param):
    parsed = urlparse.urlparse(url)
    date = parse_qs(parsed.query)[param]
    formatted_date = datetime.datetime.strptime(date[0], "%Y-%m-%d").strftime("%d/%m/%Y")
    return formatted_date
