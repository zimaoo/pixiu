# -*- coding: UTF-8 -*-

"""
分析同花顺所有行业中哪哪个字最多
"""

industry_list = u'半导体及元件,白色家电,保险及其他,包装印刷,采掘服务,传媒,电力,电气设备,电子制造,房地产开发,非汽车交运,服装家纺,纺织制造,国防军工,公交,港口航运,公路铁路运输,钢铁,光学光电子,环保工程,化工合成材料,化工新材料,化学制品,化学制药,基础化学,机场航运,酒店及餐饮,景点及旅游,计算机设备,计算机应用,家用轻工,交运设备服务,建筑材料,建筑装饰,零售,煤炭开采加工,贸易,农产品加工,农业服务,汽车零部件,汽车整车,其他电子,燃气水务,食品加工制造,视听器材,生物制品,石油矿业开采,通信服务,通信设备,通用设备,物流,新材料,医疗器械服务,饮料制造,园区开发,仪器仪表,有色冶炼加工,银行,医药商业,养殖业,综合,证券,中药,专用设备,造纸,种植业与林业'.split(',')

if __name__ == '__main__':
    word_count_dict = {}
    for industry in industry_list:
        for word in list(industry):
            if word_count_dict.has_key(word):
                word_count_dict[word] = word_count_dict[word] + 1
            else:
                word_count_dict[word] = 1
    word_count_dict = sorted(word_count_dict.items(), key=lambda word_count:word_count[1], reverse=True)
    for word_count in word_count_dict:
        print '%s:%d' % (word_count[0], word_count[1])
