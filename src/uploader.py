import json
import csv
import xml.etree.ElementTree

def upload_xml(filename):
    root = ElementTree.parse(filename).getroot()
    for element in root.findall('event'):
        pass

def upload_json(filename):
    with open(filename, mode='r') as f:
        data = json.load(f)
        result = list(data.keys())
        for i in range(len(result)):
            try:
                result[i] = result[i].split("/")[2]
                if result[i].startswith('www'):
                    result[i] = result[i][3:]
            except:
                pass
        return result

def upload_csv(filename):
    result = []
    with open(filename, mode='r') as f:
        for line in f.readlines():
            line = line.split("\"")
            line = line[1].split('/')[2]
            result.append(line)
        return result

def upload_txt(filename):
    result = []
    with open(filename, mode='r') as f:
        for line in f.readlines():
            line = line.split('/')[2]
            result.append(line)
    return result

print(upload_json('../input.json'))
