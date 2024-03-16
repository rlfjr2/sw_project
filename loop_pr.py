ef test_return():
    # ====== Loop ======
    for i in range(5):
        if i == 2:
            return
        print(f"[i=={i}] 반복 중")
    # ====== ==== ======
    print("반복 끝")


test_return()
print("코드 끝")
