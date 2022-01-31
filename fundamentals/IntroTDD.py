import unittest

def reverseList(list):
    list.reverse()
    return list


def IsPalindrome(string):
    newString = string[::-1]
    if newString == string:
        return True
    else:
        return False


def monedas(vuelto):
    vueltoAEntregar = []
    quina = 500
    gamba = 100
    cincuenta = 50
    diez = 10
    mod = 0
    if vuelto >= quina:
        vueltoAEntregar.append(int(vuelto / quina))
        var = vuelto % quina
        if var == 0:
            vueltoAEntregar.append(0)
            vueltoAEntregar.append(0)
            vueltoAEntregar.append(0)
            return vueltoAEntregar
        elif var >= gamba:
            vueltoAEntregar.append(int(var / gamba))
            varr = var % gamba
            if varr == 0:
                vueltoAEntregar.append(0)
                vueltoAEntregar.append(0)
                return vueltoAEntregar
            elif varr >= cincuenta:
                vueltoAEntregar.append(int(varr / cincuenta))
                varrr = varr % cincuenta
                if varrr == 0:
                    vueltoAEntregar.append(0)
                    return vueltoAEntregar
                else:
                    vueltoAEntregar.append(int(varrr / diez))
    elif vuelto > gamba:
        vueltoAEntregar.append(0)
        vueltoAEntregar.append(int(vuelto / gamba))
        var4 = vuelto % gamba
        if var4 == 0:
            vueltoAEntregar.append(0)
            vueltoAEntregar.append(0)
            return vueltoAEntregar
        elif var4 >= cincuenta:
            vueltoAEntregar.append(int(var4 / cincuenta))
            var5 = var4 % cincuenta
            if var5 == 0:
                vueltoAEntregar.append(0)
                return vueltoAEntregar
            else:
                vueltoAEntregar.append(int(var5 / diez))
        elif var4 < cincuenta:
            vueltoAEntregar.append(0)
            vueltoAEntregar.append(int(var4 / diez))
    elif vuelto < cincuenta:
        vueltoAEntregar.append(0)
        vueltoAEntregar.append(0)
        vueltoAEntregar.append(int(vuelto / cincuenta))
        var6 = vuelto % cincuenta
        if var6 == 0:
            vueltoAEntregar.append(0)
            return vueltoAEntregar
        else:
            vueltoAEntregar.append(int(var6 / diez))
        
    return vueltoAEntregar

print(monedas(430))

class reverseListTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([5, 4, 3]), [3, 4, 5])
    
    def testTwo(self):
        self.assertEqual(reverseList([3, 2, 1]), [1, 2, 3])
    
    def testThree(self):
        self.assertEqual(reverseList([10, 9, 8]), [8, 9, 10])

    def testOtto(self):
        self.assertEqual(IsPalindrome("otto"), True)
    
    def testAna(self):
        self.assertEqual(IsPalindrome("ana"), True)
    
    def testSergio(self):
        self.assertFalse(IsPalindrome("Guillermo"))

    def testVuelto1(self):
        self.assertEqual(monedas(800), [1, 3, 0, 0])
    
    def testVuelto2(self):
        self.assertEqual(monedas(950), [1, 4, 1, 0])
    
    def testVuelto3(self):
        self.assertEqual(monedas(430), [0, 4, 0, 3])
    
    def testVuelto4(self):
        self.assertEqual(monedas(40), [0, 0, 0, 4])
    
    def testVuelto5(self):
        self.assertEqual(monedas(380), [0, 3, 1, 3])
    
    def setUp(self):
        print("hola")
    
    def tearDown(self):
        print("chao")

if __name__ == '__main__':
    unittest.main()