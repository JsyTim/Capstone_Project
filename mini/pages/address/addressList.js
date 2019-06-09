const app = getApp();
Page({
  data: {
    id:1,
    list:[]
  },
  onShow: function () {
      var that = this;
      this.getList();
  },
  //选中谁就把谁设置为默认的
  selectTap: function (e) {
      var that = this;
      wx.request({
          url: app.buildUrl("/address/ops"),
          header: app.getRequestHeader(),
          method:'POST',
          data:{
              id:e.target.id,
              act:'default'
          },
          success: function (res) {
              var resp = res.data;
              if (resp.code != 200) {
                  app.alert({"content": resp.msg});
                  return;
              }
              that.setData({
                 list:resp.data.list
              });
          }
      });
      wx.navigateBack({});
  },
  addressSet: function (e) {
      app.console(e.target.id);
      wx.navigateTo({
          url: "/pages/address/addressSet?id=" + e.target.id
      })
  },
  getList:function(){
      var that = this;
      wx.request({
          url: app.buildUrl("/address/index"),
          header: app.getRequestHeader(),
          success: function (res) {
              var resp = res.data;
              if (resp.code != 200) {
                  app.alert({"content": resp.msg});
                  return;
              }
              that.setData({
                 list:resp.data.list
              });
          }
      });
  },
})
