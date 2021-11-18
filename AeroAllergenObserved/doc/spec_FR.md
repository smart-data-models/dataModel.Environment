Entité : AeroAllergenObserved  
=============================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Environment/blob/master/AeroAllergenObserved/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Une observation des niveaux de pollen à un certain endroit et à un certain moment.**  

## Liste des propriétés  

- `address`: L'adresse postale  - `allergenRisk`: Risque allergénique global correspondant aux aéro-allergènes observés.  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateObserved`: La date et l'heure de cette observation au format ISO8601 UTC. Elle peut être représentée par un instant précis ou par un intervalle ISO8601.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `refDevice`: Une référence au(x) dispositif(s) qui a (ont) capturé cette observation.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: NGSI Type d'entité    
Propriétés requises  
- `dateObserved`  - `id`  - `location`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AeroAllergenObserved:    
  description: 'An observation of pollen levels at a certain place and time.'    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    allergenRisk:    
      description: 'Overall allergen risk corresponding to the aero allergens observed.'    
      enum:    
        - none    
        - low    
        - moderate    
        - high    
        - veryHigh    
      type: string    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: 'The date and time of this observation in ISO8601 UTCformat. It can be represented by a specific time instant or by an ISO8601 interval.'    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
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
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *aeroallergenobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      description: 'A reference to the device(s) which captured this observation.'    
      x-ngsi:    
        type: Relationship    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - AeroAllergenObserved    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/AeroAllergenObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/AeroAllergenObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Exemples de charges utiles  
#### AeroAllergenObserved Valeurs-clés NGSI-v2 Exemple  
Voici un exemple d'AeroAllergenObserved au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### AeroAllergenObserved NGSI-v2 normalisé Exemple  
Voici un exemple d'un AeroAllergenObserved au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### AeroAllergenObserved Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'AeroAllergenObserved au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
      "addressLocality": "Ciudad de M\u00e9xico",  
      "streetAddress": "Colegio Franco-Ingl\u00e9s",  
      "type": "PostalAddress"  
    }  
  },  
  "alnus_Level": {  
    "type": "Property",  
    "value": "moderate"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### AeroAllergenObserved NGSI-LD normalisé Exemple  
Voici un exemple d'un AeroAllergenObserved au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "address": {  
    "addressCountry": "MX",  
    "addressLocality": "Ciudad de M\u00e9xico",  
    "streetAddress": "Colegio Franco-Ingl\u00e9s",  
    "type": "PostalAddress"  
  },  
  "allergenRisk": "moderate",  
  "alnus": 40,  
  "alnus_Allergenicity": "3",  
  "alnus_Level": "moderate",  
  "casuarina": 1,  
  "casuarina_Allergenicity": "3",  
  "casuarina_Level": "low",  
  "dateObserved": {  
    "@type": "DateTime",  
    "@value": "2018-02-11T00:00:00.00Z"  
  },  
  "id": "urn:ngsi-ld:AeroAllergenObserved:AeroAllergenObserved-CDMX-Pollen-Cuajimalpa",  
  "location": {  
    "coordinates": [  
      -99.276977,  
      19.381877  
    ],  
    "type": "Point"  
  },  
  "modifiedAt": "2018-02-16T17:24:39.00Z",  
  "source": "http://rema.atmosfera.unam.mx/rema/",  
  "type": "AeroAllergenObserved"  
}  
```  
