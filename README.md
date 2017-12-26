Install yarn, then:

    yarn install
    yarn run build

Outputs `static/dist/js/app.js`.
See `package.json` and [parceljs][1] for more.

To preserve `console.log`'s:

    yarn run build --no-minify

Install `pipenv`, then:

    pipenv install

Or do the usual with `venv`.

[1]: https://parceljs.org/
