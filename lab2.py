def common_letter(text1, text2):
    # data size is number n, which is length of text 1,2
    n=len(text1)
    for i in range(n):
        for j in range(n):
            if text1[i] == text2[j]:
                return True
    return False

#worst case is when there is no common letter, because both loops last n times.
#and in that case complecity is Theta(n^2)

print(common_letter("sok", "nos"))
print(common_letter("python", "aabbcc"))