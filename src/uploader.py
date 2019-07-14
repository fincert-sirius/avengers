import json
import csv
import xml.etree.ElementTree

def upload_xml(filename):
    root = ElementTree.parse(filename).getroot()
    for element in root.findall('event'):


def upload_json(filename):
    with open(filename, mode='r') as f:
        data = json.load(f)
        return data
    return []

def upload_csv(filename):
    result = []
    with open(filename, mode='r') as f:
    for line in f.readlines():
        line = line.split("/"")
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


