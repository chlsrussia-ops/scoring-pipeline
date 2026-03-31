from caps import apply_caps

def test_no_cap():
    r = apply_caps(42.0)
    assert r.value == 42.0 and not r.capped

def test_cap_applied():
    r = apply_caps(142.0)
    assert r.value == 100.0 and r.capped
