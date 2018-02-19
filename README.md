# Basics:

See the `Makefile`.

- Install [`yarn`][1]

# Building JS assets:

    make build-dev
    make build-prod  # minify

- Outputs `static/dist/js/app.bundle.js`.
- See `webpack.*.js` for details.

# 

- To preserve `console.log`'s:

    yarn run build --no-minify

[1]: https://yarnpkg.com/lang/en/docs/install/
