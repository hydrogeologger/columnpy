# the following scripts needs to be pasted in a file named **credential tb_credential_column.json**. ensure the right password is added in

{
    "comments"            : "keys -- comma separated list of telemetry keysto fetch\n startTs - unix timestamp that identifies start of the interval in milliseconds.\n endTs - unix timestamp that identifies end of the interval in milliseconds.\n interval - the aggregation interval, in milliseconds.\n agg - the aggregation function. One of MIN, MAX, AVG, SUM, COUNT, NONE.\n limit - the max amount of data points to return or intervals to process",
    "thingsboard_address" : "http://abc.uqgec.org",
    "username"            : "yuanchi.xiao@uq.net.au",
    "password"            : "abc",
    "keys"                : "all",
    "_keys_comments"      : "if keys==all, all the keys will be extracted",
    "startTs"             : "",
    "_startTs"            : "2021/May/13 16:00",
    "_endTs"               : "",
    "endTs"               : "2021/May/19 16:00",
    "interval"            : "",
    "limit"              : "",
    "_limit"               : "10",
    "_limit_comment"     : "if left as empty, all the data during the startts and endts will be extracted",
    "device_id"           : "8e293fa0-95d6-11eb-a6b8-9bd3ee7f132e"

}
