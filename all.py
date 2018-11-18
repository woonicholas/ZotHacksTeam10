import facebook
import TwitterMain
import json



def sort_time(a,b):
	return a["time"] < b["time"]
#must add data json lists together before calling sort data
def sort_data(data):
	return sorted(data,key = lambda x: x["time"],reverse = True)

fb_data = facebook.process(facebook.get_posts())
tw_data = TwitterMain.process()
TwitterMain.changeTimes(tw_data)

final = {"data": sort_data(fb_data + tw_data)}

return_json = json.dumps(final)
file=open("social_media_data.json", "w")
file.write(return_json)
file.close()