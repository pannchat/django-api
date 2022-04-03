from django.shortcuts import render
import camelot
import os.path
import json
# from django.utils import simplejson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime


scriptpath = os.path.dirname(__file__)
# print("test")
filename = os.path.join(scriptpath, 'diet2.pdf')
print(filename)
tables = camelot.read_pdf(filename,flavor='stream',
                          table_regions=['0,0,400,400'])
# print(tables[0].df[1])
print(tables[0].df)


dict = {
    "월": {
        "아침": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "점심": {
            "INTERNATIONAL": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            },
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "저녁": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        }
    },

    "화": {
        "아침": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "점심": {
            "INTERNATIONAL": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            },
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "저녁": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        }
    },
    "수": {
        "아침": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "점심": {
            "INTERNATIONAL": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            },
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "저녁": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        }
    },
    "목": {
        "아침": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "점심": {
            "INTERNATIONAL": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            },
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "저녁": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        }
    },
    "금": {
        "아침": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "점심": {
            "INTERNATIONAL": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            },
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "저녁": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        }
    },
    "토": {
        "아침": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "점심": {
            "INTERNATIONAL": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            },
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "저녁": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        }
    },
    "일": {
        "아침": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "점심": {
            "INTERNATIONAL": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            },
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        },
        "저녁": {
            "KOREAN": {
                "메뉴": [],
                "selfbar": [],
                "plusbar": []
            }
        }
    }
}

dictTojson = json.dumps(dict)

# print(tables[0].df)
# print(tables[0].df[2])

요일배열 = ['월', '화', '수', '목', '금']
# 요일 = 요일배열[datetime.datetime.today().weekday()]
# 끼니배열 = ["아침", "점심", "저녁"]
# 아침배열 = ["KOREAN1", "KOREAN2"]
# 점심배열 = ["SPECIAL", "NOODLE", "KOREAN"]
# 저녁배열 = ["KOREAN1", "KOREAN2"]
# 식사종류 = ["메뉴", "selfbar", "plusbar"]
# 아점저배열 = []

# 끼니배열 = ["아침", "점zip(range(4,17,3), 요일배열):
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
#                 if 식당 == "KOREAN" and 종류 == "plusbar":
#                     dict[요일][시간][식당][종류] = dict[요일][시간]["NOODLE"][종류]
#                 else :
#                     dict[요일][시간][식당][종류] = tables[0].df[i][j].split('\n')

# dictTojson = json.dumps(dict,ensure_ascii = False)

# with open('diet2.json','w',encoding='utf-8') as make_file:
#     json.dump(dict, make_file, ensure_ascii=False, indent='\t')
