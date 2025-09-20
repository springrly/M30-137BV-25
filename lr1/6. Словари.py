scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
scores["Bob"] = 95
scores.get("Dave")
scores.pop("Alice")
assert "Alice" not in scores
scores.keys()
scores.values()

print(scores, scores.get("Bob"), scores.get("Dave"), len(scores), scores.keys(), scores.values())
