CREATE SCHEMA dados_eleitorais;

CREATE TABLE dados_eleitorais.dados_eleicao_2022 (
    id SERIAL PRIMARY KEY,
    id_municipio VARCHAR(7) PRIMARY KEY,
    turno SMALLINT,
    cargo VARCHAR(20),
    votos_validos INT,
    votos_brancos INT,
    votos_nulos INT,
    abstencoes INT,
    total_eleitores INT
);

CREATE TABLE dados_eleitorais.dados_eleicao_2024 (
    id SERIAL PRIMARY KEY,
    id_municipio VARCHAR(7),
    turno SMALLINT,
    cargo VARCHAR(20),
    votos_validos INT,
    votos_brancos INT,
    votos_nulos INT,
    abstencoes INT,
    total_eleitores INT
);


CREATE TABLE dados_eleitorais.resultados_eleicao_2022(
    id SERIAL PRIMARY KEY,
    id_municipio VARCHAR(7),
    cargo VARCHAR(20),
    nome_candidato VARCHAR (100),
    partido VARCHAR(10),
    total_votos INT
);

CREATE TABLE dados_eleitorais.resultados_eleicao_2024(
    id SERIAL PRIMARY KEY,
    id_municipio VARCHAR(7),
    cargo VARCHAR(20),
    nome_candidato VARCHAR (100),
    partido VARCHAR(10),
    total_votos INT
);

CREATE TABLE municipios(
    id_municipio VARCHAR(7),
    nome VARCHAR(50),
    sigla_uf VARCHAR(2),
    nome_uf VARCHAR(30),
    nome_regiao VARCHAR(30)
);