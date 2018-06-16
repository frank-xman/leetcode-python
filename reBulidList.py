#encoding=utf-8
def sequence(n, k, A):
    def right_seq(remain, zero_loc, diff_list, A):
        if remain < 0 or (remain > 0 and len(zero_loc) <= 0):
            # print "not right",remain,A
            return 0
        if remain == 0 and len(zero_loc) == 0:
        # print "====right====",A
            return 1
        result = 0
        for i in range(len(diff_list)):
            A[zero_loc[0]] = diff_list[i]
            # cal the list 
            new_add = 0
            for j in range(len(A)):
                if A[j] != 0 and ((j < zero_loc[0] and A[j] < A[zero_loc[0]]) or (j > zero_loc[0] and A[j] > A[zero_loc[0]])):
                    new_add += 1
            # print "A, newadd",A,new_add
            result += right_seq(remain-new_add, zero_loc[1:], diff_list[:i]+diff_list[i+1:], A)
            A[zero_loc[0]] = 0
        return result
 
    # the missing data of list
    n_list = [i for i in range(0, n+1)]
    diff_list = list(set(n_list) ^ set(A))
    # print "diff_list",diff_list
 
    # the loc of the missing data
    zero_loc = []
    for i in range(n):
        if A[i] == 0:
            zero_loc.append(i)
    # print "zero_loc",zero_loc
    origin_pair_num = 0
    for i in range(n-1):
        if A[i] != 0:
            for j in range(i+1, n):
                if A[j] > A[i]:
                    origin_pair_num += 1
    # print "origin_pair_num",origin_pair_num
 
    return right_seq(k-origin_pair_num, zero_loc, diff_list, A)
 
if __name__ == '__main__':
    firstline = raw_input()
    secondline = raw_input()
    n,k = [int(i) for i in firstline.strip().split(' ')]
    A = [int(i) for i in secondline.strip().split(' ')]
    print sequence(n, k, A)