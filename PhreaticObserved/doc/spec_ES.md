Entidad: PhreaticObserved  
=========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Environment/blob/master/PhreaticObserved/LICENSE.md)  
Descripción global: **El modelo de datos tiene por objeto medir, observar y controlar el nivel y la calidad de las aguas subterráneas en un momento dado (T), mediante un sistema de vigilancia fijo o móvil. Según el dispositivo utilizado, también es posible medir la calidad del agua, como su conductividad eléctrica, su contenido de sal, su temperatura, etc. En este caso, los valores medidos son procesados por el modelo de datos "WaterObserved" y "WaterQualityObserved". Información adicional sobre los Atributos: Para los atributos dedicados al agua, también se puede utilizar un atributo de MetaData. Contiene el "Time-Stamp" en segundos, la "calificación" y el "estado" de control de la medición.**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateObserved`: La fecha y la hora de esta observación en formato ISO8601 UTC  - `dateObservedFrom`: Período de observación : Fecha y hora de inicio en un formato UTC ISO8601  - `dateObservedTo`: Período de observación : Fecha y hora de finalización en un formato UTC ISO8601  - `depth`: Profundidad del agua potable, desde su identificación como "mesa de agua". El código de unidad (texto) de medida dado usando los [Códigos Comunes de UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <código> MTR </código> representa Meter.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `investigationDepth`: Máxima profundidad donde se hizo la investigación. El código de unidad (texto) de medida dado usando los [Códigos Comunes de UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <código>MTR</código> representa Meter  - `isMobile`: El dispositivo utilizado es Fijo (Falso) o Móvil (Verdadero)  - `location`:   - `measurementType`: Período de observación : Tipo de medición procesada. Enum:'profundidad, volumen, calidad, otros'.  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `pollutionRate`: Tasa de contaminación. El código de unidad (texto) de medida dado usando los [Códigos Comunes de UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, P1 representa el porcentaje.  - `pressure`: Presión del agua. El código de unidad (texto) de medida dado usando los [Códigos Comunes de UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <código>BAR</código> representa Bar.  - `refDevice`: Referencia a los dispositivos que proporcionan datos  - `residueLevel`: El nivel de residuos encontrado  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `type`: Tipo de entidad NGSI. Tiene que ser PhreaticObserved  - `waterTable`: Nivel en el que se encontró agua durante esta investigación. El código de unidad (texto) de medida dado usando los [Códigos Comunes de UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <código>MTR</código> representa Meter.    
Propiedades requeridas  
- `dateObserved`  - `id`  - `location`  - `measurementType`  - `type`  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PhreaticObserved:    
  description: 'The Data Model is intended to measure, observe and control the level and quality of groundwater at a given time (T), by a fixed or mobile monitoring system. Depending on the device used, it is also possible to measure the quality of water such as its electrical conductivity, its salt content, its temperature, etc. In this case, the values measured are processed by the Data Model `WaterObserved` and `WaterQualityObserved`. Additional Information about Attributes: For attributes dedicated to water, a MetaData attribute can also be used. it contains the `TimeStamp` in seconds, the `qualification` and control `status` of the measurement.'    
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
      description: 'The date and time of this observation in ISO8601 UTC format'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateObservedFrom:    
      description: 'Observation period : Start date and time in an ISO8601 UTC format'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateObservedTo:    
      description: 'Observation period : End date and time in an ISO8601 UTC format'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    depth:    
      description: 'Depth of drinking water, since its identification `waterTable`. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code> MTR </code> represents Meter.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/depth    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &phreaticobserved_-_properties_-_owner_-_items_-_anyof    
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
    investigationDepth:    
      description: 'Maximum depth where the investigation was made. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
        units: meters    
    isMobile:    
      description: 'The device used is Fixed (False) or Mobile (True)'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
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
    measurementType:    
      description: 'Observation period : Type of measurement processed. Enum:''depth, volume, quality, other'''    
      items:    
        enum:    
          - depth    
          - volume    
          - quality    
          - other    
        type: string    
      minItems: 0    
      type: Property    
      uniqueItems: false    
      x-ngsi:    
        model: https://schema.org/Text    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *phreaticobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pollutionRate:    
      description: 'Rate of pollution. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, P1 represents Percentage.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    pressure:    
      description: 'Water Pressure. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>BAR</code> represents Bar.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
        units: Bar    
    refDevice:    
      description: 'Reference to the devices providing data'    
      items:    
        anyOf: *phreaticobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Relationship    
      x-ngsi:    
        model: https://scehma.org/URL    
    residueLevel:    
      description: 'Residue level found'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
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
    type:    
      description: 'NGSI Entity type. It has to be PhreaticObserved'    
      enum:    
        - PhreaticObserved    
      type: Property    
    waterTable:    
      description: 'Level at which water was found during this investigation. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: meter    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - measurementType    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### Ejemplo de valores clave de PhreaticObserved NGSI V2  
Aquí hay un ejemplo de un PhreaticObserved en formato JSON como valores clave. Es compatible con NGSI V2 cuando se usa "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
  "type": "PhreaticObserved",  
  "name": "STLRT-MNCA-NP-015",  
  "description": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var.",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "areaServed": "Nice Airport",  
  "dateObserved": "2020-07-07T15:05:59.408Z",  
  "refDevice": [  
    "urn:ngsi-ld:Device:T1-NP-015"  
  ],  
  "isMobile": false,  
  "measurementType": [  
    "depth",  
    "volume"  
  ],  
  "investigationDepth": 22.35,  
  "waterTable": 12.75,  
  "depth": 20.45,  
  "pressure": 2.12  
}  
```  
#### Ejemplo normalizado de PhreaticObserved NGSI V2  
Aquí hay un ejemplo de un PhreaticObserved en formato JSON como normalizado. Este es compatible con NGSI V2 cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
	"id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
	"type": "PhreaticObserved",  
	"name": {  
		"type": "Property",  
		"value": "STLRT-MNCA-NP-015"  
	},  
	"description": {  
		"type": "Property",  
		"value": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var."  
	},  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [43.664810, 7.196545]  
        }  
	},  
	"areaServed": {  
		"type": "Property",  
		"value": "Nice Airport"  
	},  
	"dateObserved": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-07-07T15:05:59.408Z"  
		}  
	},  
	"refDevice": {  
		"type": "Relationship",  
		"Object": ["urn:ngsi-ld:Device:T1-NP-015"]  
	},  
	"isMobile": {  
		"type": "Property",  
		"value": false  
	},  
	"measurementType": {  
		"type": "Property",  
		"value": ["depth", "volume"]  
	},  
	"investigationDepth": {  
		"type": "Property",  
		"value": 22.35  
	},  
	"waterTable": {  
		"type": "Property",  
		"value": 12.75,  
		"observedAt": "2020-03-17TT08:45:00Z",  
		"qualification": {  
			"type": "Property",  
			"value": "Correct"  
		},  
		"status ": {  
			"type": "Property",  
			"value": "Level 2"  
		}  
	},  
	"depth": {  
		"type": "Property",  
		"value": 20.45,  
		"observedAt": "2020-03-17TT08:45:00Z",  
		"qualification": {  
			"type": "Property",  
			"value": "Incorrect"  
		},  
		"status ": {  
			"type": "Property",  
			"value": "Level 1"  
		}  
	},  
	"pressure": {  
		"type": "Property",  
		"value": 2.12,  
		"observedAt": "2020-03-17TT08:45:00Z",  
		"qualification": {  
			"value": "Correct"  
		},  
		"status ": {  
			"type": "Property",  
			"value": "Level 3"  
		}  
	}  
}  
```  
#### Ejemplo de valores clave NGSI-LD observados por la freática  
Aquí hay un ejemplo de un PhreaticObserved en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
  "type": "PhreaticObserved",  
  "name": "STLRT-MNCA-NP-015",  
  "description": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var.",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "areaServed": "Nice Airport",  
  "dateObserved": "2020-07-07T15:05:59.408Z",  
  "refDevice": [  
    "urn:ngsi-ld:Device:T1-NP-015"  
  ],  
  "isMobile": false,  
  "measurementType": [  
    "depth",  
    "volume"  
  ],  
  "investigationDepth": 22.35,  
  "waterTable": 12.75,  
  "depth": 20.45,  
  "pressure": 2.12,  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Ejemplo normalizado de PhreaticObserved NGSI-LD  
He aquí un ejemplo de un PhreaticObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
	"id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
	"type": "PhreaticObserved",  
	"name": {  
		"type": "Property",  
		"value": "STLRT-MNCA-NP-015"  
	},  
	"description": {  
		"type": "Property",  
		"value": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var."  
	},  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [43.664810, 7.196545]  
        }  
	},  
	"areaServed": {  
		"type": "Property",  
		"value": "Nice Airport"  
	},  
	"dateObserved": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-07-07T15:05:59.408Z"  
		}  
	},  
	"refDevice": {  
		"type": "Relationship",  
		"Object": ["urn:ngsi-ld:Device:T1-NP-015"]  
	},  
	"isMobile": {  
		"type": "Property",  
		"value": false  
	},  
	"measurementType": {  
		"type": "Property",  
		"value": ["depth", "volume"]  
	},  
	"investigationDepth": {  
		"type": "Property",  
		"value": 22.35  
	},  
	"waterTable": {  
		"type": "Property",  
		"value": 12.75,  
		"observedAt": "2020-03-17TT08:45:00Z",  
		"qualification": {  
			"type": "Property",  
			"value": "Correct"  
		},  
		"status ": {  
			"type": "Property",  
			"value": "Level 2"  
		}  
	},  
	"depth": {  
		"type": "Property",  
		"value": 20.45,  
		"observedAt": "2020-03-17TT08:45:00Z",  
		"qualification": {  
			"type": "Property",  
			"value": "Incorrect"  
		},  
		"status ": {  
			"type": "Property",  
			"value": "Level 1"  
		}  
	},  
	"pressure": {  
		"type": "Property",  
		"value": 2.12,  
		"observedAt": "2020-03-17TT08:45:00Z",  
		"qualification": {  
			"value": "Correct"  
		},  
		"status ": {  
			"type": "Property",  
			"value": "Level 3"  
		}  
	},  
	"@context": [  
		"https://schema.lab.fiware.org/ld/context",  
		"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
	]  
}  
```  
