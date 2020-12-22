import random

'''
Function：Miller_Rabin素性检验

n: 待检验的数
iter_num: 迭代次数(置信度)
'''
def miller_rabin_test(n, iter_num= 50):
    # 将n-1写成2^s*t的形式
    num = n - 1
    s = 0
    while num % 2 == 0:
        num = num // 2
        s += 1

    # 结束时n-1 = 2^s * num

    for _ in range(iter_num):
        b = random.randrange(2, n-1)    # 在(2,n-1)范围内随机选择整数b
        r = pow(b, num, n)
        if r == 1 or r == n-1:
            continue
        else:
            r = (r ** 2) % n
        for iter in range(1,s):
            if iter == s-1 and r != n-1:
                return False    # n是合数
            if r == n-1:
                break
            r = (r ** 2) % n

    return True    #n是素数


# 创建小素数的列表,可以大幅加快速度
small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

'''
Function：素数的判断

num：需判断的数
'''
def is_prime(num):
    # 排除0,1和负数
    if num < 2:
        return False

    # 如果是小素数,那么直接返回true
    if num in small_primes:
        return True

    # 如果大数是这些小素数的倍数,那么就是合数,返回false
    for prime in small_primes:
        if num % prime == 0:
            return False

    # 如果这样没有分辨出来,就一定是大整数,那么就调用rabin算法
    return miller_rabin_test(num)


'''
Function：生成大素数

key_size：素数的bit位数
'''
def get_prime(key_size=1024):
    while True:
        num = random.randrange(2**(key_size-1), 2**key_size)
        if is_prime(num):
            return num