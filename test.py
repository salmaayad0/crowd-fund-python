from main import main
import unittest

class TestDemo(unittest.TestCase):
    def testMain(self):
        self.assertEqual(main.main(1),1,"right")
        self.assertEqual(main.main(2),1,"right")
        self.assertEqual(main.main(3),1,"right")
        
    def testLogin(self):
        self.assertEqual(main.login("test", "123456"),"test@gmail.com","faild")



if __name__ =="main":
    unittest.main()