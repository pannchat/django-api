from tokenize import String
from django.shortcuts import render
import camelot
import os.path
import json
# from django.utils import simplejson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import cv2
import os
import glob
from pdf2image import convert_from_path


scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'bread2.pdf')
tables = camelot.read_pdf(filename)
arr = []
dateArr = []
for i in range(1,20):
    for j in range(9):
        if(tables[0].df[j][i] != '' and not tables[0].df[j][i].isdigit() and tables[0].df[j][i].find(')') == -1):
            arr.append(tables[0].df[j][i])
            dateArr.append(tables[0].df[j][i-1])
        # if(tables[0].df[j][i] != '' and tables[0].df[j][i].isdigit()):
        #     dateArr.append(tables[0].df[j][i])

print(tables[0].df)
print(arr)
print(dateArr)

bread = {
    "bread" : []
}
for idx,b in enumerate(arr):
    bread["bread"].append({"id":dateArr[idx], "name" : b, "img" : "/static/bread/"+str(idx+1)+".jpg"})


with open('api/bread.json','w',encoding='utf-8') as make_file:
    json.dump(bread, make_file, ensure_ascii=False, indent='\t')

# print(tables[0].df[0])
# print(tables[0].df)
# scriptpath = os.path.dirname(__file__)
# filename = os.path.join(scriptpath, 'bread.jpg')
# tables = camelot.read_pdf(filename)


if os.access(filename, os.F_OK) == True:
    images = convert_from_path(filename, fmt='jpg',output_folder='tmp')

    for image in images:
        print(image.filename)
else:
    print("오류")

testRead = cv2.imread(image.filename, cv2.IMREAD_COLOR)
test_cut = testRead[826:1190, 60:348]
cnt = 1
for i in range(5):
    for j in range(5):
        test_cut = testRead[556+363*i:824+363*i, 62+ 292*j:345 + 292*j]
        cv2.imwrite('api/static/bread/'+ str(cnt-4) + '.jpg',test_cut,params=[cv2.IMWRITE_JPEG_QUALITY,100])
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        cnt = cnt + 1




