import path, { resolve } from 'path';

export default {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.join(process.cwd(), 'dist'),
    library: 'CharConverter',
    libraryTarget: 'umd',
    globalObject: 'this', 
    publicPath: '/dist/',
  },
  module: {
    rules: [
        {
            test: /\.json$/,
            type: 'json',
        },
    ],
  },
  resolve: {
    extensions: ['.js', '.json'],
  },    
  mode: 'production',
};
