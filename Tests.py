import unittest
from Application import Application

class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_cant_stacks(self):
        level = "EASY"
        numberLevel = "1"
        l = Application.getNumberStacksLevel(level, numberLevel)
        s = Application.getNumberStacksSolution(level, numberLevel)
        self.assertTrue(l==s)

    def test_create_profile_none_name(self):
        username = None
        self.assertFalse(Application.createProfile(username))

    def test_create_profile_empty_name(self):
        username = ""
        self.assertFalse(Application.createProfile(username))

    def test_create_profile(self):
        username = "test"
        self.assertTrue(Application.createProfile(username))
        self.assertTrue(username in Application.getFiles("profiles/"))

    def test_arm(self):     
        self.assertIs(Application.getArmPosition('EASY','5'),2)
        
    def test_arm2(self):     
        self.assertIsNot(Application.getArmPosition('EASY','5'),5)

    def test_getScore(self):
        with self.assertRaises(IOError):
            Application.getScores("nestorhola","5jhhjhg")
            
if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)

    """try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            pass
"""
