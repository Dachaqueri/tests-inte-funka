import unittest

if __name__ == '__main__':
    #unittest.main()
    testsuite = unittest.TestLoader().discover('test')
    print(testsuite)
    unittest.TextTestRunner(verbosity=2).run(testsuite)