import json
import csv
import xml.dom.minidom

def upload_xml(filename):
    pass

def upload_json(filename):
    with open(filename, mode='r') as f:
        data = json.load(f)
        return data
    return []

def upload_csv(filename):
    pass

def upload_txt(filename):
    result = []
    with open(filename, mode='r') as f:
        for line in f.readlines():
            line = line.split('/')[2]
            result.append(result)
    return result


