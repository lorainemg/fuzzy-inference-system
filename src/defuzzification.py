def mean_of_max(sample, membership):
    "Mean of maximum method"
    max_val = max(membership)
    total = sum([sample[i] for i in range(len(sample)) if membership[i] == max_val])
    n = len(list(filter(lambda x: x == max_val, membership)))
    return total / n

def left_of_max(sample, membership):
    "Left of maximum method"
    max_val = -1
    max_x = None
    for s, m in zip(sample, membership):
        if m > max_val:
            max_val = m
            max_x = s
    return max_x

def right_of_max(sample, membership):
    "Right of maximum method"
    max_val = -1
    max_x = None
    for s, m in zip(sample, membership):
        if m >= max_val:
            max_val = m
            max_x = s
    return max_x

def median_of_max(sample, membership):
    "Median of maximum method"
    max_value = -1
    max_xs = []
    for s, m in zip(sample, membership):
        if m > max_value:
            max_xs = [s]
            max_value = m
        elif m == max_value:
            max_xs.append(s)
    return max_xs[int(len(max_xs)/2)]

def centroid(sample, membership):
    "Centroid method (discrete)"
    num = sum([s*m for s, m in zip(sample, membership)])
    den = sum(membership)
    return num / den 

def bisector_of_area(sample, membership): # TODO: revisar
    "Bisector of area method (discrete)"
    def binary_search(i, old_l=float('-inf'), old_r=float('inf')):
        rightSum = sum([membership[idx] for idx in range(i, len(membership))])
        leftSum = sum(membership) - rightSum

        if rightSum == leftSum or abs(old_l-old_r) <= abs(leftSum-rightSum) or i+1 >= len(membership) or i-1 < 0:
            return i
        elif rightSum > leftSum:
            return binary_search(i+1, leftSum, rightSum)
        return binary_search(i-1, leftSum, rightSum)
    index = binary_search(int(len(membership)/2))
    return sample[index]


if __name__ == "__main__":
    result = mean_of_max([1,2,3,4], [4,4,1,2])
    print(result)