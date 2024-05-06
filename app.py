def validate_tw_id(id_number):
    if len(id_number) != 10:
        return False, "身分證號碼應該為10碼"
    
    # 檢查第一個字元是否為英文字母
    first_char = id_number[0]
    if not first_char.isalpha():
        return False, "第一個字元應該為英文字母碼"
    
    # 將第一個英文字母轉換為對應的數字（A為10，B為11，C為12，...，Z為33）
    num_value = ord(first_char.upper()) - ord('A') + 10
    id_number = str(num_value) + id_number[1:]
    
    # 檢查後九個字元是否為數字
    if not id_number[1:].isdigit():
        return False, "後九個字元應該為數字"
    
    # 將轉換後的兩位數字分別乘以1和9
    checksum = int(id_number[0]) * 1 + int(id_number[1]) * 9
    
    # 將第二個到第九個數字分別乘以8, 7, 6, 5, 4, 3, 2, 1
    weights = [8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(2, 10):
        checksum += int(id_number[i]) * weights[i-2]
    
    # 將以上所有乘積相加，並加上最後一個數字
    checksum += int(id_number[9])
    
    # 如果最後的結果可以被10整除，則這個身份證號碼就是正確的
    if checksum % 10 != 0:
        return False, "身分證號碼格式錯誤"
    
    # 檢查性別碼是否正確
    gender_code = int(id_number[1])
    gender = "男性" if gender_code % 2 == 1 else "女性"

    return True, f"身分證號碼格式正確，性別為{gender}"

# 測試範例
id_number = "A123456789"
is_valid, message = validate_tw_id(id_number)
if is_valid:
    print(message)
else:
    print(message)


