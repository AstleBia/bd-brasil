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
    nome_urna VARCHAR (100),
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
    nome_urna VARCHAR (100),
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

CREATE SCHEMA dicionarios;

CREATE TABLE dicionarios.dados_eleicao(
    id SERIAL PRIMARY KEY,
    coluna VARCHAR(20),
    tipo VARCHAR(15),
    chave VARCHAR(2),
    descricao TEXT,
    fonte TEXT
);

INSERT INTO dicionarios.dados_eleicao (coluna,tipo,chave,descricao,fonte)
VALUES ('id', 'SERIAL','PK','Identificador único do registro',NULL),
        ('id_municipio', 'VARCHAR(7)','FK','Código identificador do IBGE 7 dígitos', 'basedosdados.br_tse_eleicoes.detalhes_votacao_municipio'),
        ('turno','SMALLINT',NULL,'Turno','basedosdados.br_tse_eleicoes.detalhes_votacao_municipio'),
        ('cargo','VARCHAR(35)',NULL,'Cargo','basedosdados.br_tse_eleicoes.detalhes_votacao_municipio'),
        ('votos_validos','INT',NULL,'Número de votos válidos','basedosdados.br_tse_eleicoes.detalhes_votacao_municipio'),
        ('votos_brancos','INT',NULL,'Número de votos brancos','basedosdados.br_tse_eleicoes.detalhes_votacao_municipio'),
        ('votos_nulos','INT',NULL,'Número de votos nulos','basedosdados.br_tse_eleicoes.detalhes_votacao_municipio'),
        ('abstencoes','INT',NULL,'Número de abstenções','basedosdados.br_tse_eleicoes.detalhes_votacao_municipio'),
        ('total_eleitores','INT',NULL,'Número de eleitores aptos','basedosdados.br_tse_eleicoes.detalhes_votacao_municipio');

CREATE TABLE dicionarios.resultados_eleicao(
    id SERIAL PRIMARY KEY,
    coluna VARCHAR(20),
    tipo VARCHAR(15),
    chave VARCHAR(2),
    descricao TEXT,
    fonte TEXT
);

INSERT INTO dicionarios.resultados_eleicao (coluna,tipo,chave,descricao,fonte)
VALUES ('id','SERIAL','PK','Identificdor único do registro', NULL),
        ('id_municipio','VARCHAR(7)','FK','Código identificador do IBGE 7 dígitos','basedosdados.br_tse_eleicoes.resultados_candidato_municipio'),
        ('turno','SMALLINT',NULL,'Turno','basedosdados.br_tse_eleicoes.resultados_candidato_municipio'),
        ('cargo','VARCHAR(35)',NULL,'Cargo','basedosdados.br_tse_eleicoes.resultados_candidato_municipio'),
        ('nome_candidato','VARCHAR(100)',NULL,'Nome do candidato','basedosdados.br_tse_eleicoes.candidatos'),
        ('sigla_partido','VARCHAR(30)',NULL,'Sigla do partido','basedosdados.br_tse_eleicoes.resultados_candidato_municipio'),
        ('resultado','VARCHAR(30)',NULL,'Resultado do candidato na eleicao','basedosdados.br_tse_eleicoes.resultados_candidato_municipio'),
        ('total_votos','INT',NULL,'Número total de votos para este candidato','basedosdados.br_tse_eleicoes.resultados_candidato_municipio');

CREATE TABLE dicionarios.municipios(
    id SERIAL PRIMARY KEY,
    coluna VARCHAR(20),
    tipo VARCHAR(15),
    chave VARCHAR(2),
    descricao TEXT,
    fonte TEXT
);


INSERT INTO dicionarios.municipios (coluna,tipo,chave,descricao,fonte)
VALUES ('id_municipio','VARCHAR(7)','PK','Código identificador do IBGE 7 dígitos','basedosdados.br_bd_diretorios_brasil.municipio'),
        ('nome','VARCHAR(50)',NULL,'Nome do município','basedosdados.br_bd_diretorios_brasil.municipio'),
        ('sigla_uf','VARCHAR(2)',NULL,'Sigla da Unidade da Federação','basedosdados.br_bd_diretorios_brasil.municipio'),
        ('nome_uf','VARCHAR(30)',NULL,'Nome da Unidade da Federação','basedosdados.br_bd_diretorios_brasil.municipio'),
        ('nome_regiao','VARCHAR(30)',NULL,'Nome da grande região brasileira','basedosdados.br_bd_diretorios_brasil.municipio');

CREATE SCHEMA panorama_economico;

CREATE TABLE panorama_economico.pib_setores(
    id SERIAL PRIMARY KEY,
    id_municipio VARCHAR(7) REFERENCES municipios(id_municipio),
    ano INT,
    pib_total INT,
    pib_per_capita REAL,
    va_agropecuaria INT,
    va_industria INT,
    va_servicos INT,
    participacao_agropecuaria REAL,
    participacao_industria REAL,
    participacao_servicos REAL,
);