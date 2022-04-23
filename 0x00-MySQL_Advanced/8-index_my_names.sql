-- creates an index idx_name_first on the table names and the first letter of name.
-- Requirements:
-- Import this table dump: [names.sql.zip](https://alx-intranet.hbtn.io/rltoken/BluyCCIIfw0NqcjqUiUdEw)
-- Only the first letter of name must be indexed

CREATE INDEX idx_name_first ON names(name(1));
