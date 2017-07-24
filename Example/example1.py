
def testLambda():
    names=['marie','george','raj','prasu']
    p = sorted(names, key= lambda n: n.split()[-1])
    print(p)

if __name__ == '__main__':
    testLambda()