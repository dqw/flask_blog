drop table if exists blogs;
create table blogs (
    blog_id integer primary key autoincrement,
    blog_title text not null,
    blog_content text not null,
    blog_time real not null
);

drop table if exists user;
create table user (
    user_id integer primary key autoincrement,
    user_name text not null,
    user_password text not null
);
