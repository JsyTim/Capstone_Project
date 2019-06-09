const app = getApp();
import Toast from '../../vant/toast/toast';
Page({
  data: {
    code:['350000', '350100', '350121'],
    region: ['福建省', '福州市', '闽侯县'],
    nickname: '',
    mobile: '',
    address: ''
  },
  onLoad: function (option) {
    var that = this;
    that.setData({
        id: option.id
    });
  },
  onShow:function(){
      var that = this;
      that.getInfo();
      // this.getComments();
  },
  nicknameClear: function(e){
    var that = this;
    that.setData({
      nickname: '',
    });
  },
  nicknameChange: function(e){
    app.console(e);
    var that = this;
    var nicknamereg = /^[u4E00-u9FA5]+$/;
    if (!nicknamereg.test(e.detail.value)) {
      Toast.fail('姓名格式错误');
      that.nicknameClear();
      return
    }
    that.setData({
      nickname: e.detail.value
    });
  },
  mobileClear:function(e){
    var that = this;
    that.setData({
      mobile: '',
    });
  },
  mobileChange:function(e){
    var that = this;
    var mobilereg = /^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1})|(17[0-9]{1}))+\d{8})$/;
    if (!mobilereg.test(e.detail.value) || (e.detail.value).length < 11) {
      Toast.fail('手机号码格式错误');
      that.mobileClear();
      return
    }
    that.setData({
      mobile: e.detail.value,
    });

  },
  addressChange:function(e){
    var that=this;
    that.setData({
      address:e.detail.value,
    });
  },
  RegionChange: function(e) {
    app.console(e)
    this.setData({
      region: e.detail.value,
      code: e.detail.code
    })
  },
  bindCancel: function () {
      wx.navigateBack({});
  },
  bindSave: function (e) {
      var that = this;
      var nickname = that.data.nickname;
      var address = that.data.address;
      var mobile = that.data.mobile;

      if (nickname.length < 1) {
          Toast.fail('请填写联系人姓名');
          return
      }
      if (mobile.length < 1) {
          Toast.fail('请填写手机号码');
          return
      }
      if (this.data.region[0].length < 1) {
          Toast.fail('请选择地区');
          return
      }
      if (address.length < 1) {
          Toast.fail('请填写详细地址');
          return
      }
      app.console(that.data);
      wx.request({
          url: app.buildUrl("/address/set"),
          header: app.getRequestHeader(),
          method: "POST",
          data: {
              id: that.data.id,
              province_id: that.data.code[0],
              province_str: that.data.region[0],
              city_id: that.data.code[1],
              city_str: that.data.region[1],
              district_id: that.data.code[2],
              district_str: that.data.region[2],
              nickname: nickname,
              address: address,
              mobile: mobile,
          },
          success: function (res) {
              var resp = res.data;
              if (resp.code != 200) {
                  app.alert({"content": resp.msg});
                  return;
              }
              // 跳转
              wx.navigateBack({});
          }
      })
  },
  deleteAddress: function (e) {
      var that = this;
      var params = {
          "content": "确定删除？",
          "cb_confirm": function () {
              wx.request({
                  url: app.buildUrl("/address/ops"),
                  header: app.getRequestHeader(),
                  method: 'POST',
                  data: {
                      id: that.data.id,
                      act:'del'
                  },
                  success: function (res) {
                      var resp = res.data;
                      app.alert({"content": resp.msg});
                      if (resp.code == 200) {
                          // 跳转
                          wx.navigateBack({});
                      }
                  }
              });
          }
      };
      app.tip(params);
  },
  getInfo: function () {
      var that = this;
      if(that.data.id < 1){
        return
      }
      wx.request({
          url: app.buildUrl("/address/info"),
          header: app.getRequestHeader(),
          data: {
              id: that.data.id
          },
          success: function (res) {
              var resp = res.data;
              if (resp.code != 200) {
                  app.alert({"content": resp.msg});
                  return;
              }
              var info = resp.data.info;
              that.setData({
                  nickname: info.nickname,
                  mobile: info.mobile,
                  address:info.address,
                  region:[info.province_str, info.city_str, info.dist_str]
              });
          }
      });
    }
})
