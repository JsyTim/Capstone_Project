//index.js
var app = getApp();
Page({
    data: {},
    onLoad: function () {

    },
    onShow:function(){
        this.getCartList();
        app.console(book_list);
    },
    //每项前面的选中框
    selectTap: function (e) {
        var index = e.currentTarget.dataset.index;
        var book_list = this.data.book_list;
        if (index !== "" && index != null) {
            book_list[ parseInt(index) ].active = !book_list[ parseInt(index) ].active;
            this.setPageData(this.getSaveHide(), this.totalPrice(), this.allSelect(), this.noSelect(), book_list);
        }
    },
    //计算是否全选了
    allSelect: function () {
        var book_list = this.data.book_list;
        var allSelect = false;
        for (var i = 0; i < book_list.length; i++) {
            var curItem = book_list[i];
            if (curItem.active) {
                allSelect = true;
            } else {
                allSelect = false;
                break;
            }
        }
        return allSelect;
    },
    //计算是否都没有选
    noSelect: function () {
        var book_list = this.data.book_list;
        var noSelect = 0;
        for (var i = 0; i < book_list.length; i++) {
            var curItem = book_list[i];
            if (!curItem.active) {
                noSelect++;
            }
        }
        if (noSelect == book_list.length) {
            return true;
        } else {
            return false;
        }
    },
    //全选和全部选按钮
    bindAllSelect: function () {
        var currentAllSelect = this.data.allSelect;
        var book_list = this.data.book_list;
        for (var i = 0; i < book_list.length; i++) {
            book_list[i].active = !currentAllSelect;
        }
        this.setPageData(this.getSaveHide(), this.totalPrice(), !currentAllSelect, this.noSelect(), book_list);
    },
    //加数量
    jiaBtnTap: function (e) {
        var that = this;
        var index = e.currentTarget.dataset.index;
        var book_list = that.data.book_list;
        book_list[parseInt(index)].number++;
        that.setPageData(that.getSaveHide(), that.totalPrice(), that.allSelect(), that.noSelect(), book_list);
        this.setCart( book_list[parseInt(index)].book_id,book_list[parseInt(index)].number );
    },
    //减数量
    jianBtnTap: function (e) {
        var index = e.currentTarget.dataset.index;
        var book_list = this.data.book_list;
        if (book_list[parseInt(index)].number > 1) {
            book_list[parseInt(index)].number--;
            this.setPageData(this.getSaveHide(), this.totalPrice(), this.allSelect(), this.noSelect(), book_list);

            this.setCart( book_list[parseInt(index)].book_id,book_list[parseInt(index)].number );
        }
    },
    //编辑默认全不选
    editTap: function () {
        var book_list = this.data.book_list;
        for (var i = 0; i < book_list.length; i++) {
            var curItem = book_list[i];
            curItem.active = false;
        }
        this.setPageData(!this.getSaveHide(), this.totalPrice(), this.allSelect(), this.noSelect(), book_list);
    },
    //选中完成默认全选
    saveTap: function () {
        var book_list = this.data.book_list;
        for (var i = 0; i < book_list.length; i++) {
            var curItem = book_list[i];
            curItem.active = true;
        }
        this.setPageData(!this.getSaveHide(), this.totalPrice(), this.allSelect(), this.noSelect(), book_list);
    },
    getSaveHide: function () {
        return this.data.saveHidden;
    },
    totalPrice: function () {
        var book_list = this.data.book_list;
        var totalPrice = 0.00;
        for (var i = 0; i < book_list.length; i++) {
            if ( !book_list[i].active) {
                continue;
            }
            totalPrice = totalPrice + parseFloat( book_list[i].price ) * book_list[i].number;
        }
        return totalPrice;
    },
    setPageData: function (saveHidden, total, allSelect, noSelect, book_list) {
        this.setData({
            book_list: book_list,
            saveHidden: saveHidden,
            totalPrice: total,
            allSelect: allSelect,
            noSelect: noSelect,
        });
    },
    //去结算
    toPayOrder: function () {
        var data = {
            type:"cart",
            goods: []
        };
        var book_list = this.data.book_list;
        for (var i = 0; i < book_list.length; i++) {
            if ( !book_list[i].active) {
                continue;
            }
            data['goods'].push({
                "id": book_list[i].book_id,
                "price": book_list[i].price,
                "number": book_list[i].number
            });
        }
        wx.navigateTo({
            url: "/pages/order/order?data=" + JSON.stringify(data)
        });
    },
    toIndexPage: function () {
        wx.switchTab({
            url: "/pages/main/main"
        });
    },
    //选中删除的数据
    deleteSelected: function () {
        var book_list = this.data.book_list;
        var goods = [];
        book_list = book_list.filter(function ( item ) {
            if( item.active ){
                goods.push( {
                    "id":item.book_id
                } )
            }

            return !item.active;
        });

        this.setPageData( this.getSaveHide(), this.totalPrice(), this.allSelect(), this.noSelect(), book_list);
        //发送请求到后台删除数据
        wx.request({
            url: app.buildUrl("/cart/del"),
            header: app.getRequestHeader(),
            method: 'POST',
            data: {
                goods: JSON.stringify( goods )
            },
            success: function (res) {
            }
        });
    },
    getCartList: function () {
        var that = this;
        wx.request({
            url: app.buildUrl("/cart/index"),
            header: app.getRequestHeader(),
            success: function (res) {
                var resp = res.data;
                app.console(resp)
                if (resp.code != 200) {
                    app.alert({"content": resp.msg});
                    return;
                }
                that.setData({
                    book_list:resp.data.list,
                    saveHidden: true,
                    totalPrice: 0.00,
                    allSelect: true,
                    noSelect: false
                });

                that.setPageData(that.getSaveHide(), that.totalPrice(), that.allSelect(), that.noSelect(), that.data.book_list);
            }
        });
    },
    setCart:function( book_id, number ){
        var that = this;
        var data = {
            "id": book_id,
            "number": number
        };
        wx.request({
            url: app.buildUrl("/cart/set"),
            header: app.getRequestHeader(),
            method: 'POST',
            data: data,
            success: function (res) {
            }
        });
    }
});
