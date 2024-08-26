from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class AirTemperatureTSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class AmbientNoiseTSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class AqiMajorPollutant(Enum):
    arsenic = 'arsenic'
    bap = 'bap'
    benzene = 'benzene'
    co2 = 'co2'
    nh3 = 'nh3'
    no = 'no'
    no2 = 'no2'
    o2 = 'o2'
    o3 = 'o3'
    so2 = 'so2'
    pb = 'pb'


class ArsenicTSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class AtmosphericPressureTSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class BapTSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class BenzeneTSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class Co2TSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class CoTSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class DeviceModel(BaseModel):
    areaServed: Optional[str] = Field(
        None, description='Area served by the entity or a service. '
    )
    brandName: Optional[str] = Field(
        None,
        description='Name of the brand associated with an entity, e.g., sensor, device etc',
    )
    manufacturerName: Optional[str] = Field(
        None,
        description='Name of the manufacturer associated with an entity, e.g., sensor, device etc',
    )
    modelName: Optional[str] = Field(
        None,
        description='Name of a specific model associated with an entity, e.g., sensor, device etc',
    )
    modelURL: Optional[str] = Field(
        None,
        description='URL providing further information of a specific model associated with an entity, e.g., sensor, device etc',
    )


class DeviceInfo(BaseModel):
    RFID: Optional[str] = Field(None, description='Gives the ID of the RFID reader')
    deviceBatteryStatus: Optional[str] = Field(
        None,
        description='Gives the Battery charging status of the reporting device(Connected, Disconnected)',
    )
    deviceID: Optional[str] = Field(
        None,
        description='Device ID of the physical sensor/ measurement station corresponding to this observation',
    )
    deviceList: Optional[str] = Field(
        None,
        description='Information of device part number and sub devices corresponding to this observation',
    )
    deviceModel: Optional[DeviceModel] = Field(
        None,
        description='Describes the information of the device, sensor or system in consideration',
    )
    deviceName: Optional[str] = Field(
        None,
        description='Device Name or Station name of the sensor device/station corresponding to this observation',
    )
    deviceSimNumber: Optional[str] = Field(
        None,
        description='Gives the sim number of the device in the waste management vehicle',
    )
    measurand: Optional[str] = Field(
        None, description='Property/properties sensed/observed/measured by the device'
    )
    refDevice: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Nh3TSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class NickelTSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class No2TSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class NoTSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class O2TSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class O3TSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class PbTSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class Pm10TSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class Pm25TSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class RelativeHumidityTSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class So2TSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class Type6(Enum):
    AirQualityMonitoring = 'AirQualityMonitoring'


class UvTSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class VersionInfo(BaseModel):
    comments: Optional[str] = Field(
        None, description='User comments corresponding to this observation'
    )
    endDateTime: Optional[AwareDatetime] = Field(
        None, description='Reported end time corresponding to this observation'
    )
    startDateTime: Optional[AwareDatetime] = Field(
        None, description='Reported start time corresponding to this observation'
    )
    versionName: Optional[str] = Field(
        None, description='Version name corresponding to this observation'
    )
    windType: Optional[str] = Field(
        None, description='Wind type dominate during the last 24 hours'
    )


class AirQualityMonitoring(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    airQualityIndex: Optional[float] = Field(
        None, description='Overall Air Quality Index (AQI) for the observed air quality'
    )
    airQualityLevel: Optional[str] = Field(
        None,
        description="Air Quality Category Indication. Qualitative level defined according to the local health agencies. For example, 'GOOD', 'MODERATE', 'POOR', 'UNHEALTHY', 'SEVERE', 'HAZARDOUS' etc",
    )
    airTemperatureTSA: Optional[AirTemperatureTSA] = Field(
        None, description='Air temperature time series aggregation'
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    ambientNoiseTSA: Optional[AmbientNoiseTSA] = Field(
        None, description='ambient Noise time series aggregation'
    )
    aqiMajorPollutant: Optional[AqiMajorPollutant] = Field(
        None,
        description="Major pollutant in the Air Quality Index (AQI). Enum:'arsenic, bap, benzene, co2, nh3, no, no2, o2, o3, so2, pb'",
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    arsenicTSA: Optional[ArsenicTSA] = Field(
        None, description='Arsenic time series aggregation'
    )
    atmosphericPressure: Optional[float] = Field(
        None, description='Observed air (atmospheric or barometric) pressure'
    )
    atmosphericPressureTSA: Optional[AtmosphericPressureTSA] = Field(
        None, description='Atmospheric pressure time series aggregation'
    )
    bapTSA: Optional[BapTSA] = Field(
        None, description='Benzo(a)Pyrene time series aggregation'
    )
    benzeneTSA: Optional[BenzeneTSA] = Field(
        None, description='Benzene time series aggregation'
    )
    co2TSA: Optional[Co2TSA] = Field(
        None, description='Carbon dioxide time series aggregation'
    )
    coTSA: Optional[CoTSA] = Field(
        None, description='Carbon monoxide time series aggregation'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    deviceInfo: Optional[DeviceInfo] = Field(
        None,
        description='Information about the device associated with the observations',
    )
    deviceStatus: Optional[str] = Field(
        None, description='Indicates the status of physical device or devices'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    illuminance: Optional[confloat(ge=0.0)] = Field(
        None, description='Measured illuminance'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nh3TSA: Optional[Nh3TSA] = Field(
        None, description='Ammonia time series aggregation'
    )
    nickelTSA: Optional[NickelTSA] = Field(
        None, description='Nickel time series aggregation'
    )
    no2TSA: Optional[No2TSA] = Field(
        None, description='Nitrogen dioxide time series aggregation'
    )
    noTSA: Optional[NoTSA] = Field(
        None, description='Nitrogen monoxide time series aggregation'
    )
    o2TSA: Optional[O2TSA] = Field(None, description='Oxygen time series aggregation')
    o3TSA: Optional[O3TSA] = Field(None, description='Ozone time series aggregation ')
    observationDateTime: Optional[AwareDatetime] = Field(
        None, description='Last reported time of observation'
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    pbTSA: Optional[PbTSA] = Field(None, description='Lead time series aggregation')
    pm10TSA: Optional[Pm10TSA] = Field(
        None,
        description='Particulate matter in the air with a diameter of 10 micrometers or less time series aggregation',
    )
    pm25TSA: Optional[Pm25TSA] = Field(
        None,
        description='Particulate matter in the air with a diameter of 25 micrometers or less time series aggregation',
    )
    precipitation: Optional[float] = Field(
        None, description='Observed precipitation/rainfall level over a given duration'
    )
    relativeHumidityTSA: Optional[RelativeHumidityTSA] = Field(
        None, description='Relative Humidity time series aggregation'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    so2TSA: Optional[So2TSA] = Field(
        None, description='Sulfur dioxide time series aggregation'
    )
    solarRadiation: Optional[float] = Field(
        None, description='Instantaneous solar radiation measured in kW/m2'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. it has to be AirQualityMonitoring'
    )
    uvTSA: Optional[UvTSA] = Field(
        None, description='Ultra violet radiation time series aggregation'
    )
    versionInfo: Optional[VersionInfo] = Field(
        None, description='Version information corresponding to this observation'
    )
