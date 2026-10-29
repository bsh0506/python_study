"""with open("/Users/admin/Documents/deepseek-harness/default-workspace/hello.txt", "w", encoding="utf-8") as f:
    try:
        # print(f.read())
        # print(f.readlines())
        # for line in f.readlines():
        #     print(line.strip())
        f.write("谢谢！")
    except FileNotFoundError:
        print("File not found")
    finally:
        f.close()"""


def document_operate(operation: str):
    path = "/Users/admin/Documents/deepseek-harness/default-workspace/hello.txt"
    try:
        with open(path, operation, encoding="utf-8") as f:
            if operation == "w":  # 会清空重写
                f.write("谢谢！")
            elif operation == "a":  # 追加，不清空
                f.write("新增内容\n")
            elif operation == "r":  # 只读
                for line in f:  # 直接遍历文件，比 readlines() 省内存
                    print(line.strip())
    except FileNotFoundError:
        print("文件不存在")


document_operate("r")
document_operate("w")
document_operate("r")
document_operate("a")
document_operate("r")
