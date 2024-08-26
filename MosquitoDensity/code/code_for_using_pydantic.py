from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


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


class DeviceModel(BaseModel):
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
    deviceBatteryStatus: Optional[str] = Field(
        None,
        description='Gives the Battery charging status of the reporting device(Connected, Disconnected)',
    )
    deviceModel: Optional[DeviceModel] = Field(
        None,
        description='Describes the information of the device, sensor or system in consideration',
    )
    deviceName: Optional[str] = Field(
        None,
        description='Device Name or Station name of the sensor device/station corresponding to this observation',
    )
    measurand: Optional[str] = Field(
        None, description='Property/properties sensed/observed/measured by the device'
    )
    rfID: Optional[str] = Field(None, description='Gives the ID of the RFID reader')


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


class MosquitoDensity1(BaseModel):
    femaleSpeciesCount: Optional[float] = Field(
        None,
        description='The total count of the female mosquitoes of the species identified by the device',
    )
    maleSpeciesCount: Optional[float] = Field(
        None,
        description='The total count of the male mosquitoes of the species identified by the device',
    )
    mosquitoSpecies: Optional[str] = Field(
        None,
        description='The binomial/ zoological nomenclature of the mosquito species as identified by the device',
    )
    totalSpeciesCount: Optional[float] = Field(
        None,
        description='The total count of a particular species detected by the device',
    )


class Type6(Enum):
    MosquitoDensity = 'MosquitoDensity'


class MosquitoDensity(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    airTemperature: Optional[Dict[str, Any]] = Field(
        None,
        description='Observed value of air temperature. Value is an object containing attributes representing statistical aggregates derived from past data',
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    dataDescriptor: Optional[AnyUrl] = Field(
        None, description='URI pointing to the data-descriptor entity'
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
    deviceId: Optional[str] = Field(
        None,
        description='Device ID of the physical sensor/ measurement station corresponding to this observation',
    )
    deviceInfo: Optional[DeviceInfo] = Field(
        None,
        description='Information about the device associated with the observations',
    )
    deviceSimNumber: Optional[str] = Field(
        None,
        description='Gives the sim number of the device in the waste management vehicle',
    )
    femaleTotal: Optional[float] = Field(
        None,
        description='The total count of females of a particular species, as identified by the device.',
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
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    maleTotal: Optional[float] = Field(
        None,
        description='The total count of males of a particular species, as identified by the device.',
    )
    mosquitoDensity: Optional[MosquitoDensity1] = Field(
        None,
        description='The binomial (or) zoological nomenclature of the mosquito species and its count as identified by the device corresponding to this observation',
    )
    name: Optional[str] = Field(None, description='The name of this item')
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
    precipitation: Optional[float] = Field(
        None, description='Observed precipitation/rainfall level over a given duration'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    speciesName: Optional[str] = Field(
        None,
        description='The binomial/ zoological nomenclature of the species identified by the device.',
    )
    speciesTotal: Optional[float] = Field(
        None,
        description='The total count of a particular species, as detected by the device.',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be MosquitoDensity'
    )
