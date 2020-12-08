
from zongbang import zongbang
from youxi import youxi
import sys
if __name__ == '__main__':
    headers = {
        'Cookie': 'qm_check=SxJXQEUSChd+XERcXBxqGRB5QllDGGF6GxBpXEFLEHdCUUBYWVZEEgYMABYUElNYVVNbEg8VAhwJHAQUABwAEk0%3D; gr_user_id=6ed273c8-320d-4694-ab57-e8b5a9745ac6; grwng_uid=c0659410-8d9a-4905-bc21-1c2cbf607aa1; ada35577182650f1_gr_last_sent_cs1=qm10674066890; aso_ucenter=5f67sY9RkpJa9Ko9nf%2FiJvSl5Kf6nr7qcMp6gIXEAsjIUKLW8lw705u85nYVGOcZ1A; PHPSESSID=6h870476j1md25kuq2lnt3om4m; USERINFO=5Y%2FQ1BnESuTc5%2B6GouiSr%2BUQfco5F8c6db5yQszQEEXPW9wGPYMEGrE7rTkc6WCbAs11RY6WzL0VOZCpGGc7snfsvANJV185G3%2FFvAx9YDYjtiXB%2Fu7oIMiewDmAuDss8wnPVMYKf%2FuzVjygnGbQ3A%3D%3D; ada35577182650f1_gr_session_id=bf1a8ac2-367f-48d3-9a5b-72dd7c5d62ac; ada35577182650f1_gr_last_sent_sid_with_cs1=bf1a8ac2-367f-48d3-9a5b-72dd7c5d62ac; ada35577182650f1_gr_session_id_bf1a8ac2-367f-48d3-9a5b-72dd7c5d62ac=true; synct=1607436941.582; syncd=-2678; ada35577182650f1_gr_cs1=qm10674066890',
        # 'Referer': 'https://www.qimai.cn/rank/index/brand/free/device/iphone/country/jp/genre/6017',
        'Referer':'https://www.qimai.cn/rank/marketRank',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    if len(sys.argv)>2: 
        date = sys.argv[2]
        if sys.argv[1]=='youxi':
            youxi=youxi(headers, date)
            youxi.shuchu(date)
        elif sys.argv[1]=='zongbang': 
            zongbang=zongbang(headers, date)
            zongbang.shuchu(date)
    else: #如果没有传入参数，则port默认是7878
        print("Usage: python3 main.py youxi|zongbang 2020-10-24")



   

   
