CREATE TABLE RusUserInStack (
    Id VARCHAR(10),
    Reputation VARCHAR(10),
    CreationDate VARCHAR(30),
    DisplayName VARCHAR(100),
    LastAccessDate VARCHAR(30),
    WebsiteUrl TEXT,
    Location TEXT,
    AboutMe LONGTEXT,
    Views VARCHAR(30),
    UpVotes VARCHAR(30),
    DownVotes VARCHAR(30),
    AccountId VARCHAR(20)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8;


Insert into RusUserInStack(Id,Reputation,CreationDate,DisplayName, LastAccessDate, WebsiteUrl, Location, AboutMe, Views, UpVotes, DownVotes,Accountid)
select Id,Reputation,CreationDate,DisplayName, LastAccessDate, WebsiteUrl, Location, AboutMe, Views, UpVotes, DownVotes,Accountid
from UserInfo where AboutMe like "%а%" or  AboutMe like "%б%" or  AboutMe like"%в%" or AboutMe like "%г%" 
or  AboutMe like"%д%" or  AboutMe like"%е%" or  AboutMe like"%ё%" or AboutMe like "%ж%" or  AboutMe like"%з%" 
or  AboutMe like"%и%" or  AboutMe like"%й%" or  AboutMe like"%к%" or  AboutMe like"%л%" or  AboutMe like"%м%" 
or AboutMe like "%н%" or  AboutMe like"%о%" or  AboutMe like"%п%" or  AboutMe like"%р%" or  AboutMe like"%с%" 
or  AboutMe like"%т%" or  AboutMe like"%у%"or  AboutMe like"%ф%" or  AboutMe like"%х%" or  AboutMe like"%ц%" 
or AboutMe like "%ч%" or  AboutMe like"%ш%" or  AboutMe like"%щ%"or  AboutMe like"%ъ%"or  AboutMe like"%ы%" 
or  AboutMe like"%ь%" or  AboutMe like"%я%" or  AboutMe like"%ю%" or  AboutMe like"%э%"
union
select Id,Reputation,CreationDate,DisplayName, LastAccessDate, WebsiteUrl, Location, AboutMe, Views, UpVotes, DownVotes,Accountid
 from UserInfo where DisplayName like "%а%" or  DisplayName like "%б%" or  DisplayName like"%в%" or DisplayName like "%г%" 
or  DisplayName like"%д%" or  DisplayName like"%е%" or  DisplayName like"%ё%" or DisplayName like "%ж%" or  DisplayName like"%з%" 
or  DisplayName like"%и%" or  DisplayName like"%й%" or  DisplayName like"%к%" or  DisplayName like"%л%" or  DisplayName like"%м%" 
or DisplayName like "%н%" or  DisplayName like"%о%" or  DisplayName like"%п%" or  DisplayName like"%р%" or  DisplayName like"%с%" 
or  DisplayName like"%т%" or  DisplayName like"%у%"or  DisplayName like"%ф%" or  DisplayName like"%х%" or  DisplayName like"%ц%" 
or DisplayName like "%ч%" or  DisplayName like"%ш%" or  DisplayName like"%щ%"or  DisplayName like"%ъ%"or  DisplayName like"%ы%" 
or  DisplayName like"%ь%" or  DisplayName like"%я%" or  DisplayName like"%ю%" or  DisplayName like"%э%"
union
select Id,Reputation,CreationDate,DisplayName, LastAccessDate, WebsiteUrl, Location, AboutMe, Views, UpVotes, DownVotes,Accountid
 from UserInfo where Location like "%Russia%" or Location like "%Moscow%" or Location like "%kazan%" or Location like "%Novosibirsk%" 
or Location like "%Perm%" or Location like "%stavaropol%" or Location like "%Irkutsk%" or Location like "%Suchi%" 
or  Location like "%Asbest%" or Location like"%Yekaterinburg%" or Location like "%Ural%" or Location like "%Vladivostok%" 
or Location like "%Orenburg%" or Location like "%Rostov%" or Location like "%Novorossiysk%" or Location like "%Barnual%"
or Location like "%Belgorod%" or Location like "%Cheboksary%" or Location like "%Chelyabinsk%" or Location like "%Donetsk%"
or Location like "%Izhevsk%" or Location like "%Kaliningrad%" or Location like "%Kaluga%" or Location like "%Kemerovo%"
or Location like "%Klin%" or Location like "%Kotlas%" or Location like "%Krasnodar%"or Location like "%Kurgan%"
or Location like "%Leninsk%" or Location like "%Magnitogorsk%" or Location like "%Omsk%"or Location like "%Protvino%"
or Location like "%Samara%" or Location like "%Tambov%" or Location like "%Tomsk%"or Location like "%saransk%"
or Location like "%saratov%" or Location like "%Simpheropol%" or Location like "%snezhinsk%" or Location like "%Tyumen%"
or Location like "%Ufa%";

select * from RusUserInStack where AccountId not in (select AccountId from FinalCompare) order by AccountId;
select * from RusUserInStack where AccountId in (select AccountId from FinalCompare) order by AccountId;


select *
 from UserInfo where (Location like "%Russia%" or Location like "%Moscow%" or Location like "%kazan%" or Location like "%Novosibirsk%" 
or Location like "%Perm%" or Location like "%stavaropol%" or Location like "%Irkutsk%" or Location like "%Suchi%" 
or  Location like "%Asbest%" or Location like"%Yekaterinburg%" or Location like "%Ural%" or Location like "%Vladivostok%" 
or Location like "%Orenburg%" or Location like "%Rostov%" or Location like "%Novorossiysk%" or Location like "%Barnual%"
or Location like "%Belgorod%" or Location like "%Cheboksary%" or Location like "%Chelyabinsk%" or Location like "%Donetsk%"
or Location like "%Izhevsk%" or Location like "%Kaliningrad%" or Location like "%Kaluga%" or Location like "%Kemerovo%"
or Location like "%Klin%" or Location like "%Kotlas%" or Location like "%Krasnodar%"or Location like "%Kurgan%"
or Location like "%Leninsk%" or Location like "%Magnitogorsk%" or Location like "%Omsk%"or Location like "%Protvino%"
or Location like "%Samara%" or Location like "%Tambov%" or Location like "%Tomsk%"or Location like "%saransk%"
or Location like "%saratov%" or Location like "%Simpheropol%" or Location like "%snezhinsk%" or Location like "%Tyumen%"
or Location like "%Ufa%") and AccountId in (select AccountId from FinalCompare) order by AccountId;
;
