import enum
from django.shortcuts import render
import camelot
import os.path
import json
# from django.utils import simplejson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

_errRet = {
"version": "2.0",
"template": {
    "outputs": [
        {
            "simpleText": {
                "text": "아직 식단 정보가 업데이트 되지 않았습니다.\n식단이 올라오는대로 업데이트할게요."
            }
        }
    ]
}
}

@csrf_exempt
def index(request):
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'diet.json')

    with open(filename) as json_file:
        json_data = json.load(json_file)
    현재 = datetime.datetime.now()
    요일배열 = ['월', '화', '수', '목', '금', '토', '일']
    요일 = 요일배열[datetime.datetime.today().weekday()]
    끼니배열 = ["아침", "점심", "저녁"]
    아침배열 = ["KOREAN1", "KOREAN2"]
    점심배열 = ["SPECIAL", "NOODLE", "KOREAN"]
    저녁배열 = ["KOREAN1", "KOREAN2"]
    식사종류 = ["메뉴", "식수", "후식"]

    if request.method == "POST":
        # 업데이트 검사
        
        if json_data['updated'] < 현재.strftime("%U"):
          return HttpResponse(_errRet)

        postBody = json.loads(request.body.decode('utf-8'))
        _ret = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "식사 맛있게 하세요~!"
                        }
                    },
                    {
                        "carousel": {
                            "type": "itemCard",
                            "items": [
                            ]
                        }
                    }
                ],
                "quickReplies": [
                    {
                        "messageText": "아침",
                        "action": "message",
                        "label": "아침"
                    },
                    {
                        "messageText": "점심",
                        "action": "message",
                        "label": "점심"
                    },
                    {
                        "messageText": "저녁",
                        "action": "message",
                        "label": "저녁"
                    },
                    {
                        "messageText": "빵",
                        "action": "message",
                        "label": "빵"
                    }
                ]
            }
        }
        발화 = postBody['action']['detailParams']['mealTime']['value']
        if 발화 == '아침' or '점심' or '저녁':
            if 발화 == '아침':
                배열 = 아침배열
            elif 발화 == '점심':
                배열 = 점심배열
            else:
                배열 = 저녁배열

            for 식당 in 배열:
                tmp = {
                    "imageTitle": {
                        "title": 식당,
                        "imageUrl": "https://babkaotalk.herokuapp.com/static/images/DangDang.png"
                    },
                    "itemList": [
                        {
                            "title": "메뉴",
                            "description": ', '.join(s for s in json_data[요일][발화][식당]['메뉴'])
                        },
                        {
                            "title": "후식",
                            "description": ', '.join(s for s in json_data[요일][발화][식당]['후식'])
                        },
                        {
                            "title": "식수",
                            "description": ', '.join(s for s in json_data[요일][발화][식당]['식수'])
                        }
                    ],
                    "itemListAlignment": "left",
                }
                _ret['template']['outputs'][1]['carousel']['items'].append(tmp)
        _ret = json.dumps(_ret, ensure_ascii=False)

        return HttpResponse(_ret)
    return render(request, 'index.html')


def bread(request):
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'bread.json')

    with open(filename) as json_file:
        json_data = json.load(json_file)

    if request.method == "POST":

        postBody = json.loads(request.body.decode('utf-8'))
        # 발화 = postBody['action']['detailParams']['bakery']['value']

        for idx, arr in enumerate(json_data['bread']):
            if arr['id'] == datetime.datetime.now().strftime("%-d"):
                bread = arr['name']
                breadIdx = idx

        _ret = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "itemCard": {
                            "title": "",
                            "thumbnail": {
                                "imageUrl": "https://babkaotalk.herokuapp.com/static/bread/" + str(breadIdx+1) + '.jpg',
                                "width": 800,
                                "height": 800
                            },
                            "itemList": [
                                {
                                    "title": "빵",
                                    "description": bread
                                }
                            ],
                        }
                    }
                ],
                "quickReplies": [
                    {
                        "messageText": "아침",
                        "action": "message",
                        "label": "아침"
                    },
                    {
                        "messageText": "점심",
                        "action": "message",
                        "label": "점심"
                    },
                    {
                        "messageText": "저녁",
                        "action": "message",
                        "label": "저녁"
                    },
                    {
                        "messageText": "빵",
                        "action": "message",
                        "label": "빵"
                    }
                ]
            }
        }
        # _ret = {
        #     "version": "2.0",
        #     "template": {
        #         "outputs": [
        #                 {
        #                     "simpleText": {
        #                         "text": bread
        #                     }
        #                 },
        #             {
        #                     "simpleImage": {
        #                         "imageUrl": "https://babkaotalk.herokuapp.com/static/bread/" + breadIdx + '.jpg',
        #                         "altText": bread
        #                     }
        #                 }
        #         ]
        #     }
        # }
        _ret = json.dumps(_ret, ensure_ascii=False)
        return HttpResponse(_ret)

    return render(request, 'bread.html')
