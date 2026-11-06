"""Day 2 exercises. Fill in each function, then run:  python exercises.py

Rules: no Googling for the first attempt, and use a comprehension wherever one fits.
Every assert must pass before you commit.
"""


def evens(nums: list[int]) -> list[int]:
    """Return only the even numbers, in order."""
    ...


def squares_dict(n: int) -> dict[int, int]:
    """Return {1: 1, 2: 4, ..., n: n*n}."""
    ...


def flatten(nested: list[list[int]]) -> list[int]:
    """[[1, 2], [3], []] -> [1, 2, 3]. One comprehension."""
    ...


def invert(d: dict[str, int]) -> dict[int, str]:
    """Swap keys and values: {"a": 1} -> {1: "a"}."""
    ...


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """["hi", "yo", "cat"] -> {2: ["hi", "yo"], 3: ["cat"]}."""
    ...


def top_n(scores: dict[str, float], n: int) -> list[str]:
    """Names of the n highest scores, best first. Hint: sorted(..., key=...)."""
    ...


def merge_counts(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    """Add counts per key: {"x": 1} + {"x": 2, "y": 1} -> {"x": 3, "y": 1}."""
    ...


def normalize(values: list[float]) -> list[float]:
    """Min-max scale to [0, 1]. This is your first real ML preprocessing step.
    If all values are equal, return a list of zeros."""
    ...


if __name__ == "__main__":
    assert evens([1, 2, 3, 4, 6]) == [2, 4, 6]
    assert squares_dict(3) == {1: 1, 2: 4, 3: 9}
    assert flatten([[1, 2], [3], []]) == [1, 2, 3]
    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert group_by_length(["hi", "yo", "cat"]) == {2: ["hi", "yo"], 3: ["cat"]}
    assert top_n({"ana": 90, "bo": 72, "cy": 85}, 2) == ["ana", "cy"]
    assert merge_counts({"x": 1}, {"x": 2, "y": 1}) == {"x": 3, "y": 1}
    assert normalize([10, 20, 30]) == [0.0, 0.5, 1.0]
    assert normalize([5, 5]) == [0.0, 0.0]
    print("All 9 checks passed. Commit it.")
