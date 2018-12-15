#!/usr/bin/env python3

import logging
import connexion
import orm

db_session = None

logging.basicConfig(level=logging.INFO)
app = connexion.FlaskApp(__name__)
app.add_api('swagger.yaml', arguments={'title': 'SunVibe API'})
application = app.app


@application.teardown_appcontext
def shutdown_session(exception=None):
    orm.get_db().remove()


if __name__ == '__main__':
    app.run(port=8080, debug=True)
