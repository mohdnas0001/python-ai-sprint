# Day 2: lists, dicts, comprehensions, functions

Read this in 20 minutes, then close it and go to `exercises.py`.

## Lists: ordered and mutable
```python
nums = [3, 1, 4, 1, 5]
nums.append(9); nums[0]; nums[-1]; nums[1:3]   # index and slice
sorted(nums, reverse=True); len(nums); sum(nums)
```

## Dicts: key to value lookup in O(1)
```python
ages = {"ana": 31, "bo": 25}
ages["cy"] = 40
ages.get("zed", 0)                 # default instead of a KeyError
for name, age in ages.items(): ...
```

## Comprehensions: build a list or dict in one line
```python
squares = [x * x for x in range(10)]
evens   = [x for x in nums if x % 2 == 0]
lookup  = {name: len(name) for name in ["ana", "bo"]}
```

## Functions: small, named, and typed
```python
def mean(values: list[float]) -> float:
    """Return the arithmetic mean."""
    return sum(values) / len(values)
```

## Why this matters for AI
In Pandas, a DataFrame row is basically a dict and a column is basically a list.
JSON from every LLM API is dicts nested in lists. If you're fluent here, Week 2 gets easy.
