// *******************************************************************************************
//  File:  create.js
//
//  Created: 19-06-2022
//
//  Copyright (c) 2022 James Dooley <james@dooley.ch>
//
//  History:
//  19-06-2022: Initial version
//
// *******************************************************************************************

function create_config(db) {
	// This function creates the config collection
	
	db.createCollection('config', {
	  validator: {
	    $jsonSchema: {
	      bsonType: 'object',
	      title: 'config',
	      required: ['name', 'items', 'metadata'],
	      properties: {
	        name: {
	          bsonType: 'string'
	        },
	        items: {
	          bsonType: 'array',
	          items: {
	            title: 'config_item',
	            required: ['key', 'value'],
	            properties: {
	              key: {
	                bsonType: 'string'
	              },
	              value: {
	                bsonType: 'string'
	              }
	            }
	          }
	        },
	        metadata: {
	          bsonType: 'object',
	          title: 'metadata',
	          required: ['lock_version', 'created_at', 'updated_at'],
	          properties: {
	            lock_version: {
	              bsonType: 'int'
	            },
	            created_at: {
	              bsonType: 'date'
	            },
	            updated_at: {
	              bsonType: 'date'
	            }
	          }
	        }
	      }
	    }
	  }
	});
	db.config.createIndex({
	  "name": 1
	}, {
	  name: "config_ix_unique_name",
	  unique: true
	})

	db.config.createIndex({
	  "name": 1,
	  "items": 1,
	  "metadata": 1
	}, {
	  name: "config_ix_search_by_name"
	});
}

function create_master(db) {	
	// This function creates the master collection
	
	db.createCollection('master', {
	  validator: {
	    $jsonSchema: {
	      bsonType: 'object',
	      title: 'master',
	      required: ['ticker', 'name', 'cik', 'figi', 'sub_industry', 'indexes', 'metadata'],
	      properties: {
	        ticker: {
	          bsonType: 'string'
	        },
	        name: {
	          bsonType: 'string'
	        },
	        cik: {
	          bsonType: 'string'
	        },
	        figi: {
	          bsonType: 'string'
	        },
	        sub_industry: {
	          bsonType: 'string'
	        },
	        indexes: {
	          bsonType: 'array',
	          items: {
	            bsonType: 'string'
	          }
	        },
	        metadata: {
	          bsonType: 'object',
	          title: 'metadata',
	          required: ['lock_version', 'created_at', 'updated_at'],
	          properties: {
	            lock_version: {
	              bsonType: 'int'
	            },
	            created_at: {
	              bsonType: 'date'
	            },
	            updated_at: {
	              bsonType: 'date'
	            }
	          }
	        }
	      }
	    }
	  }
	});
	db.master.createIndex({
	  "ticker": 1
	}, {
	  name: "master_ix_1",
	  unique: true
	})

	db.master.createIndex({
	  "ticker": 1,
	  "name": 1,
	  "cik": 1,
	  "figi": 1,
	  "sub_industry": 1
	}, {
	  name: "master_ix_search_by_ticker"
	})

	db.master.createIndex({
	  "name": 1,
	  "ticker": 1,
	  "cik": 1,
	  "figi": 1,
	  "sub_industry": 1
	}, {
	  name: "master_ix_search_by_name"
	});
}

