const path = require('path');
const { VueLoaderPlugin } = require('vue-loader')

module.exports = {
  entry: './frontend/js/index.js',
  output: {
    path: path.resolve(__dirname, 'frontend/static/build'),
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
  ],
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    }
  }
};