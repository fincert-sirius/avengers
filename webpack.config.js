const path = require('path');
const { VueLoaderPlugin } = require('vue-loader')

module.exports = {
  entry: './frontend/js/index.js',
  output: {
    path: path.resolve(__dirname, 'frontend/build'),
    filename: 'index.js'
  },
  module: {
    rules: [
      {
          test: /\.vue$/,
          loader: 'vue-loader',
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin()
  ]
};