function create_gics_sector(db) {
	// This function creates the gics_sector collection
	
	db.createCollection('gics_sector', {
	  validator: {
	    $jsonSchema: {
	      bsonType: 'object',
	      title: 'gics_sector',
	      required: ['id', 'name', 'industry_group', 'metadata'],
	      properties: {
	        id: {
	          bsonType: 'int'
	        },
	        name: {
	          bsonType: 'string'
	        },
	        industry_group: {
	          bsonType: 'array',
	          items: {
	            title: 'gics_industry_group',
	            required: ['id', 'name', 'industry'],
	            properties: {
	              id: {
	                bsonType: 'int'
	              },
	              name: {
	                bsonType: 'string'
	              },
	              industry: {
	                bsonType: 'array',
	                items: {
	                  title: 'gics_industry',
	                  required: ['id', 'name', 'sub_industry'],
	                  properties: {
	                    id: {
	                      bsonType: 'int'
	                    },
	                    name: {
	                      bsonType: 'string'
	                    },
	                    sub_industry: {
	                      bsonType: 'array',
	                      items: {
	                        title: 'gics_sub_industry',
	                        required: ['id', 'name'],
	                        properties: {
	                          id: {
	                            bsonType: 'int'
	                          },
	                          name: {
	                            bsonType: 'string'
	                          }
	                        }
	                      }
	                    }
	                  }
	                }
	              }
	            }
	          }
	        },
	        metadata: {
	          bsonType: 'object',
	          title: 'metadata',
	          required: ['lock_version', 'created_at', 'updated_at'],
	          properties: {
	            lock_version: {
	              bsonType: 'int'
	            },
	            created_at: {
	              bsonType: 'date'
	            },
	            updated_at: {
	              bsonType: 'date'
	            }
	          }
	        }
	      }
	    }
	  }
	});
	db.gics_sector.createIndex({
	  "id": 1
	}, {
	  name: "GICSSector_ix_unique_id",
	  unique: true
	})

	db.gics_sector.createIndex({
	  "name": 1
	}, {
	  name: "GICSSector_ix_unique_name",
	  unique: true
	})

	db.gics_sector.createIndex({
	  "id": 1,
	  "name": 1,
	  "industry_group": 1
	}, {
	  name: "GICSSector_ix_search_by_id"
	})

	db.gics_sector.createIndex({
	  "name": 1,
	  "id": 1,
	  "industry_group": 1
	}, {
	  name: "GICSSector_ix_search_by_name"
	});
}

function create_company(db) {
	// This function creates the company collection
	
	db.createCollection('company', {
	  validator: {
	    $jsonSchema: {
	      bsonType: 'object',
	      title: 'company',
	      required: ['ticker', 'name', 'description', 'cik', 'figi', 'exchange', 'currency', 'country', 'sub_industry', 'indexes', 'metadata'],
	      properties: {
	        ticker: {
	          bsonType: 'string'
	        },
	        name: {
	          bsonType: 'string'
	        },
	        description: {
	          bsonType: 'string'
	        },
	        cik: {
	          bsonType: 'string'
	        },
	        figi: {
	          bsonType: 'string'
	        },
	        exchange: {
	          bsonType: 'string'
	        },
	        currency: {
	          bsonType: 'string'
	        },
	        country: {
	          bsonType: 'string'
	        },
	        sub_industry: {
	          bsonType: 'string'
	        },
	        indexes: {
	          bsonType: 'array',
	          items: {
	            bsonType: 'string'
	          }
	        },
	        metadata: {
	          bsonType: 'object',
	          title: 'metadata',
	          required: ['lock_version', 'created_at', 'updated_at'],
	          properties: {
	            lock_version: {
	              bsonType: 'int'
	            },
	            created_at: {
	              bsonType: 'date'
	            },
	            updated_at: {
	              bsonType: 'date'
	            }
	          }
	        }
	      }
	    }
	  }
	});
	db.company.createIndex({
	  "ticker": 1
	}, {
	  name: "company_ix_unique_ticker",
	  unique: true
	})

	db.company.createIndex({
	  "ticker": 1,
	  "name": 1,
	  "description": 1,
	  "cik": 1,
	  "figi": 1,
	  "sub_industry": 1,
	  "exchange": 1,
	  "currency": 1,
	  "country": 1
	}, {
	  name: "company_ix_search_by_ticker"
	})

	db.company.createIndex({
	  "name": 1,
	  "ticker": 1,
	  "description": 1,
	  "cik": 1,
	  "figi": 1,
	  "exchange": 1,
	  "currency": 1,
	  "country": 1,
	  "sub_industry": 1
	}, {
	  name: "company_ix_search_by_name"
	});
}

