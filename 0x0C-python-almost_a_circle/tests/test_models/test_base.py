
from models.base import Base
import unittest

'''
    Test_Base class

it tasts all modules of Base class
'''
class Test_Base(unittest.TestCase):

    """
    test_init
tests all instances of Base constracter
    """
    def test_init(self):
        t1 = Base().id
        t2 = Base().id
        t3 = Base().id
        t4 = Base(23).id
        t5 = Base().id

        tst = [t1, t2, t3]

        for i, t in enumerate(tst):
            self.assertEqual(t, i+1)

        self.assertEqual(t4, 23)
        self.assertEqual(t5, 4)
