#저장된 data 읽어오기
import pickle

file = open('important', 'rb')
data = pickle.load(file)
file.close()

print('showing the pickled data')
for idx, item in enumerate(data):
    print(idx, item)