# schedule={}
# schedule["RIS"]=["09:00","10:00"]
# schedule["ANG"]=["09:30","10:30"]
# schedule["MAT"]=["10:00","11:00"]
# schedule["INF"]=["10:30","11:30"]
# schedule["MUZ"]=["11:00","12:00"]
#
# print(schedule)

stations = {}
stations["kone"] =set(["id", "nv", "ut"])
stations["ktwo"] =set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "са"])
stations["kfour"] =set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
states_needed = set( [ "mt", "wa", "or", "id", "nv", "ut", "са", "az"] )

final_stations=set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)


print(final_stations)