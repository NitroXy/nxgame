CREATE TABLE `answers` (
		`id` INT PRIMARY KEY AUTO_INCREMENT,
		`user_id` INT  NOT NULL,
		`episode` INT  NOT NULL,
		`level`	  INT  NOT NULL,
		`answer`  TEXT NOT NULL,
		`correct` INT  NOT NULL
);
