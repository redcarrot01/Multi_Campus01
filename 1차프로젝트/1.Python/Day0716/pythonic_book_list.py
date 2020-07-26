books = list()

books.append({'제목':'개발자의 코드', '출판연도':'2013.02.28', \
              '출판사':'A출판', '쪽수':200, '추천유무':False})
books.append({'제목':'클린 코드', '출판연도':'2013.03.04', \
              '출판사':'B출판', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014.07.02', \
              '출판사':'A출판', '쪽수':296, '추천유무':True})
books.append({'제목':'구글드', '출판연도':'2010.02.10', \
              '출판사':'B출판', '쪽수':526, '추천유무':False})
books.append({'제목':'강의력', '출판연도':'2013.12.12', \
              '출판사':'C출판', '쪽수':248, '추천유무':True})

# [{}, {}, {}]
#print(books)
# 책제목 리스트
title_list = list()
# 출판사 리스트
pub_comp = set()
# 쪽수가 250 초과인 리스트
many_page_list = list()
# 추천유무가 True인 리스트
recommend_list = list()
# 전체 페이지수
all_pages = int()

for book in books:
    #print(type(book), book['제목'])
    title_list.append(book['제목'])
    pub_comp.add(book['출판사'])
    # 쪽수가 250 초과
    if book['쪽수'] > 250:
        many_page_list.append(book['제목'])
    if book['추천유무']:
        recommend_list.append(book['제목'])
    
    #all_pages += book['쪽수']
    all_pages = all_pages + book['쪽수']

# print(title_list)
# print(pub_comp)
# print(many_page_list)
# print(recommend_list)
# print(all_pages)

# List Comprehension 스타일
title_list = [book['제목'] for book in books]
print(title_list)
pub_comp = set([book['출판사'] for book in books])
print(pub_comp)
many_page_list = [book['제목'] for book in books if book['쪽수'] > 250]
print(many_page_list)
recommend_list = [book['제목'] for book in books if book['추천유무']]
print(recommend_list)

all_pages = sum(book['쪽수'] for book in books)
print(all_pages)
