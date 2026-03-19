import json

def desensitize_data(data):
    """简单脱敏示例：隐藏手机号中间4位、身份证号中间10位"""
    if "phone" in data:
        data["phone"] = data["phone"][:3] + "****" + data["phone"][7:]
    if "id_card" in data:
        data["id_card"] = data["id_card"][:6] + "**********" + data["id_card"][16:]
    return data

if __name__ == "__main__":
    # 读取原始数据
    with open("demo.json", "r", encoding="utf-8") as f:
        raw_data = json.load(f)
    
    # 脱敏处理
    sensitive_data = desensitize_data(raw_data)
    
    # 保存脱敏后数据
    with open("desensitized_demo.json", "w", encoding="utf-8") as f:
        json.dump(sensitive_data, f, ensure_ascii=False, indent=2)
    
    print("脱敏完成！已生成 desensitized_demo.json")