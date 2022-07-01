# *******************************************************************************************
#  File:  gics.py
#
#  Created: 01-07-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  01-07-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"
__all__ = ['load_gics']

import attrs
import orjson
import csCore.utils as utils


@attrs.frozen
class SubIndustry:
    id: int
    name: str


@attrs.frozen
class Industry:
    id: int
    name: str
    sub_industries: list[SubIndustry] = attrs.Factory(list)


@attrs.frozen
class IndustryGroup:
    id: int
    name: str
    industries: list[Industry] = attrs.Factory(list)


@attrs.frozen
class Sector:
    id: int
    name: str
    industry_groups: list[IndustryGroup] = attrs.Factory(list)


def load_gics() -> list[Sector] | None:
    data_folder = utils.find_data_folder()
    data_file = data_folder.joinpath('gics.json')

    if data_file.exists():
        sectors: list[Sector] = list()

        content = data_file.read_text()
        data = orjson.loads(content)

        # Sectors
        for sec in data:
            id = sec['id']
            name = sec['name']
            grps = sec['items']

            sec_obj = Sector(id, name)
            sectors.append(sec_obj)

            # Groups
            for grp in grps:
                id = grp['id']
                name = grp['name']
                inds = grp['items']

                grp_obj = IndustryGroup(id, name)
                sec_obj.industry_groups.append(grp_obj)

                # Industry
                for ind in inds:
                    id = ind['id']
                    name = ind['name']
                    subs = ind['items']

                    ind_obj = Industry(id, name)
                    grp_obj.industries.append(ind_obj)

                    # Sub Industry
                    for sub in subs:
                        id = sub['id']
                        name = sub['name']
                        ind_obj.sub_industries.append(SubIndustry(id, name))

        return sectors