function create_financial_statements(db) {
	// This function creates the financial_statements collection
	
	db.createCollection('financial_statements', {
	  validator: {
	    $jsonSchema: {
	      bsonType: 'object',
	      title: 'financial_statements',
	      required: ['income_statement_annual', 'income_statement_quarter', 'cash_flow_statement_annual', 'cash_flow_statement_quarter', 'balance_sheet_statement_annual', 'balance_sheet_statement_quarter', 'earnings_statement_annual', 'earnings_statement_quarter', 'metadata'],
	      properties: {
	        ticker: {
	          bsonType: 'string'
	        },
	        name: {
	          bsonType: 'string'
	        },
	        income_statement_annual: {
	          bsonType: 'object',
	          title: 'statement',
	          properties: {
	            items: {
	              bsonType: 'array',
	              items: {
	                title: 'accounts_entry',
	                required: ['tag', 'value_1', 'value_2', 'value_3', 'value_4', 'value_5'],
	                properties: {
	                  tag: {
	                    bsonType: 'string'
	                  },
	                  value_1: {
	                    bsonType: 'string'
	                  },
	                  value_2: {
	                    bsonType: 'string'
	                  },
	                  value_3: {
	                    bsonType: 'string'
	                  },
	                  value_4: {
	                    bsonType: 'string'
	                  },
	                  value_5: {
	                    bsonType: 'string'
	                  }
	                }
	              }
	            }
	          }
	        },
	        income_statement_quarter: {
	          bsonType: 'object',
	          title: 'statement',
	          properties: {
	            items: {
	              bsonType: 'array',
	              items: {
	                title: 'accounts_entry',
	                required: ['tag', 'value_1', 'value_2', 'value_3', 'value_4', 'value_5'],
	                properties: {
	                  tag: {
	                    bsonType: 'string'
	                  },
	                  value_1: {
	                    bsonType: 'string'
	                  },
	                  value_2: {
	                    bsonType: 'string'
	                  },
	                  value_3: {
	                    bsonType: 'string'
	                  },
	                  value_4: {
	                    bsonType: 'string'
	                  },
	                  value_5: {
	                    bsonType: 'string'
	                  }
	                }
	              }
	            }
	          }
	        },
	        cash_flow_statement_annual: {
	          bsonType: 'object',
	          title: 'statement',
	          properties: {
	            items: {
	              bsonType: 'array',
	              items: {
	                title: 'accounts_entry',
	                required: ['tag', 'value_1', 'value_2', 'value_3', 'value_4', 'value_5'],
	                properties: {
	                  tag: {
	                    bsonType: 'string'
	                  },
	                  value_1: {
	                    bsonType: 'string'
	                  },
	                  value_2: {
	                    bsonType: 'string'
	                  },
	                  value_3: {
	                    bsonType: 'string'
	                  },
	                  value_4: {
	                    bsonType: 'string'
	                  },
	                  value_5: {
	                    bsonType: 'string'
	                  }
	                }
	              }
	            }
	          }
	        },
	        cash_flow_statement_quarter: {
	          bsonType: 'object',
	          title: 'statement',
	          properties: {
	            items: {
	              bsonType: 'array',
	              items: {
	                title: 'accounts_entry',
	                required: ['tag', 'value_1', 'value_2', 'value_3', 'value_4', 'value_5'],
	                properties: {
	                  tag: {
	                    bsonType: 'string'
	                  },
	                  value_1: {
	                    bsonType: 'string'
	                  },
	                  value_2: {
	                    bsonType: 'string'
	                  },
	                  value_3: {
	                    bsonType: 'string'
	                  },
	                  value_4: {
	                    bsonType: 'string'
	                  },
	                  value_5: {
	                    bsonType: 'string'
	                  }
	                }
	              }
	            }
	          }
	        },
	        balance_sheet_statement_annual: {
	          bsonType: 'object',
	          title: 'statement',
	          properties: {
	            items: {
	              bsonType: 'array',
	              items: {
	                title: 'accounts_entry',
	                required: ['tag', 'value_1', 'value_2', 'value_3', 'value_4', 'value_5'],
	                properties: {
	                  tag: {
	                    bsonType: 'string'
	                  },
	                  value_1: {
	                    bsonType: 'string'
	                  },
	                  value_2: {
	                    bsonType: 'string'
	                  },
	                  value_3: {
	                    bsonType: 'string'
	                  },
	                  value_4: {
	                    bsonType: 'string'
	                  },
	                  value_5: {
	                    bsonType: 'string'
	                  }
	                }
	              }
	            }
	          }
	        },
	        balance_sheet_statement_quarter: {
	          bsonType: 'string'
	        },
	        earnings_statement_annual: {
	          bsonType: 'object',
	          title: 'statement',
	          properties: {
	            items: {
	              bsonType: 'array',
	              items: {
	                title: 'accounts_entry',
	                required: ['tag', 'value_1', 'value_2', 'value_3', 'value_4', 'value_5'],
	                properties: {
	                  tag: {
	                    bsonType: 'string'
	                  },
	                  value_1: {
	                    bsonType: 'string'
	                  },
	                  value_2: {
	                    bsonType: 'string'
	                  },
	                  value_3: {
	                    bsonType: 'string'
	                  },
	                  value_4: {
	                    bsonType: 'string'
	                  },
	                  value_5: {
	                    bsonType: 'string'
	                  }
	                }
	              }
	            }
	          }
	        },
	        earnings_statement_quarter: {
	          bsonType: 'object',
	          title: 'statement',
	          properties: {
	            items: {
	              bsonType: 'array',
	              items: {
	                title: 'accounts_entry',
	                required: ['tag', 'value_1', 'value_2', 'value_3', 'value_4', 'value_5'],
	                properties: {
	                  tag: {
	                    bsonType: 'string'
	                  },
	                  value_1: {
	                    bsonType: 'string'
	                  },
	                  value_2: {
	                    bsonType: 'string'
	                  },
	                  value_3: {
	                    bsonType: 'string'
	                  },
	                  value_4: {
	                    bsonType: 'string'
	                  },
	                  value_5: {
	                    bsonType: 'string'
	                  }
	                }
	              }
	            }
	          }
	        },
	        metadata: {
	          bsonType: 'object',
	          title: 'metadata',
	          required: ['lock_version', 'created_at', 'updated_at'],
	          properties: {
	            lock_version: {
	              bsonType: 'int'
	            },
	            created_at: {
	              bsonType: 'date'
	            },
	            updated_at: {
	              bsonType: 'date'
	            }
	          }
	        }
	      }
	    }
	  }
	});
	db.financial_statements.createIndex({
	  "ticker": 1
	}, {
	  name: "financial_statements_ix_unique_ticker",
	  unique: true
	})

	db.financial_statements.createIndex({
	  "ticker": 1,
	  "name": 1,
	  "income_statement": 1,
	  "cash_flow_statement": 1,
	  "balance_sheet_statement": 1,
	  "earnings_statement": 1
	}, {
	  name: "financial_statements_ix_search_by_ticker"
	});
}

