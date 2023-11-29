-- Visualização df_listings_bronze com as linhas distintas
WITH df_listings_bronze AS (
    SELECT DISTINCT *
    FROM public.df_listings_bronze
)

-- Configuração para a visualização
{{ config(
    materialized='table',
    tags=['silver']
) }}

-- Dados da visualização
SELECT *
FROM df_listings_bronze