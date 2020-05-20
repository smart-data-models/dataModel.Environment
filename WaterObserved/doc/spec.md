Water Observed:
  - required:
    - location
    - dateObserved
    - dateObservedFrom
    - dateObservedTo
  - type: "object"
    - allOf:
      - $ref: ""https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"
      - "$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons"  
   - description: >
      ## Description
      Water observation data model is intended to represent the parameters of flow, level and volume of water observed, as well as the swell information, over a fixed or variable area. This observation also includes the masses of floating objects on this area.
The data collected is provided by [Sensors], [Cameras], [Water stations] positioned at specific or sensitive locations for rivers, streams, torrent, lakes, seas, etc..
      ## Data Model
  - properties:  
    - id:
      - x-ngsi:
        - type: "Property"
      - type : "string"
      - format: "uri"
      - Description: "mandatory element for NGSI"
    - type:
      - x-ngsi:
        - type: "Property"
      - type : "string"
      - value: "WaterObserved"
      - Description: "mandatory element for NGSI"
    - dataProvider:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
        Specifies the URL to information about the provider of this information
    - source:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text", "https://schema.org/URL"
      - type: "string"
      - description: >
            A sequence of characters giving the source of the entity data.
    - name:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/name"
      - type: "string"
      - type: "string"
      - description: >
            Name given to the observation.
    - alternateName:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/alternateName"
      - type: "string"
      - description: >
            Alternative Name given to the observation
    - description:
      - x-ngsi:
        - type: "Property"
        - model: "https://uri.etsi.org/ngsi-ld/description", "https://schema.org/description"
      - $ref: 'https://jason-fox.github.io/swagger-datamodel-test/common.yaml#/Description'   
    - seeAlso:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text", "https://schema.org/URL"
      - type: "string"
      - description: >
            Text or Link that can provide additional information.
    - location:
      - $ref: "https://github.com/smart-data-models/data-models/blob/master/common-schema.yaml#/Movable"
    - address:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/address"
      - $ref: "https://github.com/smart-data-models/data-models/blob/master/common-schema.yaml#/Address"
    - areaServed:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"
      - description: >
            Zone of level higher to the attributes Location & Address to gather and cross information (ex district, etc).
    - refDevice:
      - x-ngsi:
        - type: "Relationship"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
         A reference to the device which captured this observation.
    - dateObserved:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/DateTime"
      - type: "string"
      - format: "date-time"
      - description: >
        Date and time of this observation represented by an ISO8601 UTC format.
        It can be represented by an specific time instant or by an ISO8601 interval to 
        separate attributes `dateObservedFrom`,`dateObservedTo`.
    - dateObservedFrom:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/DateTime"
      - type: "string"
      - format: "date-time"
      - description: >
         Observation period : Start date and time in an ISO8601 UTC format.
    - dateObservedTo:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/DateTime"
      - type: "string"
      - format: "date-time"
      - description: >
         Observation period : End date and time in an ISO8601 UTC format.
    - flow:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/Number"
      - type: "number"
      - minimum: 0
      - description: >
         Water Flow observed. The unit code (text) of measurement given using the 
         [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)
          (max. 3 characters). For instance, **MQS** represents Cubic Meter per Second.
    - height:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/Number"
      - type: "number"
      - minimum: 0
      - description: >
         Water height - Level reach on alert coasts. The unit code (text) of measurement given using the 
         [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)
          (max. 3 characters). For instance, **MTR** represents Meter.
    - swellHeight:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/Number"
      - type: "number"
      - minimum: 0      
      - description: >
         Water height - Level reach on alert coasts. The unit code (text) of measurement given using the 
         [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)
          (max. 3 characters). For instance, **MTR** represents Meter.    
    - swellPeriod:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/Number"
      - type: "number"
      - minimum: 0      
      - description: >
         Water height - Level reach on alert coasts. The unit code (text) of measurement given using the 
         [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)
          (max. 3 characters). For instance, **SEC** represents Seconds.    
    - swellDirection:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/Number"
      - type: "number"
      - minimum: 0
      - maximum: 360
      - description: >
         Water height - Level reach on alert coasts. The unit code (text) of measurement given using the 
         [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)
          (max. 3 characters). For instance, **DD** represents Degree. If entered, the value must be between 0 and 360.    
    - waveLength:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/Number"
      - type: "number"
      - minimum: 0
      - description: >
         Water height - Level reach on alert coasts. The unit code (text) of measurement given using the 
         [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)
          (max. 3 characters). For instance, **MTR** represents Meters.
    - measuredArea:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/Number"
      - type: "number"
      - minimum: 0      
      - description: >
         Reference of the surface measured. The unit code (text) of measurement given using the 
         [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)
          (max. 3 characters). For instance, **MTK** represents Square Meters.
    - objectArea:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/Number"
      - type: "number"
      - minimum: 0      
      - description: >
         Percentage occupied by floating object in the area.. The unit code (text) of measurement 
         given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, **P1** represents Percentage.
    - objectHeightAverage:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/Number"
      - type: "number"
      - minimum: 0
      - description: >
         Average height raised. The unit code (text) of measurement given using the 
         [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)
          (max. 3 characters). For instance, **MTR** represents Meter.
    - objectHeightMax:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/Number"
      - type: "number"
      - minimum: 0
      - description: >
         Maximum height raised. The unit code (text) of measurement given using the 
         [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)
          (max. 3 characters). For instance, **MTR** represents Meter.
    - objectVolume:
      - x-ngsi:
        - type: "Property"
        model: "https://schema.org/Number"
      - type: "number"
      - minimum: 0
      - description: >
         Estimated volume raised. The unit code (text) of measurement given using the 
         [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)
          (max. 3 characters). For instance, **MTQ** represents Cubic Meter.
