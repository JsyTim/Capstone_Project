//index.js
//获取应用实例
var app = getApp();
var utils = require('../../utils/util.js');
Page({
    data: {
        autoplay: true,
        interval: 3000,
        duration: 1000,
        swiperCurrent: 0,
        hideShopPopup: true,
        buyNumber: 1,
        buyNumMin: 1,
        buyNumMax: 1,
        canSubmit: false, //  选中时候是否允许加入购物车
        shopCarInfo: {},
        shopType: "addShopCar",//购物类型，加入购物车或立即购买，默认为加入购物车,
        commentCount:2,
        shopCarNum:'',
    },
    onLoad: function (option) {
      app.console(option);
      var that = this;
      that.setData({
          id: option.id
      });
    },
    onShow:function(e){
        var that = this;
        that.getInfo();
        // this.getComments();
    },
    goShopCar: function () {
        wx.reLaunch({
            url: "/pages/cart/cart"
        });
    },
    toAddShopCar: function () {
        this.setData({
            shopType: "addShopCar"
        });
        this.bindGuiGeTap();
    },
    tobuy: function () {
        this.setData({
            shopType: "tobuy"
        });
        this.bindGuiGeTap();
    },
    addShopCar: function () {
        var that = this;
        var data = {
            "id": this.data.id,
            "number": this.data.buyNumber
        };
        wx.request({
            url: app.buildUrl("/cart/set"),
            header: app.getRequestHeader(),
            method: 'POST',
            data: data,
            success: function (res) {
                var resp = res.data;
                app.alert({"content": resp.msg});
                that.setData({
                    hideShopPopup: true
                });
            }
        });
    },
    buyNow: function () {
        var data = {
            goods: [
                {
                    "id": this.data.id,
                    "price": this.data.price,
                    "number": this.data.buyNumber
                }
            ]
        };
        this.setData({
            hideShopPopup: true
        });
        wx.navigateTo({
            url: "/pages/order/order?data=" + JSON.stringify(data)
        });
    },
    /**
     * 规格选择弹出框
     */
    bindGuiGeTap: function () {
        this.setData({
            hideShopPopup: false
        });
    },
    /**
     * 规格选择弹出框隐藏
     */
    closePopupTap: function () {
        this.setData({
            hideShopPopup: true
        })
    },
    numJianTap: function () {
        if (this.data.buyNumber <= this.data.buyNumMin) {
            return;
        }
        var currentNum = this.data.buyNumber;
        currentNum--;
        this.setData({
            buyNumber: currentNum
        });
    },
    numJiaTap: function () {
        if (this.data.buyNumber >= this.data.buyNumMax) {
            return;
        }
        var currentNum = this.data.buyNumber;
        currentNum++;
        this.setData({
            buyNumber: currentNum
        });
    },
    getInfo: function () {
        var that = this;
        // app.console(that.data.id)
        wx.request({
            url: app.buildUrl("/book/info"),
            header: app.getRequestHeader(),
            data: {
                id:that.data.id
            },
            success: function (res) {
                var resp = res.data;
                if (resp.code != 200) {
                    app.alert({"content": resp.msg});
                    wx.navigateTo({
                        url: "/pages/main/main"
                    });
                    return;
                }
                that.setData({
                    title:resp.data.title,
                    price:resp.data.price,
                    oprice:resp.data.oprice,
                    author:resp.data.author,
                    press:resp.data.press,
                    grade:resp.data.grade,
                    binding:resp.data.binding,
                    main_image:resp.data.main_image,
                    desc: resp.data.desc,
                    buyNumMax: resp.data.stock,
                });
            }
        });
    },
    // getComments:function(){
    //     var that = this;
    //     wx.request({
    //         url: app.buildUrl("/book/comments"),
    //         header: app.getRequestHeader(),
    //         data: {
    //             id: that.data.id
    //         },
    //         success: function (res) {
    //             var resp = res.data;
    //             if (resp.code != 200) {
    //                 app.alert({"content": resp.msg});
    //                 return;
    //             }
    //
    //             that.setData({
    //                 commentList: resp.data.list,
    //                 commentCount: resp.data.count,
    //             });
    //         }
    //     });
    // },
    onShareAppMessage: function () {
        var that = this;
        return {
            title: that.data.name,
            path: '/pages/book/info?id=' + that.data.id,
            success: function (res) {
                // 转发成功
                wx.request({
                    url: app.buildUrl("/member/share"),
                    header: app.getRequestHeader(),
                    method: 'POST',
                    data: {
                        url: utils.getCurrentPageUrlWithArgs()
                    },
                    success: function (res) {

                    }
                });
            },
            fail: function (res) {
                // 转发失败
            }
        }
    }
});
