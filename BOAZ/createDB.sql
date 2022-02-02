   create table tb_youplace(
        videoID varchar(32) primary key not null,
        placeName varchar(32) primary key not null,
        viewCount int,
        publishTime datetime,
        likeCount int,
        x double(30,20),
        y double(30,20),
        category_name varchar(32),
        place_url varchar(32),
        address_6 varchar(32)
        )