import json
import requests

import argparse
import sys
import operator

# parse input args as ami-name
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', type=str, required=True)
args = vars(parser.parse_args())

api_url = "http://spot-price.s3.amazonaws.com/spot.js"

def getSpots(machine_type, api_url):
    print "Loading spots for Machine Type: {} ...".format(machine_type)
    
    res = requests.get(api_url)
    cleaned = res.content[len('callback('):-len(');')]
    result = json.loads(cleaned)
    
    # get all spots by region
    reg_machine_spots = {
        region['region']:{
            size['size']: [
                os['prices']['USD'] 
                for os in size['valueColumns'] if os['name']=='linux'
            ][0] 
            for it in region['instanceTypes'] for size in it['sizes']
        }
        for region in result['config']['regions']
    }
    
    # get all regional spots
    try:
        ami_spots = {
            region: prices[machine_type] 
            for region,prices in reg_machine_spots.iteritems()
        }
    except KeyError:
        print "Machine Type: {} doesn't exist!".format(machine_type)
        sys.exit()
    
    # print the prices sorted lowest first
    ami_spots = sorted(ami_spots.items(), key=operator.itemgetter(1))
    for reg,spot in ami_spots: print reg.ljust(15) + spot
    pass

if __name__ == '__main__':
    if 'type' in args: 
        machine_type = args['type']
        getSpots(machine_type, api_url)
    