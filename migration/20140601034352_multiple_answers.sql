CREATE TABLE `questionanswers` (
        `id` INT PRIMARY KEY AUTO_INCREMENT,
        `ans_id` INT NOT NULL,
        `answer` text,
        CONSTRAINT FOREIGN KEY(ans_id) 
        REFERENCES questions(id) ON DELETE cascade);
