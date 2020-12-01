import json
import requests
import execjs
import re
import pandas as pd
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

class zongbang():
    def __init__(self, headers):
        self.headers = headers

    # 用execjs运行七麦数据js文件，破解analysis参数
    def analysis_parser(self,data, url):
        with open('qimai.js', 'r', encoding='utf-8') as f:
            myjs = f.read()
            ctx = execjs.compile(myjs)
            new_pwd = ctx.call('getAnalysis', list(data.values()), url)
            # print(new_pwd)
        return new_pwd
    # 获取app相关数据
    def get_app_data(self,brand, device, country, genre, date, page, data_dict):
        data = {
            'brand': brand,
            'device': device,
            'country': country,
            'genre': genre,
            'date': date,
            'page': page,
            'is_rank_index': '1'
        }
        params = {
            'analysis': self.analysis_parser(data, url='/rank/index'),
            'brand': data['brand'],
            'device': data['device'],
            'country': data['country'],
            'genre': data['genre'],
            'date': data['date'],
            'page': data['page'],
            'is_rank_index': data['is_rank_index']
        }
        # print(params)
        res = requests.get(
            url='https://api.qimai.cn/rank/index',
            params=params,
            headers=self.headers
        )
        html = res.text
        html = html.encode('utf-8').decode('unicode_escape')
        html = json.loads(html)
        print("apple:",html)
        rankInfo = html['rankInfo']
        for one in rankInfo:
            index = one['index']
            keywordCover = one['keywordCover']
            keywordCoverTop3 = one['keywordCoverTop3']
            appId = one['appInfo']['appId']  # app_id
            appName = one['appInfo']['appName']  # app名称
            # compId = one['company']['id']  
            compName = one['company']['name']  # app名称
            comment_rating = one['comment']['rating']  # 分数
            comment_num = one['comment']['num']  # 评分数量
            rank_a = one['rank_a']['ranking']  
            # rank_a_change = one['rank_a']['change'] 
            # rank_a_genre = one['rank_a']['genre']
            rank_b = one['rank_b']['ranking']  
            # rank_b_change = one['rank_b']['change'] 
            rank_b_genre = one['rank_b']['genre']
            rank_c = one['rank_c']['ranking'] 
            # rank_c_change = one['rank_c']['change'] 
            rank_c_genre = one['rank_c']['genre']
            lastReleaseTime = one['lastReleaseTime']

            
            #print(appId)
            data_dict['#'].append(index)
            data_dict['应用'].append(appName)
            data_dict['appId'].append(appId)
            data_dict['company'].append(compName)
            data_dict['总榜排名'].append(rank_a)
            data_dict['应用/游戏'].append(rank_b_genre)
            data_dict['应用/游戏排名'].append(rank_b)
            data_dict['分类'].append(rank_c_genre)
            data_dict['分类排名'].append(rank_c)
            data_dict['关键词覆盖数'].append(keywordCover)
            data_dict['TOP3'].append(keywordCoverTop3)
            data_dict['分数'].append(comment_rating)
            data_dict['评分数'].append(comment_num)
            data_dict['最新版本'].append(pd.to_datetime(lastReleaseTime))

    def shuchu(self,date):

        data_dict1 = {
            '#': [], '应用': [], 'appId': [], 'company': [], '总榜排名': [], '应用/游戏': [], '应用/游戏排名': [], '分类': [], '分类排名': [], '关键词覆盖数': [], 'TOP3': [], '分数': [], '评分数': [], '最新版本': [],
        }
        # 未登录只能看前4页200条数据
        for page in range(1, 31):
            try:
                self.get_app_data(
                    brand='free',
                    device='iphone',
                    country='cn',
                    genre='36',
                    date=date,
                    page=str(page),
                    data_dict=data_dict1,
                )
            except:
                pass
            # pd.DataFrame(data_dict).to_excel('h.xlsx', sheet_name="Sheet2",index=False, encoding='utf-8')
            df1 = pd.DataFrame(data_dict1)
            # 获取ExcelWriter对象
            # writer = pd.ExcelWriter('')
            writer = pd.ExcelWriter(r'总榜单.xlsx')
            # 将df1与df2写入writer中
            df1.to_excel(writer, sheet_name='免费', index=False, encoding='utf-8')




        data_dict2 = {
            '#': [], '应用': [], 'appId': [], 'company': [], '总榜排名': [], '应用/游戏': [], '应用/游戏排名': [], '分类': [], '分类排名': [], '关键词覆盖数': [], 'TOP3': [], '分数': [], '评分数': [], '最新版本': [],
        }
        # 未登录只能看前4页200条数据
        for page in range(1, 31):
            try:
                self.get_app_data(
                    brand='paid',
                    device='iphone',
                    country='cn',
                    genre='36',
                    date=date,
                    page=str(page),
                    data_dict=data_dict2,
                )
            except:
                pass
            df1 = pd.DataFrame(data_dict2)
            df1.to_excel(writer, sheet_name='付费', index=False, encoding='utf-8')



        data_dict3 = {
            '#': [], '应用': [], 'appId': [], 'company': [], '总榜排名': [], '应用/游戏': [], '应用/游戏排名': [], '分类': [], '分类排名': [], '关键词覆盖数': [], 'TOP3': [], '分数': [], '评分数': [], '最新版本': [],
        }
        # 未登录只能看前4页200条数据
        for page in range(1, 31):
            try:
                self.get_app_data(
                    brand='grossing',
                    device='iphone',
                    country='cn',
                    genre='36',
                    date=date,
                    page=str(page),
                    data_dict=data_dict3,
                )
            except:
                pass
            df1 = pd.DataFrame(data_dict3)
            df1.to_excel(writer, sheet_name='畅销', index=False, encoding='utf-8')

        # 保存writer
        writer.save()
        writer.close()

