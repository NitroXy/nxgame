CREATE TABLE `questions` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`episode` INT NOT NULL,
	`level` INT NOT NULL,
	`question` TEXT NOT NULL,
	`answer` TEXT NOT NULL
);
