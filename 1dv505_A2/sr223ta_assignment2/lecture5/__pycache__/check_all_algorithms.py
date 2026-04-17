




from test_sorting import test_sorting_algorithms


try:
    test_sorting_algorithms()
    print("All sorteringsalgoritmes passed the tests!")
except AssertionError as a:
    print("one test failed:")
    print(a)
