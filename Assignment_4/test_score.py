# test_score.py

from score import score  # now only score(text, threshold)

def test_score_types_and_range():
    p, prop = score("hello world", 0.5)
    assert isinstance(p, bool)
    assert isinstance(prop, float)
    assert 0.0 <= prop <= 1.0

def test_threshold_edge_cases():
    p0, _ = score("anything", 0.0)
    p1, _ = score("anything", 1.0)
    assert p0 is True
    assert p1 is False

def test_spam_vs_ham_detection():
    """Spam text should get higher propensity than ham text."""
    spam = "Congratulations! You've won a free lottery ticket. Call now!"
    ham  = "Let's meet for coffee tomorrow at 10am."

    ps, prop_spam = score(spam, 0.5)
    ph, prop_ham  = score(ham,  0.5)

    # Both props in [0,1]
    assert 0.0 <= prop_ham <= 1.0
    assert 0.0 <= prop_spam <= 1.0

    # The spam example must have strictly higher propensity than the ham example
    assert prop_spam > prop_ham
