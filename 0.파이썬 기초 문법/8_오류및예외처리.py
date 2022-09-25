try:
    dkssudgktpdy
except:
    print("에러발생")

try:
    dkssudgktpdy
except:
    pass
print("에러를 무시")

try:
    dkssudgktpdy
except Exception as e:
    print("에러발생원인", e)