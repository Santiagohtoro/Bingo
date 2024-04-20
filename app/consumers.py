import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.parse import parse_qs
import random
from channels.db import database_sync_to_async
from .models import User
from .funciones import * 

class BingoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        
        
        
        await self.channel_layer.group_add(self.room_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

   
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        
        await self.channel_layer.group_send(
            self.room_name, {"type": "chat.message", "message": message}
        )

    
    async def chat_message(self, event):
        message = event["message"]

        
        await self.send(text_data=json.dumps({"message": message}))
        

    
class BingoNumber(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        
        
        
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()
        asyncio.ensure_future(self.send_number())

    

    async def disconnect(self, close_code):
      
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
    
    async def send_number(self):
        
        balotas=simulador_bingo()
        for i in balotas:
        
            await self.channel_layer.group_send(
                self.room_name, {"type": "chat.message", "message": f"{i}"}
                )
            await asyncio.sleep(10)
      
   
    
    async def chat_message(self, event):
        message = event["message"]

     
        await self.send(text_data=json.dumps({"message": message}))
    