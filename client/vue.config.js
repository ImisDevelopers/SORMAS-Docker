module.exports = {
  devServer: {
    proxy: 'http://sormas/sormas-rest:80',
    publicPath: '/imis/',
    public: 'sormas-docker-test.com'
  },
}