function create_csapi_log(db) {
	// This function creates the csapi_log collection
	
	db.createCollection('csapi_log', {
	  validator: {
	    $jsonSchema: {
	      bsonType: 'object',
	      title: 'csapi_log',
	      required: ['logged_at', 'level'],
	      properties: {
	        logged_at: {
	          bsonType: 'date'
	        },
	        level: {
	          bsonType: 'string'
	        },
	        function: {
	          bsonType: 'string'
	        },
	        file: {
	          bsonType: 'string'
	        },
	        line: {
	          bsonType: 'int'
	        },
	        message: {
	          bsonType: 'string'
	        }
	      }
	    }
	  }
	});
	db.csapi_log.createIndex({
	  "logged_at": -1,
	  "level": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "csapi_log_ix_search_by_date"
	})

	db.csapi_log.createIndex({
	  "level": 1,
	  "logged_at": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "csapi_log_ix_search_by_level"
	});
}

function create_csapi_activity_log(db) {
	// This function creates the csapi_activity collection
	
	db.createCollection('csapi_activity_log', {
	  validator: {
	    $jsonSchema: {
	      bsonType: 'object',
	      title: 'csapi_activity_log',
	      required: ['logged_at', 'level'],
	      properties: {
	        logged_at: {
	          bsonType: 'date'
	        },
	        level: {
	          bsonType: 'string'
	        },
	        function: {
	          bsonType: 'string'
	        },
	        file: {
	          bsonType: 'string'
	        },
	        line: {
	          bsonType: 'int'
	        },
	        message: {
	          bsonType: 'string'
	        }
	      }
	    }
	  }
	});
	db.csapi_activity_log.createIndex({
	  "logged_at": -1,
	  "level": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "csapi_activity_log_ix_search_by_date"
	})

	db.csapi_activity_log.createIndex({
	  "level": 1,
	  "logged_at": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "csapi_activity_log_ix_search_by_level"
	});
}

