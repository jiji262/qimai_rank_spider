
from zongbang import zongbang
from youxi import youxi
if __name__ == '__main__':

   date='2020-12-01'  #设置日期

   headers = {
        'Cookie': 'qm_check=SxJXQEUSChd+XERcXBxqGRB5QllDGGF6GxBpXEFLEHdCUUBYWVZEEgYMABYUElNYVVNbEg8VAhwJHAQUABwAEk0%3D; gr_user_id=6ed273c8-320d-4694-ab57-e8b5a9745ac6; grwng_uid=c0659410-8d9a-4905-bc21-1c2cbf607aa1; USERINFO=5Y%2FQ1BnESuTc5%2B6GouiSr%2BUQfco5F8c6db5yQszQEEXPW9wGPYMEGrE7rTkc6WCbAs11RY6WzL0VOZCpGGc7ssnXVPhiiVi7xLpif%2FkSMy5SJwt2GJjSJR4OAaNxi86MhcpolDlbj4SKmVmcssk1Ug%3D%3D; ada35577182650f1_gr_last_sent_cs1=qm10674066890; aso_ucenter=5f67sY9RkpJa9Ko9nf%2FiJvSl5Kf6nr7qcMp6gIXEAsjIUKLW8lw705u85nYVGOcZ1A; synct=1606826414.821; syncd=36; PHPSESSID=6h870476j1md25kuq2lnt3om4m; ada35577182650f1_gr_session_id=937c6547-4079-4bd7-8adc-a6fdf58268e2; ada35577182650f1_gr_last_sent_sid_with_cs1=937c6547-4079-4bd7-8adc-a6fdf58268e2; ada35577182650f1_gr_session_id_937c6547-4079-4bd7-8adc-a6fdf58268e2=true; ada35577182650f1_gr_cs1=qm10674066890',
        # 'Referer': 'https://www.qimai.cn/rank/index/brand/free/device/iphone/country/jp/genre/6017',
        'Referer':'https://www.qimai.cn/rank/marketRank',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

   zongbang=zongbang(headers, date)
   zongbang.shuchu(date)

   youxi=youxi(headers, date)
   youxi.shuchu(date)
