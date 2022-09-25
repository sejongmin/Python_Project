a_str = "hello python"
if a_str == "hello python":
    print("hello python 문자열이 같습니다.")
if a_str == "hi python":
    print("hello python 문자열이 같습니다.")
if "hello" in a_str:
    print("hello 가 포함되어 있습니다.")
if "hello" not in a_str:
    print("hello 가 포함되어 있지 않습니다")
if "hi" not in a_str:
    print("hi 가 포함되어 있지 않습니다.")

a_list = ["안녕", 1, 2, "파이썬"]
if "안녕" in a_list:
    print("a_list에 안녕 이 포함되어 있습니다.")
if 2 in a_list:
    print("a_list에 숫자 2 가 포함되어 있습니다.")