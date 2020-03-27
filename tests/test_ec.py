from sorting import quick_sort, cmp_standard, cmp_reverse
from hypothesis import given
import hypothesis.strategies as st
import timeit

'''
ints = st.lists(st.integers())


@given(str1=ints)
def test__quick_sort(str1):
    xs = list(str1)
    quick_sort(xs)
    assert xs == sorted(str1)

@given(str1=ints)
def test__quick_sort_cmp1(str1):
    xs = list(str1)
    quick_sort(xs,cmp_reverse)
    assert xs == list(reversed(sorted(str1)))
'''
