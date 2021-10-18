# main.py
import json
from fastapi import FastAPI
from pydantic import BaseModel
import requests

def send_request(new_data):
    host_router = 'http://uatomis.homecredit.vn:5000/'
    end_point_router = 'vnpost'
    url = host_router + end_point_router
    res = requests.post(url,json=new_data,proxies=proxy_dict)

app = FastAPI()

class Item(BaseModel):
    Data: str
    SendDate: str
    SignData: str

@app.post('/')
async def create_item(item: Item):
    
    data = item.Data
    data_dict = json.loads(data)
    new_data = {
        "Data" : data_dict['ItemCode']
    }
    send_request(new_data)
    return item