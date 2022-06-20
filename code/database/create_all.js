// *******************************************************************************************
//  File:  create_all.js
//
//  Created: 19-06-2022
//
//  Copyright (c) 2022 James Dooley <james@dooley.ch>
//
//  History:
//  19-06-2022: Initial version
//
// *******************************************************************************************

load("create_db.js")

const array = ["common_stocks_prod", "common_stocks_test", "common_stocks_dev"]

array.forEach(function (item, index) {
  create_database(item);
});
