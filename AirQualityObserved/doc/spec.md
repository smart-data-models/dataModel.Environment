<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: AirQualityObserved  
==========================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Open License](https://github.com/smart-data-models//dataModel.Environment/blob/master/AirQualityObserved/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **An observation of air quality conditions at a certain place and time.**  

version: 0.1.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## List of properties  


<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)
- `airQualityIndex[number]`: Air quality index is a number used to report the quality of the air on any given day.  . Model: [https://schema.org/Number](https://schema.org/Number)
- `airQualityLevel[string]`: Overall qualitative level of health concern corresponding to the air quality observed  . Model: [https://schema.org/Tex ](https://schema.org/Tex )
- `alternateName[string]`: An alternative name for this item  
- `areaServed[string]`: Higher level area to which this air quality measurement belongs to  . Model: [https://schema.org/Text ](https://schema.org/Text )
- `as[number]`: Arsenic detected  . Model: [https://schema.org/Number](https://schema.org/Number)
- `c6h6[number]`: Benzene detected  
- `cd[number]`: Cadmium detected  
- `co[number]`: Carbon Monoxide detected  
- `co2[number]`: Carbon Dioxide detected  
- `coLevel[string]`: Qualitative Carbon Monoxide presence  
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `dateObserved[string]`: The date and time of this observation in ISO8601 UTCformat  . Model: [https://schema.org/Text ](https://schema.org/Text )
- `description[string]`: A description of this item  
- `id[*]`: Unique identifier of the entity  
- `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name[string]`: The name of this item.  
- `ni[number]`: Nickel detected  
- `no[number]`: Nitrogen monoxide detected  
- `no2[number]`: Nitrogen dioxide detected  
- `nox[number]`: Other Nitrogen oxides detected  
- `o3[number]`: Ozone detected  
- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `pb[number]`: Lead detected  
- `pm1[number]`: Particulate matter 1 micrometers or less in diameter.  
- `pm10[number]`: Particulate matter 10 micrometers or less in diameter  
- `pm25[number]`: Particulate matter 2.5 micrometers or less in diameter  
- `precipitation[number]`: Amount of water rain  . Model: [https://schema.org/Number](https://schema.org/Number)
- `refDevice[*]`: A reference to the device(s) which captured this observation.  
- `refPointOfInterest[*]`: A reference to a point of interest (usually an air quality station) associated to this observation.  
- `refWeatherObserved[*]`:  Weather observed associated to the air quality conditions described by this entity.  
- `relativeHumidity[number]`: Relative Humidity of the air (a number between 0 and 1 representing the range of 0% to 100%)  
- `reliability[number]`: Reliability (percentage, expressed in parts per one) corresponding to the air quality observed  . Model: [https://schema.org/Number ](https://schema.org/Number )
- `seeAlso[*]`: list of uri pointing to additional resources about the item  
- `sh2[number]`: Hydrogen sulfide detected  
- `so2[number]`: Sulfur dioxide detected  
- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `temperature[number]`: Temperature of the item  
- `type[string]`: NGSI Entity type. It has to be AirQualityObserved  
- `typeofLocation[string]`: Type of location of the sampled item  . Model: [https://schema.org/Text](https://schema.org/Text)
- `volatileOrganicCompoundsTotal[number]`: Alkanes <C10, ketones <C6, aldehydes <C10, carboxylic acids <C5, aspirits<C7, Alkenes <C8, Aromatics  
- `windDirection[number]`: Direction of the weather vane  . Model: [http://schema.org/Number](http://schema.org/Number)
- `windSpeed[number]`: Intensity of the wind  . Model: [http//schema.org/Number](http//schema.org/Number)
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Required properties  
- `dateObserved`  
- `id`  
- `location`  
- `type`  
<!-- /35-RequiredProperties -->
  
<!-- 40-RequiredProperties -->
  

Not all pollutants are included in this data model. In case of new ones to extend the model please refer to this source http://dd.eionet.europa.eu/vocabulary/aq/pollutant/view?page=1#vocabularyConceptResults where most of the are listed.  
<!-- /40-RequiredProperties -->
  
<!-- 50-DataModelHeader -->
  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
AirQualityObserved:    
  description: An observation of air quality conditions at a certain place and time.    
  properties:    
    address:    
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    airQualityIndex:    
      description: Air quality index is a number used to report the quality of the air on any given day.    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    airQualityLevel:    
      description: Overall qualitative level of health concern corresponding to the air quality observed    
      minLength: 2    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/Tex '    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: Higher level area to which this air quality measurement belongs to    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/Text '    
        type: Property    
    as:    
      description: Arsenic detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    c6h6:    
      description: Benzene detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    cd:    
      description: Cadmium detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    co:    
      description: Carbon Monoxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    co2:    
      description: Carbon Dioxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    coLevel:    
      description: Qualitative Carbon Monoxide presence    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: The date and time of this observation in ISO8601 UTCformat    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/Text '    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &airqualityobserved_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
        - description: GeoProperty. Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    ni:    
      description: Nickel detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    no:    
      description: Nitrogen monoxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    no2:    
      description: Nitrogen dioxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    nox:    
      description: Other Nitrogen oxides detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    o3:    
      description: Ozone detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *airqualityobserved_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    pb:    
      description: Lead detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    pm1:    
      description: Particulate matter 1 micrometers or less in diameter.    
      type: number    
      x-ngsi:    
        type: Property    
    pm10:    
      description: Particulate matter 10 micrometers or less in diameter    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    pm25:    
      description: Particulate matter 2.5 micrometers or less in diameter    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    precipitation:    
      description: Amount of water rain    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Liters per square meter.    
    refDevice:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: A reference to the device(s) which captured this observation.    
      x-ngsi:    
        type: Relationship    
    refPointOfInterest:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: A reference to a point of interest (usually an air quality station) associated to this observation.    
      x-ngsi:    
        type: Relationship    
    refWeatherObserved:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: ' Weather observed associated to the air quality conditions described by this entity.'    
      x-ngsi:    
        type: Relationship    
    relativeHumidity:    
      description: Relative Humidity of the air (a number between 0 and 1 representing the range of 0% to 100%)    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    reliability:    
      description: 'Reliability (percentage, expressed in parts per one) corresponding to the air quality observed'    
      maximum: 1.0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: 'https://schema.org/Number '    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
    sh2:    
      description: Hydrogen sulfide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    so2:    
      description: Sulfur dioxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: Temperature of the item    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be AirQualityObserved    
      enum:    
        - AirQualityObserved    
      type: string    
      x-ngsi:    
        type: Property    
    typeofLocation:    
      description: Type of location of the sampled item    
      enum:    
        - indoor    
        - outdoor    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    volatileOrganicCompoundsTotal:    
      description: 'Alkanes <C10, ketones <C6, aldehydes <C10, carboxylic acids <C5, aspirits<C7, Alkenes <C8, Aromatics'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    windDirection:    
      description: Direction of the weather vane    
      maximum: 180    
      minimum: -180    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    windSpeed:    
      description: Intensity of the wind    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http//schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/AirQualityObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/AirQualityObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.1.1    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Example payloads    

#### AirQualityObserved NGSI-v2 key-values Example    

Here is an example of a AirQualityObserved in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    

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
  "windDirection": 176,  
  "windSpeed": 0.64,  
  "airQualityLevel": "moderate",  
  "airQualityIndex": 65,  
  "reliability": 0.7,  
  "co": 500,  
  "no": 45,  
  "co2": 69,  
  "nox": 139,  
  "so2": 11,  
  "coLevel": "moderate",  
  "refPointOfInterest": "28079004-Pza.deEspanya"  
}  
```  
</details>  

#### AirQualityObserved NGSI-v2 normalized Example    

Here is an example of a AirQualityObserved in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    

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
</details>  

#### AirQualityObserved NGSI-LD key-values Example    

Here is an example of a AirQualityObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
    "id": "urn:ngsi-ld:AirQualityObserved:Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
    "type": "AirQualityObserved",  
    "CO": 500,  
    "CO_Level": "moderate",  
    "NO": 45,  
    "NO2": 69,  
    "NOx": 139,  
    "SO2": 11,  
    "address": {  
        "addressCountry": "ES",  
        "addressLocality": "Madrid",  
        "streetAddress": "Plaza de Espa\u00f1a",  
        "type": "PostalAddress"  
    },  
    "airQualityIndex": 65,  
    "airQualityLevel": "moderate",  
    "areaServed": "Brooklands",  
    "dateObserved": "2016-03-15T11:00:00/2016-03-15T12:00:00",  
    "location": {  
        "coordinates": [  
            -3.712247222222222,  
            40.423852777777775  
        ],  
        "type": "Point"  
    },  
    "precipitation": 0,  
    "refPointOfInterest": "urn:ngsi-ld:PointOfInterest:28079004-Pza.deEspanya",  
    "relativeHumidity": 0.54,  
    "reliability": 0.7,  
    "source": "http://datos.madrid.es",  
    "temperature": 12.2,  
    "typeOfLocation": "outdoor",  
    "windDirection": 186,  
    "windSpeed": 0.64,  
    "@context": [  
      
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  

#### AirQualityObserved NGSI-LD normalized Example    

Here is an example of a AirQualityObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
    "id": "urn:ngsi-ld:AirQualityObserved:Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
    "type": "AirQualityObserved",  
    "CO": {  
        "type": "Property",  
        "value": 500,  
        "unitCode": "GP"  
    },  
    "CO_Level": {  
        "type": "Property",  
        "value": "moderate"  
    },  
    "NO": {  
        "type": "Property",  
        "value": 45,  
        "unitCode": "GQ"  
    },  
    "NO2": {  
        "type": "Property",  
        "value": 69,  
        "unitCode": "GQ"  
    },  
    "NOx": {  
        "type": "Property",  
        "value": 139,  
        "unitCode": "GQ"  
    },  
    "SO2": {  
        "type": "Property",  
        "value": 11,  
        "unitCode": "GQ"  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "ES",  
            "addressLocality": "Madrid",  
            "streetAddress": "Plaza de Espa\u00f1a",  
            "type": "PostalAddress"  
        }  
    },  
    "airQualityIndex": {  
        "type": "Property",  
        "value": 65  
    },  
    "airQualityLevel": {  
        "type": "Property",  
        "value": "moderate"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Brooklands"  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": "2016-03-15T11:00:00/2016-03-15T12:00:00"  
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
    "precipitation": {  
        "type": "Property",  
        "value": 0  
    },  
    "refPointOfInterest": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:PointOfInterest:28079004-Pza.deEspanya"  
    },  
    "relativeHumidity": {  
        "type": "Property",  
        "value": 0.54  
    },  
    "reliability": {  
        "type": "Property",  
        "value": 0.7  
    },  
    "source": {  
        "type": "Property",  
        "value": "http://datos.madrid.es"  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 12.2  
    },  
    "typeOfLocation": {  
        "type": "Property",  
        "value": "outdoor"  
    },  
    "windDirection": {  
        "type": "Property",  
        "value": 186  
    },  
    "windSpeed": {  
        "type": "Property",  
        "value": 0.64  
    },  
    "@context": [  
      
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->
  
<!-- 90-FooterNotes -->
  
<!-- /90-FooterNotes -->
  
<!-- 95-Units -->
  

See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->
  
<!-- 97-LastFooter -->
  
---  

[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->
  
