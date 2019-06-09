//app.js
App({
  onLaunch: function () {
    // 展示本地存储能力
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
    wx.getSystemInfo({
      success: e => {
        this.globalData.StatusBar = e.statusBarHeight;
        let custom = wx.getMenuButtonBoundingClientRect();
        this.globalData.Custom = custom;
        this.globalData.CustomBar = custom.bottom + custom.top - e.statusBarHeight;
      }
    })
    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              // 可以将 res 发送给后台解码出 unionId
              this.globalData.userInfo = res.userInfo

              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })
  },
  globalData: {
    userInfo: null,
    domain: "http://192.168.56.1:8999/mini"
  },
  tip:function( params ){
      var that = this;
      var title = params.hasOwnProperty('title')?params['title']:'提示信息';
      var content = params.hasOwnProperty('content')?params['content']:'';
      wx.showModal({
          title: title,
          content: content,
          success: function(res) {

              if ( res.confirm ) {//点击确定
                  if( params.hasOwnProperty('cb_confirm') && typeof( params.cb_confirm ) == "function" ){
                      params.cb_confirm();
                  }
              }else{//点击否
                  if( params.hasOwnProperty('cb_cancel') && typeof( params.cb_cancel ) == "function" ){
                      params.cb_cancel();
                  }
              }
          }
      })
  },
  alert:function( params ){
      var title = params.hasOwnProperty('title')?params['title']:'提示信息';
      var content = params.hasOwnProperty('content')?params['content']:'';
      wx.showModal({
          title: title,
          content: content,
          showCancel:false,
          success: function(res) {
              if (res.confirm) {//用户点击确定
                  if( params.hasOwnProperty('cb_confirm') && typeof( params.cb_confirm ) == "function" ){
                      params.cb_confirm();
                  }
              }else{
                  if( params.hasOwnProperty('cb_cancel') && typeof( params.cb_cancel ) == "function" ){
                      params.cb_cancel();
                  }
              }
          }
      })
  },
  console:function( msg ){
      console.log( msg);
  },
  getRequestHeader:function(){
    return {
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization': this.getCache( "token" )
    }
  },
  buildUrl: function(path, params){
        var url = this.globalData.domain + path;
        var _paramUrl = "";
        if(  params ){
        _paramUrl = Object.keys( params ).map( function( k ){
            return [ encodeURIComponent( k ),encodeURIComponent( params[ k ] ) ].join("=");
        }).join("&");
        _paramUrl = "?" + _paramUrl;
        }
        return url + _paramUrl;
  },
  getCache:function( key ){
        var value = undefined;
        try {
          value = wx.getStorageSync( key );
        } catch (e) {
        }
        return value;
  },
  setCache:function(key,value){
        wx.setStorage({
            key:key,
            data:value
        });
  }
})
