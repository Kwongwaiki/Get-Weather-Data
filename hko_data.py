import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from pathlib import Path

def getData(startYear, endYear):
    recordList = []
    for index in range(startYear, endYear):
        year = str(index)
        print('Progress: ' + year)
        xml = 'https://www.hko.gov.hk/cis/dailyExtract/dailyExtract_'+year+'.xml'
        response = requests.get(xml)
        xml_content = response.text
        json_content = json.loads(html_content)
        for data in json_content['stn']['data']:
            month = str(data['month']).zfill(2)
            date = year+','+month+','
            for dayData in data['dayData']:
                if not(dayData[0] in ['Mean/Total','Normal']):
                    dayNum = (datetime.strptime(year+month+dayData[0], "%Y%m%d")).strftime("%j")
                    record = date+dayData[0]+','+dayNum+','+((",".join(dayData[1:])).replace(" ", "")).replace("Trace", "0.05")
                    recordList.append(record)
    return recordList

def dataTxt(outFile, dataList):
    with open(outFile, 'w') as fp:
        fp.write('\n'.join(dataList))
        print('Exported to: ' + outFile)
    
if __name__ == '__main__':
    yearData = []
    print("Inputs: [Year]")
    startYear = int(input("Start from (min: 1884): ").strip() or datetime.today().year)
    endYear = int(input("End in (max: current): ").strip() or datetime.today().year)
    if endYear > datetime.today().year:
        endYear = datetime.today().year + 1
    else:
        endYear += 1
    yearData = getData(startYear, endYear)
    txtDir = str(input("TxT output file name (no extension): "))
    txtDir = str(Path().absolute()) + '/' + txtDir + '.txt'
    dataTxt(txtDir, yearData)
    
    