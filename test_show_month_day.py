import unittest

from show_month_day import TimeScript

class TestShowMonthDay(unittest.TestCase):
     """
         Our basic test class
     """
     dmc1 = []
     #learn to set up initial values or actions before testing process
     @classmethod
     def setUpClass(cls):
        print('setUpClass')
     
     #learn to set up some actions after the whole test is finished
     @classmethod
     def tearDownClass(cls):
        print('tearDownClass') 
      
     #try to set up initial values for each testing part 
     def setUP(self):
        pass#self.days_1 = TimeScript(2018, 2, 20, 2018, 3, 1)
     
     #try to set some actions for each testing part
     def tearDown(self):
        pass
     
     def test_fact(self):
        """ 
        The actual test.
        Any method which starts with ''test_'' will considered	as a test case. 
        """ 
        dmc1 = TimeScript([], 2018, 2, 20, 2018, 2, 21)
        ans = ['2018-02-20', '2018-02-21']#, '2018-02-22', '2018-02-23', '2018-02-24', '2018-02-25', '2018-02-26', '2018-02-27', '2018-02-28', '2018-03-01']
        #print(dmc1.year_month_date_list)
        self.assertEqual(dmc1.year_month_date_list, ans) 
     
     def test_error(self):
        """
        To test exception raise due to run time error
        """ 
        pass
		#self.assertRaises(ValueError, , ) 
     
if __name__ == '__main__':
     unittest.main()