BOT_NAME = 'livingsocial'

SPIDER_MODULES = ['scraper_app.spiders']

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': '',
    'database': 'scrape'
}