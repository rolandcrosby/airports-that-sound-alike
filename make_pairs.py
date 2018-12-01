import csv

airports = {}
with open('airports.csv') as f:
    # 1,"Goroka Airport","Goroka","Papua New Guinea","GKA","AYGA",-6.081689834590001,145.391998291,5282,10,"U","Pacific/Port_Moresby","airport","OurAirports"
    r = csv.reader(f)
    for l in r:
        airports[l[0]] = l

pairs = set()
with open('routes.csv') as f:
    # 2B,410,AER,2965,KZN,2990,,0,CR2
    r = csv.reader(f)
    for l in r:
        from_id, to_id = l[3], l[5]
        from_code, to_code = l[2], l[4]
        if from_id in airports and to_id in airports:
            from_city, to_city = airports[from_id][2], airports[to_id][2]
            if from_city > to_city:
                from_id, to_id = to_id, from_id
                from_city, to_city = to_city, from_city
                from_code, to_code = to_code, from_code
            pairs.add((from_code, to_code, from_city, to_city))

pairs = sorted(list(pairs), key=lambda x: [x[2], x[3]])
with open('pairs.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(pairs)

