select *
from UserInfo where accountid in (select accountId from Russianuserinfo) and (AboutMe like "%а%" or  AboutMe like "%б%" or  AboutMe like"%в%" or AboutMe like "%г%" 
or  AboutMe like"%д%" or  AboutMe like"%е%" or  AboutMe like"%ё%" or AboutMe like "%ж%" or  AboutMe like"%з%" 
or  AboutMe like"%и%" or  AboutMe like"%й%" or  AboutMe like"%к%" or  AboutMe like"%л%" or  AboutMe like"%м%" 
or AboutMe like "%н%" or  AboutMe like"%о%" or  AboutMe like"%п%" or  AboutMe like"%р%" or  AboutMe like"%с%" 
or  AboutMe like"%т%" or  AboutMe like"%у%"or  AboutMe like"%ф%" or  AboutMe like"%х%" or  AboutMe like"%ц%" 
or AboutMe like "%ч%" or  AboutMe like"%ш%" or  AboutMe like"%щ%"or  AboutMe like"%ъ%"or  AboutMe like"%ы%" 
or  AboutMe like"%ь%" or  AboutMe like"%я%" or  AboutMe like"%ю%" or  AboutMe like"%э%")
union
select * 
from UserInfo where accountid in (select accountId from Russianuserinfo) and (Displayname like "%а%" or  AboutMe like "%б%" or  AboutMe like"%в%" or AboutMe like "%г%" 
or  AboutMe like"%д%" or  AboutMe like"%е%" or  AboutMe like"%ё%" or AboutMe like "%ж%" or  AboutMe like"%з%" 
or  AboutMe like"%и%" or  AboutMe like"%й%" or  AboutMe like"%к%" or  AboutMe like"%л%" or  AboutMe like"%м%" 
or AboutMe like "%н%" or  AboutMe like"%о%" or  AboutMe like"%п%" or  AboutMe like"%р%" or  AboutMe like"%с%" 
or  AboutMe like"%т%" or  AboutMe like"%у%"or  AboutMe like"%ф%" or  AboutMe like"%х%" or  AboutMe like"%ц%" 
or AboutMe like "%ч%" or  AboutMe like"%ш%" or  AboutMe like"%щ%"or  AboutMe like"%ъ%"or  AboutMe like"%ы%" 
or  AboutMe like"%ь%" or  AboutMe like"%я%" or  AboutMe like"%ю%" or  AboutMe like"%э%");
