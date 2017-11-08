# -*- coding: utf-8 -*-


def calc_parity(x):
    ''' if the number of 1 bit is odd.'''
    pass


def swap_bits(x, i, j):
    pass


def reverse_bit(x):
    pass


def closest_int(x):
    ''' the same number of 1 bit, and return y to make min|y-x|
    solution: 找到第一对连续的不相同的bit，交换即可。
    '''
    pass


def string2Int(s):
    pass


def int2String(x):
    pass


def change_base(b1, s1, b2):
    """
    change the int s1(represented in string format) of base b1
    to a int s2(represented in string format) of base b2
    """
    pass


def gcd(x1, x2):
    """
    x1, x2: positive integers.
    """
    if x1 < x2:
        return gcd(x2, x1)
    if x2 == 0:
        return x1
    else:
        return gcd(x2, x1 % x2)


def enum_primes(n):
    '''
    n>=2 integers. enumerating all primes <= n
    solution: 筛数法
    '''
    is_prime = [True for i in range(n-1)] # num in index num-2
    p = 2
    while p*p <= n:
        while is_prime[p-2] is False:
            p += 1
        for cur in range(p*p, n+1, p):
            is_prime[cur-2] = False
        p += 1

    result = []
    for i in range(n-1):
        if is_prime[i] is True:
            result.append(i+2)
    return result


class Rect(object):
    def __init__(self, x, y, width, height):
        self.x, self.y, self.width, self.height = x, y, width, height


def intersect_rect(rect1, rect2):
    '''
    rect1, rect2 are xy-aligned.
    return the intersect rect of rect1 and rect2, otherwise, return None
    '''
    if not _is_intersect(rect1, rect2):
        return None
    return Rect(max(rect1.x, rect2.x), max(rect1.y, rect2.y),
                min(rect1.x+rect1.width, rect2.x+rect2.width) - max(rect1.x, rect2.x),
                min(rect1.y+rect1.height, rect2.y+rect2.height) - max(rect1.y, rect2.y))


def _is_intersect(rect1, rect2):
    return rect1.x + rect1.width >= rect2.x and rect1.x <= rect2.x + rect2.width \
            and rect1.y + rect1.height >= rect2.y and rect1.y <= rect2.y + rect2.height


class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __cmp__(self, other):
        if self.x < other.x:
            return -1
        elif self.x > other.x:
            return 1
        elif self.y < other.y:
            return -1
        elif self.y > other.y:
            return 1
        else:
            return 0

def is_xy_aligned(p1, p2, p3, p4):
    ''' pi 构成一个矩形，判断该矩形是否与x,y轴对齐'''
    ps = [p1, p2, p3, p4]
    ps.sort()
    return ps[0].x == ps[1].x and ps[2].x == ps[3].x and \
            ps[0].y == ps[2].y and ps[1].y == ps[3].y


def intersect_rect(rect1, rect2):
    ''' 矩形rect1, rect2不一定是xy-aligned. 它有四个顶点确定'''

if __name__ == '__main__':
    p1 = Point(0,0)
    p2 = Point(1,1)
    p3 = Point(0,1)
    p4 = Point(1,0)
    print is_xy_aligned(p1, p2, p3, p4)