def add(a, b):
    """返回两数之和"""
    return a + b

def safe_div(a, b):
    print(f"[DEBUG] {__file__} safe_div(a={a}, b={b})")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numbers")
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


if __name__ == "__main__":
    print("add(2, 3) ->", add(2, 3))

    # 演示：在调用处优雅捕获错误
    try:
        print("safe_div(10, 2) ->", safe_div(10, 2))
    except Exception as e:
        print("捕获到错误：", repr(e))

    # 你可以再加一行正常调用验证：
    # print("safe_div(9, 3) ->", safe_div(9, 3))
