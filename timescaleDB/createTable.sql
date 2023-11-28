CREATE TABLE spot (
    "OpenTime"      TIMESTAMPTZ     NOT NULL,
    "Instrument"    VARCHAR(10)     NOT NULL,
    "Open"          NUMERIC(18, 8)  NOT NULL,
    "High"          NUMERIC(18, 8)  NOT NULL,
    "Low"           NUMERIC(18, 8)  NOT NULL,
    "Close"         NUMERIC(18, 8)  NOT NULL,
    "Volume"        NUMERIC(18, 8)  NOT NULL
);

SELECT create_hypertable('spot', 'OpenTime');