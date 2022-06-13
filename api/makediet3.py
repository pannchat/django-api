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
test = camelot.read_pdf(filename, table_regions=[
    '348, 1678, 2140, 1479',
    '348, 1509, 2153, 1415',
    '348, 1446, 2138, 1250',
    '348, 1274, 2135, 1191',
    '348, 1214, 2136, 1052',
    '348, 927, 2136, 771',
    '348, 800, 2136, 690',
    '348, 711, 2136, 669',
    '348, 684, 2136, 644',
    '348, 658, 2136, 438',
    '348, 458, 2136, 260'
    ])


# for i in range(len(test[0].df)):
#     print(test[0].df[i])

print(test[0].df)
print(test[1].df)

# for i in test2:
#     print(i)
    
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
