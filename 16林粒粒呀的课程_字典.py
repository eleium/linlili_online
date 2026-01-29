# 用字典制作一个通讯录
'''
可以用以前的变量来做通讯录：
phone_number_xiaoming='130111111'
phone_number_xiaoliang='130222222'
也可以用列表：
phone_number=['130111111','130222222']
以上的方法都很麻烦,我们可以用字典来实现 dictionary
字典是键、值对,一个key对应一个value ，用{ }包裹
phone_number_list={'xiaoming':'130111111','xiaoliang':'130222222'}
'''


'''
因为列表[]是可变的list['a','b','130111111','130222222'],但是元组() tuple 是不可变的：
可变的有： 列表 list[] 和 字典dictionary{key: value}，集合 set{}.
不可变的有：元组()tuple,字符串str,整数int，浮点数float，布尔值bool，空值None
            元组([列表], 字符串,整数,浮点数等组成),若其中的[列表]改变，元组也就改变。
                 
'''
# 课堂实践

# 定义一个新的字典：
new_language = {
    "YYds": "永远的神，用来形容某人或某事物非常优秀。",#
    "pua": "情感操控，多用于揭露不健康的恋爱关系。",#
    "emo": "情绪低落、丧。"#
}
# 增加新的键值对给字典：
new_language["破防"] = "情绪被触动到破裂，无法保持理性。"
new_language["摆烂"] = "放弃努力，消极对待。"
new_language["躺平"] = "主动放弃内卷和竞争，选择佛系生活。"
new_language["绝绝子"] = "非常绝妙的事物或行为，夸张的称赞。"
new_language["拿捏"] = "对某事掌控自如。"
new_language["社死"] = "社交场合中令人尴尬到想“当场去世”的行为。"
new_language["内卷"] = "过度竞争，导致资源浪费或不必要的努力。"

from pprint import pprint#导入pprint模块，可以逐行打印。
pprint(new_language)

print(new_language['躺平'])#打印出其中一个键的值
#查询功能：
query=input('请输入你要查询的网络用语：')#query:不确定的意思
if query in new_language:
    print('你查询的'+query+'含义如下；')
    print(new_language[query])
else:
    print('你查询的词条暂未收录。')
    print('本词条收录的词条数目为：'+str(len(new_language))+'条')