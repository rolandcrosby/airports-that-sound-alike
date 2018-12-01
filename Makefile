pairs.csv: airports.csv routes.csv
	python make_pairs.py

airports.csv:
	curl https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat -o airports.csv

routes.csv:
	curl https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat -o routes.csv


