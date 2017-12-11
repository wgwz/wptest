const path = require('path');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const appPath = 'backend/static/dist';

module.exports = {
  entry: {
    app: './src/app.js'
  },
  plugins: [
    new CleanWebpackPlugin([appPath])
  ],
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, appPath)
  }
}
