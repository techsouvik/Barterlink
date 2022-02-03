import subprocess
import os
import sys 
import json 
from copy import deepcopy  
import PinataAPIKey as Pinata
from Naked.toolshed.shell import muterun_js

api_key = Pinata.keys()['api_key']
api_scret = Pinata.keys()['api_scret']
jwt_token = Pinata.keys()['jwt_token']

#create environment variables
os.environ['PINATA_API_KEY'] = api_key
os.environ['PINATA_API_SECRET'] = api_scret
os.environ['PINATA_JWT_TOKEN'] = jwt_token

img_path = sys.argv[1]
metadata_path = sys.argv[2]

print("img_path: ", img_path)
print("metadata_path: ", metadata_path)

node_path = 'C:/Users/bhaga/AppData/Roaming/npm'
f=open(metadata_path, 'r')
base_metadata = json.load(open(metadata_path))
metadata_hashes = json.load(f)
metadata_hashes[img_path] = []

def pin_img_to_pinata(img_path):
    res = muterun_js('./pinImgToPinata.js', img_path)
    ipfs_hash = res.stdout.decode().strip()
    return ipfs_hash

# def pin_metadata_to_pinata(img_ipfs_hash, edition_index):
#     metadata = deepcopy(base_metadata)
#     metadata['image'] = base_metadata['image'] + img_ipfs_hash
#     metadata['attributes'].append({'display_type': 'number', 'trait_type': 'Edition', 'max_value': 10, 'value': edition_index + 1})
#     metadata_ipfs_hash = subprocess.check_output([node_path, './_pinMetadataToPinata.js', json.dumps(metadata), str(edition_index+1)])
#     return metadata_ipfs_hash.decode().strip()

img_ipfs_hash = pin_img_to_pinata(img_path)

# for i in range(0, base_metadata['total_editions']):
#     metadata_hash = pin_metadata_to_pinata(img_ipfs_hash, i)
#     metadata_hashes[img_path].append(metadata_hash)
#     print(f'Edition: {i+1}; Metadata Hash: {metadata_hash}')

# json.dump(metadata_hashes, open('./metadata_hashes.json', 'w'))
print("Done")
print(img_ipfs_hash)