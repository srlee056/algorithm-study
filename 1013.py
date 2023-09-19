#  정규식 문제 더 풀어본 이후에 다시 풀러 올 것

def checkStringFormat(s):
    if (len(s) < 4) or (not s.startswith('100')) or (not s.endswith('1')):
        return False

    tempOne = False
    for c in s[3:-1]:
        if c == '1':  # should compare with string
            tempOne = True
        if c == '0' and tempOne:
            return False

    return True


numCases = int(input())

for i in range(numCases):
    string01 = input()
    isValidPattern = True
    # string01이 비어있지 않으면 계속 돌아감
    while isValidPattern and string01:
        if string01.startswith('01'):
            string01 = string01[2:]  # 01으로 시작하는 문자열이면 잘라냄
        else:
            # 문자열을 가르는 기준 문자열을 찾는다.
            # 101 or 110
            idx1 = string01.find('101')
            idx2 = string01.find('110')

            # -1이 아닌 작은 수를 찾고 문자열을 자른다.
            # 만약 둘 다 -1이라면 원본 문자열이 100.. ..1을 만족하는지 확인한다.

            if idx1 == -1 and idx2 == -1:
                idx = len(string01)
            elif idx1 == -1 or idx2 == -1:
                idx = max(idx1, idx2)+1
            else:
                idx = min(idx1, idx2)+1

            isValidPattern = checkStringFormat(string01[:idx])
            string01 = string01[idx:]

    print('YES') if isValidPattern else print('NO')