function create_cswebapp_log(db) {
	// This function creates the cswebapp_log collection
	
	db.createCollection('cswebapp_log', {
	  validator: {
	    $jsonSchema: {
	      bsonType: 'object',
	      title: 'cswebapp_log',
	      required: ['logged_at', 'level'],
	      properties: {
	        logged_at: {
	          bsonType: 'date'
	        },
	        level: {
	          bsonType: 'string'
	        },
	        function: {
	          bsonType: 'string'
	        },
	        file: {
	          bsonType: 'string'
	        },
	        line: {
	          bsonType: 'int'
	        },
	        message: {
	          bsonType: 'string'
	        }
	      }
	    }
	  }
	});
	db.cswebapp_log.createIndex({
	  "logged_at": -1,
	  "level": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "cswebapp_log_ix_search_by_date"
	})

	db.cswebapp_log.createIndex({
	  "level": 1,
	  "logged_at": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "cswebapp_log_ix_search_by_level"
	});
}

function create_cswebapp_activity_log(db) {
	// This function creates the cswebapp_activity_log collection
	
	db.createCollection('cswebapp_activity_log', {
	  validator: {
	    $jsonSchema: {
	      bsonType: 'object',
	      title: 'cswebapp_activity_log',
	      required: ['logged_at', 'level'],
	      properties: {
	        logged_at: {
	          bsonType: 'date'
	        },
	        level: {
	          bsonType: 'string'
	        },
	        function: {
	          bsonType: 'string'
	        },
	        file: {
	          bsonType: 'string'
	        },
	        line: {
	          bsonType: 'int'
	        },
	        message: {
	          bsonType: 'string'
	        }
	      }
	    }
	  }
	});
	db.cswebapp_activity_log.createIndex({
	  "logged_at": -1,
	  "level": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "cswebapp_activity_log_ix_search_by_date"
	})

	db.cswebapp_activity_log.createIndex({
	  "level": 1,
	  "logged_at": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "cswebapp_activity_log_ix_search_by_level"
	});
}

function create_csqueue_log(db) {
	// This function creates the csqueue_log collection
	
	db.createCollection('csqueue_log', {
	  validator: {
	    $jsonSchema: {
	      bsonType: 'object',
	      title: 'csqueue_log',
	      required: ['logged_at', 'level'],
	      properties: {
	        logged_at: {
	          bsonType: 'date'
	        },
	        level: {
	          bsonType: 'string'
	        },
	        function: {
	          bsonType: 'string'
	        },
	        file: {
	          bsonType: 'string'
	        },
	        line: {
	          bsonType: 'int'
	        },
	        message: {
	          bsonType: 'string'
	        }
	      }
	    }
	  }
	});
	db.csqueue_log.createIndex({
	  "logged_at": -1,
	  "level": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "csqueue_log_ix_search_by_date"
	})

	db.csqueue_log.createIndex({
	  "level": 1,
	  "logged_at": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "csqueue_log_ix_search_by_level"
	});
}

