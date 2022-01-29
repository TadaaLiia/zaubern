$description
the file description

$start
-- a create table instruction
create table player (
	game_id 	VARCHAR(255) primary key,
	player_id 	VARCHAR(255) primary key,
	r1 			INT,
	r2 			INT,
	r3 			INT,
	r4 			INT,
	r5 			INT,
	r6 			INT,
	r7 			INT,
	r8 			INT,
	r9 			INT,
	r10 		INT,
	r11 		INT,
	r12 		INT,
	r13 		INT,
	r14 		INT,
	r15 		INT,
	r16 		INT,
	r17 		INT,
	r18 		INT,
	r19 		INT,
	r20 		INT
);

$start
-- copy csv file in db
COPY player
FROM '../data/player.csv'
WITH(
	DELIMIER ',',
	FORMAT CSV,
	HEADER
);

$kill
-- the kill section, which in this case would contain the drop table statement
drop table player;