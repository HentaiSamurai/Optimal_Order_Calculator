import gspread
import json

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials 

g_credential = None
SPREADSHEET_KEY = None
spreadsheet = None

def init():
    global g_credential
    global SPREADSHEET_KEY
    global spreadsheet
    #2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    #認証情報設定
    #ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
    credentials = ServiceAccountCredentials.from_json_keyfile_name('../Resources/Key/optimal-order-calculator-3e6b3fb3b701.json', scope)

    #OAuth2の資格情報を使用してGoogle APIにログインします。
    g_credential = gspread.authorize(credentials)
    
    #共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
    SPREADSHEET_KEY = get_spreadsheet_key()

    spreadsheet = g_credential.open_by_key(SPREADSHEET_KEY)

def get_spreadsheet_key():
	with open('../sheet.txt') as fp:
		key = fp.readline()
	return key

def add_worksheet(title, rows=1, cols=1):
    spreadsheet.add_worksheet(title=title, rows=rows, cols=cols)

def append_row(sheet_title, data):
    sheet = spreadsheet.worksheet(sheet_title)
    sheet.append_row(data)

def delete_row(sheet_title, row):
    sheet = spreadsheet.worksheet(sheet_title)
    sheet.delete_rows(row)    

def find_row(sheet_title, value, col=0):
    sheet = spreadsheet.worksheet(sheet_title)
    if col > 0:
        values = sheet.col_values(col)
        if value in values:
            return values.index(value) + 1
    else:
        cell = sheet.find(value)
        if cell is not None:
            return cell.row
    return 0

def update_cell(sheet_title, row, col, value):
    sheet = spreadsheet.worksheet(sheet_title)
    sheet.update_cell(row, col, value)

def test():
    #共有設定したスプレッドシートのシート1を開く
    worksheet = g_credential.open_by_key(SPREADSHEET_KEY).sheet1

    #A1セルの値を受け取る
    import_value = int(worksheet.acell('A1').value)

    #A1セルの値に100加算した値をB1セルに表示させる
    export_value = import_value+100
    worksheet.update_cell(1,2, export_value)

init()