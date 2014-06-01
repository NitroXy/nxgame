ALTER TABLE useranswers ADD INDEX user_id (user_id);
ALTER TABLE useranswers ADD FOREIGN KEY (user_id) REFERENCES user (user_id);
