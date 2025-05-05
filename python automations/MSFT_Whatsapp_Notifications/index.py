import requests

# -----------------Configuration ---------------------#
client_id = ""
client_secret =""
phone_id_from = ""
phone_id_to = ""
token =""
#------------------get access token -----------------#

def get_accesstoken()->str:
    params = {
    'client_id':     client_id,
    'client_secret': client_secret,
    'grant_type':    'client_credentials'
    }
    response = requests.get("https://graph.facebook.com/oauth/access_token",params=params)
    response.raise_for_status
    access_token = response.json()['access_token']
    return access_token
    
token = get_accesstoken()

url = f"https://graph.facebook.com/v16.0/{phone_id_from}/messages"

headers = {
  "Authorization": f"Bearer {token}",
  "Content-Type": "application/json"
}
payload = {
  "messaging_product": "whatsapp",
  "to": phone_id_to,
  "type": "template",
  "template": {
      "name": "hello_world",
      "language": { "code": "en_US" }
    }
}

resp = requests.post(url, json=payload, headers=headers)
print(resp.status_code, resp.json())
