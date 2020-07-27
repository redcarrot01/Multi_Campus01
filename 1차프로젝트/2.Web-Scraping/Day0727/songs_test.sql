select * from songs where artist ='이하이';
#1. release_date 순서대로 descending 정렬, name, artist album , release_date, gnere
select name, artist, album, release_date, genre from songs order by release_date desc;
#2. release_date가 2020 -07-01 인  name, artist album , release_date, gnere 가져오기
select name, artist, album, release_date, genre
from songs
where release_date>'2020-07-01'
order by release_date desc;
#3. release_date가 2020-07-01 이후에 발매되고
#genre  댄스인 name, artist album , release_date, gnere 가져오기
select name, artist, album, release_date, genre
from songs
where release_date>'2020-07-01' and genre ='댄스'
order by release_date desc;
#4.1 중복되지 않은 name 값 가져오기
select distinct name from songs;
#4.1.1 artist 별 row count
select artist, count(*) as cnt from songs group by artist order by cnt desc;
#4.1.2 cnt가 3곡 이상만 출력
select artist, count(*) as cnt from songs group by artist having cnt>=3 order by cnt desc;
#4.2. 중복되지 않은 genre 값 가져오기
select distinct genre from songs;
#4.2.2 genre 별 row count
select genre, count(*) as cnt from songs group by genre order by cnt desc;


# id 컬럼을 modify - not null, auto_increment, primary key
alter table songs modify id int not null auto_increment primary key;
#insert
insert into songs (name, artist, album, release_date, genre, lyric) value ('아침이슬', '양희은', '명작6070','2004-08-14','발라드','룰루');
# id 컬럼은 insert 할때 주는 것이 아니다
select *from songs;
#update
# 쿼리를 잘 줘서 응답시간 짧게
update songs set release_date = '2006-07-01', lyric='아침이슬가사 수정' where id=101;
delete from songs where id='101';

select distinct album from songs;
# ost songs 가져오기,  name, artist album , release_date, gnere 가져오기
select name, artist, album, release_date, genre
from songs
where album like '%OST %';
select name, artist, album, release_date, genre
from songs
where album not like '%OST %';

select * from songs limit 10;