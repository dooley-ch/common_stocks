# *******************************************************************************************
#  File:  gics_sector_test.py
#
#  Created: 22-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  22-06-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

import orjson
import csCore.model.data as db_model

_gics_data_1 = """
    {
        "id":60,
        "name":"Real Estate",
        "industry_group":[
            {
                "id":6010,
                "name":"Real Estate",
                "industry":[
                    {
                        "id":601010,
                        "name":"Equity Real Estate Investment Trusts (REITs)",
                        "sub_industry":[
                            {"id":60101010, "name": "Diversified REITs"},
                            {"id":60101020, "name": "Industrial REITs"},
                            {"id":60101030, "name": "Hotel & Resort REITs"},
                            {"id":60101040, "name": "Office REITs"},
                            {"id":60101050, "name": "Health Care REITs"},
                            {"id":60101060, "name": "Residential REITs"},
                            {"id":60101070, "name": "Retail REITs"},
                            {"id":60101080, "name": "Specialized REITs"}
                        ]
                    },
                    {
                        "id":601020,
                        "name":"Real Estate Management & Development",
                        "sub_industry":[
                            {"id":60102010, "name": "Diversified Real Estate Activities"},
                            {"id":60102020, "name": "Real Estate Operating Companies"},
                            {"id":60102030, "name": "Real Estate Development"},
                            {"id":60102040, "name": "Real Estate Services"}
                        ]
                    }
                ]
            },
            {
                "id":6010,
                "name":"Real Estate",
                "industry":[
                    {
                        "id":601010,
                        "name":"Equity Real Estate Investment Trusts (REITs)",
                        "sub_industry":[
                            {"id":60101010, "name": "Diversified REITs"},
                            {"id":60101020, "name": "Industrial REITs"},
                            {"id":60101030, "name": "Hotel & Resort REITs"},
                            {"id":60101040, "name": "Office REITs"},
                            {"id":60101050, "name": "Health Care REITs"},
                            {"id":60101060, "name": "Residential REITs"},
                            {"id":60101070, "name": "Retail REITs"},
                            {"id":60101080, "name": "Specialized REITs"}
                        ]
                    }
                ]
            }
        ]
    }
"""

_gics_data_2 = """
    {
        "id":60,
        "name":"Real Estate",
        "industry_group":[
            {
                "id":6010,
                "name":"Real Estate",
                "industry":[
                    {
                        "id":601010,
                        "name":"Equity Real Estate Investment Trusts (REITs)",
                        "sub_industry":[
                            {"id":60101010, "name": "Diversified REITs"},
                            {"id":60101020, "name": "Industrial REITs"},
                            {"id":60101030, "name": "Hotel & Resort REITs"},
                            {"id":60101040, "name": "Office REITs"},
                            {"id":60101050, "name": "Health Care REITs"},
                            {"id":60101060, "name": "Residential REITs"},
                            {"id":60101070, "name": "Retail REITs"},
                            {"id":60101080, "name": "Specialized REITs"}
                        ]
                    },
                    {
                        "id":601020,
                        "name":"Real Estate Management & Development",
                        "sub_industry":[
                            {"id":60102010, "name": "Diversified Real Estate Activities"},
                            {"id":60102020, "name": "Real Estate Operating Companies"},
                            {"id":60102030, "name": "Real Estate Development"},
                            {"id":60102040, "name": "Real Estate Services"}
                        ]
                    }
                ]
            },
            {
                "id":6010,
                "name":"Real Estate",
                "industry":[
                    {
                        "id":601010,
                        "name":"Equity Real Estate Investment Trusts (REITs)",
                        "sub_industry":[
                            {"id":60101010, "name": "Diversified REITs"},
                            {"id":60101020, "name": "Industrial REITs"},
                            {"id":60101030, "name": "Hotel & Resort REITs"},
                            {"id":60101040, "name": "Office REITs"},
                            {"id":60101050, "name": "Health Care REITs"},
                            {"id":60101060, "name": "Residential REITs"},
                            {"id":60101070, "name": "Retail REITs"},
                            {"id":60101080, "name": "Specialized REITs"}
                        ]
                    }
                ]
            }
        ],
        "metadata": {
            "lock_version": 1,
            "created_at": "2022-06-16T16:28:29.940+00:00",
            "updated_at": "2022-06-16T16:28:29.940+00:00"
        }
    }
"""


class TestGicsSector:
    """
    This class tests the GicsSector DTO class
    """
    def test_create(self) -> None:
        sector = db_model.GicsSector(10, 'Energy')

        assert sector.id == 10
        assert sector.name == 'Energy'

    def test_create_item(self) -> None:
        sub_industry = db_model.SubIndustry(60101080, 'Specialized REITs')

        industry = db_model.Industry(601010, 'Equity Real Estate Investment Trusts (REITs)')
        industry.sub_industry.append(sub_industry)

        industry_group = db_model.IndustryGroup(6010, 'Real Estate')
        industry_group.industry.append(industry)

        sector = db_model.GicsSector(60, 'Real Estate')
        sector.industry_group.append(industry_group)

        assert sector.id == 60
        assert sector.name == 'Real Estate'
        assert len(sector.industry_group) == 1

    def test_create_extended(self) -> None:
        sub_industry = db_model.SubIndustry(60101080, 'Specialized REITs')

        industry = db_model.Industry(601010, 'Equity Real Estate Investment Trusts (REITs)')
        industry.sub_industry.append(sub_industry)

        industry_group = db_model.IndustryGroup(6010, 'Real Estate')
        industry_group.industry.append(industry)

        sector = db_model.GicsSectorExt(60, 'Real Estate')
        sector.industry_group.append(industry_group)

        assert sector.id == 60
        assert sector.name == 'Real Estate'
        assert len(sector.industry_group) == 1
        assert sector.metadata.lock_version == 0

    def test_parse_config(self) -> None:
        data = orjson.loads(_gics_data_1)
        sector = db_model.GicsSector.parse(data)

        assert sector.id == 60
        assert sector.name == 'Real Estate'
        assert len(sector.industry_group) == 2

    def test_parse_config_ext(self) -> None:
        data = orjson.loads(_gics_data_2)
        sector = db_model.GicsSectorExt.parse(data)

        assert sector.id == 60
        assert sector.name == 'Real Estate'
        assert len(sector.industry_group) == 2
        assert sector.metadata.lock_version == 1
