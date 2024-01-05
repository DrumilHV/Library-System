-- -----------------------------------Schemas-----------------------------------
--      Books Schema

create table books(
	bookId uuid default gen_random_uuid(),
	isbn13 char(13),
	isbn10 char(10),
	title text,
	subtitle text, 
    authors text[],
    categories text[],
    thumbnail text,
    discription text,
    publication_year integer,
    avrage_rating real,
    pages integer,
    rating_count integer,
    price real
);



-- Admins

Create table admins(
    id uuid default gen_random_uuid(),
	email text not null, 
    pass text not null,
    previlage varchar(20)
);


-- Users

create table users(
    user_id uuid default gen_random_uuid(),
    user_name varchar(30) not null,
    user_email varchar(50) not null,
    user_password text not null
);

