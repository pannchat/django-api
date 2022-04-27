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

filename = os.path.join(scriptpath, 'diet.pdf')



tables = []
tables.append(camelot.read_pdf(filename, table_regions=['81,720,145,232']))
tables.append(camelot.read_pdf(filename, table_regions=['142,720,206,232']))
tables.append(camelot.read_pdf(filename, table_regions=['203,720,275,232']))
tables.append(camelot.read_pdf(filename, table_regions=['270,720,344,232']))
tables.append(camelot.read_pdf(filename, table_regions=['338,720,416,232'], copy_text=['h']))
tables.append(camelot.read_pdf(filename, table_regions=['411,720,483,232'], copy_text=['h']))
tables.append(camelot.read_pdf(filename, table_regions=['478,720,542,232']))

print(len(tables))

for i in range(len(tables)):
    tables[i][0].df.replace('', np.nan , inplace=True)

    # print(tables[i][0].df[0:15])
    tables[i][0].df['res'] = tables[i][0].df[0:15].dropna(axis=1, thresh=7)
    print(tables[i][0].df['res'])    
    # print(tables[i][0].df)

# tables[0][0].df.replace('', np.nan , inplace=True)
# resTable = tables[0][0].df.dropna(axis=1, thresh = 5)
# print(resTable)

# colCnt = len(tables[0][0].df.columns)

# if colCnt > 1 :
#     print(colCnt)

weekend = camelot.read_pdf(filename, table_regions=['80,217,542,109'])
print(weekend[0].df)
# for i in range(0, len(tables)):
#     print(tables[i][0].df[0])
#     print('------------')

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

식사종류 = ["메뉴", "식수", "후식"]



for i in range(len(식당)):
    if i < 2 :
        시간 = "아침"
    elif 2<= i <5 :
        시간 = "점심"
    else :
        시간 = "저녁"
    j = 0
    for 요일 in 요일배열[:5]:
        for 종류 in 식사종류:
            dict[요일][시간][식당[i]][종류] = str(tables[i][0].df['res'][j]).split('\n')
            j = j+1

for i in range(3):
    if i == 0 : 
        시간 = "아침"
        식당 = "KOREAN1"
    elif i == 1 :
        시간 = "점심"
        식당 = "KOREAN"
    else :
        시간 = "저녁"
        식당 = "KOREAN1"
    j=0
    for 요일 in 요일배열[-2:]:
        for 종류 in 식사종류[:2]:
            dict[요일][시간][식당][종류] = weekend[0].df[i][j].split('\n')
            j += 1

dictTojson = json.dumps(dict, ensure_ascii=False)
print(dictTojson)
with open('api/diet.json', 'w', encoding='utf-8') as make_file:
    json.dump(dict, make_file, ensure_ascii=False, indent='\t')
