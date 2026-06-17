SELECT
    TEAM_ID,
    TEAM_NAME,

    SUM(APPEARANCES)      AS APPEARANCES,
    SUM(GOALS)            AS GOALS,
    SUM(ASSISTS)          AS ASSISTS,
    SUM(SHOTS)            AS SHOTS,
    SUM(SHOTS_ON_TARGET)  AS SHOTS_ON_TARGET,
    SUM(YELLOW_CARDS)     AS YELLOW_CARDS,
    SUM(RED_CARDS)        AS RED_CARDS,

    ROUND(
        100 * SUM(SHOTS_ON_TARGET)
        / NULLIF(SUM(SHOTS),0),
        2
    ) AS TEAM_SHOT_ACCURACY_PCT,

    ROUND(
        100 * SUM(GOALS)
        / NULLIF(SUM(SHOTS),0),
        2
    ) AS TEAM_CONVERSION_PCT

FROM {{ ref('fact_player_performance') }}

GROUP BY
    TEAM_ID,
    TEAM_NAME