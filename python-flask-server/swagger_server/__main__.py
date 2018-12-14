#!/usr/bin/env python3

import connexion


def main():
    app = connexion.App(__name__, specification_dir='./')
    app.add_api('swagger.yaml', arguments={'title': 'SunVibe API'})
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
