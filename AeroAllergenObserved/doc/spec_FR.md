Entité : AeroAllergenObserved  
=============================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Environment/blob/master/AeroAllergenObserved/LICENSE.md)  
Description globale : **Une observation des niveaux de pollen à un certain endroit et à un certain moment.**  

## Liste des biens  

- `address`: L'adresse postale.  - `allergenRisk`: Risque allergique global correspondant aux aéroallergènes observés.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateObserved`: La date et l'heure de cette observation au format UTC ISO8601. Elle peut être représentée par un instant précis ou par un intervalle ISO8601.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `refDevice`: Une référence au(x) dispositif(s) qui a(ont) capté cette observation.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: NGSI Type d'entité    
Propriétés requises  
- `dateObserved`  - `id`  - `location`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AeroAllergenObserved:    
  description: 'An observation of pollen levels at a certain place and time.'    
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
    allergenRisk:    
      description: 'Overall allergen risk corresponding to the aero allergens observed.'    
      enum:    
        - none    
        - low    
        - moderate    
        - high    
        - veryHigh    
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
      description: 'The date and time of this observation in ISO8601 UTCformat. It can be represented by a specific time instant or by an ISO8601 interval.'    
      type: Property    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *aeroallergenobserved_-_properties_-_owner_-_items_-_anyof    
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
      description: 'A reference to the device(s) which captured this observation.'    
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
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - AeroAllergenObserved    
      type: Property    
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### AeroAllergenObserved NGSI V2 key-values Exemple  
Voici un exemple d'AeroAllergenObserved en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### AeroAllergenObserved NGSI V2 normalisé Exemple  
Voici un exemple d'AeroAllergenObserved au format JSON tel que normalisé. Ce format est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### AeroAllergenObserved NGSI-LD valeurs clés Exemple  
Voici un exemple d'AeroAllergenObserved en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### AeroAllergenObserved NGSI-LD normalisé Exemple  
Voici un exemple d'AeroAllergenObserved au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
