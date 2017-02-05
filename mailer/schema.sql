drop table if exists datasets;
create table datasets (
  id integer primary key autoincrement,
  name text not null,
  data text not null,
  creation_date date, 
  last_updated date
);