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
tables.append(camelot.read_pdf(filename, table_regions=['338,720,418,232'], copy_text=['h']))
tables.append(camelot.read_pdf(filename, table_regions=['411,720,483,232'], copy_text=['h']))
tables.append(camelot.read_pdf(filename, table_regions=['478,720,542,232'], copy_text=['h']))

print(len(tables))

for i in range(len(tables)):
    print(tables[i][0].df)
    tables[i][0].df.replace('', np.nan , inplace=True)
    tables[i][0].df['res'] = tables[i][0].df[0:len(tables[i][0].df)].dropna(axis=1, thresh=7)
    # print(tables[i][0].df['res'])
    # print(tables[i][0].df)

# tables[0][0].df.replace('', np.nan , inplace=True)
# resTable = tables[0][0].df.dropna(axis=1, thresh = 5)
# print(resTable)

# colCnt = len(tables[0][0].df.columns)

# if colCnt > 1 :
#     print(colCnt)

weekend = camelot.read_pdf(filename, table_regions=['80,264,546,142'])
# weekend = weekend[0].df[1]
weekend = (weekend[0].df[2:6].drop(labels=0, axis=1))
weekend = weekend.reset_index(drop=True)
weekend = weekend.values.tolist()

print(weekend)

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



for i in range(len(tables)):
    if i < 2 :
        시간 = "아침"
    elif 2<= i <5 :
        시간 = "점심"
    else :
        시간 = "저녁"

    j = 0
    for 요일 in 요일배열[:5]:
        for 종류 in 식사종류:            
            try:
                tmp = str(tables[i][0].df['res'][j]).split('\n')
                if tmp[0] == 'nan':
                    del tmp[0]
                dict[요일][시간][식당[i]][종류] = tmp
            except:
                dict[요일][시간][식당[i]][종류] = []
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
            try:
                tmp = weekend[j][i].split('\n')
                if tmp[0] == 'nan':
                    del tmp[0]
                elif tmp[0] =='':
                    del tmp[0]
                dict[요일][시간][식당][종류] = tmp
            except:
                dict[요일][시간][식당][종류] = []
            j += 1

dictTojson = json.dumps(dict, ensure_ascii=False)
# print(dictTojson)
with open('api/diet.json', 'w', encoding='utf-8') as make_file:
    json.dump(dict, make_file, ensure_ascii=False, indent='\t')
[
    ['김치찌개\n쌀밥\n김치볶음/도시락김\n계란후라이\n요구르트\n연근조림','제육볶음\n쌀밥\n시금치된장국\n쥐어채볶음\n마늘종지무침\n도시락김\n배추김치', '쇠고기대파해장국\n쌀밥\n미트볼조림\n다시마튀각\n호박나물\n도시락김\n깍두기'], 
    ['식수/칼로리(5/800Kcal)', '식수/칼로리(10/911Kcal)', '식수/칼로리(10/825Kcal)'],
    ['사골곰탕\n쌀밥\n김치볶음/도시락김\n계란후라이\n요구르트\n근대나물', '카레라이스\n유부맑은국\n꼬마돈가스&케찹\n단무지\n도시락김\n배추김치', '간장오리주물럭\n쌀밥\n고추장찌개\n얼갈이생채\n무나물\n도시락김\n열무김치'], 
    ['식수/칼로리(5/819Kcal)', '식수/칼로리(10/916Kcal)', '식수/칼로리(10/924Kcal)']]