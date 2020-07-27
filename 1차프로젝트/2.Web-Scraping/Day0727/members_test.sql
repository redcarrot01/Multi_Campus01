desc members;

#id 컬럼 auto increment , pk 설정
# alter table members modify id int not null auto_increment primary key;
# 생년월일 컬럼 텍스트 -> date 타입으로 변경
# alter table members change 생년월일 생년월일 DATE null;
# alter table members drop column 당선횟수;
# alter table members drop column 선거구;
#alter table members change column '취미, 특기' 취미특기;

###where, having 차이###
# where-> select *from 테이블명 where 조건절 : from 뒤 어디나
# having -> select *from 테이블명 group by 필드명 having 조건절 : group by 뒤

select * from members;
#1. 나이 순으로 desc id, 이름, 나이, 정당
select id, 이름 , 나이, 정당 from members order by 나이 desc;
#2. 나이가 60~80 id, 이름 , 나이, 정당 , 취미특기
select id, 이름, 나이, 정당, 취미특기 from members
where 나이>=60 and 나이<=80;
#where 나이 between 60 and 80;

#2.1 나이가 20~40 id, 이름 나이, 정당, 취미특기
select id, 이름, 나이, 정당, 취미특기 from members
where 나이 >=20 and 나이 <=40;
#where 나이 between 20 and 40;

#3. 취미특기가 없는 member 가져오기
select * from members where 취미특기 ='';
#3.1 취미특기가 없는 member의 취미특기 컬럼 값을 '없음'으로 업데이트
update members set 취미특기='없음' where 취미특기 ='';

#substr, substring
#substr(str, pos, len) : str에서 pos번째 위치에서 len개의 문자읽어들인다
#substring(str, pos, len)
#4. 이름 홍길동 -> 홍 만 빼기 substring
select *from members where substr(이름, 1, 1)='홍';
select substring(이름, 1,1) as 성 from members;
#4.1 이름의 각 성 몇명 (성씨별 카운트) 김 10...
select substring(이름, 1,1) as 성, count(*) as 갯수 from members
group by 성 order by 갯수 DESC;

select 정당, count(*) from members where substr(이름, 1, 1)='홍' group by 정당;

#5. 소속위원회 문자열 중 '보건복지' 인 멤버 가져오기
select * from members where substr(소속위원회, 1, 4)='보건복지';
#5.1 소속위원회 문자열 중 '보건복지' 이거나 '법제사법' sort 소속위원회 asc
select * from members where substr(소속위원회, 1, 4)= '보건복지' or substr(소속위원회, 1, 4)= '법제사법'
order by 소속위원회 ASC;
select 이름,정당,소속위원회 from members
where 소속위원회 like '%보건복지%' or 소속위원회 like '%법제사법%'
order by 소속위원회;

#6. 비서가 4명인 member
#subquery 사용 - 2개의 쿼리를 사용
##비서 문제가 뭔지도 모르겠음..

#7. 더불어민주당, 초선, 경기 member 가져오기
select * from members where 정당='더불어민주당'and 당선횟수='초선'and 선거구='경기';
#7.1 미래통합당, 초선, 경기 member 가져오기
select * from members where 정당='미래통합당'and 당선횟수='초선'and 선거구='경기';
#7.2 정달별로 초선, 경기 인 member 가 몇명인지 가져오기
select * from members where 정당 in('더불어민주당', '미래통합당') and 당선횟수='초선'
and 선거구='경기' group by 정당;

