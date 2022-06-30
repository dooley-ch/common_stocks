# *******************************************************************************************
#  File:  gics_test.py
#
#  Created: 30-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  30-06-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

import csCore.datastore as ds
import csCore.model.data as model


class TestGics:
    def test_insert(self, mongodb_connection, database_name) -> None:
        store = ds.GicsSectorStore(mongodb_connection, database_name)
        store.clear()

        sub_industry = model.SubIndustry(60101080, 'Specialized REITs')

        industry = model.Industry(601010, 'Equity Real Estate Investment Trusts (REITs)')
        industry.sub_industry.append(sub_industry)

        industry_group = model.IndustryGroup(6010, 'Real Estate')
        industry_group.industry.append(industry)

        sector = model.GicsSectorExt(60, 'Real Estate')
        sector.industry_group.append(industry_group)

        assert store.insert(sector)

    def test_get(sel, mongodb_connection, database_name) -> None:
        store = ds.CompanyStore(mongodb_connection, database_name)
        store.clear()

        store = ds.GicsSectorStore(mongodb_connection, database_name)
        store.clear()

        sub_industry = model.SubIndustry(60101080, 'Specialized REITs')

        industry = model.Industry(601010, 'Equity Real Estate Investment Trusts (REITs)')
        industry.sub_industry.append(sub_industry)

        industry_group = model.IndustryGroup(6010, 'Real Estate')
        industry_group.industry.append(industry)

        sector = model.GicsSectorExt(60, 'Real Estate')
        sector.industry_group.append(industry_group)

        assert store.insert(sector)

        record = store.get('Real Estate')
        assert record