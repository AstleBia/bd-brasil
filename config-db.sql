CREATE SCHEMA dados_eleitorais;

CREATE TABLE dados_eleitorais.dados_eleicao_2022 (
    id SERIAL PRIMARY KEY,
    id_municipio INT,
    sigla_uf VARCHAR(2),
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
    id_municipio INT,
    sigla_uf VARCHAR(2),
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
    id_municipio INT,
    cargo VARCHAR(20),
    nome_candidato VARCHAR (100),
    partido VARCHAR(10),
    total_votos INT
);

CREATE TABLE dados_eleitorais.resultados_eleicao_2024(
    id SERIAL PRIMARY KEY,
    id_municipio INT,
    cargo VARCHAR(20),
    nome_candidato VARCHAR (100),
    partido VARCHAR(10),
    total_votos INT
);