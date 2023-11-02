from times import compute_overlap_time, time_range  # Put all imports from times.py on 1 line
import pytest

def test_different_sizes():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected


def test_no_overlap():
    periodone = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    periodtwo = time_range("2010-01-12 15:00:00", "2010-01-12 17:00:00")
    result = compute_overlap_time(periodone, periodtwo)
    expected = []
    assert result == expected


def test_several_intervals():
    periodone = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    periodtwo = time_range("2010-01-12 09:00:00", "2010-01-12 12:00:00", 2, 120)
    result = compute_overlap_time(periodone, periodtwo)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:29:00'), ('2010-01-12 10:31:00', '2010-01-12 10:37:00'),
                ('2010-01-12 10:38:00', '2010-01-12 10:29:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_immediate_continue():
    periodone = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    periodtwo = time_range("2010-01-12 12:00:00", "2010-01-12 15:00:00")
    result = compute_overlap_time(periodone, periodtwo)
    expected = [('2010-01-12 12:00:00', '2010-01-12 12:00:00')]
    assert result == expected

def test_reverse_time():
    with pytest.raises(ValueError): # Makes sure there is a value error here
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")

