Entité : WaterObserved  
======================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : ** Le modèle de données d'observation de l'eau est destiné à représenter les paramètres du débit, du niveau et du volume d'eau observés, ainsi que les informations sur la houle, sur une zone fixe ou variable. Cette observation comprend également les masses d'objets flottants sur cette zone. Les données collectées sont fournies par des capteurs, des caméras, des stations d'eau positionnées à des endroits spécifiques ou sensibles pour les rivières, les ruisseaux, les torrents, les lacs, les mers, etc.  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateObserved`:   - `dateObservedFrom`:   - `dateObservedTo`:   - `description`: Une description de cet article  - `flow`:   - `height`:   - `id`:   - `location`:   - `measuredArea`:   - `name`: Le nom de cet article.  - `objectArea`:   - `objectHeightAverage`:   - `objectHeightMax`:   - `objectVolume`:   - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `refDevice`:   - `seeAlso`:   - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `swellDirection`:   - `swellHeight`:   - `swellPeriod`:   - `type`: NGSI Type d'entité  - `waveLength`:   ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterObserved:    
  description: ' Water observation data model is intended to represent the parameters of flow, level and volume of water observed, as well as the swell information, over a fixed or variable area. This observation also includes the masses of floating objects on this area. The data collected is provided by Sensors, Cameras,Water stations positioned at specific or sensitive locations for rivers, streams, torrent, lakes, seas, etc.'    
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
      format: date-time    
      type: string    
    dateObservedFrom:    
      format: date-time    
      type: string    
    dateObservedTo:    
      format: date-time    
      type: string    
    description:    
      description: 'A description of this item'    
      type: Property    
    flow:    
      minimum: 0    
      type: number    
    height:    
      minimum: 0    
      type: number    
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
      minimum: 0    
      type: number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    objectArea:    
      minimum: 0    
      type: number    
    objectHeightAverage:    
      minimum: 0    
      type: number    
    objectHeightMax:    
      minimum: 0    
      type: number    
    objectVolume:    
      minimum: 0    
      type: number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *waterobserved_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    refDevice:    
      anyOf: *waterobserved_-_properties_-_owner_-_items_-_anyof    
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
    swellDirection:    
      maximum: 360    
      minimum: 0    
      type: number    
    swellHeight:    
      minimum: 0    
      type: number    
    swellPeriod:    
      minimum: 0    
      type: number    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - WaterObserved    
      type: string    
    waveLength:    
      minimum: 0    
      type: number    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### WaterObserved NGSI V2 valeurs clés Exemple  
Voici un exemple de WaterObserved au format JSON comme valeurs clés. Ce format est compatible avec la version 2 du NGSI lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### WaterObserved NGSI V2 normalisé Exemple  
Voici un exemple de WaterObserved au format JSON tel que normalisé. Ce format est compatible avec la version 2 du NGSI lorsque l'on utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
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
#### WaterObserved NGSI-LD valeurs clés Exemple  
Voici un exemple de WaterObserved au format JSON-LD comme valeurs clés. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### WaterObserved NGSI-LD normalisé Exemple  
Voici un exemple de WaterObserved au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
