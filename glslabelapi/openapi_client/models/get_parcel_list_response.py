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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.error_info import ErrorInfo
from openapi_client.models.print_data_info import PrintDataInfo
from typing import Optional, Set
from typing_extensions import Self

class GetParcelListResponse(BaseModel):
    """
    GetParcelListResponse
    """ # noqa: E501
    get_parcel_list_errors: Optional[List[ErrorInfo]] = Field(default=None, alias="GetParcelListErrors")
    print_data_info_list: Optional[List[PrintDataInfo]] = Field(default=None, alias="PrintDataInfoList")
    __properties: ClassVar[List[str]] = ["GetParcelListErrors", "PrintDataInfoList"]

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
        """Create an instance of GetParcelListResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in get_parcel_list_errors (list)
        _items = []
        if self.get_parcel_list_errors:
            for _item_get_parcel_list_errors in self.get_parcel_list_errors:
                if _item_get_parcel_list_errors:
                    _items.append(_item_get_parcel_list_errors.to_dict())
            _dict['GetParcelListErrors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in print_data_info_list (list)
        _items = []
        if self.print_data_info_list:
            for _item_print_data_info_list in self.print_data_info_list:
                if _item_print_data_info_list:
                    _items.append(_item_print_data_info_list.to_dict())
            _dict['PrintDataInfoList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetParcelListResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "GetParcelListErrors": [ErrorInfo.from_dict(_item) for _item in obj["GetParcelListErrors"]] if obj.get("GetParcelListErrors") is not None else None,
            "PrintDataInfoList": [PrintDataInfo.from_dict(_item) for _item in obj["PrintDataInfoList"]] if obj.get("PrintDataInfoList") is not None else None
        })
        return _obj


