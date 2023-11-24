-- this is a throw-away code to create database schema
-- used for quick bootstraping during early development stage
-- consider to use migrations instead in the future

-- this is sqlite syntax

create table if not exists rules (
    uuid text primary key,
    group text,
    topic text,
    addresses text,
    agencies text
)

create table if not exists processed_messages (
    uuid text primary key,
    text text,
    group text,
    topic text,
    addresses text,
    agencies text
)
