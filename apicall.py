import requests
import base64
import json
import traceback
import os

def main():

    with open("./download.png", "rb") as image_file:
      image_string = base64.b64encode(image_file.read())

    endpoint = "http://127.0.0.1:8000/predict/image"
    json_data = {"instance": image_string.decode('utf-8'),}
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    result = requests.post(endpoint, json=json_data, headers=headers)
    if os.path.isfile('image_temp.txt'):
        os.remove('image_temp.txt')
    with open('image_temp.txt',"wb") as file:
       file.write(image_string)
    print(result.json())

if __name__ == "__main__":
  main()