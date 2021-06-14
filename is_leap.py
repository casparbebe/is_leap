y = int(input('請輸入年分: ')) # 讓使用者輸入年份

# 檢測閏年的函示
def is_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

print(is_leap(y))

# 印出答案
if is_leap:
	print(y, '是閏年')
else:
	print(y, '不是閏年')