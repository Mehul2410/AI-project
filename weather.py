def temp(json_data):
    temprature = round(json_data['main']['temp']-273,1)
    return str(temprature) + ' degree celcius'

def des(json_data):
    description = json_data['weather'][0]['description']
    return description

