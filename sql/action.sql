-- Criação da tabela action_types
CREATE TABLE IF NOT EXISTS action_types (
    id SERIAL PRIMARY KEY,  -- id gerado automaticamente
    name VARCHAR(100) NOT NULL
);

-- Criação da tabela action
CREATE TABLE IF NOT EXISTS action (
    id UUID PRIMARY KEY, 
    action_type INTEGER NOT NULL,  
    expect_date DATE NOT NULL,
    investment NUMERIC(15, 2) NOT NULL,
    FOREIGN KEY (action_type) REFERENCES action_types(id) 
);

-- Inserção dos tipos de ação na tabela action_types
INSERT INTO action_types (name) VALUES 
    ('Palestra'),
    ('Evento'),
    ('Apoio Gráfico');
