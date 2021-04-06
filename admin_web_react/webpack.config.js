let path = require('path');
let HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode:'development',
    entry: "./app/app.jsx", // входная точка - исходный файл
    output:{
        // path: path.resolve(__dirname, './public'),
        // publicPath: '/public/',
        // filename: "bundle.js"
        path: path.resolve(__dirname, './public/js/'),     // путь к каталогу выходных файлов - папка public
        publicPath: 'http://localhost:8080/js/',
        filename: '[name].[contenthash].js',// название создаваемого файла
        clean: true,
    },
    devServer: {
     historyApiFallback: true,
     port: 3000,
     open: true
   },
    module:{
        rules:[   //загрузчик для jsx
            {
                test: /\.jsx?$/, // определяем тип файлов
                exclude: /(node_modules)/,  // исключаем из обработки папку node_modules
                loader: "babel-loader",   // определяем загрузчик
                options:{
                    presets:["@babel/preset-env", "@babel/preset-react"]    // используемые плагины
                }
            },
            {
                test: /\.css$/i,
                exclude: /node_modules/,
                use: [
                  'style-loader',
                  {
                    loader: 'css-loader',
                    options: {
                      modules: {
                        localIdentName: "[path]__[local]--[hash:base64:5]"
                      },
                    },
                  },
                ],
            },
            
        ]
    },
    plugins: [
      new HtmlWebpackPlugin({
        template: "./public/index.html"
      })
    ]
}
