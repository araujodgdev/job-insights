from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'
    words = ['python', 'javascript']
    ocurrences_python = 1639
    ocurrences_javascript = 122
    assert count_ocurrences(path, words[0]) == ocurrences_python
    assert count_ocurrences(path, words[1]) == ocurrences_javascript
