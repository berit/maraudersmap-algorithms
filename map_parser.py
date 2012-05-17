import json


router_dict = dict()

all_lines = []
with open("JulianRoom.txt") as f:
    all_lines = f.readlines()

line_count = len(all_lines)

for num, line in enumerate(all_lines):
    curr_dict = json.loads(line)
    for (router,signal) in curr_dict.iteritems():
        if router not in router_dict:
            router_dict[router] = [0]*line_count
        router_dict[router][num] = signal

with open("Data.csv", 'w') as f:
    for router, router_signals in router_dict.iteritems():
        f.write('%s,%s\n' % (router, ','.join([str(s) for s in router_signals])))
    
