CREATE TABLE `user` (
		`user_id` INT PRIMARY KEY,
		`username` TEXT NOT NULL,
		`name` TEXT NOT NULL,
		`admin` BOOLEAN NOT NULL DEFAULT FALSE
) Engine=InnoDB;
