try:
    print("=" * 20)
    print(na.name)
except NameError as e:
    print('名字出错', e)
except Exception as e:
    print(e)
finally:
    print('资源释放')
