import json
out_file = open('verbs.txt', 'wt')

Verbs=["aller", "être"]

neu = input("Ein neues Verb:")
Verbs.append(neu)
mehrVerben = input("Möchtest du mehr Verben hinzufügen?")
while mehrVerben == "ja":
    neu = input("Ein neues Verb:")
    if neu == "break":
        mehrVerben = "break"
    else:
        Verbs.append(neu)

out_file.write(json.dumps(Verbs))
out_file.close()
print("Alle Verben wurden in die verbs.txt gespeichert.")
