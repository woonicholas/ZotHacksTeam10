import facebook


def sort_time(a,b)
	return a["time"] < b["time"]

def sort_data(data):
	return sorted(data,key = sort_time,reverse = True)




return_json = json.dumps(process(get_posts()))
file=open("social_media_data.json", "w")
file.write(return_json)
file.close()