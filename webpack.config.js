var path = require('path');

var staticPrefix = path.join(__dirname, 'src/static/app');
var distPath = staticPrefix + '/dist';


module.exports = {
  entry: staticPrefix + '/app.js',
  output: {
    path: distPath,
    filename: 'bundle.js'
  },
  devServer: {
    contentBase: staticPrefix
  },
  module: {
    loaders: [{
      test: /\.js$/,
      exclude: /node_modules/,
      loader: 'babel',
      query: {
        presets: ['es2015', 'react', 'react-hmre']
      }
    }]
  }
};
