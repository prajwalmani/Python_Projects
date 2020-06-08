'''
A small python script to create instagram quotes images by reterving from the google sheets
if u want just image creattion remove  gsheetsauthorization() and  gsheetsretrival() functions
if you are using gsheets APi then dont forget to enable the API services
'''
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from PIL import Image, ImageDraw, ImageFont
import datetime
def gsheetsauthorization():
    '''
     function to pass particular credentials for google api for more info please read the docs
    credential are given in json format which you need to download and  link to your project
    :return:
    '''
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('responses').sheet1
    return sheet


def gsheetsretrival(sheet, rowvalue):
    '''
    function to retrive data from the gsheets
    gsheet contains 3 columns that is singername,lyrics,instagramid
    :param sheet:
    :param rowvalue:
    :return:
    '''
    instagramid = sheet.cell(rowvalue, 2).value
    singername = sheet.cell(rowvalue, 3).value
    lyrics = str(sheet.cell(rowvalue, 4).value)
    if len(instagramid) == 0:
        return [0, singername, lyrics]
    else:
        return [instagramid, singername, lyrics]


def drawimage(list):
    '''
    function to create the text on the image u can change few values based on your need
    font used in insta story is into repo
    :param list:
    :return:
    '''
    singername = str(list[1])
    lyric = str (list[2])
    lyrics = lyric + "-" + singername
    x1 = 612
    y1 = 612
    font = ImageFont.truetype(r'C:\Users\prajw\PycharmProjects\ghhets\Aveny.ttf', 40)
    img = Image.new('RGB', (x1, y1), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    sum = 0
    for letter in lyrics:
        sum += draw.textsize(letter, font=font)[0]
    average_length_of_letter = sum / len(lyrics)
    number_of_letters_for_each_line = (x1 / 1.618) / average_length_of_letter
    incrementer = 0
    fresh_sentence = ''
    for letter in lyrics:
        if (letter == '-'):
            fresh_sentence += '\n\n' + letter
        elif (incrementer < number_of_letters_for_each_line):
            fresh_sentence += letter
        else:
            if (letter == ' '):
                fresh_sentence += '\n'
                incrementer = 0
            else:
                fresh_sentence += letter
        incrementer += 1
    dim = draw.textsize(fresh_sentence, font=font)
    x2 = dim[0]
    y2 = dim[1]
    qx = (x1 / 2 - x2 / 2)
    qy = (y1 / 2 - y2 / 2)
    draw.text((qx, qy), fresh_sentence, align="center", font=font, fill=(100, 100, 100))
    img.save('lyrics.png')
    if datetime.datetime.today().weekday() ==0:
        f=open('buffer.txt','w')
    else:
        f = open('buffer.txt', 'a')
    for ele in list:
        f.write(str(ele) )


sheet = gsheetsauthorization()
for i in range(2, 3):
    retrivedlist = gsheetsretrival(sheet, i)
    drawimage(retrivedlist)
    sheet.delete_rows(i)
