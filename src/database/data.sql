-- data.sql

INSERT INTO users (age, department, salary, experience) VALUES
(32, 'Sales', 60000, 4),
(24, 'Marketing', 30000, 2),
(45, 'Sales', 80000, 10),
(29, 'HR', 40000, 5),
(22, 'Marketing', 25000, 1);



INSERT INTO rules (rule_text) VALUES
('((age > 30 AND department = ''Sales'') OR (age < 25 AND department = ''Marketing'')) AND (salary > 50000 OR experience > 5)'),
('((age > 30 AND department = ''Marketing'') AND (salary > 20000 OR experience > 5))');
