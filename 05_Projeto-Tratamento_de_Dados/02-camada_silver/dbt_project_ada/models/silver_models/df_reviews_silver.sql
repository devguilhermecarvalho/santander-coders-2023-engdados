-- Visualização df_reviews_silver com as linhas distintas
WITH df_reviews_bronze AS (
    SELECT DISTINCT *
    FROM public.df_reviews_bronze
)

-- Configuração para a visualização
{{ config(
    materialized='table',
    tags=['silver']
) }}

-- Dados da visualização
SELECT *
FROM df_reviews_silver