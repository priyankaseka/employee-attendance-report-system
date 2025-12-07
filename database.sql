create database attendance
use attendance
create table emp(emp_id int primary key,name varchar(50))
create table attendance(id int auto_increment primary key,emp_id int,date date,status varchar(20),foreign key(emp_id) references emp(emp_id))
select * from emp
select * from attendance
drop database attendance
show databases

