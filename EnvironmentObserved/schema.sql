/* (Beta) Export of data model EnvironmentObserved of the subject dataModel.Environment for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE EnvironmentObserved_type AS ENUM ('EnvironmentObserved');
CREATE TABLE EnvironmentObserved (address json, airQualityObserved json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, id text, location json, name text, owner json, pointOfInterest json, seeAlso json, source text, type EnvironmentObserved_type, waterQualityObserved json, weatherObserved json);