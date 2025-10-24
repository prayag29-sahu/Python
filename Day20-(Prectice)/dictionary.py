d = {"name": "Prayag", "age": 21}
print(d["name"])
d["city"] = "Delhi"
d.update({"age": 22})
print(d.keys())
print(d.values())
print(d.items())
d.pop("age")
for k, v in d.items():
    print(k, v)
