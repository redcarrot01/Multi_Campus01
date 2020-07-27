desc members;
#drop table members;

select 이름,나이,사무실전화 from members where 사무실전화 is null or 사무실전화 = '';
select distinct 정당 from members;
select 정당,count(*) as 정당수 from members group by 정당 order by 정당수 desc;

select id,이름 from members;

#ALTER TABLE members MODIFY id int NOT NULL AUTO_INCREMENT PRIMARY KEY;
#ALTER TABLE members CHANGE 생년월일 생년월일 DATE NULL;

select id,이름,나이,정당 from members order by 나이 desc;
select 이름,나이,정당,취미특기 from members where 나이 between 60 and 80;
select 이름,나이,정당,취미특기 from members where 나이 between 20 and 40;

update members set 취미특기 = '없음' where 취미특기 = '';
select * from members where 취미특기 = '';
select * from members where 취미특기 = '없음';

select substring(이름, 1, 1) as 성 from members;
select substring(이름, 1, 1) as 성, count(*) as 갯수 from members group by 성 order by 갯수 desc;

select distinct 소속위원회 from members;
select 이름,정당,소속위원회 from members where 소속위원회 like '%보건복지%' or 소속위원회 like '%법제사법%' order by 소속위원회;

select 이름,비서관,비서 from members;
select (LENGTH(비서)),비서 from members;
select (LENGTH(비서)),LENGTH(REPLACE(비서, ',', '')),(LENGTH(비서) - LENGTH(REPLACE(비서, ',', '')) + 1), 비서 from members;
# select (LENGTH(비서)),LENGTH(REPLACE(비서, ',', '')),(LENGTH(비서) - LENGTH(REPLACE(비서, ',', '')) + 1) as cnt, 비서 from members
# where cnt = 4;

SELECT (LENGTH(비서) - LENGTH(REPLACE(비서, ',', '')) + 1) as value_count FROM members;

select m.id,m.이름,m.비서,n.value_count
  from members m,
       (SELECT id,(LENGTH(비서) - LENGTH(REPLACE(비서, ',', '')) + 1) as value_count FROM members) n
where m.id = n.id
  and n.value_count = 4;

select * from members where 생년월일 > '1985-01-01' order by 생년월일;

select distinct 정당 from members;

select id,정당 from members
where 정당 in ('더불어민주당', '미래통합당')
  and 당선횟수 = '초선'
  and 선거구 = '경기'
order by 정당;

select 정당,count(*) from members
        where 정당 in ('더불어민주당', '미래통합당')
          and 당선횟수 = '초선'
          and 선거구 = '경기'
group by 정당;

select * from members where 이메일 like '%naver.com%';