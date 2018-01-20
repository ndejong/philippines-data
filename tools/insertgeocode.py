#!/usr/bin/env python3

import os
import sys
import csv
import json
import hashlib
import requests


class InsertGeocodeException(Exception):
    pass


class InsertGeocode():

    jsonfile = None
    google_geocode_url='https://maps.googleapis.com/maps/api/geocode/json'
    cache_path = '/tmp/geocode-cache'

    def __init__(self, jsonfile=None):
        if not os.path.isfile(jsonfile):
            raise InsertGeocodeException('file not found', jsonfile)
        self.jsonfile = jsonfile

    def main(self):
        data = None
        with open(self.jsonfile, 'r') as json_file:
            data = json.load(json_file)

        for index, item in enumerate(data):
            address = self.generate_geocode_lookup_address(item)
            #print('{}'.format(address))

            geocode_data = self.get_cached(key=address)
            if geocode_data is None:
                geocode_data = self.save_cached(key=address, data=self.get_geocode_data(address))
            data[index]['google_geocode'] = geocode_data

        print(json.dumps(data))

    def get_cached(self, key):
        cache_file = self.generate_cache_filename(key)
        if not os.path.isfile(cache_file):
            return None
        data = None
        with open(cache_file, 'r') as f:
            data = json.load(f)
        return data

    def save_cached(self, key, data):
        cache_file = self.generate_cache_filename(key)
        with open(cache_file, 'w') as f:
            f.write(json.dumps(data))
        return data

    def get_geocode_data(self, address):
        r = requests.get(self.google_geocode_url, params = {'address': address})
        if r.status_code != 200:
            raise InsertGeocodeException('geocode request did not return http-200', address)
        data = json.loads(r.text)
        if 'status' not in data:
            raise InsertGeocodeException('geocode request return data has no status value', address)
        if data['status'] != 'OK':
            raise InsertGeocodeException('geocode request return status is not OK', [address, data['status']])
        return data['results']

    def generate_cache_filename(self, key):
        return os.path.join(self.cache_path, format(hashlib.md5(key.encode('utf-8')).hexdigest()))

    def generate_geocode_lookup_address(self, item):
        return '{}, {}, {}, Philippines'.format(item['city_municipality'], item['province'], item['region_name'],)

InsertGeocode(sys.argv[1]).main()

