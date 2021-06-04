Entité : RainFallRadarObservation  
=================================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Environment/blob/master/RainFallRadarObservation/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Le modèle de données est destiné à mesurer les glissements d'eau sur une zone prédéfinie par un ensemble de 4 lieux représentés par un format de propriété géographique**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `atmosphericPressure`: La pression atmosphérique observée mesurée en Hecto Pascals  - `cellsSize`: Taille de chaque cellule constituant le radar. Le code d'unité (texte) de mesure est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **MTR** représente **Mètres**.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateObserved`: La date et l'heure de cette observation au format ISO8601 UTC. Elle peut être représentée par un instant précis ou par un intervalle ISO8601.  - `dateObservedFrom`: Date et heure de début de la période d'observation. Voir dateObserved. Elle peut être représentée par un instant précis ou par un intervalle ISO8601.  - `dateObservedTo`: Date et heure de fin de la période d'observation. Voir dateObserved. Elle peut être représentée par un instant précis ou par un intervalle ISO8601.  - `description`: Une description de cet article  - `feelLikesTemperature`: Appréciation de la température de l'objet  - `id`: Identifiant unique de l'entité  - `illuminance`: (https://en.wikipedia.org/wiki/Illuminance) observée mesurée en lux (lx) ou en lumens par mètre carré (cd-sr-m-2).  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `mapScale`: Échelle de la carte. Relation entre la longueur de la cellSize et sa représentation sur la carte.  - `measuredArea`: Référence de la surface mesurée. Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **MTK** représente les mètres carrés.  - `name`: Le nom de cet élément.  - `numberOfCol`: Nombre de Cols permettant la lecture de l'attribut `rainFallradarContent`.  - `numberOfRow`: Nombre de lignes permettant la lecture de l'attribut `rainFallradarContent`.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `rainFallRadarContent`: Chemin et nom du fichier qui a fourni l'information observée  - `refDevice`: Référence à un [Dispositif] (https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) qui a capturé cette observation.  - `refPointOfInterest`: Référence à un [PointOfInterest] (https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) lié à l'observation.  - `relativeHumidity`: L'humidité dans l'air  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `temperature`: Température de l'article  - `type`: Type d'entité NGSI. Il doit être RainFallRadarObserved.  - `visibility`: Catégories de visibilité  - `weatherType`: Description textuelle de la météo  - `windDirection`: Direction du pari du vent  - `windSpeed`: Intensité du vent    
Propriétés requises  
- `dateObserved`  - `id`  - `location`  - `rainFallRadarContent`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    atmosphericPressure:    
      description: 'The atmospheric pressure observed measured in Hecto Pascals'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Hecto pascals'    
    cellsSize:    
      description: 'Size of each cell constituting the radar. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents **Meters**'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
      description: 'The date and time of this observation in ISO8601 UTC format. It can be represented by a specific time instant or by an ISO8601 interval'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateObservedFrom:    
      description: 'Observation period start date and time. See dateObserved. It can be represented by a specific time instant or by an ISO8601 interval'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateObservedTo:    
      description: 'Observation period end date and time. See dateObserved. It can be represented by a specific time instant or by an ISO8601 interval'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    description:    
      description: 'A description of this item'    
      type: Property    
    feelLikesTemperature:    
      description: 'Temperature appreciation of the item'    
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
      type: Property    
    illuminance:    
      description: '(https://en.wikipedia.org/wiki/Illuminance) observed measured in lux (lx) or lumens per square metre (cd·sr·m−2).'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
      type: Geoproperty    
    mapScale:    
      description: 'Map Scale. Relationship between the length of the cellSize and its representation on the map'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    measuredArea:    
      description: 'Reference of the surface measured. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTK** represents Square Meters'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'square meters'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    numberOfCol:    
      description: 'Number of Cols allowing the reading of the `rainFallradarContent` attribute'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    numberOfRow:    
      description: 'Number of Rows allowing the reading of the `rainFallradarContent` attribute'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *rainfallradarobservation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    rainFallRadarContent:    
      description: 'Path and filename which provided the information observed'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
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
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    relativeHumidity:    
      description: 'Humidity in the Air'    
      maximum: 1    
      minimum: 0    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    temperature:    
      description: 'Temperature of the item'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be RainFallRadarObserved'    
      enum:    
        - RainFallRadarObserved    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    weatherType:    
      description: 'Text description of the weather'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text.    
    windDirection:    
      description: 'Direction of the wind bet'    
      maximum: 180    
      minimum: -180    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    windSpeed:    
      description: 'Intensity of the wind'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http//schema.org/Number    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - rainFallRadarContent    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### RainFallRadarObservation NGSI-v2 valeurs-clés Exemple  
Voici un exemple d'une observation RainFallRadarObservation au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### RainFallRadarObservation NGSI-v2 normalisée Exemple  
Voici un exemple d'une observation RainFallRadarObservation au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### RainFallRadarObservation Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'une observation RainFallRadarObservation au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### RainFallRadarObservation NGSI-LD normalisé Exemple  
Voici un exemple d'une observation RainFallRadarObservation au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
