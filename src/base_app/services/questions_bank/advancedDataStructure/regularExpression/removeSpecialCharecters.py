import pandas as pd
import re


def removeSpecialCharInCSV_Header(fileName="../fileHandling/src_file/input_CSV.csv"):
    data = pd.read_csv(fileName)
    for row in data:
        print(row)
        print(type(row))
    # print(data)
    # print(type(data))

removeSpecialCharInCSV_Header()


def removeSpecialChar_re(str1 = "Special $#! characters   spaces 88832,:;,3"):
    # str2 = re.sub(r"[^a-zA-Z0-9]","",str1).lower()
    str2 = re.sub(r"[^a-zA-Z0-9,:;]", "", str1).lower()
    print(str2)
    print(str2.count("a"))


def removeSpecialChar_basics(str1 = "Special $#! characters   spaces 888323"):
    print("str1 original : ", str1)
    print (''.join(e for e in str1 if e.isalnum()))


def removeSpecialChar_filter(str1 = "Special $#! characters   spaces 888323"):
    print(filter(str.isalnum, str1))


def processReg(str1="atul@gmail.com, Atul , Anand, atul@g.com 353845kjgfgg2546%&%#^&"):
    lst1 = re.findall('[0-9]+', str1)
    lst2 = re.findall('\S+@\S+', str1)
    print("lst1", lst1)
    print("lst2", lst2)

# removeSpecialChar()
# removeSpecialCharInCSV()
removeSpecialChar_re()
removeSpecialChar_basics()
removeSpecialChar_filter()
processReg()
