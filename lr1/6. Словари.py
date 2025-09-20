scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
scores["Bob"] = 95
scores.get("Dave")
scores.pop("Alice")
assert "Alice" not in scores
scores.keys()
scores.values()

print(scores)
print(scores.get("Bob"))
print(scores.get("Dave"))
print(len(scores))
print(scores.keys())
print(scores.values())
