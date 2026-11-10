-- Staging model for FARS accident data cleaning and standardization
WITH source_data AS (
    SELECT 
        STATE,
        ST_CASE,
        VEH_NO,
        -- Add primary temporal or spatial transformations below
        -- e.g., CAST(CATHOUSE AS INT) as cathouse
    FROM {{ ref('accident') }} -- or your raw source table
),

cleaned AS (
    SELECT DISTINCT
        STATE AS state_code,
        ST_CASE as case_number,
        VEH_NO as vehicle_number
    FROM source_data
    WHERE ST_CASE IS NOT NULL
)

SELECT * FROM cleaned;