const path = require('path');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const distPath = 'static/js';

module.exports = {
  entry: {
    app: './src/app.js'
  },
  plugins: [
    new CleanWebpackPlugin([distPath])
  ],
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, distPath)
  }
}
