def find_anagrams(word, candidates):
    """Return list of anagram from candidates"""
    return [c for c in candidates if sorted(c.lower()) == sorted(word.lower()) if c.lower() != word.lower()]
