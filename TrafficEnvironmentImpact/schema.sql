/* (Beta) Export of data model TrafficEnvironmentImpact of the subject dataModel.Environment for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE TrafficEnvironmentImpact_type AS ENUM ('TrafficEnvironmentImpact');
CREATE TABLE TrafficEnvironmentImpact (address json, alternateName text, areaServed text, co2 text, dataProvider text, dateCreated timestamp, dateModified timestamp, dateObservedFrom timestamp, dateObservedTo timestamp, description text, id text, location json, name text, owner json, seeAlso json, source text, traffic json, type TrafficEnvironmentImpact_type);