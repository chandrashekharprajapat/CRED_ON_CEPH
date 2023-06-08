import requests
import json

endpoint_url = 'https://10.82.2.14:8443'
AUTHN_URL = '/api/auth'
CEPH_USER_URL = '/api/rgw/user'
CEPH_BUCKET_URL = '/api/rgw/bucket'
username = 'ashok'
password = 'India@14356'

def Auth(endpoint_url, username , password):
    headers = {
        "accept": 'application/vnd.ceph.api.v1.0+json',
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "username": username,
        "password": password
    })
    response = requests.post(endpoint_url + AUTHN_URL, verify=False, data=payload, headers=headers)
    response = json.loads(response.content)
    print(response)
    token = response['token']
    return token

token = Auth(endpoint_url, username, password)


def get_bucket(endpoint_url, token):
    new_headers = {
        'Authorization': f'Bearer {token}',
        "accept": 'application/vnd.ceph.api.v1.0+json',
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
     "username": "ashok",
      "password": "India@14356"
    })
    response = requests.get(endpoint_url+CEPH_BUCKET_URL, verify=False, data=payload, headers=new_headers)
    print(response.__dict__, "these are buckets")


get_bucket(endpoint_url, token)

def create_bucket(endpoint_url, token, bucket_name):
    headers = {
        'Authorization': f'Bearer {token}',
        "accept": 'application/vnd.ceph.api.v1.0+json',
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "bucket": bucket_name,
        "uuid": "test"
    })
    response = requests.post(endpoint_url + CEPH_BUCKET_URL, verify=False, data=payload, headers=headers)
    if response.status_code == 200:
        print(f"Bucket '{bucket_name}' created successfully!")
    else:
        print(f"Failed to create bucket. Error: {response.text}")

bucket_name = 'my_first_bucket'
create_bucket(endpoint_url, token, bucket_name)
get_bucket(endpoint_url,token)

def delete_bucket(endpoint_url,token,bucket_name):
    headers = {
        'Authorization': f'Bearer {token}',
        "accept": 'application/vnd.ceph.api.v1.0+json',
        'Content-Type': 'application/json'
    }

    response = requests.delete(endpoint_url + CEPH_BUCKET_URL + f'/{bucket_name}', verify=False,headers=headers)
    if response.status_code == 200:
        print(f"Bucket '{bucket_name}' delete successfully!")
    else:
        print(f"Failed to delete bucket. Error: {response.text}")
bucket_name='my_first_bucket'
delete_bucket(endpoint_url,token,bucket_name)
get_bucket(endpoint_url,token)

