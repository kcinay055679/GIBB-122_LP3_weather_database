drop database if exists weather;
create database weather;
use weather;

create table conditions(
	condition_code int primary key not null,
    text text not null,
    icon_link text not null
);

CREATE TABLE day_weather (
    date Date primary key not null default current_timestamp,
    temp_c float not null,
    wind_kph float not null,
    wind_degree int not null,
    wind_direction varchar(3) not null,
    temp_c_feels_like float not null,
    condition_code int not null,
    foreign key (condition_code) REFERENCES conditions(condition_code)
);
