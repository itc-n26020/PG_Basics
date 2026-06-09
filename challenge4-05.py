def float_to(s):
    try:
        return float(s)
    except (ValueError):
        print("数字ではないので処理を中止します")
f = float_to("")
print(f)
