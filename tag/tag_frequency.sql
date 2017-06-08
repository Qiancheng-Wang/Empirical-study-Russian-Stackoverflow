insert into russiantagsinrussian
select * from russiantags where TagName like "%б%" or  TagName like"%в%" or TagName like "%г%" 
or  TagName like"%д%" or  TagName like"%е%" or  TagName like"%ё%" or TagName like "%ж%" or  TagName like"%з%" 
or  TagName like"%и%" or  TagName like"%й%" or  TagName like"%к%" or  TagName like"%л%" or  TagName like"%м%" 
or TagName like "%н%" or  TagName like"%о%" or  TagName like"%п%" or  TagName like"%р%" or  TagName like"%с%" 
or  TagName like"%т%" or  TagName like"%у%"or  TagName like"%ф%" or  TagName like"%х%" or  TagName like"%ц%" 
or TagName like "%ч%" or  TagName like"%ш%" or  TagName like"%щ%"or  TagName like"%ъ%"or  TagName like"%ы%" 
or  TagName like"%ь%" or  TagName like"%я%" or  TagName like"%ю%" or  TagName like"%э%";

insert into overlaptags
select * from stacktags where TagName in  (select tagname from russiantags where TagName not in (select tagname from russiantagsinrussian));

select sum(count) from stacktags ;

alter table stacktags add frequncy float;


SET SQL_SAFE_UPDATES = 0;
update russiantags set frequncy= count/319186 where tagname in (select TagName from overlaptags);
SET SQL_SAFE_UPDATES = 1;

SET SQL_SAFE_UPDATES = 0;
update stacktags set frequncy= count/39987153 where tagname in (select TagName from overlaptags);
SET SQL_SAFE_UPDATES = 1;


select * from russiantags;
select * from stacktags;

ALTER TABLE overlaptags change  Count  stackcount varchar(30);
alter table overlaptags add russiancount float;
alter table overlaptags add russian_frequncy float;
alter table overlaptags add stack_frequncy float;

update overlaptags set russiancount =(select Count from russiantags where overlaptags.tagname = russiantags.TagName);

select sum(russiancount) from overlaptags where tagname in (select TagName from overlaptags);
select sum(stackcount) from overlaptags where tagname in (select TagName from overlaptags);

SET SQL_SAFE_UPDATES = 0;
update overlaptags set russian_frequncy= russiancount/259284 where true;
update overlaptags set stack_frequncy= stackcount/26880174 where true;
SET SQL_SAFE_UPDATES = 1;

select * from overlaptags where stackcount - russiancount >0;

select sum(stackcount) from overlaptags;

select * from russiantagsinrussian;

