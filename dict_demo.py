# 字典
# 定义字典
d1 = {"one": 1, "two": 2, "three": 3}
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())
for k, v in d1.items():
    print(k, v)
"""
    {'one': 1, 'two': 2, 'three': 3}
    dict_keys(['one', 'two', 'three'])
    dict_values([1, 2, 3])
    dict_items([('one', 1), ('two', 2), ('three', 3)])
    one 1
    two 2
    three 3
"""

# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
##添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
##修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
##删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
##查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
##退出购物车
shopping_cart = []
while True:
    print("=" * 30, "购物车管理系统", "=" * 30)
    print("=" * 30, "1.添加商品", "=" * 30)
    print("=" * 30, "2.修改商品", "=" * 30)
    print("=" * 30, "3.删除商品", "=" * 30)
    print("=" * 30, "4.查询商品", "=" * 30)
    print("=" * 30, "5.退出系统", "=" * 30)
    choice = input("请输入要操作的序号：")
    if choice == "1":
        shopping_name = input('请输入商品名称：')
        shopping_price = input('请输入该商品的价格：')
        shopping_count = input('请输入该商品的数量：')
        shopping_item = {"商品名称": shopping_name, "商品价格": shopping_price, "商品数量": shopping_count}
        shopping_cart.append(shopping_item)
        print("现在的购物车里有：", shopping_cart)
    elif choice == "2":
        shopping_name = input("请输入要修改的商品名称：")
        flag = False
        for item in shopping_cart:
            if item["商品名称"] == shopping_name:
                shopping_price = input("请输入要修改的商品价格：")
                shopping_count = input("请输入要修改的商品数量：")
                item["商品价格"] = shopping_price
                item["商品数量"] = shopping_count
                flag = True
                break
        if not flag:
            print('商品不存在')
        else:
            print("商品修改完成：", shopping_cart)
    elif choice == "3":
        shopping_name = input("请输入要删除的商品名称：")
        flag = False
        for item in shopping_cart:
            if item["商品名称"] == shopping_name:
                shopping_cart.remove(item)
                flag = True
                break
        if not flag:
            print("商品不存在")
        else:
            print("商品删除完成", shopping_cart)
    elif choice == "4":
        shopping_name = input("请输入要查询的商品名称：")
        flag = False
        for item in shopping_cart:
            if item["商品名称"] == shopping_name:
                print(
                    f"商品详细信息：商品名称：{shopping_name},商品价格：{item["商品价格"]}，商品数量：{item["商品数量"]}", )
                flag = True
                break
        if not flag:
            print("商品不存在")
    else:
        break
    isContinue = input('是否继续操作(y/n)：')
    match isContinue:
        case "y":
            continue
        case _:
            break
