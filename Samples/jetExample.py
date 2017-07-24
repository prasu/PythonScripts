#!/usr/bin/env python3

''' example asked in jet interview '''
def test():
    people={1:"dd", 2:"Raj", 3:"Prasu", 4:"Madhav"}
    relations=({1,2},{2,3},{1,3},{2,3},{2,1})
    d={}


    for i in people.keys():
        for r in relations:
            if i in r:
                pass



        print(i)

if __name__ == '__main__':
	test()
	