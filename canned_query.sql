-- SQLite
CREATE TABLE IF NOT EXISTS ADDRESS (
    symbol_1 TEXT NOT NULL,
    symbol_2 TEXT NOT NULL,
    symbol_3 TEXT NOT NULL,
    symbol_4 TEXT NOT NULL,
    symbol_5 TEXT NOT NULL,
    symbol_6 TEXT NOT NULL,
    symbol_7 TEXT NOT NULL,
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CONSTRAINT con UNIQUE (symbol_1,symbol_2,symbol_3,symbol_4,symbol_5,symbol_6,symbol_7)  
);

CREATE TABLE IF NOT EXISTS RINGS (
    origin_key TEXT NOT NULL,
    origin_value  TEXT NOT NULL,
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CONSTRAINT con UNIQUE (origin_key, origin_value)
);

select * from rings

drop table ADDRESS
select * from ADDRESS

delete from ADDRESS where symbol_1 = 'sol2'





SELECT * FROM ADDRESS WHERE symbol_1 = 'sol' AND symbol_2 = 'vega' AND symbol_3 = 'siruis' AND symbol_4 = 'betelgeuse' AND symbol_5 = 'polaris' AND symbol_6 = 'mira' AND symbol_7 = 'alpha centauri A';