var app = getApp();
Component({
  options: {
    addGlobalClass: true,
  },
  data: {
    starCount: 798,
    forksCount: 300,
    visitTotal: 1500,
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
  },
  methods:{
    CopyLink(e) {
      wx.setClipboardData({
        data: e.currentTarget.dataset.link,
        success:function(e) {
          wx.showToast({
            title: '已复制',
            duration: 1000,
          })
        }
      })
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
    getUserInfo: function(e) {
      app.globalData.userInfo = e.detail.userInfo
      this.setData({
        userInfo: e.detail.userInfo,
        hasUserInfo: true
      })
    },
    onShow:function(e){}
  }


})
