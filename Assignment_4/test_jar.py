import pytest 

from jar import Jar

def test_init (): 
   jar = Jar(12)
   assert jar.capacity == 12
   assert jar.size == 0

   with pytest.raises(ValueError):
       Jar(-3)
   with pytest.raises(ValueError):
       Jar(1.5)
   with pytest.raises(ValueError):
       Jar("five")

def test_str():
   jar = Jar(12)
   assert str(jar) ==""

   jar.deposit(6)
   assert str(jar) == "🍪🍪🍪🍪🍪🍪"

   jar.withdraw(4)
   assert str(jar) == "🍪🍪"

def test_deposit ():
   jar = Jar(12)

   jar.deposit (2)
   jar.deposit(5)
   assert jar.size == 7
   
def test_withdraw ():
   jar = Jar(12) 

   jar.deposit (5)
   jar.withdraw (2)
   
   assert jar.size == 3