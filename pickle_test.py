import unittest, pickle
from pickler import list_pickler, unpickler
class PickleTests(unittest.TestCase):

    def setUp(self):
        pass

    def variable_equivalence(self):
        my_list = [a, b, c]
        output = open('my_list.pkl', 'wb')
        pickle.dump(my_list, output)
        input = open('my_list.pkl', 'rb')
        another_list = pickle.load(input)
        self.assertEqual(my_list, another_list)


    def tearDown(self):
        pass
