import json
import requests


class BotController:
    def retrieve_messages(channelid):
        result = []
        headers = {
            'authorization': 'MTg5MDkxMDMwODc0NzE4MjA5.Gny4e9.XmN2LfvN3HDrpNTv5NDe1vZU6n7NBvPo4zcWMI'
        }
        r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages?limit=100', headers=headers)
        jsonn = json.loads(r.text)
        for value in jsonn:
            result.append(value['content'])
            print(value, '\n')

        return result
