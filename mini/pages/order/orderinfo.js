var app = getApp();
Page({
    data: {},
    onLoad: function (e) {
        var that = this;
    },
    onShow: function () {
        var that = this;
        that.setData({
            info: {
                order_sn:"123123",
                status: -8,
                status_desc: "待支付",
                deadline:"2019-05-31 12:00",
                pay_price: "33.00",
                yun_price: 0.00,
                total_price: "33.00",
                address: {
                    name: "TIM",
                    mobile: "12345678901",
                    address: "福建省福州市闽侯县XX"
                },
                goods: [
                    {
                        name: "三体",
                        price: "12.00",
                        unit: 1,
                        pic_url: "https://img1.doubanio.com\/view\/subject\/m\/public\/s2768378.jpg"
                    },
                    {
                        name: "白夜行",
                        price: "21.00",
                        unit: 1,
                        pic_url: "https://img3.doubanio.com\/view\/subject\/m\/public\/s4610502.jpg"
                    }
                ]
            }
        });
    }
});
