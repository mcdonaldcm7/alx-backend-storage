-- Creates an index `idx_name_first` on the table `names` and the first letter of `name`
ALTER TABLE names
MODIFY COLUMN name CHAR(1);

CREATE INDEX idx_name_first ON names (name(1));
