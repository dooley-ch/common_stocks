# Data Services

## Introduction

The application takes its data from four sources:

**Alphavantage:** This site provides the core data for the application, including:

- Company Description
- Earnings estimates
- Financial statements: income statement, cash flow, balance sheet and earning statement

**Wikipedia:** The application limits its company data servie offering to the conponents of the S&P 600, 400 and 500 
indexes.  The application scrapes the list of comonents for each index from the corrsponding wikipedia page. 

**EDGAR/SEC:** The application uses the EDGAR website do obtain the CIK code for the company covered by the application.

A Central Index Key or CIK number is a number given to an individual, company, or foreign government by the 
United States Securities and Exchange Commission. The number is used to identify its filings in several online 
databases, including EDGAR. The numbers are up to ten digits in length.

**OpenFIGI:** The application uses the OpenFIGI website to obtain the FIGI code for the company covered by the 
application.

## Alphavantage

As mentioned above the Alphavantage provides the core data for the application.  To access this data, you will need an
API key which can be obtained on the website at this address [API Key](https://www.alphavantage.co/support/#api-key).

The key has to constaints:

- Limited to 5 calls per minute
- Limited to 500 calls per data

Commercial keys are also available, see the website for details.

### Earnings Calendar

This API returns a list of company earnings expected in the next 3, 6, or 12 months.

```mermaid
erDiagram    
    EarningCalendar {
        string symbol PK
        string name
        date reportDate
        date fiscalDateEnding
        int estimate
        string currency
    }
```

### Company Description

This API returns the company information, financial ratios, and other key metrics for the equity specified. 
Data is generally refreshed on the same day a company reports its latest earnings and financials.  We use a sub set of 
this data in the application.

```mermaid
erDiagram
    CompanyOverview {
        string Symbol PK
        string Name
        string Description
        string CIK
        string Exchange
        string Currency
        string Country
        string Sector
        string Industry
        string Address
        string FiscalYearEnd
        string LatestQuarter
    }
```

### Income Statement

This API returns the annual and quarterly income statements for the company of interest, with normalized fields mapped 
to GAAP and IFRS taxonomies of the SEC. Data is generally refreshed on the same day a company reports its latest 
earnings and financials.

```mermaid
erDiagram
    AnnualIncomeStatement {
        string fiscalDateEnding
        string reportedCurrency
        string grossProfit
        string totalRevenue
        string costOfRevenue
        string costofGoodsAndServicesSold
        string operatingIncome
        string sellingGeneralAndAdministrative
        string researchAndDevelopment
        string operatingExpenses
        string investmentIncomeNet
        string netInterestIncome
        string interestIncome
        string interestExpense
        string nonInterestIncome
        string otherNonOperatingIncomestring 
        string depreciation
        string depreciationAndAmortization
        string incomeBeforeTax
        string incomeTaxExpense
        string interestAndDebtExpense
        string netIncomeFromContinuingOperations
        string comprehensiveIncomeNetOfTax
        string ebit
        string ebitda
        string netIncome
    }
   
    QuarterIncomeStatement {
        string fiscalDateEnding
        string reportedCurrency
        string grossProfit
        string totalRevenue
        string costOfRevenue
        string costofGoodsAndServicesSold
        string operatingIncome
        string sellingGeneralAndAdministrative
        string researchAndDevelopment
        string operatingExpenses
        string investmentIncomeNet
        string netInterestIncome
        string interestIncome
        string interestExpense
        string nonInterestIncome
        string otherNonOperatingIncomestring 
        string depreciation
        string depreciationAndAmortization
        string incomeBeforeTax
        string incomeTaxExpense
        string interestAndDebtExpense
        string netIncomeFromContinuingOperations
        string comprehensiveIncomeNetOfTax
        string ebit
        string ebitda
        string netIncome
    }
    
```
### Cash Flow Statement

This API returns the annual and quarterly cash flow for the company of interest, with normalized fields mapped to GAAP 
and IFRS taxonomies of the SEC. Data is generally refreshed on the same day a company reports its latest earnings and 
financials.

```mermaid
erDiagram
    AnnualCashFlowStatement {
        string fiscalDateEnding
        string reportedCurrency
        string operatingCashflow
        string paymentsForOperatingActivities
        string proceedsFromOperatingActivities
        string changeInOperatingLiabilities
        string changeInOperatingAssets
        string depreciationDepletionAndAmortization
        string capitalExpenditures
        string changeInReceivables
        string changeInInventory
        string profitLoss
        string cashflowFromInvestment
        string cashflowFromFinancing
        string proceedsFromRepaymentsOfShortTermDebt
        string paymentsForRepurchaseOfCommonStock
        string paymentsForRepurchaseOfEquity
        string paymentsForRepurchaseOfPreferredStock
        string dividendPayout
        string dividendPayoutCommonStock
        string dividendPayoutPreferredStock
        string proceedsFromIssuanceOfCommonStock
        string proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet
        string proceedsFromIssuanceOfPreferredStock
        string proceedsFromRepurchaseOfEquity
        string proceedsFromSaleOfTreasuryStock
        string changeInCashAndCashEquivalents
        string changeInExchangeRate
        string netIncome
    }
    
    QuarterCashFlowStatement {
        string fiscalDateEnding
        string reportedCurrency
        string operatingCashflow
        string paymentsForOperatingActivities
        string proceedsFromOperatingActivities
        string changeInOperatingLiabilities
        string changeInOperatingAssets
        string depreciationDepletionAndAmortization
        string capitalExpenditures
        string changeInReceivables
        string changeInInventory
        string profitLoss
        string cashflowFromInvestment
        string cashflowFromFinancing
        string proceedsFromRepaymentsOfShortTermDebt
        string paymentsForRepurchaseOfCommonStock
        string paymentsForRepurchaseOfEquity
        string paymentsForRepurchaseOfPreferredStock
        string dividendPayout
        string dividendPayoutCommonStock
        string dividendPayoutPreferredStock
        string proceedsFromIssuanceOfCommonStock
        string proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet
        string proceedsFromIssuanceOfPreferredStock
        string proceedsFromRepurchaseOfEquity
        string proceedsFromSaleOfTreasuryStock
        string changeInCashAndCashEquivalents
        string changeInExchangeRate
        string netIncome
    }
```

### Balance Sheet

This API returns the annual and quarterly balance sheets for the company of interest, with normalized fields mapped 
to GAAP and IFRS taxonomies of the SEC. Data is generally refreshed on the same day a company reports its latest 
earnings and financials.

```mermaid
erDiagram
    AnnualBalanceSheetStatement {
        string fiscalDateEnding
        string reportedCurrency
        string totalAssets
        string totalCurrentAssets
        string cashAndCashEquivalentsAtCarryingValue
        string cashAndShortTermInvestments
        string inventory
        string currentNetReceivables
        string totalNonCurrentAssets
        string propertyPlantEquipment
        string accumulatedDepreciationAmortizationPPE
        string intangibleAssets
        string intangibleAssetsExcludingGoodwill
        string goodwill
        string investments
        string longTermInvestments
        string shortTermInvestments
        string otherCurrentAssets
        string otherNonCurrrentAssets
        string totalLiabilities
        string totalCurrentLiabilities
        string currentAccountsPayable
        string deferredRevenue
        string currentDebt
        string shortTermDebt
        string totalNonCurrentLiabilities
        string capitalLeaseObligations
        string longTermDebtstring 
        string currentLongTermDebt
        string longTermDebtNoncurrent
        string shortLongTermDebtTotal
        string otherCurrentLiabilities
        string otherNonCurrentLiabilities
        string totalShareholderEquity
        string treasuryStock
        string retainedEarnings
        string commonStock
        string commonStockSharesOutstanding
    }
    
    QuarterBalanceSheetStatement {
        string fiscalDateEnding
        string reportedCurrency
        string totalAssets
        string totalCurrentAssets
        string cashAndCashEquivalentsAtCarryingValue
        string cashAndShortTermInvestments
        string inventory
        string currentNetReceivables
        string totalNonCurrentAssets
        string propertyPlantEquipment
        string accumulatedDepreciationAmortizationPPE
        string intangibleAssets
        string intangibleAssetsExcludingGoodwill
        string goodwill
        string investments
        string longTermInvestments
        string shortTermInvestments
        string otherCurrentAssets
        string otherNonCurrrentAssets
        string totalLiabilities
        string totalCurrentLiabilities
        string currentAccountsPayable
        string deferredRevenue
        string currentDebt
        string shortTermDebt
        string totalNonCurrentLiabilities
        string capitalLeaseObligations
        string longTermDebtstring 
        string currentLongTermDebt
        string longTermDebtNoncurrent
        string shortLongTermDebtTotal
        string otherCurrentLiabilities
        string otherNonCurrentLiabilities
        string totalShareholderEquity
        string treasuryStock
        string retainedEarnings
        string commonStock
        string commonStockSharesOutstanding
    }
```

### Earnings

This API returns the annual and quarterly earnings (EPS) for the company of interest. Quarterly data also includes 
analyst estimates and surprise metrics.

```mermaid
erDiagram
    AnnualEarnings {
        string fiscalDateEnding
        string reportedEPS
    }
    
    QuarterEarnings {
        string fiscalDateEnding
        string reportedDate
        string reportedEPS
        string estimatedEPS
        string surprise
        string surprisePercentage
    }
```

### Implementation

```mermaid
classDiagram
    AlphavantageService ..> EarningsCalendar
    AlphavantageService ..> CompanyOverview
    AlphavantageService ..> FinancialStatements
    
    FinancialStatements ..> Statement
    Statement ..> AccountingItem
    
    class AlphavantageService {
        -str api_key
        +__init__(api_key)
        +get_earnings_calendar() list~EarningsCalendar~
        +get_company(ticker) CompanyOverview
        +get_financial_statements(ticker) AccountingStatements
    }
    
    class EarningsCalendar {
        +str ticker
        +str name
        +date report_date
        +date fiscal_date_ending
        int estimate
        +str currency
    }
    
    class CompanyOverview {
        +str ticker
        +str  name
        +str  description
        +str  cik
        +str  exchange
        +str  currency
        +str  country
        +str  sector
        +str  industry
        +str  address
        +date fiscal_year_end
        +date latest_quarter
    }
    
    class AccountingItem {
        +str tag
        +str value_1
        +str value_2
        +str value_3
        +str value_4
        +str value_5
    }
    
    class Statement {
        +List~AccountingItem~ annual_items
        +List~AccountingItem~ quarter_items
    }
    
    class FinancialStatements {
        +str ticker
        +str  name
        +Statement income
        +Statement cash_flow
        +Statement balance_sheet
        +Statement earnings     
    }
    
```

## Wikipedia

The application provides a data service for the components of the S&P 600, 400 and 500 indexes.  In additional it flags 
the components of the S&P 100, so a small data set can be used in the test and development environments.

The application uses the following urls to download the data:

| Index   | URL                                                                                                                    |
|---------|------------------------------------------------------------------------------------------------------------------------|
| S&P 100 | [https://en.wikipedia.org/wiki/S%26P_100](https://en.wikipedia.org/wiki/S%26P_100)                                     |
| S&P 600 | [https://en.wikipedia.org/wiki/List_of_S%26P_600_companies](https://en.wikipedia.org/wiki/List_of_S%26P_600_companies) |
| S&P 400 | [https://en.wikipedia.org/wiki/List_of_S%26P_400_companies](https://en.wikipedia.org/wiki/List_of_S%26P_400_companies) |
| S&P 500 | [https://en.wikipedia.org/wiki/List_of_S%26P_500_companies](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies) |

```mermaid
erDiagram
    SPRecord {
        string ticker
        string name
        string sector
        string sub_industry
    }
```

### Implementation

```mermaid
classDiagram
    WikiService ..> SPComponent
    
    class SPComponent {
        +str ticker
        +str name
        +str sector
        +str sub_industry
    }
    
    class WikiService {
        +get_sp100() list~SPComponent~
        +get_sp600() list~SPComponent~
        +get_sp400() list~SPComponent~
        +get_sp500() list~SPComponent~
    }
```

## EDGAR/SEC

The application uses the EDGAR site to look up a company's CIK code.  The information is downloaded as a single JSON 
file from the following url: [EDGAR Files](https://www.sec.gov/files/company_tickers_exchange.json).

The records have the following format:

```mermaid
erDiagram
    CIKRecord {
        string cik
        string name
        string ticker
        string exchange
    }
```

### Implementation

```mermaid
classDiagram
    EdgarService ..> CIKCode
    
    class CIKCode {
        +str cik
        +str name
        +str ticker
        +str exchange
    }
    
    class EdgarService {
        +get_codes() list~CIKCode~
    }
```

## OpenFIGI

The Financial Instrument Global Identifier (FIGI) (formerly Bloomberg Global Identifier (BBGID)) is an open standard, 
unique identifier of financial instruments that can be assigned to instrument including common stock, options, 
derivatives, futures, corporate and government bonds, municipals, currencies, and mortgage products.

The application uses the OpenFIGI website to obtain the FIGI code for the company  covered by the 
application.

```mermaid
erDiagram
    FIGIRecord {
        string ticker
        string figi
    }
```

### Implementation

```mermaid
classDiagram
    OpenFigiService ..> FigiCode
    
    class FigiCode {
        +str ticker
        +str figi
    }
    
    class OpenFigiService {
        -str api_key
        +__init__(api_key)
        +get_codes(tickers list~str~) list~FigiCode~
    }
```
