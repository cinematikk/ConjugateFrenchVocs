import json
out_file = open('verbs.txt', 'wt')

Verbs=["aller", "être"]

out_file.write(json.dumps(Verbs))
out_file.close()
