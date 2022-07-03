import enum
from django.shortcuts import render
import camelot
import os.path
import json
# from django.utils import simplejson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

요일배열 = ['월', '화', '수', '목', '금', '토', '일']
errRet = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": ''}
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


@csrf_exempt
def index(request):
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'diet.json')

    with open(filename) as json_file:
        json_data = json.load(json_file)
    현재 = datetime.datetime.now()
    요일 = 요일배열[datetime.datetime.today().weekday()]
    끼니배열 = ["아침", "점심", "저녁"]
    아침배열 = ["KOREAN1", "KOREAN2"]
    점심배열 = ["SPECIAL", "NOODLE", "KOREAN"]
    저녁배열 = ["KOREAN1", "KOREAN2"]
    식사종류 = ["메뉴", "식수", "후식"]

    if request.method == "POST":
        # 업데이트 검사
        postBody = json.loads(request.body.decode('utf-8'))
        발화 = postBody['action']['detailParams']['mealTime']['value']
        try: 
            if postBody['action']['detailParams']['dateTime']['value'] == '내일' and 요일배열[datetime.datetime.today().weekday()] != '일':
                요일 = 요일배열[(datetime.datetime.today().weekday() + 1) % 7 ]
            elif postBody['action']['detailParams']['dateTime']['value'] == '내일' and 요일배열[datetime.datetime.today().weekday()] == '일':
                _errRet = errRet
                _errRet['template']['outputs'][0]['simpleText']['text'] = "아직 일요일에는 내일 식단 정보를 조회할 수 없습니다."
                _errRet = json.dumps(_errRet, ensure_ascii=False)
                return HttpResponse(_errRet)
            else:
                요일 = postBody['action']['detailParams']['dateTime']['value']
        except:
            요일 = 요일배열[datetime.datetime.today().weekday()]


        if json_data['updated'] < int(현재.strftime("%W")):
            _errRet = errRet
            _errRet['template']['outputs'][0]['simpleText']['text'] = "아직 식단 정보가 업데이트 되지 않았습니다.\n식단이 올라오는대로 업데이트할게요."
            _errRet = json.dumps(_errRet, ensure_ascii=False)
            return HttpResponse(_errRet)

        
        _ret = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": 요일+"요일 " + 발화 + " 메뉴입니다.\n식사 맛있게 하세요~!"
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
                        "imageUrl": "https://babkaotalk.herokuapp.com/static/images/namu.png"
                    },
                    "itemList": [
                        {
                            "title": "메뉴",
                            "description": ', '.join(s for s in json_data[요일][발화][식당]['메뉴'][:-2])
                        },
                        {
                            "title": " ",
                            "description": ', '.join(s for s in json_data[요일][발화][식당]['메뉴'][-2:])
                            
                        },
                        {
                            "title": "PLUS",
                            "description": ', '.join(s for s in json_data[요일][발화][식당]['후식'])
                        }
                    ],
                    "itemListAlignment": "left",
                }
                if len(json_data[요일][발화][식당]['메뉴'])>0:
                    _ret['template']['outputs'][1]['carousel']['items'].append(tmp)
                print(json_data[요일][발화][식당]['메뉴'],json_data[요일][발화][식당]['후식'],json_data[요일][발화][식당]['식수'])
                # print(_ret['template']['outputs'][1]['carousel']['items'])
        print((_ret['template']['outputs'][1]['carousel']['items']))
        if len(_ret['template']['outputs'][1]['carousel']['items']) == 0:
            _ret['template']['outputs'][0]['simpleText']['text'] = "응답 내용이 없습니다. 문제가 발생했거나 식사가 제공되지 않나봐요."
            del _ret['template']['outputs'][1]
        _ret = json.dumps(_ret, ensure_ascii=False)

        return HttpResponse(_ret)
    return render(request, 'index.html', {'now': datetime.datetime.now(),"updated":json_data['updated'], "nows": 현재.strftime("%W")})


def bread(request):
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'bread.json')

    with open(filename) as json_file:
        json_data = json.load(json_file)

    if request.method == "POST":

        postBody = json.loads(request.body.decode('utf-8'))
        # 발화 = postBody['action']['detailParams']['bakery']['value']
        요일 = 요일배열[datetime.datetime.today().weekday()]
        breadIdx = -1
        if(len(json_data['bread']) == 0) :
            _errRet['template']['outputs'][0]['simpleText']['text'] = "빵 정보가 아직 업데이트되지 않았습니다. 업로드되는 대로 반영하겠슴다~!"
        for idx, arr in enumerate(json_data['bread']):
            if arr['id'] == datetime.datetime.now().strftime("%-d"):
                bread = arr['name']
                breadIdx = idx
        if breadIdx == -1:
            _errRet = errRet
            if 요일 == '토' or 요일 == '일':
                _errRet['template']['outputs'][0]['simpleText']['text'] = "오늘은 빵이 제공되지 않아요. "
            else:
                _errRet['template']['outputs'][0]['simpleText']['text'] = "빵 정보가 정상적으로 표시되지 않고 있습니다. 불편을 드려 죄송합니다."
            _errRet = json.dumps(_errRet, ensure_ascii=False)
            return HttpResponse(_errRet)
        _ret = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "itemCard": {
                            "title": "",
                            "thumbnail": {
                                # "imageUrl": "https://babkaotalk.herokuapp.com/static/bread/" + str(breadIdx+1+2) + '.jpg',
                                "imageUrl": "https://babkaotalk.herokuapp.com" + arr['img'],
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
