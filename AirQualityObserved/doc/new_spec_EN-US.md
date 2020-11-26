Entity: AirQualityObserved  
==========================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **An observation of air quality conditions at a certain place and time.**  

## List of properties  

- `address`: The mailing address.  - `airQualityIndex`:   - `airQualityLevel`:   - `alternateName`: An alternative name for this item  - `areaServed`:   - `as`: Arsenic  - `c6h6`: Benzene  - `cd`: Cadmium  - `co`: Carbon Monoxide  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `dateObserved`:   - `description`: A description of this item  - `id`:   - `location`:   - `name`: The name of this item.  - `ni`: Nickel  - `False`: Nitrogen monoxide  - `no2`: Nitrogen dioxide  - `o3`: ozone  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `pb`: Lead  - `pm10`: Particulate matter 10 micrometers or less in diameter  - `pm25`: Particulate matter 2.5 micrometers or less in diameter  - `refDevice`:   - `refPointOfInterest`:   - `refWeatherObserved`:   - `reliability`:   - `seeAlso`:   - `sh2`: Hydrogen sulfide  - `so2`: Sulfur dioxide  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity type  - `volatileOrganicCompoundsTotal`: Alkanes <C10, ketones <C6, aldehydes <C10, carboxylic acids <C5, aspirits<C7, Alkenes <C8, Aromatics    
Required properties  
- `dateObserved`  - `id`  - `location`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AirQualityObserved:    
  description: 'An observation of air quality conditions at a certain place and time.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    airQualityIndex:    
      minimum: 0    
      type: integer    
    airQualityLevel:    
      minLength: 2    
      type: string    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      type: string    
    as:    
      description: Arsenic    
      minimum: 0    
      type: number    
    c6h6:    
      description: Benzene    
      minimum: 0    
      type: number    
    cd:    
      description: Cadmium    
      minimum: 0    
      type: number    
    co:    
      description: 'Carbon Monoxide'    
      minimum: 0    
      type: number    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateObserved:    
      type: string    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &airqualityobserved_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    ni:    
      description: Nickel    
      minimum: 0    
      type: number    
    no:    
      description: 'Nitrogen monoxide'    
      minimum: 0    
      type: number    
    no2:    
      description: 'Nitrogen dioxide'    
      minimum: 0    
      type: number    
    o3:    
      description: ozone    
      minimum: 0    
      type: number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *airqualityobserved_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    pb:    
      description: Lead    
      minimum: 0    
      type: number    
    pm10:    
      description: 'Particulate matter 10 micrometers or less in diameter'    
      minimum: 0    
      type: number    
    pm25:    
      description: 'Particulate matter 2.5 micrometers or less in diameter'    
      minimum: 0    
      type: number    
    refDevice:    
      anyOf: *airqualityobserved_-_properties_-_owner_-_items_-_anyof    
    refPointOfInterest:    
      anyOf: *airqualityobserved_-_properties_-_owner_-_items_-_anyof    
    refWeatherObserved:    
      anyOf: *airqualityobserved_-_properties_-_owner_-_items_-_anyof    
    reliability:    
      maximum: 1.0    
      minimum: 0    
      type: number    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    sh2:    
      description: 'Hydrogen sulfide'    
      minimum: 0    
      type: number    
    so2:    
      description: 'Sulfur dioxide'    
      minimum: 0    
      type: number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - AirQualityObserved    
      type: string    
    volatileOrganicCompoundsTotal:    
      description: 'Alkanes <C10, ketones <C6, aldehydes <C10, carboxylic acids <C5, aspirits<C7, Alkenes <C8, Aromatics'    
      minimum: 0    
      type: number    
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
  type: object    
