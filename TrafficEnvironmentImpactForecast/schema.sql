/* (Beta) Export of data model TrafficEnvironmentImpactForecast of the subject dataModel.Environment for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE TrafficEnvironmentImpactForecast_type AS ENUM ('TrafficEnvironmentImpact');
CREATE TABLE TrafficEnvironmentImpactForecast (address json, alternateName text, areaServed text, co2 text, dataProvider text, dateCreated timestamp, dateIssued timestamp, dateModified timestamp, description text, id text, location json, name text, owner json, seeAlso json, source text, traffic json, type TrafficEnvironmentImpactForecast_type, validFrom timestamp, validTo timestamp, validity text);