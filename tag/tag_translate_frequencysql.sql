
alter table russiantagsinrussian add translate_tagname varchar(100);


alter table russiantagsinrussian add russian_frequncy float;


select * from russiantagsinrussian;

update russiantagsinrussian set translate_tagname = 'Prox' where russiantagsinrussian.tagname= thistagname;


ALTER TABLE russiantagsinrussian CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;

ALTER TABLE russiantagsinrussian MODIFY tagname VARCHAR(30) CHARACTER SET koi8r COLLATE koi8r_general_ci;

select * from russiantagsinrussian ;

select * from russiantagsinrussian where translate_tagname in (select tagname from  russiantags);
select * from russiantagsinrussian where translate_tagname in (select tagname from  stacktags);

