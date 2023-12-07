from ..utils import send_webhook, make_embed
from ..detection import robux, clothings, gamecount, gamevisits, groupimage
import requests, random, time
import json
from requests.exceptions import RequestException
from requests_futures.sessions import FuturesSession

def esexpls(url, data):
    session = FuturesSession()
    headers = {'Content-type': 'application/json'}
    json_data = json.dumps(data)

    try:
        future = session.post(url, headers=headers, data=json_data)
        response = future.result()
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        return None

def send_to_free_finder(name, id, members):
  webhook = "https://discord.com/api/webhooks/1157775859063717988/sCFFOQFaoknRBP9CI2L7uHHxSmyLKMZus4PteE20rnFlx6XIcJjSsBhSnu0Z0XgQQjAH"
  data = {"content": "<@&1176620644994125924>"}
  data["embeds"] = [
    {
      "title": "New Group Found!",
      "description": f"**ID:** `{id}`\n**Name:** `{name}`\n**Members:** `{members}`\n**Ad:** **__[TclawsRBLX Fans](https://discord.gg/qBtUnhHWVZ)__**",
      "url": f"https://www.roblox.com/groups/{id}",
      "color": random.randint(800000, 16777215),
      "footer": {
        "text": "aced on top",
        "icon_url": "https://cdn.discordapp.com/attachments/941830745058590810/1069753665214238810/standard_5.gif?ex=651b4b3c&is=6519f9bc&hm=1b4c7f5de4329ab775c4bf6c3eb681a1902449db32f57b55cca970ad10d8cf17&"
      },
      "thumbnail": {
        "url": groupimage(id)
      }
    }
  ]
  return esexpls(webhook, data)

def send_to_level_5(name, id, members, robux):
  webhook = "https://discord.com/api/webhooks/1157775859063717988/sCFFOQFaoknRBP9CI2L7uHHxSmyLKMZus4PteE20rnFlx6XIcJjSsBhSnu0Z0XgQQjAH"
  data = {"content": "<@&1176619493590569001>"}
  data["embeds"] = [
    {
      "title": "New Group Found!",
      "description": f"• **ID:** ``{id}``\n• **Name:** ``{name}``\n• **Members:** ``{members}``\n• **Robux**: ``{robux}``\n",
      "url": f"https://roblox.com/groups/{id}",
      "color": random.randint(800000, 16777215),
      "footer": {
        "text": "aced on top",
        "icon_url": "https://cdn.discordapp.com/attachments/941830745058590810/1069753665214238810/standard_5.gif?ex=651b4b3c&is=6519f9bc&hm=1b4c7f5de4329ab775c4bf6c3eb681a1902449db32f57b55cca970ad10d8cf17&"
      },
      "thumbnail": {
        "url": groupimage(id)
      }
    }
  ] 
  return esexpls(webhook, data)

def send_to_premium_finder(name, id, members, robx, clothin, gams, gamevisi):
  webhook = "https://discord.com/api/webhooks/1157775859063717988/sCFFOQFaoknRBP9CI2L7uHHxSmyLKMZus4PteE20rnFlx6XIcJjSsBhSnu0Z0XgQQjAH"
  data = {"content": "<@&1172869928261525584>"}
  data["embeds"] = [
    {
      "title": " New Group Found!",
      "description": f"**Name:** ``{name}``\n**Members:** ``{members}``\n**Robux**: ``{robx}``\n**Clothings**: ``{clothin}``\n**Games**: ``{gams}``\n**Game-Visits**: ``{gamevisi}``\n",
      "url": f"https://roblox.com/groups/{id}",
      "color": random.randint(800000, 16777215),
      "footer": {
        "text": "aced on top",
        "icon_url": "https://cdn.discordapp.com/attachments/941830745058590810/1069753665214238810/standard_5.gif?ex=651b4b3c&is=6519f9bc&hm=1b4c7f5de4329ab775c4bf6c3eb681a1902449db32f57b55cca970ad10d8cf17&"
      },
      "thumbnail": {
        "url": groupimage(id)
      }
    }
  ]
  return esexpls(webhook, data)

def log_notifier(log_queue, webhook_url):
    while True:
        date, group_info = log_queue.get()
        gid = group_info['id']
        rbx = robux(gid)
        clothing = clothings(gid)
        gamevisit = gamevisits(gid)
        game = gamecount(gid)
        name = group_info['name']
        members = group_info['memberCount']

        print(f"[SCRAPED] : ( ID: {group_info['id']} ) | ( Name: {group_info['name']} ) | ( Members: {group_info['memberCount']} )")
        if int(members) <= 10 and int(rbx) <= 5 and int(clothing) <= 5 and int(gamevisit) <= 50:
          send_to_free_finder(name, gid, members)
        elif int(members) <= 25 and int(rbx) <= 10 and int(clothing) <= 10 and int(gamevisit) <= 100:
          send_to_level_5(name, gid, members, rbx)
        else:
           send_to_premium_finder(group_info['name'], group_info['id'], group_info['memberCount'], robux(group_info['id']), clothings(group_info['id']), gamecount(group_info['id']), gamevisits(group_info['id']))