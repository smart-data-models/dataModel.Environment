Entity: WaterObserved  
=====================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: ** Water observation data model is intended to represent the parameters of flow, level and volume of water observed, as well as the swell information, over a fixed or variable area. This observation also includes the masses of floating objects on this area. The data collected is provided by Sensors, Cameras,Water stations positioned at specific or sensitive locations for rivers, streams, torrent, lakes, seas, etc.**  

## List of properties  

- `address`: The mailing address.  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `dateObserved`: Date and time of this observation represented by an ISO8601 UTC format.  - `dateObservedFrom`: Observation period : Start date and time in an ISO8601 UTC format.  - `dateObservedTo`: Observation period : End date and time in an ISO8601 UTC format.  - `description`: A description of this item  - `flow`: Water Flow observed. The unit code (text) of measurement given using the UN/CEFACAT  - `height`: Water height - Level reach on alert coasts.  - `id`: Unique identifier of the entity  - `location`:   - `measuredArea`: Water height - Level reach on alert coasts.   - `name`: The name of this item.  - `objectArea`: Percentage occupied by floating object in the area.  - `objectHeightAverage`: Average height raised.  - `objectHeightMax`: Maximum height raised.  - `objectVolume`: Estimated volume raised.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `refDevice`: A reference to a point of interest associated to this observation.  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `swellDirection`: Water height - Level reach on alert coasts.  - `swellHeight`: Water height - Level reach on alert coasts.  - `swellPeriod`: Water height - Level reach on alert coasts.  - `type`: NGSI Entity type  - `waveLength`: Water height - Level reach on alert coasts.     
Required properties  
- `dateObserved`  - `id`  - `location`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterObserved:    
  description: ' Water observation data model is intended to represent the parameters of flow, level and volume of water observed, as well as the swell information, over a fixed or variable area. This observation also includes the masses of floating objects on this area. The data collected is provided by Sensors, Cameras,Water stations positioned at specific or sensitive locations for rivers, streams, torrent, lakes, seas, etc.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'Date and time of this observation represented by an ISO8601 UTC format.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateObservedFrom:    
      description: 'Observation period : Start date and time in an ISO8601 UTC format.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateObservedTo:    
      description: 'Observation period : End date and time in an ISO8601 UTC format.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    description:    
      description: 'A description of this item'    
      type: Property    
    flow:    
      description: 'Water Flow observed. The unit code (text) of measurement given using the UN/CEFACAT'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    height:    
      description: 'Water height - Level reach on alert coasts.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &waterobserved_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
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
    measuredArea:    
      description: 'Water height - Level reach on alert coasts. '    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    objectArea:    
      description: 'Percentage occupied by floating object in the area.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    objectHeightAverage:    
      description: 'Average height raised.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    objectHeightMax:    
      description: 'Maximum height raised.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    objectVolume:    
      description: 'Estimated volume raised.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *waterobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      description: 'A reference to a point of interest associated to this observation.'    
      type: Relationship    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    swellDirection:    
      description: 'Water height - Level reach on alert coasts.'    
      maximum: 360    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    swellHeight:    
      description: 'Water height - Level reach on alert coasts.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    swellPeriod:    
      description: 'Water height - Level reach on alert coasts.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - WaterObserved    
      type: Property    
    waveLength:    
      description: 'Water height - Level reach on alert coasts. '    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
  type: object    
```  
</details>    
## Example payloads    
#### WaterObserved NGSI V2 key-values Example    
Here is an example of a WaterObserved in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
	"id": "WaterObserved:MNCA-001",  
	"type": "WaterObserved",  
	"name": "STLRT-MNCA-AP-WO-012",  
	"alternateName":"Var River Alert for safety procedure for Airport",  
	"description": "Observation of Evolution of the water levels",  
	"location": {  
			"type": "Point",  
			"coordinates": [43.664810,7.196545]  
	},  
	"areaServed":"Nice Airport",  
	"refDevice": "Device:T2-NP-018",  
	"dateObserved": "2020-03-17T08:45:00.209Z",  
	"flow": 12,  
	"height": 3.52,  
	"measuredArea": 250,  
	"objectArea": 35,  
	"objectHeightAverage": 1.75,  
	"objectHeightMax": 2.25,  
	"objectVolume": 17.5  
}  
```  
#### WaterObserved NGSI V2 normalized Example    
Here is an example of a WaterObserved in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
```json  
{  
	"id": "WaterObserved:MNCA-001",  
	"type": "WaterObserved",  
	"name": {  
		"value": "STLRT-MNCA-AP-WO-012"  
	},  
	"alternateName": {  
		"value": "Var River Alert for safety procedure for Airport"  
	},  
	"description": {  
		"value": "Observation of Evolution of the water levels"  
	},  
	"location": {  
			"type": "Point",  
			"coordinates": [43.664810,7.196545]  
	},  
	"areaServed": {  
		"value": "Nice Airport"  
	},  
	"refDevice": {  
		"type": "Relationship",  
		"value": "Device:T2-NP-018"  
	},  
	"dateObserved": {  
		"type": "DateTime",  
		"value": "2020-03-17T08:45:00.209Z"  
	},  
	"flow": {  
		"value": 12  
	},  
	"height": {  
		"value": 3.52  
	},  
	"measuredArea": {  
		"value": 250  
	},  
	"objectArea": {  
		"value": 35  
	},  
	"objectHeightAverage": {  
		"value": 1.75  
	},  
	"objectHeightMax": {  
		"value": 2.25  
	},  
	"objectVolume": {  
		"value": 17.5  
	}  
}  
```  
#### WaterObserved NGSI-LD key-values Example    
Here is an example of a WaterObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "uri:ngsi:WaterObserved:MNCA-001",  
  "type": "WaterObserved",  
  "name": "STLRT-MNCA-AP-WO-012",  
  "alternateName": "Var River Alert for safety procedure for Airport",  
  "description": "Observation of Evolution of the water levels",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "areaServed": "Nice Airport",  
  "refDevice": "uri:ngsi:Device:T2-NP-018",  
  "dateObserved": "2020-03-17T08:45:00.209Z",  
  "flow": 12,  
  "height": 3.52,  
  "measuredArea": 250,  
  "objectArea": 35,  
  "objectHeightAverage": 1.75,  
  "objectHeightMax": 2.25,  
  "objectVolume": 17.5,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld"  
  ]  
}  
```  
#### WaterObserved NGSI-LD normalized Example    
Here is an example of a WaterObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi:WaterObserved:MNCA-001",  
  "type": "WaterObserved",  
  "name": {  
    "type": "Text",  
    "value": "STLRT-MNCA-AP-WO-012"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Var River Alert for safety procedure for Airport"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Observation of Evolution of the water levels"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice Airport"  
  },  
  "refDevice": {  
    "type": "Text",  
    "value": "uri:ngsi:Device:T2-NP-018"  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00.209Z"  
  },  
  "flow": {  
    "type": "Number",  
    "value": 12  
  },  
  "height": {  
    "type": "Number",  
    "value": 3.52  
  },  
  "measuredArea": {  
    "type": "Number",  
    "value": 250  
  },  
  "objectArea": {  
    "type": "Number",  
    "value": 35  
  },  
  "objectHeightAverage": {  
    "type": "Number",  
    "value": 1.75  
  },  
  "objectHeightMax": {  
    "type": "Number",  
    "value": 2.25  
  },  
  "objectVolume": {  
    "type": "Number",  
    "value": 17.5  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld"  
  ]  
}  
```  
