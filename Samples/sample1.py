#!/usr/bin/env python3

def sample_items():
    for i in range(3):
        print(i)


def test(items):
    print(items[2:])




if __name__ == '__main__':
    #sample_items()
    test([1,2,3,4,5])
