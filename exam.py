"""
① 读文本文件 读取 hello.txt，打印出非空行的数量。

检测：open() + with、按行读取、strip() 判空。答案应是 4。

② JSON 解析 在代码里写一个字符串 '{"name": "小明", "score": [90, 85, 88]}'，用 json.loads 转成字典，打印 score 的平均分。

检测：loads（字符串→对象）与 load（文件→对象）的区别、嵌套取值。

③ 写 JSON 文件 把 data = {"标题": "测试", "数字": 123, "列表": [1, 2, 3]} 写入 result.json，要求：中文不乱码、缩进格式化（不挤在一行）。

检测：json.dump、ensure_ascii=False、indent=2。
"""
import json

"""
try:
    with open("/Users/admin/Documents/deepseek-harness/default-workspace/hello.txt", encoding="utf-8") as f:
        count = 0
        for line in f.readlines():
            if line.strip():
                count += 1
        print(count)
except FileNotFoundError:
    print('文件不存在')
except Exception as e:
    print(e)

des = '{"name": "小明", "score": [90, 85, 88]}'
des_dict = json.loads(des)
score_list = des_dict["score"]
print(f"平均分为：{round(sum(score_list, start=0) / len(score_list), 2)}")

data = {"标题": "测试", "数字": 123, "列表": [1, 2, 3]}

with open("/Users/admin/Documents/deepseek-harness/default-workspace/result.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)"""


def document_write(path, json_data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
        print(f"文件{path}写入成功～")


try:
    with open('/Users/admin/Documents/deepseek-harness/default-workspace/logs.json', encoding="utf-8") as f:
        data = json.load(f)
        clear_list = []
        summary = {}
        message_dict = {}
        for dict_item in data:
            # 新增字段
            dict_item["total_tokens"] = dict_item["usage"]["prompt_tokens"] + dict_item["usage"]["completion_tokens"]
            # 过滤出 status == "success"的记录，存到cleaned.json
            if dict_item["status"] == "success":
                clear_list.append(dict_item)
            # 统计每个用户role = "user"的消息条数
            message = dict_item["messages"]
            for message_item in message:
                if message_item["role"] == "user":
                    message_dict[dict_item["user"]] = message_dict.get(dict_item["user"], 0) + 1
        summary["success_count"] = len(clear_list)
        summary["total_tokens"] = sum([i["total_tokens"] for i in clear_list])
        summary["user_messages"] = message_dict
    document_write("/Users/admin/Documents/deepseek-harness/default-workspace/cleaned.json", clear_list)
    document_write("/Users/admin/Documents/deepseek-harness/default-workspace/summary.json", summary)
except FileNotFoundError:
    print('文件没有找到哦～')
except Exception as e:
    print(e)
