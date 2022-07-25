Entity: RainFallRadarObservation  
================================  
[Open License](https://github.com/smart-data-models//dataModel.Environment/blob/master/RainFallRadarObservation/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **The Data Model is intended to measure the water slides on a predefined area by a set of 4 Location represented by a Geo property format.**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `atmosphericPressure`: The atmospheric pressure observed measured in Hecto Pascals  - `cellsSize`: Size of each cell constituting the radar. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents **Meters**  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `dateObserved`: The date and time of this observation in ISO8601 UTC format. It can be represented by a specific time instant or by an ISO8601 interval  - `dateObservedFrom`: Observation period start date and time. See dateObserved. It can be represented by a specific time instant or by an ISO8601 interval  - `dateObservedTo`: Observation period end date and time. See dateObserved. It can be represented by a specific time instant or by an ISO8601 interval  - `description`: A description of this item  - `feelLikesTemperature`: Temperature appreciation of the item  - `gustSpeed`: A sudden burst of high-speed wind over the observed average wind speed lasting only for a few seconds.  - `id`: Unique identifier of the entity  - `illuminance`: (https://en.wikipedia.org/wiki/Illuminance) observed measured in lux (lx) or lumens per square metre (cd·sr·m−2).  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `mapScale`: Map Scale. Relationship between the length of the cellSize and its representation on the map  - `measuredArea`: Reference of the surface measured. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTK** represents Square Meters  - `name`: The name of this item.  - `numberOfCol`: Number of Cols allowing the reading of the `rainFallradarContent` attribute  - `numberOfRow`: Number of Rows allowing the reading of the `rainFallradarContent` attribute  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `rainFallRadarContent`: Path and filename which provided the information observed  - `refDevice`: Reference to a [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) which captured this observation  - `refPointOfInterest`: Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the observation  - `relativeHumidity`: Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `temperature`: Temperature of the item  - `type`: NGSI Entity type. It has to be RainFallRadarObserved  - `visibility`: Categories of visibility  - `weatherType`: Text description of the weather  - `windDirection`: Direction of the wind bet  - `windSpeed`: Intensity of the wind    
Required properties  
- `dateObserved`  - `id`  - `location`  - `rainFallRadarContent`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RainFallRadarObservation:    
  description: 'The Data Model is intended to measure the water slides on a predefined area by a set of 4 Location represented by a Geo property format.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    atmosphericPressure:    
      description: 'The atmospheric pressure observed measured in Hecto Pascals'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Hecto pascals'    
    cellsSize:    
      description: 'Size of each cell constituting the radar. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents **Meters**'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: 'The date and time of this observation in ISO8601 UTC format. It can be represented by a specific time instant or by an ISO8601 interval'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period start date and time. See dateObserved. It can be represented by a specific time instant or by an ISO8601 interval'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period end date and time. See dateObserved. It can be represented by a specific time instant or by an ISO8601 interval'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    feelLikesTemperature:    
      description: 'Temperature appreciation of the item'    
      type: number    
      x-ngsi:    
        type: Property    
    gustSpeed:    
      description: 'A sudden burst of high-speed wind over the observed average wind speed lasting only for a few seconds.'    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &rainfallradarobservation_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    illuminance:    
      description: '(https://en.wikipedia.org/wiki/Illuminance) observed measured in lux (lx) or lumens per square metre (cd·sr·m−2).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    mapScale:    
      description: 'Map Scale. Relationship between the length of the cellSize and its representation on the map'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    measuredArea:    
      description: 'Reference of the surface measured. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTK** represents Square Meters'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'square meters'    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numberOfCol:    
      description: 'Number of Cols allowing the reading of the `rainFallradarContent` attribute'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    numberOfRow:    
      description: 'Number of Rows allowing the reading of the `rainFallradarContent` attribute'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *rainfallradarobservation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    rainFallRadarContent:    
      description: 'Path and filename which provided the information observed'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) which captured this observation'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    refPointOfInterest:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the observation'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    relativeHumidity:    
      description: 'Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: 'Temperature of the item'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be RainFallRadarObserved'    
      enum:    
        - RainFallRadarObserved    
      type: string    
      x-ngsi:    
        type: Property    
    visibility:    
      anyOf:    
        - enum:    
            - veryPoor    
            - poor    
            - moderate    
            - good    
            - veryGood    
            - excellent    
          type: string    
        - minimum: 0    
          type: number    
      description: 'Categories of visibility'    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    weatherType:    
      description: 'Text description of the weather'    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text.    
        type: Property    
    windDirection:    
      description: 'Direction of the wind bet'    
      maximum: 180    
      minimum: -180    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    windSpeed:    
      description: 'Intensity of the wind'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http//schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - rainFallRadarContent    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/RainFallRadarObservation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Weather/RainFallRadarObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Example payloads    
