from django.shortcuts import render
import camelot
import os.path
import json
# from django.utils import simplejson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'diet.json')

    with open(filename) as json_file:
        json_data = json.load(json_file)

    # print(json_data)

    # scriptpath = os.path.dirname(__file__)
    # # print("test")
    # filename = os.path.join(scriptpath, 'test7.pdf')
    # print(filename)
    # tables = camelot.read_pdf(filename)

    # dict = {
    #         "월": {
    #             "아침": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             },
    #             "점심": {
    #                 "SPECIAL": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "NOODLE": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 }
    #             },
    #             "저녁": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             }
    #         },

    #         "화": {
    #             "아침": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             },
    #             "점심": {
    #                 "SPECIAL": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "NOODLE": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 }
    #             },
    #             "저녁": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             }
    #         },
    #         "수": {
    #             "아침": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             },
    #             "점심": {
    #                 "SPECIAL": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "NOODLE": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 }
    #             },
    #             "저녁": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             }
    #         },
    #         "목": {
    #             "아침": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             },
    #             "점심": {
    #                 "SPECIAL": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "NOODLE": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 }
    #             },
    #             "저녁": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             }
    #         },
    #         "금": {
    #             "아침": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             },
    #             "점심": {
    #                 "SPECIAL": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "NOODLE": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 }
    #             },
    #             "저녁": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             }
    #         },
    #         "토": {
    #             "아침": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             },
    #             "점심": {
    #                 "SPECIAL": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "NOODLE": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 }
    #             },
    #             "저녁": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             }
    #         },
    #         "일": {
    #             "아침": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             },
    #             "점심": {
    #                 "SPECIAL": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "NOODLE": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 }
    #             },
    #             "저녁": {
    #                 "KOREAN1": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #                 "KOREAN2": {
    #                     "메뉴": [],
    #                     "식수": [],
    #                     "후식": []
    #                 },
    #             }
    #         }
    #     }

    # dictTojson = json.dumps(dict)
    # print(dictTojson)

    요일배열 = ['월', '화', '수', '목', '금']
    끼니배열 = ["아침", "점심", "저녁"]
    # 요일배열 = ['월']
    # 끼니배열 = ["아침"]
    아침배열 = ["KOREAN1", "KOREAN2"]
    점심배열 = ["SPECIAL", "NOODLE", "KOREAN"]
    저녁배열 = ["KOREAN1", "KOREAN2"]
    식사종류 = ["메뉴", "식수", "후식"]
    # 아점저배열 = []

    # for row,요일 in zip(range(4,17,3), 요일배열):
    #     for 시간 in 끼니배열:
    #         if 시간 == "아침":
    #             s=1
    #             e=3
    #             아점저배열=아침배열
    #         elif 시간 == "점심":
    #             s=3
    #             e=6
    #             아점저배열=점심배열
    #         else:
    #             s=6
    #             e=8
    #             아점저배열=저녁배열
    #         for i, 식당 in zip(range(s,e), 아점저배열):
    #             for j, 종류 in zip(range(row, row+3), 식사종류):
    #                 if 식당 == "KOREAN" and 종류 == "후식":
    #                     dict[요일][시간][식당][종류] = dict[요일][시간]["NOODLE"][종류]
    #                 else :
    #                     dict[요일][시간][식당][종류] = tables[0].df[i][j].split('\n')

    # dictTojson = json.dumps(dict,ensure_ascii = False)
    def getDiet(언제):
        menu = '\n'.join(s for s in json_data["월"][언제]["KOREAN1"]['메뉴'])
        nom = '\n'.join(s for s in json_data["월"][언제]["KOREAN1"]['식수'])
        dessert = '\n'.join(s for s in json_data["월"][언제]["KOREAN1"]['후식'])
        return {'menu': menu, 'nom': nom, 'dessert': dessert}

    if request.method == "POST":
        postBody = json.loads(request.body.decode('utf-8'))
        _ret = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "총 2개의 예약 내역이 있습니다. 취소할 예약을 선택해 주세요."
                        }
                    },
                    {
                        "carousel": {
                            "type": "itemCard",
                            "items": [
                                {
                                    "imageTitle": {
                                        "title": "예약 완료",
                                        "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/wine.jpg"
                                    },
                                    "itemList": [
                                    ],
                                    "itemListAlignment": "left",
                                    "buttons": [
                                        {
                                            "label": "예약 정보",
                                            "action": "message",
                                            "messageText": "예약 정보"
                                        },
                                        {
                                            "label": "예약 취소",
                                            "action": "message",
                                            "messageText": "예약 취소"
                                        }
                                    ]
                                },
                                {
                                    "imageTitle": {
                                        "title": "결제 대기",
                                        "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/pizza.jpg"
                                    },
                                    "itemList": [
                                        {
                                            "title": "매장명",
                                            "description": "정자역점"
                                        },
                                        {
                                            "title": "예약 일시",
                                            "description": "2022.12.25, 19:25"
                                        },
                                        {
                                            "title": "예약 인원",
                                            "description": "3명"
                                        },
                                        {
                                            "title": "예약금",
                                            "description": "30,000원 (결제 대기)"
                                        }
                                    ],
                                    "itemListAlignment": "left",
                                    "buttons": [
                                        {
                                            "label": "예약 취소",
                                            "action": "message",
                                            "messageText": "예약 취소"
                                        },
                                        {
                                            "label": "결제",
                                            "action": "message",
                                            "messageText": "결제"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ],
                "quickReplies": [
                    {
                        "messageText": "인기 메뉴",
                        "action": "message",
                        "label": "인기 메뉴"
                    },
                    {
                        "messageText": "최근 주문",
                        "action": "message",
                        "label": "최근 주문"
                    },
                    {
                        "messageText": "장바구니",
                        "action": "message",
                        "label": "장바구니"
                    }
                ]
            }
        }
        print(postBody['userRequest']['utterance'])
        if postBody['userRequest']['utterance'] == '아침' or '점심' or '저녁':
            resDiet = getDiet(postBody['userRequest']['utterance'])
            _ret['template']['outputs'][1]['carousel']['items'][0]['itemList'].append({
                "title": "메뉴",
                "description": ' '.join(s for s in json_data["월"][postBody['userRequest']['utterance']]["KOREAN1"]['메뉴'])
            })
      
            for idx, 후식 in enumerate(json_data["월"][postBody['userRequest']['utterance']]["KOREAN1"]['후식']):
                if idx == 0:
                    _ret['template']['outputs'][1]['carousel']['items'][0]['itemList'].append({
                        "title": "후식",
                        "description": 후식
                    })
                else:
                    _ret['template']['outputs'][1]['carousel']['items'][0]['itemList'].append({
                        "title": "",
                        "description": 후식
                    })
        _ret = json.dumps(_ret, ensure_ascii=False)
        # pprint.pprint(_ret)
        return HttpResponse(_ret)
    return render(request, 'index.html')

    # {
    #     "week" : "월",
    #     "아침": [
    #         {
    #             "hall": "KOREAN1",
    #             "메뉴" : [],
    #             "식수" : [],
    #             "후식" : [],
    #         }
    #     ],
    #     "점심": [],
    #     "저녁": [],
    # },
    # for 시간 in dict[요일]:
    #     for i, 식당 in zip(range(1, 3), dict[요일][시간]):
    #         tmp = 0
    #         for j, 종류 in zip(range(2, 5), dict[요일][시간][식당]):
    #             dict[요일][시간][식당][종류] = tables[0].df[i][j].split(
    #                 '\n')
    #         print(tables[0].df[i][j].split('\n'))
    #         # print(tables[0].df[i][j].split('\n'))
    #         tmp = tmp + 1
