
def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

s = input()

length = len(s)

n = 0

for i in range(length):
    res_str = s[:i] +  s[i+1:]
    if is_palindrome(res_str):
        n+=1

print("При удалении",n,"символов получаются палиндромы")

