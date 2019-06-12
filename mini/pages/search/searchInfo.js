// pages/search/searchInfo.js
const app = getApp()
Page({

  data: {

  },

  onLoad: function (e) {
    var that = this;
    that.setData({
        mix_kw: e.searchValue
    });
  },

  onShow: function () {
    var that = this;
    that.getBannerAndCat();
  },
  getBannerAndCat: function () {
      var that = this;
      wx.request({
          url: app.buildUrl("/book/search"),
          header: app.getRequestHeader(),
          data: {
              mix_kw:that.data.mix_kw
          },
          success: function (res) {
              var resp = res.data;
              if (resp.code != 200) {
                  app.alert({"content": resp.msg});
                  return;
              }
              that.setData({
                  booklist:resp.data.list,
              });
          }
      });
  },
})
