const path = require("path");

module.exports = {
  entry: "./src/index.ts",
  target: "node",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "dist"),
    library: 'adventOfCode2021',
    libraryTarget: 'commonjs2'
  },
  module: {
    rules: [
      {
        test: /\.ts$/,
        loader: "babel-loader",
        exclude: /node_modules/
      }, {
        test: /\.js$/,
        loader: "source-map-loader",
        exclude: /node_modules/
      }
    ]
  },
  resolve: {
    extensions: [ ".js", ".ts" ]
  }
};