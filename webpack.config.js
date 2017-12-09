const path = require('path');

module.exports = {
  entry: './src/app.js',
  output: {
    filename: 'dist/bundle.js',
    path: path.resolve(__dirname, 'dist')
  }
}
