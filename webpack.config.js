module.exports = {
  entry: './src/static/app/app.js',
  output: {
    path: './src/static/app/dist',
    filename: 'bundle.js'
  },
  devServer: {
    contentBase: './src/static/app'
  },
  module: {
    loaders: [{
      test: /\.js$/,
      exclude: /node_modules/,
      loader: 'babel',
      query: {
        presets: ['es2015', 'react']
      }
    }]
  }
};
