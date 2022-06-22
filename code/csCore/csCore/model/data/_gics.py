# *******************************************************************************************
#  File:  _gics.py
#
#  Created: 22-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  22-06-2022: Initial version
#
# *******************************************************************************************
from __future__ import annotations

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"
__all__ = ['SubIndustry', 'SubIndustryList', 'Industry', 'IndustryList', 'IndustryGroup',
           'IndustryGroupList', 'GicsSector', 'GicsSectorExt']

from typing import NewType, Any
import attrs
from ._core import Metadata


@attrs.frozen
class SubIndustry:
    id: int = attrs.field(validator=[attrs.validators.instance_of(int), attrs.validators.ge(10101010),
                           attrs.validators.le(60102040)])
    name: str = attrs.field(validator=[attrs.validators.instance_of(str)])


SubIndustryList = NewType('SubIndustryList', list[SubIndustry])


@attrs.frozen
class Industry:
    id: int = attrs.field(validator=[attrs.validators.instance_of(int), attrs.validators.ge(101010),
                                     attrs.validators.le(601020)])
    name: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    sub_industry: SubIndustryList = attrs.Factory(list)


IndustryList = NewType('IndustryList', list[Industry])


@attrs.frozen
class IndustryGroup:
    id: int = attrs.field(validator=[attrs.validators.instance_of(int), attrs.validators.ge(1010),
                                     attrs.validators.le(6010)])
    name: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    industry: IndustryList = attrs.Factory(list)


IndustryGroupList = NewType('IndustryList', list[IndustryGroup])


@attrs.frozen
class GicsSector:
    id: int = attrs.field(validator=[attrs.validators.instance_of(int), attrs.validators.ge(10),
                                     attrs.validators.le(60)])
    name: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    industry_group: IndustryGroupList = attrs.Factory(list)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> GicsSector:
        id = data['id']
        name = data['name']
        groups = data['industry_group']

        sector = GicsSector(id, name)
        for item in groups:
            id = item['id']
            name = item['name']
            industries = item['industry']

            group = IndustryGroup(id, name)
            for item in industries:
                id = item['id']
                name = item['name']
                sub_industries = item['sub_industry']

                industry = Industry(id, name)
                for item in sub_industries:
                    id = item['id']
                    name = item['name']

                    industry.sub_industry.append(SubIndustry(id, name))

                group.industry.append(industry)

            sector.industry_group.append(group)

        return sector


@attrs.frozen
class GicsSectorExt(GicsSector):
    metadata: Metadata = attrs.Factory(Metadata)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> GicsSectorExt:
        id = data['id']
        name = data['name']
        groups = data['industry_group']
        metadata = data['metadata']

        sector = GicsSectorExt(id, name, metadata=Metadata(**metadata))
        for item in groups:
            id = item['id']
            name = item['name']
            industries = item['industry']

            group = IndustryGroup(id, name)
            for item in industries:
                id = item['id']
                name = item['name']
                sub_industries = item['sub_industry']

                industry = Industry(id, name)
                for item in sub_industries:
                    id = item['id']
                    name = item['name']

                    industry.sub_industry.append(SubIndustry(id, name))

                group.industry.append(industry)

            sector.industry_group.append(group)

        return sector
