#!/usr/bin/env python3

import os
import sys
import csv
import json

class CsvToJsonException(Exception):
    pass

class CsvToJson():

    csvfile = None

    def __init__(self, csvfile=None):
        if not os.path.isfile(csvfile):
            raise CsvToJsonException('file not found', csvfile)
        self.csvfile = csvfile

    def main(self):
        header = []
        data = []
        with open(self.csvfile, 'r') as f:
            rows = csv.reader(f, delimiter=',', quotechar='"')
            for row in rows:
                if len(header) == 0:
                    header = row
                else:
                    data_item = {}
                    for row_index, item in enumerate(row):
                        data_item[header[row_index]] = item
                    data.append(data_item)

        print(json.dumps(data))

CsvToJson(sys.argv[1]).main()

