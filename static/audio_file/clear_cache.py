import os


all_file = os.listdir('.')

print('正在清理缓存')
for i in all_file:
    if 'auido' in i or 'clear' in i:
        continue
    os.remove(i)
