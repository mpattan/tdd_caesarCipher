import unittest
import mycipher
import sys


class TestDrivenDev(unittest.TestCase):
    #to setup command line arguments
    def setUp(self):
        self.action = sys.argv[1]
        self.string_input = sys.argv[2]
        self.cipher_input = sys.argv[3]     

    #to test encrypt function
    def test_encrypt(self):
        self.assertEqual(mycipher.encrypt(self.string_input,mycipher.get_cipher_value(self.cipher_input)), 'nkrru') 

if __name__ == '__main__':

    tdd = TestDrivenDev()
    tdd.setUp()
    # run all the tests
    if tdd.action == 'encrypt' :
        tdd.test_encrypt()
    # status
    print('### ALL TESTS PASSED ###')
