Entity: AeroAllergenObserved  
============================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **An observation of pollen levels at a certain place and time.**  

## List of properties  

`address`: The mailing address.  `allergenRisk`:   `alternateName`: An alternative name for this item  `areaServed`: The geographic area where a service or offered item is provided.  `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  `dateObserved`:   `description`: A description of this item  `id`:   `location`:   `name`: The name of this item.  `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  `refDevice`:   `seeAlso`:   `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  `type`: NGSI Entity type  ## Data Model description of properties  
Sorted alphabetically  
```yaml  
AeroAllergenObserved:    
  description: 'An observation of pollen levels at a certain place and time.'    
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
    allergenRisk:    
      enum:    
        - none    
        - low    
        - moderate    
        - high    
        - veryHigh    
      type: string    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
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
      anyOf: &aeroallergenobserved_-_properties_-_owner_-_items_-_anyof    
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
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *aeroallergenobserved_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    refDevice:    
      anyOf: *aeroallergenobserved_-_properties_-_owner_-_items_-_anyof    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - AeroAllergenObserved    
      type: string    
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
  type: object    
```  
Here is an example of a AeroAllergenObserved in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "AeroAllergenObserved-CDMX-Pollen-Cuajimalpa",  
  "type": "AeroAllergenObserved",  
  "alnus_Level": "moderate",  
  "alnus": 40,  
  "alnus_Allergenicity": "3",  
  "casuarina_Level": "low",  
  "casuarina": 1,  
  "casuarina_Allergenicity": "3",  
  "allergenRisk": "moderate",  
  "address": {  
    "addressCountry": "MX",  
    "addressLocality": "Ciudad de México",  
    "streetAddress": "Colegio Franco-Inglés"  
  },  
  "dateModified": "2018-02-16T17:24:39.00Z",  
  "dateObserved": "2018-02-11T00:00:00.00Z",  
  "location": {  
    "type": "Point",  
    "coordinates": [-99.276977, 19.381877]  
  },  
  "source": "http://rema.atmosfera.unam.mx/rema/"  
}  
```  
Here is an example of a AeroAllergenObserved in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "AeroAllergenObserved-CDMX-Pollen-Cuajimalpa",  
  "type": "AeroAllergenObserved",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2018-02-11T00:00:00.00Z"  
  },  
  "alnus": {  
    "value": 40  
  },  
  "alnus_Allergenicity": {  
    "value": "3"  
  },  
  "allergenRisk": {  
    "value": "moderate"  
  },  
  "casuarina": {  
    "value": 1  
  },  
  "casuarina_Level": {  
    "value": "low"  
  },  
  "casuarina_Allergenicity": {  
    "value": "3"  
  },  
  "source": {  
    "value": "http://rema.atmosfera.unam.mx/rema/"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-99.276977, 19.381877]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressCountry": "MX",  
      "addressLocality": "Ciudad de M\u00e9xico",  
      "streetAddress": "Colegio Franco-Ingl\u00e9s"  
    }  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2018-02-16T17:24:39.00Z"  
  },  
  "alnus_Level": {  
    "value": "moderate"  
  }  
}  
```  
Here is an example of a AeroAllergenObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address": {"addressCountry": "MX",  
             "addressLocality": "Ciudad de México",  
             "streetAddress": "Colegio Franco-Inglés",  
             "type": "PostalAddress"},  
 "allergenRisk": "moderate",  
 "alnus": 40,  
 "alnus_Allergenicity": "3",  
 "alnus_Level": "moderate",  
 "casuarina": 1,  
 "casuarina_Allergenicity": "3",  
 "casuarina_Level": "low",  
 "dateObserved": {"@type": "DateTime", "@value": "2018-02-11T00:00:00.00Z"},  
 "id": "urn:ngsi-ld:AeroAllergenObserved:AeroAllergenObserved-CDMX-Pollen-Cuajimalpa",  
 "location": {"coordinates": [-99.276977, 19.381877], "type": "Point"},  
 "modifiedAt": "2018-02-16T17:24:39.00Z",  
 "source": "http://rema.atmosfera.unam.mx/rema/",  
 "type": "AeroAllergenObserved"}  
```  
Here is an example of a AeroAllergenObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:AeroAllergenObserved:AeroAllergenObserved-CDMX-Pollen-Cuajimalpa",  
    "type": "AeroAllergenObserved",  
    "modifiedAt": "2018-02-16T17:24:39.00Z",  
    "dateObserved": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-02-11T00:00:00.00Z"  
        }  
    },  
    "alnus": {  
        "type": "Property",  
        "value": 40  
    },  
    "alnus_Allergenicity": {  
        "type": "Property",  
        "value": "3"  
    },  
    "allergenRisk": {  
        "type": "Property",  
        "value": "moderate"  
    },  
    "casuarina": {  
        "type": "Property",  
        "value": 1  
    },  
    "casuarina_Level": {  
        "type": "Property",  
        "value": "low"  
    },  
    "casuarina_Allergenicity": {  
        "type": "Property",  
        "value": "3"  
    },  
    "source": {  
        "type": "Property",  
        "value": "http://rema.atmosfera.unam.mx/rema/"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -99.276977,  
                19.381877  
            ]  
        }  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "MX",  
            "addressLocality": "Ciudad de México",  
            "streetAddress": "Colegio Franco-Inglés",  
            "type": "PostalAddress"  
        }  
    },  
    "alnus_Level": {  
        "type": "Property",  
        "value": "moderate"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
