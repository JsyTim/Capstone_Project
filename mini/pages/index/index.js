//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    regFlag: true
  },
  onLoad: function () {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  onShow:function(e){
    this.checkLogin();
  },
  goToIndex:function(){
    wx.navigateTo({
        url: '/pages/main/main',
    });
  },
  checkLogin: function(){
    var that = this;
    wx.login({
        success: function(res){
            wx.request({
                url: app.buildUrl('/member/check-reg'),
                header: app.getRequestHeader(),
                method: 'POST',
                data: {code: res.code},
                success: function(res){
                    if( res.data.code != 200 ){
                        that.setData({
                            regFlag: false
                        });
                        return;
                    }
                    app.setCache("token", res.data.data.token);
                    that.goToIndex();
                }
            })
        }
    })
  },
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },
  onGetUserInfo: function(e){
    var data = e.detail.userInfo;
    var that = this;
    wx.login({
        success:function(res){
            if(!res.code){
                app.alert({'content': '登录失败，请重试'});
                return;
            }
            data['code'] = res.code;
            wx.request({
              url: app.buildUrl('/member/login'),
              header: app.getRequestHeader(),
              method: 'POST',
              data: data,
              success: function(res){
                if( res.data.code != 200 ){
                    app.alert({'content': res.data.msg });
                    return;
                }
                app.setCache("token", res.data.data.token);
                that.goToIndex();
              }
            })
        }
    })
  },
})
