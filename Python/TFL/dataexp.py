import json

path = "response2.json"

with open(path, 'r') as f:
    data = f.read()
    data = json.loads(data)

for bus in sorted(data, key=lambda x: x["timeToStation"]):
    print(
        bus["lineName"],
        "→",
        bus["destinationName"],
        "in",
        bus["timeToStation"] // 60,
        "min"
    )

# * The important information from response2.json of each of the 6 objects is:
#  1- vehicleId  -> Number plate
#  2- stationName -> The station that has been asked for
#  3- destinationName -> Where that bus will go next
#  4- timeToStation -> Time to reach the asked station
#  5- modeName -> Vehicle type like a 'bus'
