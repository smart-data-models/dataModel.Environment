Entity: WaterQualityObserved  
============================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **Water Quality data model is intended to represent water quality parameters at a certain water mass (river,  lake, sea, etc.) section**  

## List of properties  

- `Chla`:   - `Cl-`:   - `NH3`:   - `NH4`:   - `NO3`:   - `O2`:   - `PC`:   - `PE`:   - `address`: The mailing address.  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided.  - `conductance`:   - `conductivity`:   - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `dateObserved`:   - `description`: A description of this item  - `id`:   - `location`:   - `measurand`:   - `name`: The name of this item.  - `orp`:   - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `pH`:   - `refPointOfInterest`:   - `salinity`:   - `seeAlso`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `tds`:   - `temperature`:   - `tss`:   - `turbidity`:   - `type`: NGSI Entity type  ## Data Model description of properties  
Sorted alphabetically  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterQualityObserved:    
  description: 'Water Quality data model is intended to represent water quality parameters at a certain water mass (river,  lake, sea, etc.) section'    
  properties:    
    Chla:    
      minimum: 0    
      type: number    
    Cl-:    
      minimum: 0    
      type: number    
    NH3:    
      minimum: 0    
      type: number    
    NH4:    
      minimum: 0    
      type: number    
    NO3:    
      minimum: 0    
      type: number    
    O2:    
      minimum: 0    
      type: number    
    PC:    
      minimum: 0    
      type: number    
    PE:    
      minimum: 0    
      type: number    
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
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    conductance:    
      minimum: 0    
      type: number    
    conductivity:    
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
      anyOf: &waterqualityobserved_-_properties_-_owner_-_items_-_anyof    
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
    measurand:    
      items:    
        type: string    
      minItems: 1    
      type: array    
    name:    
      description: 'The name of this item.'    
      type: Property    
    orp:    
      minimum: 0    
      type: number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *waterqualityobserved_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    pH:    
      maximum: 14    
      minimum: 0    
      type: number    
    refPointOfInterest:    
      anyOf: *waterqualityobserved_-_properties_-_owner_-_items_-_anyof    
    salinity:    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    tds:    
      minimum: 0    
      type: number    
    temperature:    
      type: number    
    tss:    
      minimum: 0    
      type: number    
    turbidity:    
      minimum: 0    
      type: number    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - WaterQualityObserved    
      type: string    
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
  type: object    
```  
</details>    
#### WaterQualityObserved NGSI V2 key-values Example    
Here is an example of a WaterQualityObserved in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "waterqualityobserved:Sevilla:D1",  
  "type": "WaterQualityObserved",  
  "dateObserved": "2017-01-31T06:45:00Z",  
  "measurand": ["NO3, 0.01, M1, Concentration of Nitrates"],  
  "location": {  
    "type": "Point",  
    "coordinates": [-5.993307, 37.362882]  
  },  
  "temperature": 24.4,  
  "conductivity": 0.005,  
  "pH": 7.4,  
  "NO3": 0.01  
}  
```  
#### WaterQualityObserved NGSI V2 normalized Example    
Here is an example of a WaterQualityObserved in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "waterqualityobserved:Sevilla:D1",  
  "type": "WaterQualityObserved",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2017-01-31T06:45:00Z"  
  },  
  "temperature": {  
    "value": 24.4  
  },  
  "NO3": {  
    "value": 0.01  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-5.993307, 37.362882]  
    }  
  },  
  "pH": {  
    "value": 7.4  
  },  
  "measurand": {  
    "value": ["NO3, 0.01, M1, Concentration of Nitrates"]  
  },  
  "conductivity": {  
    "value": 0.005  
  }  
}  
```  
#### WaterQualityObserved NGSI-LD key-values Example    
Here is an example of a WaterQualityObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "NO3": 0.01,  
 "conductivity": 0.005,  
 "dateObserved": {"@type": "DateTime", "@value": "2017-01-31T06:45:00Z"},  
 "id": "urn:ngsi-ld:WaterQualityObserved:waterqualityobserved:Sevilla:D1",  
 "location": {"coordinates": [-5.993307, 37.362882], "type": "Point"},  
 "measurand": ["NO3, 0.01, M1, Concentration of Nitrates"],  
 "pH": 7.4,  
 "temperature": 24.4,  
 "type": "WaterQualityObserved"}  
```  
#### WaterQualityObserved NGSI-LD normalized Example    
Here is an example of a WaterQualityObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:WaterQualityObserved:waterqualityobserved:Sevilla:D1",  
    "type": "WaterQualityObserved",  
    "dateObserved": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2017-01-31T06:45:00Z"  
        }  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 24.4  
    },  
    "NO3": {  
        "type": "Property",  
        "value": 0.01  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -5.993307,  
                37.362882  
            ]  
        }  
    },  
    "pH": {  
        "type": "Property",  
        "value": 7.4  
    },  
    "measurand": {  
        "type": "Property",  
        "value": [  
            "NO3, 0.01, M1, Concentration of Nitrates"  
        ]  
    },  
    "conductivity": {  
        "type": "Property",  
        "value": 0.005  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
