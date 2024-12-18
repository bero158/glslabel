# coding: utf-8

"""
    MyGLS API

    API for MyGLS services

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Service(BaseModel):
    """
    Service
    """ # noqa: E501
    adr_parameter: Optional[StrictStr] = Field(default=None, alias="ADRParameter")
    aos_parameter: Optional[StrictStr] = Field(default=None, alias="AOSParameter")
    cs1_parameter: Optional[StrictStr] = Field(default=None, alias="CS1Parameter")
    dds_parameter: Optional[StrictStr] = Field(default=None, alias="DDSParameter")
    dpv_parameter: Optional[StrictStr] = Field(default=None, alias="DPVParameter")
    fds_parameter: Optional[StrictStr] = Field(default=None, alias="FDSParameter")
    fss_parameter: Optional[StrictStr] = Field(default=None, alias="FSSParameter")
    ins_parameter: Optional[StrictStr] = Field(default=None, alias="INSParameter")
    mmp_parameter: Optional[StrictStr] = Field(default=None, alias="MMPParameter")
    psd_parameter: Optional[StrictStr] = Field(default=None, alias="PSDParameter")
    sds_parameter: Optional[StrictStr] = Field(default=None, alias="SDSParameter")
    sm1_parameter: Optional[StrictStr] = Field(default=None, alias="SM1Parameter")
    sm2_parameter: Optional[StrictStr] = Field(default=None, alias="SM2Parameter")
    szl_parameter: Optional[StrictStr] = Field(default=None, alias="SZLParameter")
    value: Optional[StrictStr] = Field(default=None, alias="Value")
    __properties: ClassVar[List[str]] = ["ADRParameter", "AOSParameter", "CS1Parameter", "DDSParameter", "DPVParameter", "FDSParameter", "FSSParameter", "INSParameter", "MMPParameter", "PSDParameter", "SDSParameter", "SM1Parameter", "SM2Parameter", "SZLParameter", "Value"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Service from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if adr_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.adr_parameter is None and "adr_parameter" in self.model_fields_set:
            _dict['ADRParameter'] = None

        # set to None if aos_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.aos_parameter is None and "aos_parameter" in self.model_fields_set:
            _dict['AOSParameter'] = None

        # set to None if cs1_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.cs1_parameter is None and "cs1_parameter" in self.model_fields_set:
            _dict['CS1Parameter'] = None

        # set to None if dds_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.dds_parameter is None and "dds_parameter" in self.model_fields_set:
            _dict['DDSParameter'] = None

        # set to None if dpv_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.dpv_parameter is None and "dpv_parameter" in self.model_fields_set:
            _dict['DPVParameter'] = None

        # set to None if fds_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.fds_parameter is None and "fds_parameter" in self.model_fields_set:
            _dict['FDSParameter'] = None

        # set to None if fss_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.fss_parameter is None and "fss_parameter" in self.model_fields_set:
            _dict['FSSParameter'] = None

        # set to None if ins_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.ins_parameter is None and "ins_parameter" in self.model_fields_set:
            _dict['INSParameter'] = None

        # set to None if mmp_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.mmp_parameter is None and "mmp_parameter" in self.model_fields_set:
            _dict['MMPParameter'] = None

        # set to None if psd_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.psd_parameter is None and "psd_parameter" in self.model_fields_set:
            _dict['PSDParameter'] = None

        # set to None if sds_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.sds_parameter is None and "sds_parameter" in self.model_fields_set:
            _dict['SDSParameter'] = None

        # set to None if sm1_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.sm1_parameter is None and "sm1_parameter" in self.model_fields_set:
            _dict['SM1Parameter'] = None

        # set to None if sm2_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.sm2_parameter is None and "sm2_parameter" in self.model_fields_set:
            _dict['SM2Parameter'] = None

        # set to None if szl_parameter (nullable) is None
        # and model_fields_set contains the field
        if self.szl_parameter is None and "szl_parameter" in self.model_fields_set:
            _dict['SZLParameter'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['Value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Service from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ADRParameter": obj.get("ADRParameter"),
            "AOSParameter": obj.get("AOSParameter"),
            "CS1Parameter": obj.get("CS1Parameter"),
            "DDSParameter": obj.get("DDSParameter"),
            "DPVParameter": obj.get("DPVParameter"),
            "FDSParameter": obj.get("FDSParameter"),
            "FSSParameter": obj.get("FSSParameter"),
            "INSParameter": obj.get("INSParameter"),
            "MMPParameter": obj.get("MMPParameter"),
            "PSDParameter": obj.get("PSDParameter"),
            "SDSParameter": obj.get("SDSParameter"),
            "SM1Parameter": obj.get("SM1Parameter"),
            "SM2Parameter": obj.get("SM2Parameter"),
            "SZLParameter": obj.get("SZLParameter"),
            "Value": obj.get("Value")
        })
        return _obj

