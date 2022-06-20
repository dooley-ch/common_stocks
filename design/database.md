# Database Design

## Introduction

The application's data is stored in an instance of MongoDB.  The database contains a set of documents covering the 
following areas:
- Configuration
- Application 
- Logging

## Metadata

Each document in the database has a sub-document containing the following information about the document:

```mermaid
classDiagram
    class Metadata{
        <<Document>>
        +int lock_version
        +date created_at
        +data updated_at
    }
```

| Field        | Description                                 |
|--------------|---------------------------------------------|
| lock_version | concurrency flag                            | 
| created_at   | Date and time the document was created      |
| updated_at   | Date and time the document was last updated |

## Configuration

All the configuration data is stored in a singel document collection.  Each document consists of a name or key used to 
indicate the configuration information stored in the document plus an array of key/value pairs containing the 
configuration information.

```mermaid
classDiagram
    Config --* ConfigItem
    Config --* Metadata
    
    class ConfigItem {
        <<Document>>
        +string key
        +string value
    }
    
    class Metadata{
        <<Document>>
        +int lock_version
        +date created_at
        +data updated_at
    }
    
    class Config {
        <<Container>>
        +string name
        +list[ConfigItem] items
        +Metadata metadata
    }
```

## Application

This section covers the main collections in the database - the core collections used to provide the application's 
functionality.

### GICS Sector

The Global Industry Classification Standard is an industry taxonomy developed in 1999 by MSCI and Standard & Poor's 
for use by the global financial community. The GICS structure consists of 11 sectors, 24 industry groups, 69 industries 
and 158 sub-industries into which S&P has categorized all major public companies

```mermaid
classDiagram
    GICSSector --* GICSIndustryGroup   
    GICSIndustryGroup --* GICSIndustry  
    GICSIndustry --* GICSSubIndustry
    GICSSector --* Metadata
    
    class Metadata {
        <<Document>>
        +int lock_version
        +date created_at
        +data updated_at
    }
    
    class GICSSubIndustry {
        <<Document>>
        +int id
        +string name
    }
    
    class GICSIndustry {
        <<Document>>
        +int id
        +string name
        +list[GICSSubIndustry] sub_industry
    }

    class GICSIndustryGroup {
        <<Document>>
        +int id
        +string name
        +list[GICSIndustry] industry
    }
 
    class GICSSector {
        <<Container>>
        +int id
        +string name
        +list[GICSIndustryGroup] industry_group
        +Metadata metadata
    }    
```

The GICS structure consits of four elements the lowest being a sub-industry and the highest being a sector.  The 
structure is stored in the database as collection of documents at the sector level.

### Master

The master collection is used to allow users search for the company they wish to work with.  The list is limited to the
components of the S&P 600, 400 and 500 indexes.  It provides basic information about each compay in the indexes.

```mermaid
classDiagram
    Master --* Metadata
    Master --* IndexType
    
    class Metadata {
        <<Document>>
        +int lock_version
        +date created_at
        +data updated_at
    }
    
    class IndexType {
        <<Enum>>
        +string SP100
        +string SP500
        +string SP400
        +string SP600
    }
    
    class Master {
        <<Container>>
        +string ticker
        +string name
        +string cik
        +string figi
        +string sub_industry
        +list[IndexType] indexes
        +Metadata metadata
    }
```

| Field        | Description                             |
|--------------|-----------------------------------------|
| ticker       | The stock market ticker for the company | 
| name         | The company name                        |
| cik          | The SEC code used for filing documents  |
| figi         | The Open FIGI code for the company      |
| sub_industry | The GICS classification for the company |

### Company

This collection contains detailed informaton about public company as provided by the Alphavantage data service:


```mermaid
classDiagram
    Company --* Metadata
    
    class Metadata {
        <<Document>>
        +int lock_version
        +date created_at
        +data updated_at
    }
    
    class Company {
        <<Container>>
        +string ticker
        +string name
        +string description
        +string cik
        +string figi
        +string exchange
        +string currency
        +string country 
        +string sub_industry
        +Metadata metadata
    }
```

| Field        | Description                                         |
|--------------|-----------------------------------------------------|
| ticker       | The stock market ticker for the company             | 
| name         | The company name                                    |
| description  | A description of the company's business activities  |
| cik          | The SEC code used for filing documents              |
| figi         | The Open FIGI code for the company                  |
| exchange     | The main stock exchange where the company is traded |
| currency     | The company's reporting currency                    |
| country      | The country where the company is head quartered     |
| sub_industry | The GICS classification for the company             |

### Financials

The financial data for each company, provided by Alphavantage, covers three statements: income, cash flow and 
balance sheet and also statement of earnings.  The information is available for both annual and quarterly reports.  Each 
accounting entry is represented by a tag such as Revenue and up to five period entries for the tag.  The financials are
stored in a single document, with sub documents for each financial statement

```mermaid
classDiagram
    FinancialStatements --* Statement
    FinancialStatements --* Metadata
    Statement --* AccountsEntry
    
    class Metadata {
        <<Document>>
        +int lock_version
        +date created_at
        +data updated_at
    }
    
    class AccountsEntry {
        <<Document>>
        +string ticker
        +string value_1
        +string value_2
        +string value_3
        +string value_4
        +string value_5
    }
    
    class Statement {
        <<Document>>
        +string ticker
        +string name
        +list[AccountsEntry] items
    }
    
    class FinancialStatements {
        <<Container>>
        +string ticker
        +string name
        +Statement income
        +Statement cash_flow
        +Statement balance_sheet
        +Statement earnings
        +Metadata metadata    
    }
```

## Logging

The logging data is stored in one of more collections per service, each table has the same structure:

```mermaid
classDiagram
    Log <|-- csAPILog
    Log <|-- csAPILogActivity

    Log <|-- csWebAppLog
    Log <|-- csWebAppLogActivity

    Log <|-- csLoaderLog
    Log <|-- csLoaderLogActivity

    Log <|-- csQueueLog
    Log <|-- csQueueLogActivity
    
    class Log {
        <<Document>>
        +date logged_at
        +string level
        +string function
        +string file
        +int line
        +string message
    }
    
    class csAPILog {
        <<Container>>
    }

    class csAPILogActivity {
        <<Container>>
    }
    
    class csWebAppLog {
        <<Container>>
    }

    class csWebAppLogActivity {
        <<Container>>
    }
    
    class csLoaderLog {
        <<Container>>
    }
    
    class csLoaderLogActivity {
        <<Container>>
    }
    
    class csQueueLog {
        <<Container>>
    }
    
    class csQueueLogActivity {
        <<Container>>
    }    
```

## Depoloyment

A javascript scripts are provided for creating the database.  The scripts are stored in the code/database folder.  The
following scripts are provided.

| File           | Comments                                      |
|----------------|-----------------------------------------------|
| create_db.js   | Contains routines used to create the database |
| create_all.js  | Creates all three databases: Prod, Test, Dev  |
| create_prod.js | Creates the production database               |
| create_test.js | Creates the test database                     |
| create_dev.js  | Creates the dev database                      |
