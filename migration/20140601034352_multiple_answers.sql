CREATE TABLE `questionanswers` (
		`id` INT PRIMARY KEY AUTO_INCREMENT,
		`question_id` INT NOT NULL,
		`answer` text,
		CONSTRAINT FOREIGN KEY(question_id) 
		REFERENCES questions(id) ON DELETE cascade);
