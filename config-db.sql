CREATE SCHEMA dados_eleitorais;

CREATE TABLE dados_eleitorais.dados_eleicao_2022 (
    id SERIAL PRIMARY KEY,
    id_municipio VARCHAR(7) REFERENCES municipios(id_municipio),
    turno SMALLINT,
    cargo VARCHAR(35),
    votos_validos INT,
    votos_brancos INT,
    votos_nulos INT,
    abstencoes INT,
    total_eleitores INT
);

CREATE TABLE dados_eleitorais.dados_eleicao_2024 (
    id SERIAL PRIMARY KEY,
    id_municipio VARCHAR(7) REFERENCES municipios(id_municipio),
    turno SMALLINT,
    cargo VARCHAR(35),
    votos_validos INT,
    votos_brancos INT,
    votos_nulos INT,
    abstencoes INT,
    total_eleitores INT
);


CREATE TABLE dados_eleitorais.resultados_eleicao_2022(
    id SERIAL PRIMARY KEY,
    id_municipio VARCHAR(7) REFERENCES municipios(id_municipio),
    turno SMALLINT,
    cargo VARCHAR(35),
    nome_candidato VARCHAR (100),
    sigla_partido VARCHAR(30),
    resultado VARCHAR(30),
    total_votos INT
);

CREATE TABLE dados_eleitorais.resultados_eleicao_2024(
    id SERIAL PRIMARY KEY,
    id_municipio VARCHAR(7) REFERENCES municipios(id_municipio),
    turno SMALLINT,
    cargo VARCHAR(35),
    nome_candidato VARCHAR (100),
    sigla_partido VARCHAR(30),
    resultado VARCHAR(30),
    total_votos INT
);

CREATE TABLE municipios(
    id_municipio VARCHAR(7) PRIMARY KEY,
    nome VARCHAR(50),
    sigla_uf VARCHAR(2),
    nome_uf VARCHAR(30),
    nome_regiao VARCHAR(30)
);