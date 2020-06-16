module.exports = {
  publicPath: '/imis/',
  devServer: {
    proxy: 'https://sormas-docker-test.com/imis/',
    public: 'sormas-docker-test.com',
  },
}
