from cmath import nan
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
import numpy as np


scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'bread2.pdf')
tables = camelot.read_pdf(filename)
arr = []
dateArr = []
# print(tables[0].df)
res = tables[0].df.replace('', np.nan , inplace=True)
res = tables[0].df.dropna(axis=1, thresh = 5)



# print(tables[0].df)


res = res.values.tolist()
print(res)
for i in range(1,len(res)):
    for j in range(5):
        if(str(res[i][j]) != 'nan' and not str(res[i][j]).isdigit() and str(res[i][j]).find(')') == -1):
            arr.append(res[i][j])
            dateArr.append(res[i-1][j])
        # if(res[j][i] != '' and tables[0].df[j][i].isdigit()):
        #     dateArr.append(tables[0].df[j][i])

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
# test_cut = testRead[600:600+272,155:155+296]
# cv2.imshow('Gray scale',test_cut)
# cv2.waitKey()
# cv2.destroyAllWindows()
cnt = 1
for i in range(5):
    for j in range(5):
        test_cut = testRead[600+361*i:860+361*i, 155+297*j:453+297*j]
        cv2.imwrite('api/static/bread/'+ str(cnt) + '.jpg',test_cut,params=[cv2.IMWRITE_JPEG_QUALITY,100])
        # cv2.imshow('Gray scale',test_cut)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        cnt = cnt + 1




