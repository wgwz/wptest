Install yarn, then:

    yarn run build --config <webpack.config>

Outputs `./dist/bundle.js`.
Note that this setup requires configuration in webpack for new js src files.
See `package.json` for more.


Install `pipenv`, then:

    # from project directory
    pipenv install


Flask config order:

1. system env variables -> `prod_settings.py`
2. `instance/.env` -> `prod_settings.py`
3. `backend/dev_settings.py`


Improvements: 

- http://flask.pocoo.org/docs/dev/config/#development-production
