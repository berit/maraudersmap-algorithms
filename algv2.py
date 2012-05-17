import numpy
from operator import itemgetter

# Dot product between two signal vectors (union of routers)
def nearest_binds(signals, limit = 10, **crit):
	signalsA = {k.lower(): v for k, v in signals.items()}
        crit['$or'] = []
	for k, v in signalsA.items():
                crit['$or'].append({('signals.%s' % k): {"$exists": True}})

	matches = []
        for bind in binds.find(crit):
		signalsB = bind['signals']

		macs = set(signalsA.keys()).union(signalsB.keys())

                pt1 = numpy.array([float(signalsA.get(k, 0)) for k in macs])
                pt2 = numpy.array([float(signalsB.get(k, 0)) for k in macs])

                dist = numpy.dot(
			pt1/numpy.linalg.norm(pt1),
			pt2/numpy.linalg.norm(pt2))
                matches.append((dist, bind))

	return [__format_bind(x[1]) for x in sorted(matches, key=itemgetter(0), reverse=True)[0:limit]]

def __format_bind(bind):
	return {"id": str(bind['_id']),
		"username": bind['username'],
		"place": str(bind['place']),
		"x": bind['x'],
		"y": bind['y'],
		"signals": bind['signals']
		}
