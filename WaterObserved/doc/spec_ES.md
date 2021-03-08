Entidad: AguaObservada  
======================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Environment/blob/master/WaterObserved/LICENSE.md)  
Descripción global: ** El modelo de datos de observación del agua está destinado a representar los parámetros de flujo, nivel y volumen de agua observados, así como la información sobre el oleaje, sobre un área fija o variable. Esta observación también incluye las masas de objetos flotantes en esta área. Los datos recogidos son proporcionados por Sensores, Cámaras, Estaciones de Agua posicionadas en lugares específicos o sensibles para ríos, arroyos, torrentes, lagos, mares, etc.**.  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateObserved`: Fecha y hora de esta observación representada por un formato ISO8601 UTC.  - `dateObservedFrom`: Período de observación : Fecha y hora de inicio en formato ISO8601 UTC.  - `dateObservedTo`: Período de observación : Fecha y hora de finalización en formato ISO8601 UTC.  - `description`: Una descripción de este artículo  - `flow`: Flujo de agua observado. El código de la unidad (texto) de medida dado utilizando el UN/CEFACAT  - `height`: XXXPropiedad. Altura del agua - Alcance del nivel en las costas de alerta.  - `id`: Identificador único de la entidad  - `location`:   - `measuredArea`: Altura del agua - Alcance del nivel en las costas de alerta. El código de la unidad (texto) de medida que se da utilizando los [Códigos comunes de la ONU/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <código>MTK</código> representa M².  - `name`: El nombre de este artículo.  - `objectArea`: Porcentaje ocupado por el objeto flotante en la zona. El código de la unidad (texto) de medida que se da utilizando los [Códigos Comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <código>P1</código> representa el Porcentaje.  - `objectHeightAverage`: Altura media elevada. El código de la unidad (texto) de medida que se da utilizando los [Códigos Comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <código>MTR</código> representa el Metro.  - `objectHeightMax`: Altura máxima elevada. El código de la unidad (texto) de medida dado utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <código>MTR</código> representa el Metro.  - `objectVolume`: Volumen estimado recaudado. El código de la unidad (texto) de medida que se da utilizando los [Códigos Comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máximo 3 caracteres). Por ejemplo, <código>MTQ</código> representa Metros Cúbicos  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refDevice`: Una referencia a un punto de interés asociado a esta observación.  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `swellDirection`: Altura del agua - Alcance del nivel en las costas de alerta.  - `swellHeight`: XXXPropiedad. Altura del agua - Alcance del nivel en las costas de alerta.  - `swellPeriod`: Altura del agua - Alcance del nivel en las costas de alerta.  - `type`: Tipo de entidad NGSI. Tiene que ser WaterObserved  - `waveLength`: Altura del agua - Alcance del nivel en las costas de alerta.    
Propiedades requeridas  
- `dateObserved`  - `id`  - `location`  - `type`    
El modelo de datos de observación del agua tiene por objeto representar los parámetros de flujo, nivel y volumen de agua observados, así como la información sobre el oleaje, en una zona fija o variable. Esta observación también incluye las masas de objetos flotantes en esta área.  Los datos recogidos son proporcionados por [Sensores], [Cámaras], [Estaciones acuáticas] colocados en lugares específicos o sensibles para los ríos, arroyos, torrentes, lagos, mares, etc.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
      description: 'XXXProperty. Water height - Level reach on alert coasts.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/height    
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
      description: 'Water height - Level reach on alert coasts. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTK</code> represents M².'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'square meters'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    objectArea:    
      description: 'Percentage occupied by floating object in the area. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>P1</code> represents Percentage.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    objectHeightAverage:    
      description: 'Average height raised. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: meters    
    objectHeightMax:    
      description: 'Maximum height raised. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: meters    
    objectVolume:    
      description: 'Estimated volume raised. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTQ</code> represents Cubic Meters'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'cubic meters'    
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
      description: 'XXXProperty. Water height - Level reach on alert coasts.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/height    
    swellPeriod:    
      description: 'Water height - Level reach on alert coasts.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI Entity type. It has to be WaterObserved'    
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
## Ejemplo de carga útil  
#### WaterObserved NGSI V2 key-values Ejemplo  
Aquí hay un ejemplo de un WaterObserved en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### AguaObservada NGSI V2 normalizada Ejemplo  
Este es un ejemplo de un WaterObserved en formato JSON normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### WaterObserved NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un WaterObserved en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### AguaObservada NGSI-LD normalizada Ejemplo  
Este es un ejemplo de un WaterObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
