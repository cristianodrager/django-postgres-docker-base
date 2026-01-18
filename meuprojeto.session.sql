#listar tabelas do banco de dados
SELECT table_name FROM information_schema.tables WHERE table_schema='public';