#### RainFallRadarObservation NGSI-v2 key-values Example    
Here is an example of a RainFallRadarObservation in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:RainFallRadarObserved:RainFallRadarObserved:MNCA-RFRO-018",  
  "type": "RainFallRadarObserved",  
  "name": "MNCA-RFRO-018",  
  "alternateName": "AirPort global Observation",  
  "description": "Rain fall Radar Observation",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [[  
      [43.66,7.19],  
      [44.66,7.19],  
      [44.66,7.21],  
      [43.66,7.21],  
      [43.66,7.19]  
    ]]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport Area Coverage + 4 km distance"  
  },  
  "areaServed": "Nice Aeroport",  
  "refDevice": "urn:ngsi-ld:Device:NCE-RFRO-018",  
  "dateObserved": "2020-03-17T08:30:00Z",  
  "dateObservedFrom": "2020-03-17T08:30:00Z",  
  "dateObservedTo": "2020-03-17T08:45:00Z",  
  "rainFallRadarContent": "https://particuliers/rainFallRadar/NCE-RFRO-018-2020-03-17T08:30:00",  
  "numberOfRow": 25,  
  "numberOfCol": 48,  
  "cellsSize": 1,  
  "mapScale": "1/10.000",  
  "measuredArea": 250  
}  
```  
#### RainFallRadarObservation NGSI-v2 normalized Example    
Here is an example of a RainFallRadarObservation in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
	"id": "urn:ngsi-ld:RainFallRadarObserved:RainFallRadarObserved:MNCA-RFRO-018",  
	"type": "RainFallRadarObserved",  
	"name": {  
		"type": "Property",  
		"value": "MNCA-RFRO-018"  
	},  
	"alternateName": {  
		"type": "Property",  
		"value": "AirPort  global Observation"  
	},  
	"description": {  
		"type": "Property",  
		"value": "Rain fall Radar Observation"  
	},  
	"location": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "polygon",  
			"coordinates": [[  
				[43.66, 7.19],  
				[44.66, 7.19],  
				[44.66, 7.21],  
				[43.66, 7.21],  
				[43.66, 7.19]  
			]]  
		}  
	},  
	"address": {  
		"type": "Property",  
		"value": {  
			"addressCountry": "FR",  
			"addressLocality": "Nice",  
			"streetAddress": "Airport Area Coverage + 4 km distance"  
		}  
	},  
	"areaServed": {  
		"type": "Property",  
		"value": "Nice Aeroport"  
	},  
	"refDevice": {  
		"type": "Relationship",  
		"object": "urn:ngsi-ld:Device:NCE-RFRO-018"  
	},  
	"dateObserved": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-03-17T08:30:00Z"  
		}  
	},  
	"dateObservedFrom": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-03-17T08:30:00Z"  
		}  
	},  
	"dateObservedTo": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-03-17T08:45:00Z"  
		}  
	},  
	"rainFallRadarContent": {  
		"type": "Property",  
		"value": "https://particuliers/rainFallRadar/NCE-RFRO-018-2020-03-17T08:30:00"  
	},  
	"numberOfRow": {  
		"type": "Property",  
		"value": 25  
	},  
	"numberOfCol": {  
		"type": "Property",  
		"value": 48  
	},  
	"cellsSize": {  
		"type": "Property",  
		"value": 1  
	},  
	"mapScale": {  
		"type": "Property",  
		"value": "1/10.000"  
	},  
	"measuredArea": {  
		"type": "Property",  
		"value": 250  
	}  
}  
```  
#### RainFallRadarObservation NGSI-LD key-values Example    
Here is an example of a RainFallRadarObservation in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:RainFallRadarObserved:RainFallRadarObserved:MNCA-RFRO-018",  
  "type": "RainFallRadarObserved",  
  "name": {  
    "type": "Property",  
    "value": "MNCA-RFRO-018"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirPort \u0096 global Observation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Rain fall Radar Observation"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "polygon",  
      "coordinates": [  
        [  
          [  
            43.66,  
            7.19  
          ],  
          [  
            44.66,  
            7.19  
          ],  
          [  
            44.66,  
            7.21  
          ],  
          [  
            43.66,  
            7.21  
          ],  
          [  
            43.66,  
            7.19  
          ]  
        ]  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport Area Coverage + 4 km distance"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Aeroport"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Device:NCE-RFRO-018"  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "2020-03-17T08:30:00Z"  
    }  
  },  
  "dateObservedFrom": {  
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "2020-03-17T08:30:00Z"  
    }  
  },  
  "dateObservedTo": {  
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "2020-03-17T08:45:00Z"  
    }  
  },  
  "rainFallRadarContent": {  
    "type": "Property",  
    "value": "https://particuliers/rainFallRadar/NCE-RFRO-018-2020-03-17T08:30:00"  
  },  
  "numberOfRow": {  
    "type": "Property",  
    "value": 25  
  },  
  "numberOfCol": {  
    "type": "Property",  
    "value": 48  
  },  
  "cellsSize": {  
    "type": "Property",  
    "value": 1  
  },  
  "mapScale": {  
    "type": "Property",  
    "value": "1/10.000"  
  },  
  "measuredArea": {  
    "type": "Property",  
    "value": 250  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### RainFallRadarObservation NGSI-LD normalized Example    
Here is an example of a RainFallRadarObservation in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:RainFallRadarObserved:RainFallRadarObserved:MNCA-RFRO-018",  
  "type": "RainFallRadarObserved",  
  "name": "MNCA-RFRO-018",  
  "alternateName": "AirPort global Observation",  
  "description": "Rain fall Radar Observation",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          43.66,  
          7.19  
        ],  
        [  
          44.66,  
          7.19  
        ],  
        [  
          44.66,  
          7.21  
        ],  
        [  
          43.66,  
          7.21  
        ],  
        [  
          43.66,  
          7.19  
        ]  
      ]  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport Area Coverage + 4 km distance"  
  },  
  "areaServed": "Nice Aeroport",  
  "refDevice": "urn:ngsi-ld:Device:NCE-RFRO-018",  
  "dateObserved": "2020-03-17T08:30:00Z",  
  "dateObservedFrom": "2020-03-17T08:30:00Z",  
  "dateObservedTo": "2020-03-17T08:45:00Z",  
  "rainFallRadarContent": "https://particuliers/rainFallRadar/NCE-RFRO-018-2020-03-17T08:30:00",  
  "numberOfRow": 25,  
  "numberOfCol": 48,  
  "cellsSize": 1,  
  "mapScale": "1/10.000",  
  "measuredArea": 250,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units