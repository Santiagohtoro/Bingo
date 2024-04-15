import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.parse import parse_qs
import random
from channels.db import database_sync_to_async
from .models import User

class BingoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        
        
        # Join room group
        await self.channel_layer.group_add(self.room_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
        

    
class BingoNumber(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        
        
        # Join room group
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()
        asyncio.ensure_future(self.send_number())

    

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
    
    async def send_number(self):
        while True:
                # Generate a random number
                random_number = random.randint(1, 75)

                # Send the random number to the room group
                await self.channel_layer.group_send(
                    self.room_name, {"type": "chat.message", "message": str(random_number)}
                )
                # Wait for 10 seconds before sending the next random number
                await asyncio.sleep(10)
        # Receive message from room group
   
    
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
    