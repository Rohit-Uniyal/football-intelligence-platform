SELECT
    PLAYER_ID,
    PLAYER_NAME,
    TEAM_ID,
    TEAM_NAME,

    SUM(IFF(STAT_NAME = 'appearances', TRY_TO_NUMBER(STAT_VALUE), 0))      AS APPEARANCES,
    SUM(IFF(STAT_NAME = 'totalGoals', TRY_TO_NUMBER(STAT_VALUE), 0))       AS GOALS,
    SUM(IFF(STAT_NAME = 'goalAssists', TRY_TO_NUMBER(STAT_VALUE), 0))      AS ASSISTS,
    SUM(IFF(STAT_NAME = 'totalShots', TRY_TO_NUMBER(STAT_VALUE), 0))       AS SHOTS,
    SUM(IFF(STAT_NAME = 'shotsOnTarget', TRY_TO_NUMBER(STAT_VALUE), 0))    AS SHOTS_ON_TARGET,
    SUM(IFF(STAT_NAME = 'yellowCards', TRY_TO_NUMBER(STAT_VALUE), 0))      AS YELLOW_CARDS,
    SUM(IFF(STAT_NAME = 'redCards', TRY_TO_NUMBER(STAT_VALUE), 0))         AS RED_CARDS,

    ROUND(
        100 * SUM(IFF(STAT_NAME = 'shotsOnTarget', TRY_TO_NUMBER(STAT_VALUE), 0))
        / NULLIF(
            SUM(IFF(STAT_NAME = 'totalShots', TRY_TO_NUMBER(STAT_VALUE), 0)),
            0
        ),
        2
    ) AS SHOT_ACCURACY_PCT,

    ROUND(
        100 * SUM(IFF(STAT_NAME = 'totalGoals', TRY_TO_NUMBER(STAT_VALUE), 0))
        / NULLIF(
            SUM(IFF(STAT_NAME = 'totalShots', TRY_TO_NUMBER(STAT_VALUE), 0)),
            0
        ),
        2
    ) AS GOAL_CONVERSION_PCT

FROM {{ ref('stg_player_stat_details') }}

GROUP BY
    PLAYER_ID,
    PLAYER_NAME,
    TEAM_ID,
    TEAM_NAME