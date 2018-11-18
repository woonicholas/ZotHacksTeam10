def getNumMonth(month):
    if month=="Jan":
        return "01"
    elif month=="Feb":
        return "02"
    elif month=="Mar":
        return "03"
    elif month=="Apr":
        return "04"
    elif month=="May":
        return "05"
    elif month=="Jun":
        return "06"
    elif month=="Jul":
        return "07"
    elif month=="Aug":
        return "08"
    elif month=="Sep":
        return "09"
    elif month=="Oct":
        return "10"
    elif month=="Nov":
        return "11"
    else:
        return "12"

def makeFacebookTime(time):
    return time[-4:]+"-"+getNumMonth(time[4:7])+"-"+time[8:10]+"T"+time[11:19]+"+0000"
    
