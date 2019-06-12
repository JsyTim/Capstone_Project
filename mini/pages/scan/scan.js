const app = getApp()
Component({
  options: {
    addGlobalClass: true,
  },
  data: {},
  methods:{
    scanCode: function(e){
    // 允许从相机和相册扫码
        wx.scanCode({
            onlyFromCamera:true,
            scanType:['barCode'],
            success:function(res){
                wx.request({
                  url: app.buildUrl('/scan/index'),
                  header: app.getRequestHeader(),
                  method: 'POST',
                  data: {ISBN: res.result},
                  success: function(res){
                    if( res.data.code != 200 ){
                        app.alert({'content': res.data.msg });
                        return;
                    }
                    Dialog.confirm({
                      title: '回收信息',
                      message: '建议回收价为' + JSON()
                    }).then(() => {
                      // on confirm
                      
                    }).catch(() => {
                      // on cancel
                    });
                    console.log(res);
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
