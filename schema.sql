drop table if exists video;
drop table if exists image;
drop table if exists word;

create table video(
    no int not null auto_increment primary key,
    outerpath varchar(256),
    localpath varchar(256),
    extender varchar(16), 
    postdate datetime
);

create table image(
    no int not null auto_increment primary key,
    owner int references video(no),
    title text not null,
    caption varchar(256),
    localpath varchar(256),
    postdate datetime
);

create table word(
    no int not null auto_increment primary key,
    owner int not null references image(no),
    content varchar(128),
    postdate datetime
);