from median import get_median

def test_median():
    get_median([1, 2, 3, 4, 5]) == 3
    get_median([3, 1, 2, 5, 3]) == 3
    get_median([1, 300, 2, 200, 1]) == 2
    get_median([3, 6, 20, 99, 10, 15]) == 12.5