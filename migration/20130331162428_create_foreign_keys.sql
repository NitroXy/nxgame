ALTER TABLE answers ADD INDEX user_id (user_id);
ALTER TABLE answers ADD FOREIGN KEY (user_id) REFERENCES user (user_id);
