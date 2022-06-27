-- first creat a user 'dheeraj'
-- then create a database 'superhero'.

create table heroes(
       id serial primary key,
       name text not null,
       gender varchar(1) not null
);
