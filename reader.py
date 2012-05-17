import json
import signal_strength

with open("out.txt", 'a') as f:
    while True:
        a = signal_strength.get_avg_signals_dict()
        f.write(json.dumps(a))
        f.write("\n")
