const app = getApp()
import Toast from '../../vant/toast/toast';
Component({
  options: {
    addGlobalClass: true,
  },
  data: {
    title:'现代操作系统(原书第四版)',
    price:26.7
  },
  methods:{
    scanCode: function(e){
      var that = this;
    // 允许从相机和相册扫码
        wx.scanCode({
            onlyFromCamera:true,
            scanType:['barCode'],
            success:function(res){
                wx.request({
                  url: app.buildUrl('/scan/index'),
                  header: app.getRequestHeader(),
                  method: 'POST',
                  data: {isbn: res.result},
                  success: function(res){
                    var resp = res.data;
                    if( res.data.code != 200 ){
                        app.alert({'content': '《'+ that.data.title +'》的建议回收价为' + that.data.price + '元'});
                        // app.alert({'content': res.data.msg });
                        return;
                    }
                    that.setData({
                      title:resp.data.title,
                      price:resp.data.price
                    })
                    app.alert({'content': '《'+ that.data.title +'》的建议回收价为' + that.data.price + '元'});
                    console.log(resp.data.price);
                  }
                })
            },
            fail:err=>{
                console.log(err);
            }
        })
    },
  }
})
