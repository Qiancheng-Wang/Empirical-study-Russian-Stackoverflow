select sum((length(Body) - length(REPLACE(Body, 'http://' , '')))/length('http://')) from RussianPost;
select sum((length(Body) - length(REPLACE(Body, 'https://' , '')))/length('https://')) from RussianPost;
select sum((length(Body) - length(REPLACE(Body, 'http://stackoverflow.com' , '')))/length('http://stackoverflow.com')) from RussianPost;
select sum((length(Body) - length(REPLACE(Body, 'https://stackoverflow.com' , '')))/length('https://stackoverflow.com')) from RussianPost;
select sum((length(Body) - length(REPLACE(Body, 'http://ru.stackoverflow' , '')))/length('http://ru.stackoverflow')) from RussianPost;
select sum((length(Body) - length(REPLACE(Body, 'https://ru.stackoverflow' , '')))/length('https://ru.stackoverflow')) from RussianPost;

select sum((length(Text) - length(REPLACE(Text, 'http://' , '')))/length('http://')) from RuPostComment;
select sum((length(Text) - length(REPLACE(Text, 'https://' , '')))/length('https://')) from RuPostComment;
select sum((length(Text) - length(REPLACE(Text, 'http://stackoverflow.com' , '')))/length('http://stackoverflow.com')) from RuPostComment;
select sum((length(Text) - length(REPLACE(Text, 'https://stackoverflow.com' , '')))/length('https://stackoverflow.com')) from RuPostComment;
select sum((length(Text) - length(REPLACE(Text, 'http://ru.stackoverflow' , '')))/length('http://ru.stackoverflow')) from RuPostComment;
select sum((length(Text) - length(REPLACE(Text, 'https://ru.stackoverflow' , '')))/length('https://ru.stackoverflow')) from RuPostComment;
