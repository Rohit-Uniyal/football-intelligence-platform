SELECT
    PLAYER_ID,
    PLAYER_NAME,
    TEAM_ID,
    TEAM_NAME,

    APPEARANCES,
    GOALS,
    ASSISTS,
    SHOTS,
    SHOTS_ON_TARGET,

    SHOT_ACCURACY_PCT,
    GOAL_CONVERSION_PCT,

    (
        GOALS * 5
        + ASSISTS * 3
        + SHOTS_ON_TARGET * 1.5
    ) AS ATTACKING_SCORE

FROM {{ ref('fact_player_performance') }}

WHERE APPEARANCES >= 10