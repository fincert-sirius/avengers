from openpyxl import load_workbook

def get_json_from_xls(filename):
    wb = load_workbook(filename)
    sheet = wb['Лист1']
    result = {}
    for row in sheet.rows:
        emails = str(row[1].value).split(' ')
        result[row[0].value] = emails
    return result

print(get_json_from_xls('hosters.xlsx'))
