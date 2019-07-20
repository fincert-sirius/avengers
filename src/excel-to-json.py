from openpyxl import load_workbook
import json

def get_json_from_xls(filename):
    wb = load_workbook(filename)
    sheet = wb['Лист1']
    result = {}
    for row in sheet.rows:
        emails = str(row[1].value).split(' ')
        result[row[0].value] = emails
    return result

if __name__ == "__main__":
    with open('hosters.json', mode='w') as f:
        json.dump(get_json_from_xls('hosters.xlsx'), f)
    print('Done')

