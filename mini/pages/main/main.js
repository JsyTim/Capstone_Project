// pages/main/main.js
var WxSearch = require('../../wxSearchView/wxSearchView.js');
var app = getApp();
Page({
  data: {
    value: 4,
    activeCategoryId:1,
    swiperList: [{
      id: 0,
      type: 'image',
      url: '../../images/banner/emotion.png'
    }, {
      id: 1,
        type: 'image',
        url: '../../images/banner/history.png',
    }, {
      id: 2,
      type: 'image',
      url: '../../images/banner/ideal.png'
    }, {
      id: 3,
      type: 'image',
      url: '../../images/banner/technology.png'
    }, {
      id: 4,
      type: 'image',
      url: '../../images/banner/warmth.png'
    }],
    tagList: [
      {
        name: '新上架',
        id: '0',
      },
      {
        name: '猜你喜欢',
        id: '1',
      },
      {
        name: '畅销榜',
        id: '2',
      },
      {
        name: '外国文学',
        id: '3',
      },
      {
        name: '世界名著',
        id: '4',
      },
      {
        name: '三毛',
        id: '5',
      }],
  },
  onLoad: function (options) {
    var that = this;
    that.towerSwiper('swiperList');
    that.getBannerAndCat();
    if (options && options.searchValue){
      this.setData({
        searchValue: "搜索："+options.searchValue
      });
    }
  },
  onChange:function(e) {
    this.setData({
      value: e.detail
    });
  },
  wxSearchTab: function () {
    wx.redirectTo({
      url: '../search/search'
    })
  },
  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },
  swiperClick:function(e){
    var that = this;
    console.log(e.target.id);
  },
  tagClick: function(e){
    console.log(e.target.id);
    this.setData({
        activeCategoryId: e.target.id
    });
  },
  getBannerAndCat: function () {
      var that = this;
      wx.request({
          url: app.buildUrl("/book/index"),
          header: app.getRequestHeader(),
          success: function (res) {
              var resp = res.data;
              if (resp.code != 200) {
                  app.alert({"content": resp.msg});
                  return;
              }
              that.setData({
                  booklist:resp.data.book_list,
              });
          }
      });
  },
  cardClick:function(e){
    app.console( e.currentTarget.id);
    wx.navigateTo({
      url: "/pages/book/bookinfo?id=" + e.currentTarget.id
    });
  },
  onPullDownRefresh: function () {

  },
  onReachBottom: function () {

  },
  // towerSwiper
  // 初始化towerSwiper
  towerSwiper(name) {
    let list = this.data[name];
    for (let i = 0; i < list.length; i++) {
      list[i].zIndex = parseInt(list.length / 2) + 1 - Math.abs(i - parseInt(list.length / 2))
      list[i].mLeft = i - parseInt(list.length / 2)
    }
    this.setData({
      swiperList: list
    })
  },
  // towerSwiper触摸开始
  towerStart(e) {
    this.setData({
      towerStart: e.touches[0].pageX
    })
  },
  // towerSwiper计算方向
  towerMove(e) {
    this.setData({
      direction: e.touches[0].pageX - this.data.towerStart > 0 ? 'right' : 'left'
    })
  },
  // towerSwiper计算滚动
  towerEnd(e) {
    let direction = this.data.direction;
    let list = this.data.swiperList;
    if (direction == 'right') {
      let mLeft = list[0].mLeft;
      let zIndex = list[0].zIndex;
      for (let i = 1; i < list.length; i++) {
        list[i - 1].mLeft = list[i].mLeft
        list[i - 1].zIndex = list[i].zIndex
      }
      list[list.length - 1].mLeft = mLeft;
      list[list.length - 1].zIndex = zIndex;
      this.setData({
        swiperList: list
      })
    } else {
      let mLeft = list[list.length - 1].mLeft;
      let zIndex = list[list.length - 1].zIndex;
      for (let i = list.length - 1; i > 0; i--) {
        list[i].mLeft = list[i - 1].mLeft
        list[i].zIndex = list[i - 1].zIndex
      }
      list[0].mLeft = mLeft;
      list[0].zIndex = zIndex;
      this.setData({
        swiperList: list
      })
    }
  }
})
