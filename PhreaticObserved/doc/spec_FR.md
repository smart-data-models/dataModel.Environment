<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : PhréatiqueObservée  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Environment/blob/master/PhreaticObserved/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Le modèle de données est destiné à mesurer, observer et contrôler le niveau et la qualité des eaux souterraines à un moment donné (T), au moyen d'un système de surveillance fixe ou mobile. Selon le dispositif utilisé, il est également possible de mesurer la qualité de l'eau telle que sa conductivité électrique, sa teneur en sel, sa température, etc. Dans ce cas, les valeurs mesurées sont traitées par les modèles de données `WaterObserved` et `WaterQualityObserved`. Informations supplémentaires sur les attributs : Pour les attributs dédiés à l'eau, un attribut MetaData peut également être utilisé. Il contient le `TimeStamp` en secondes, la `qualification` et le contrôle `status` de la mesure.  
version : 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Date de création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage.  - `dateModified[string]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage.  - `dateObserved[string]`: La date et l'heure de cette observation au format ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedFrom[string]`: Période d'observation : Date et heure de début au format ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[string]`: Période d'observation : Date et heure de fin au format ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `depth[number]`: Profondeur de l'eau potable, depuis son identification `waterTable`. Le code d'unité (texte) de mesure donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (3 caractères au maximum). Par exemple, <code> MTR </code> représente le mètre.  . Model: [https://schema.org/depth](https://schema.org/depth)- `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `investigationDepth[number]`: Profondeur maximale à laquelle l'enquête a été effectuée. Le code d'unité (texte) de mesure donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (3 caractères au maximum). Par exemple, <code>MTR</code> représente le mètre.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `isMobile[boolean]`: L'appareil utilisé est fixe (Faux) ou mobile (Vrai)  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `measurementType[array]`: Période d'observation : Type de mesure traitée. Enum : "profondeur, volume, qualité, autre  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `pollutionRate[number]`: Taux de pollution. Le code d'unité (texte) de mesure donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (3 caractères au maximum). Par exemple, P1 représente le pourcentage.  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressure[number]`: Pression de l'eau. Le code d'unité (texte) de mesure donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (3 caractères au maximum). Par exemple, <code>BAR</code> représente le bar.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `refDevice[array]`: Référence aux dispositifs fournissant des données  . Model: [https://scehma.org/URL](https://scehma.org/URL)- `residueLevel[number]`: Niveau de résidus trouvé  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type d'entité NGSI. Il doit s'agir de PhreaticObserved  - `waterTable[number]`: Niveau auquel l'eau a été trouvée au cours de cette enquête. Le code d'unité (texte) de mesure donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (3 caractères au maximum). Par exemple, <code>MTR</code> représente le mètre.  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `dateObserved`  - `id`  - `location`  - `measurementType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PhreaticObserved:    
  description: 'The Data Model is intended to measure, observe and control the level and quality of groundwater at a given time (T), by a fixed or mobile monitoring system. Depending on the device used, it is also possible to measure the quality of water such as its electrical conductivity, its salt content, its temperature, etc. In this case, the values measured are processed by the Data Model `WaterObserved` and `WaterQualityObserved`. Additional Information about Attributes: For attributes dedicated to water, a MetaData attribute can also be used. it contains the `TimeStamp` in seconds, the `qualification` and control `status` of the measurement.'    
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
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: The date and time of this observation in ISO8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period : Start date and time in an ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period : End date and time in an ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    depth:    
      description: 'Depth of drinking water, since its identification `waterTable`. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code> MTR </code> represents Meter.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/depth    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &phreaticobserved_-_properties_-_owner_-_items_-_anyof    
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
    investigationDepth:    
      description: 'Maximum depth where the investigation was made. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter'    
      type: number    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
        units: meters    
    isMobile:    
      description: The device used is Fixed (False) or Mobile (True)    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
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
    measurementType:    
      description: 'Observation period : Type of measurement processed. Enum:''depth, volume, quality, other'''    
      items:    
        enum:    
          - depth    
          - other    
          - quality    
          - volume    
        type: string    
      minItems: 0    
      type: array    
      uniqueItems: false    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *phreaticobserved_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    pollutionRate:    
      description: 'Rate of pollution. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, P1 represents Percentage.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pressure:    
      description: 'Water Pressure. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>BAR</code> represents Bar.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
        units: Bar    
    refDevice:    
      description: Reference to the devices providing data    
      items:    
        anyOf: *phreaticobserved_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        model: https://scehma.org/URL    
        type: Relationship    
    residueLevel:    
      description: Residue level found    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be PhreaticObserved    
      enum:    
        - PhreaticObserved    
      type: string    
      x-ngsi:    
        type: Property    
    waterTable:    
      description: 'Level at which water was found during this investigation. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meter    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - measurementType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/PhreaticObserved/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### PhreaticObserved Valeurs clés de l'INSG-v2 Exemple  
Voici un exemple de PhreaticObserved au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### PhreaticObserved NGSI-v2 normalisé Exemple  
Voici un exemple de PhreaticObserved au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Valeurs clés de l'INSL-DL observées par les phréatiques Exemple  
Voici un exemple de PhreaticObserved au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
    "type": "PhreaticObserved",  
    "areaServed": "Nice Airport",  
    "dateObserved": "2020-07-07T15:05:59.408Z",  
    "depth": 20.45,  
    "description": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var.",  
    "investigationDepth": 22.35,  
    "isMobile": false,  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.66481,  
            7.196545  
        ]  
    },  
    "measurementType": [  
        "depth",  
        "volume"  
    ],  
    "name": "STLRT-MNCA-NP-015",  
    "pressure": 2.12,  
    "refDevice": [  
        "urn:ngsi-ld:Device:T1-NP-015"  
    ],  
    "waterTable": 12.75,  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### PhreaticObserved NGSI-LD normalisé Exemple  
Voici un exemple de PhreaticObserved au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
    "type": "PhreaticObserved",  
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
    "description": {  
        "type": "Property",  
        "value": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var."  
    },  
    "investigationDepth": {  
        "type": "Property",  
        "value": 22.35  
    },  
    "isMobile": {  
        "type": "Property",  
        "value": false  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                43.66481,  
                7.196545  
            ]  
        }  
    },  
    "measurementType": {  
        "type": "Property",  
        "value": [  
            "depth",  
            "volume"  
        ]  
    },  
    "name": {  
        "type": "Property",  
        "value": "STLRT-MNCA-NP-015"  
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
    "refDevice": {  
        "type": "Relationship",  
        "Object": [  
            "urn:ngsi-ld:Device:T1-NP-015"  
        ]  
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
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
