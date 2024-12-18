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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetPrintedLabelsRequest(BaseModel):
    """
    GetPrintedLabelsRequest
    """ # noqa: E501
    username: Optional[StrictStr] = Field(default=None, alias="Username")
    password: Optional[List[StrictInt]] = Field(default=None, alias="Password")
    parcel_id_list: Optional[List[StrictInt]] = Field(default=None, alias="ParcelIdList")
    print_position: Optional[StrictInt] = Field(default=None, alias="PrintPosition")
    show_print_dialog: Optional[StrictBool] = Field(default=None, alias="ShowPrintDialog")
    type_of_printer: Optional[StrictStr] = Field(default=None, alias="TypeOfPrinter")
    __properties: ClassVar[List[str]] = ["Username", "Password", "ParcelIdList", "PrintPosition", "ShowPrintDialog", "TypeOfPrinter"]

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
        """Create an instance of GetPrintedLabelsRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetPrintedLabelsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Username": obj.get("Username"),
            "Password": obj.get("Password"),
            "ParcelIdList": obj.get("ParcelIdList"),
            "PrintPosition": obj.get("PrintPosition"),
            "ShowPrintDialog": obj.get("ShowPrintDialog"),
            "TypeOfPrinter": obj.get("TypeOfPrinter")
        })
        return _obj