```  
</details>    
## Example payloads    
#### AirQualityObserved NGSI V2 key-values Example    
Here is an example of a AirQualityObserved in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
  "type": "AirQualityObserved",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Madrid",  
    "streetAddress": "Plaza de España"  
  },  
  "dateObserved": "2016-03-15T11:00:00/2016-03-15T12:00:00",  
  "areaServed": "Brooklands",  
  "location": {  
    "type": "Point",  
    "coordinates": [-3.712247222222222, 40.423852777777775]  
  },  
  "source": "http://datos.madrid.es",  
  "typeOfLocation": "outdoor",  
  "precipitation": 0,  
  "relativeHumidity": 0.54,  
  "temperature": 12.2,  
  "windDirection": 186,  
  "windSpeed": 0.64,  
  "airQualityLevel": "moderate",  
  "airQualityIndex": 65,  
  "reliability": 0.7,  
  "CO": 500,  
  "NO": 45,  
  "NO2": 69,  
  "NOx": 139,  
  "SO2": 11,  
  "CO_Level": "moderate",  
  "refPointOfInterest": "28079004-Pza.deEspanya"  
}  
```  
#### AirQualityObserved NGSI V2 normalized Example    
Here is an example of a AirQualityObserved in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
  "type": "AirQualityObserved",  
  "dateObserved": {  
    "value": "2016-03-15T11:00:00/2016-03-15T12:00:00"  
  },  
  "areaServed": {  
    "value": "Brooklands"  
  },  
  "airQualityLevel": {  
    "value": "moderate"  
  },  
  "CO": {  
    "value": 500,  
    "metadata": {  
      "unitCode": {  
        "value": "GP"  
      }  
    }  
  },  
  "temperature": {  
    "value": 12.2  
  },  
  "NO": {  
    "value": 45,  
    "metadata": {  
      "unitCode": {  
        "value": "GQ"  
      }  
    }  
  },  
  "refPointOfInterest": {  
    "type": "Relationship",  
    "value": "28079004-Pza.deEspanya"  
  },  
  "windDirection": {  
    "value": 186  
  },  
  "source": {  
    "value": "http://datos.madrid.es"  
  },  
  "windSpeed": {  
    "value": 0.64  
  },  
  "SO2": {  
    "value": 11,  
    "metadata": {  
      "unitCode": {  
        "value": "GQ"  
      }  
    }  
  },  
  "NOx": {  
    "value": 139,  
    "metadata": {  
      "unitCode": {  
        "value": "GQ"  
      }  
    }  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-3.712247222222222, 40.423852777777775]  
    }  
  },  
  "typeOfLocation": {  
    "value": "outdoor"  
  },  
  "airQualityIndex": {  
    "value": 65  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Madrid",  
      "streetAddress": "Plaza de Espa\u00f1a"  
    }  
  },  
  "reliability": {  
    "value": 0.7  
  },  
  "relativeHumidity": {  
    "value": 0.54  
  },  
  "precipitation": {  
    "value": 0  
  },  
  "NO2": {  
    "value": 69,  
    "metadata": {  
      "unitCode": {  
        "value": "GQ"  
      }  
    }  
  },  
  "CO_Level": {  
    "value": "moderate"  
  }  
}  
```  
#### AirQualityObserved NGSI-LD key-values Example    
Here is an example of a AirQualityObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "CO": 500,  
 "CO_Level": "moderate",  
 "NO": 45,  
 "NO2": 69,  
 "NOx": 139,  
 "SO2": 11,  
 "address": {"addressCountry": "ES",  
             "addressLocality": "Madrid",  
             "streetAddress": "Plaza de EspaÃ±a",  
             "type": "PostalAddress"},  
 "airQualityIndex": 65,  
 "airQualityLevel": "moderate",  
 "areaServed": "Brooklands",  
 "dateObserved": "2016-03-15T11:00:00/2016-03-15T12:00:00",  
 "id": "urn:ngsi-ld:AirQualityObserved:Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
 "location": {"coordinates": [-3.712247222222222, 40.423852777777775],  
              "type": "Point"},  
 "typeOfLocation": "outdoor",  
 "precipitation": 0,  
 "refPointOfInterest": "urn:ngsi-ld:PointOfInterest:28079004-Pza.deEspanya",  
 "relativeHumidity": 0.54,  
 "reliability": 0.7,  
 "source": "http://datos.madrid.es",  
 "temperature": 12.2,  
 "type": "AirQualityObserved",  
 "windDirection": 186,  
 "windSpeed": 0.64}  
```  
#### AirQualityObserved NGSI-LD normalized Example    
Here is an example of a AirQualityObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:AirQualityObserved:Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
    "type": "AirQualityObserved",  
    "dateObserved": {  
        "type": "Property",  
        "value": "2016-03-15T11:00:00/2016-03-15T12:00:00"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Brooklands"  
    },  
    "airQualityLevel": {  
        "type": "Property",  
        "value": "moderate"  
    },  
    "CO": {  
        "type": "Property",  
        "value": 500,  
        "unitCode": "GP"  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 12.2  
    },  
    "NO": {  
        "type": "Property",  
        "value": 45,  
        "unitCode": "GQ"  
    },  
    "refPointOfInterest": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:PointOfInterest:28079004-Pza.deEspanya"  
    },  
    "windDirection": {  
        "type": "Property",  
        "value": 186  
    },  
    "source": {  
        "type": "Property",  
        "value": "http://datos.madrid.es"  
    },  
    "windSpeed": {  
        "type": "Property",  
        "value": 0.64  
    },  
    "SO2": {  
        "type": "Property",  
        "value": 11,  
        "unitCode": "GQ"  
    },  
    "NOx": {  
        "type": "Property",  
        "value": 139,  
        "unitCode": "GQ"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -3.712247222222222,  
                40.423852777777775  
            ]  
        }  
    },  
    "typeOfLocation": {  
        "type": "Property",  
        "value": "outdoor"  
    },  
    "airQualityIndex": {  
        "type": "Property",  
        "value": 65  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "ES",  
            "addressLocality": "Madrid",  
            "streetAddress": "Plaza de EspaÃ±a",  
            "type": "PostalAddress"  
        }  
    },  
    "reliability": {  
        "type": "Property",  
        "value": 0.7  
    },  
    "relativeHumidity": {  
        "type": "Property",  
        "value": 0.54  
    },  
    "precipitation": {  
        "type": "Property",  
        "value": 0  
    },  
    "NO2": {  
        "type": "Property",  
        "value": 69,  
        "unitCode": "GQ"  
    },  
    "CO_Level": {  
        "type": "Property",  
        "value": "moderate"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
