DROP DATABASE IF EXISTS marketdata;
CREATE DATABASE marketdata KEEP 365000;
USE marketdata;
CREATE STABLE spot (OpenTime timestamp, Open DOUBLE, High DOUBLE, Low DOUBLE, Close DOUBLE, Volume DOUBLE) TAGS (Instrument VARCHAR(128));