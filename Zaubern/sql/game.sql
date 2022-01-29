$description
the file description

$start
-- a create table instruction
create table game (
	game_id VARCHAR(255) primary key,
	player 	INT,
	p0		VARCHAR(255),
	p1		VARCHAR(255),
	p2		VARCHAR(255),
	p3		VARCHAR(255),
	p4		VARCHAR(255),
	p5 		VARCHAR(255),
	winner	VARCHAR(255)
);

$start
-- copy csv file in db
COPY game
FROM '../data/game.csv'
WITH(
	DELIMIER ',',
	FORMAT CSV,
	HEADER
);

$kill
-- the kill section, which in this case would contain the drop table statement
drop table game;