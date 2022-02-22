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

    #to test decrypt function
    def test_decrypt(self):
        self.assertEqual(mycipher.decrypt(self.string_input,mycipher.get_cipher_value(self.cipher_input)), 'hello')
        
if __name__ == '__main__':

    tdd = TestDrivenDev()
    tdd.setUp()
    # run all the tests
    if tdd.action == 'encrypt' :
        tdd.test_encrypt()
    else :
        tdd.test_decrypt()
    # status
    print('### ALL TESTS PASSED ###')
