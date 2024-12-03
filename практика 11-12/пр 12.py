import tkinter as tk
import json
import requests
rep_name = 'rust-lang/rust'
url = f'https://api.github.com/repos/{rep_name}'
resp = requests.get(url)
data = resp.json()
data = {
    'company': data['owner'].get('company'),
    'created_at': data.get('created_at'),
    'email': data['owner'].get('email'), 
    'id': data.get('id'),
    'url': data.get('html_url'),  
}

print(data)
with open('states.json', 'w') as f:
    json.dump(data, f, indent=5)
root = tk.Tk()
label = tk.Label(root, text='Информация о репозитории').pack(pady=10)
root.mainloop()