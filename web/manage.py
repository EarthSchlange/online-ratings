from flask.ext.script import Manager
from flask_migrate import MigrateCommand

from app import get_app

from scripts.create_db import drop_all_tables, create_barebones_data, create_all_data, create_server
from scripts.load_agagd_data import AGAHistoricalGamesLoader
from scripts.rate_all import RatingsAtCommand

app = get_app('config.DockerConfiguration')

manager = Manager(app)
manager.command(drop_all_tables)
manager.command(create_barebones_data)
manager.command(create_all_data)
manager.command(create_server)

manager.add_command('db', MigrateCommand)

@manager.command
def config():
    'Print out all config values from the fully assembled flask app'
    print('\n'.join('%s=%s' % item for item in sorted(app.config.items())))

manager.add_command('load_agagd_data', AGAHistoricalGamesLoader)
manager.add_command('rate_at', RatingsAtCommand)

if __name__ == '__main__':
    manager.run()
