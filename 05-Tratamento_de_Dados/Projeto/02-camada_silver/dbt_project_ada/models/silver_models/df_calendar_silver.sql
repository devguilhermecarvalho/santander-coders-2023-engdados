-- Visualização df_calendar_bronze com as linhas distintas
WITH df_calendar_bronze AS (
    SELECT DISTINCT *
    FROM public.df_calendar_bronze
)

-- Configuração para a visualização
{{ config(
    materialized='table',
    tags=['silver']
) }}

-- Dados da visualização
SELECT *
FROM df_calendar_bronze