from django.shortcuts import render
import camelot
import os.path
import json
# from django.utils import simplejson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PyPDF2 import PdfFileWriter, PdfFileReader
import datetime
import numpy as np

scriptpath = os.path.dirname(__file__)

filename = os.path.join(scriptpath, 'diet2.pdf')
tables = []

# tables.append(camelot.read_pdf(filename, table_regions=['348, 1678, 2140, 1479']))
# tables.append(camelot.read_pdf(filename, table_regions=['348, 1509, 2153, 1415']))
# tables.append(camelot.read_pdf(filename, table_regions=['348, 1446, 2138, 1250']))
# tables.append(camelot.read_pdf(filename, table_regions=['348, 1274, 2135, 1191']))
# tables.append(camelot.read_pdf(filename, table_regions=['348, 1214, 2136, 1052']))
# test = camelot.read_pdf(filename, table_regions=[
#     '348, 1678, 2140, 1479',
#     '348, 1509, 2153, 1415',
#     '348, 1446, 2138, 1250',
#     '348, 1274, 2135, 1191',
#     '348, 1214, 2136, 1052',
#     '348, 927, 2136, 771',
#     '348, 800, 2136, 690',
#     '348, 711, 2136, 669',
#     '348, 684, 2136, 644',
#     '348, 658, 2136, 438',
#     '348, 458, 2136, 260'
#     ])


# 세로
# xy = [
#     '348, 1678, 2140, 1479',
#     '348, 1509, 2153, 1415',
#     '348, 1446, 2138, 1250',
#     '348, 1274, 2135, 1191',
#     '348, 1214, 2136, 1052',
#     '348, 927, 2136, 771',
#     '348, 800, 2136, 690',
#     '348, 711, 2136, 669',
#     '348, 684, 2136, 644',
#     '348, 658, 2136, 438',
#     '348, 458, 2136, 260'
# ]

# arr_table = []

# for i in range(len(xy)):
#     temp_table = camelot.read_pdf(filename, table_regions=[xy[i]])
#     temp_table[0].df.replace('', np.nan , inplace=True)
#     arr_table.append(temp_table[0].df.dropna(axis=0, thresh=4).dropna(axis=1, thresh=1).values.tolist())
#     if i == 2:
#         break


now = datetime.datetime.now()

dict = {
        "updated": int(now.strftime("%W")),
        "월": {
            "아침": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            },
            "점심": {
                "SPECIAL": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "NOODLE": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                }
            },
            "저녁": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            }
        },

        "화": {
            "아침": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            },
            "점심": {
                "SPECIAL": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "NOODLE": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                }
            },
            "저녁": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            }
        },
        "수": {
            "아침": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            },
            "점심": {
                "SPECIAL": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "NOODLE": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                }
            },
            "저녁": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            }
        },
        "목": {
            "아침": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            },
            "점심": {
                "SPECIAL": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "NOODLE": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                }
            },
            "저녁": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            }
        },
        "금": {
            "아침": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            },
            "점심": {
                "SPECIAL": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "NOODLE": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                }
            },
            "저녁": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            }
        },
        "토": {
            "아침": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            },
            "점심": {
                "SPECIAL": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "NOODLE": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                }
            },
            "저녁": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            }
        },
        "일": {
            "아침": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            },
            "점심": {
                "SPECIAL": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "NOODLE": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                }
            },
            "저녁": {
                "KOREAN1": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
                "KOREAN2": {
                    "메뉴": [],
                    "식수": [],
                    "후식": []
                },
            }
        }
    }


dictTojson = json.dumps(dict)
# print(dictTojson)

요일배열 = ['월', '화', '수', '목', '금', '토', '일']
요일 = 요일배열[datetime.datetime.today().weekday()]



식당 = ["KOREAN1", "KOREAN2", "SPECIAL",
      "NOODLE", "KOREAN", "KOREAN1", "KOREAN2"]

식사종류 = ["메뉴", "후식"]


weekday = camelot.read_pdf(filename, table_areas=[
    "368.6, 1669.4, 2129.2, 1493.1",
    "368.6, 1493.1, 2129.2, 1437.6",
    "368.6, 1437.6, 2129.2, 1259.8",
    "368.6, 1259.8, 2129.2, 1205",
    "368.6, 1205, 2129.2, 1063.7",
    "368.6, 1063.7, 2129.2, 913",
    "368.6, 913, 2129.2, 786",
    "368.6, 786, 2129.2, 703.3",
    "368.6, 703.3, 2129.2, 676.5",
    "368.6, 676.5, 2129.2, 652",
    "368.6, 652, 2129.2, 450",
    "368.6, 450, 2129.2, 243",
], flavor="stream"
)


    
# for i in range(len(weekday)):
#     if len(weekday[i].df.columns) != 5:
#         raise Exception('컬럼의 갯수가 5개가 아닙니다.')
#     if 0 < i < 4 :
#         식사시간 = "아침"
#     elif 4 < i < 10 : 
#         식사시간 = "점심"
#     else :
#         식사시간 = "저녁"
#     dict[요일배열[i]][식사시간] 
#     print(weekday[i].df)

for i in range(len(weekday)):
    print(weekday[i].df[2].values.tolist())

# weekend = camelot.read_pdf(filename, table_areas=[
#     "2194, 1670, 2620.3, 1205",
#     "2194, 1205, 2620.3, 652",
#     "2194, 652, 2620.3, 245"
# ], flavor="stream"
# )

# for i in range(len(weekend)):
#     print(weekend[i].df)