function create_csqueue_activity_log(db) {
	// This function creates the csqueue_activity_log collection
	
	db.createCollection('csqueue_activity_log', {
	  validator: {
	    $jsonSchema: {
	      bsonType: 'object',
	      title: 'csqueue_activity_log',
	      required: ['logged_at', 'level'],
	      properties: {
	        logged_at: {
	          bsonType: 'date'
	        },
	        level: {
	          bsonType: 'string'
	        },
	        function: {
	          bsonType: 'string'
	        },
	        file: {
	          bsonType: 'string'
	        },
	        line: {
	          bsonType: 'int'
	        },
	        message: {
	          bsonType: 'string'
	        }
	      }
	    }
	  }
	});
	db.csqueue_activity_log.createIndex({
	  "logged_at": -1,
	  "level": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "csqueue_activity_log_ix_search_by_date"
	})

	db.csqueue_activity_log.createIndex({
	  "level": 1,
	  "logged_at": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "csqueue_activity_log_ix_search_by_level"
	});
}

function create_csloader_log(db) {
	// This function creates the csloader_log collection
	
	db.createCollection('csloader_log', {
	  validator: {
	    $jsonSchema: {
	      bsonType: 'object',
	      title: 'csloader_log',
	      required: ['logged_at', 'level'],
	      properties: {
	        logged_at: {
	          bsonType: 'date'
	        },
	        level: {
	          bsonType: 'string'
	        },
	        function: {
	          bsonType: 'string'
	        },
	        file: {
	          bsonType: 'string'
	        },
	        line: {
	          bsonType: 'int'
	        },
	        message: {
	          bsonType: 'string'
	        }
	      }
	    }
	  }
	});
	db.csloader_log.createIndex({
	  "logged_at": -1,
	  "level": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "csloader_log_ix_search_by_date"
	})

	db.csloader_log.createIndex({
	  "level": 1,
	  "logged_at": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "csloader_log_ix_search_by_level"
	});
}

function create_csloader_activity_log(db) {
	// This function creates the csloader_activity_log collection
	
	db.createCollection('csloader_activity_log', {
	  validator: {
	    $jsonSchema: {
	      bsonType: 'object',
	      title: 'csloader_activity_log',
	      required: ['logged_at', 'level'],
	      properties: {
	        logged_at: {
	          bsonType: 'date'
	        },
	        level: {
	          bsonType: 'string'
	        },
	        function: {
	          bsonType: 'string'
	        },
	        file: {
	          bsonType: 'string'
	        },
	        line: {
	          bsonType: 'int'
	        },
	        message: {
	          bsonType: 'string'
	        }
	      }
	    }
	  }
	});
	db.csloader_activity_log.createIndex({
	  "logged_at": -1,
	  "level": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "csloader_activity_log_ix_search_by_date"
	})

	db.csloader_activity_log.createIndex({
	  "level": 1,
	  "logged_at": 1,
	  "function": 1,
	  "file": 1,
	  "line": 1,
	  "message": 1
	}, {
	  name: "csloader_activity_log_ix_search_by_level"
	});
}

function drop_database(name) {	
	// This function drops the named database
	
    db = db.getSiblingDB(name);
    db.dropDatabase();
}

function create_database(name) {
	// This function orcistrates the creation of the database with the given name
	
	drop_database(name);
	
    db = db.getSiblingDB(name);
	
	create_config(db);
	
	create_master(db);
	create_gics_sector(db);
	
	create_company(db);
	create_financial_statements(db);
	
	create_csapi_log(db);
	create_csapi_activity_log(db);
	
	create_cswebapp_log(db);
	create_cswebapp_activity_log(db);
	
	create_csqueue_log(db);
	create_csqueue_activity_log(db);
	
	create_csloader_log(db);
	create_csloader_activity_log(db);
}
