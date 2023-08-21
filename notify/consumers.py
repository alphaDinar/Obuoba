from channels.generic.websocket import AsyncWebsocketConsumer
import json

class HomeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'home'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        self.channel_layer.group_discard(self.group_name, self.channel_name)
        print(close_code)

    async def receive(self, text_data):
        await self.send(text_data=json.dumps({
            'message' : 'kong'
        }))
        print(text_data)

    # async def food_update(self):
    #     await self.channel_layer.group_send(self.group_name ,{
    #         'type' : 'food_handler',
    #         'message' : 'New Food generated'
    #     })
        
    async def food_handler(self,event):
        message = event['message']
        await self.send(json.dumps({
            'message' : message
        }))