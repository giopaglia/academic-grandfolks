import json
import requests

# Number of generations to run
N = 40

url = "https://github.com/j2kun/math-genealogy-scraper/raw/main/data.json"
data = requests.get(url=url).json() # Check the JSON Response Content documentation below
# data = json.load(open("data.json", "r"))

d = {}
for v in data["nodes"]:
	d[v["id"]] = v

print(f"{len(d)} entries retrieved.")

my_ancestors = {}

# Setup starting state
my_ancestors[120829] = 2
my_ancestors[120747] = 2

# Run for N generations
for _gen in range(0,N):
	new_my_ancestors = {}
	for id, gen in my_ancestors.items():
		for parid in d[id]["advisors"]:
			if parid not in new_my_ancestors.keys():
				if not parid in d.keys():
					print(f"Advisor not found: {parid}")
				else:
					new_my_ancestors[parid] = gen+1
	my_ancestors = dict(list(new_my_ancestors.items()) + list(my_ancestors.items()))

ancs = list(my_ancestors.items())
ancs.sort(key = lambda x : x[1])

# ancs.sort(key = lambda x : len(d[x[0]]["students"])) # Sort by # of students
for id,gen in ancs:
  print(d[id]["name"], f"({gen})")

