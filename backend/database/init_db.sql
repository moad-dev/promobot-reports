-- this is a throw-away code to create database schema
-- used for quick bootstraping during early development stage
-- consider to use migrations instead in the future

PRAGMA journal_mode=WAL;

create table if not exists rules (
    uuid text primary key,
    `group` text,
    topic text,
    address text,
    agencies text
);

create table if not exists processed_messages (
    uuid text primary key,
    text text,
    `group` text,
    topic text,
    is_trash bool,
    addresses text,
    agencies text
);
