country = input('请问你是哪国人：')
age = input('请输入年龄：')
age = int(age)
if country == '中国':
	if age >= 18:
		print('你可以考驾照')
	else:
		print('你还不能考驾照')
elif country == '美国':
	if age >= 16:
		print('你可以考驾照')
	else:
		print('你还不能考驾照')
else:
	print('你只能输入 中国/美国')