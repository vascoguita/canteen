#!/usr/bin/python3

import requests
import datetime


today = datetime.datetime.today().date()

json = requests.get("https://fenix.tecnico.ulisboa.pt/api/fenix/v1/canteen").json()

for menu in json:
	if datetime.datetime.strptime(menu["day"], "%d/%m/%Y").date() == today:
		for meal in menu["meal"]:
            		print("======== {} {} ========".format(meal["type"], menu["day"]))
            		for info in meal["info"]:
                		print("===> {}".format(info["menu"]))
                		print("   {} > {}".format(info["type"], info["name"]))
