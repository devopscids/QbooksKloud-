# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': "Sales Contract and Recurring Invoice Customer Portal",
    'price': 99.0,
    'version': '6.1.1',
    'depends': ['contract_recurring_invoice_analytic', 'portal'],
    'currency': 'EUR',
    'license': 'Other proprietary',
    # 'live_test_url': 'https://youtu.be/B0jGAQPwT2Q',
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/subscription_contract_customer_portal/934',#'https://youtu.be/FR7gRxIeP6s',
    'summary': """This module provide your customer to access all contracts from Portal/My Account.""",
    'description': """
    Subscription Contract Customer Portal
    This module show customer contracts on website
    This module provide your customer to access all contracts from Portal/My Account.
    Contracts of Customer
    Customer Contracts
    List of Contracts
contract portal
customer portal contract
subscription portal
portal contract subscription
account portal
portal customer contract
Create recurring invoice from analytic account.
Menus:
- Sales/Sales/Products
- Sales/Configuration/Sales/Quotation Templates
- Sales/Sales/Quotations
- Invoicing/Configuration/Analytic Accounting/Analytic Accounts
- Invoicing/Sales/Customer Invoices
Sales Contract and Recurring Invoice
Recurring Invoice For Contract/Analytic Account
This module uses below menus:
- Sales/Sales/Products
- Sales/Configuration/Sales/Quotation Templates
- Sales/Sales/Quotations
- Invoicing/Configuration/Analytic Accounting/Analytic Accounts
- Invoicing/Sales/Customer Invoices
Recurring Invoice
Contract
contract report
Analytic Account
Quotation Template
Sales Contract and Recurring Invoice

This module used to maintain the contracts for the product sold by the company. 
It is also allowing you to create recurrinig invoice from contract based on period configured on contract
Configuration of Contract product
Odoo Sales Contract/ Recurring Invoice
Recurring Invoice
contract_recurring_invoice_analytic
Odoo Sales Contract
Recurring
Warranty
contract Warranty
maintenance Warranty
maintenance contract
maintenance analytic account
maintenance subscription
subscription
contract management
contract invoice
Recurring invoice
maintenance invoice
yearly contract
contract customer
customer contract
analytic account
subscription contract
subscription management
customer recurring invoice
community subscription
community version
Sales Contract and Recurring Invoice

This module allow you to create product for warranty/maintenance/subscription and based on that product on Sales order line it will create sales contract for that customer automatically on confirmation of sales order. It is also allowing you to create recurrinig invoice from contract based on period configured on contract. It also support in future if you sale some more service on same contract then you can select that contract on quote/sales order and it will append that line on contract.

This module create below menu(s):

- Sales/Sales/Contracts


Product Configuration

Create product as Contract/Warranty/Subscription product and set Recurring Period.
Quotation Template

Create your custom quotation template using contract/subscription product this will allow you to select on sale order and auto set contract/subscription line on sales order..
Case 1 - Sales Quote / Sale Order

Create Quote by selecting Quotation template and that will set contract/warranty line on sale order lines along with selling product lines.
We have to select recurring period on sales order which will be used during recurring invoice creation from contract.

Sale Order Confirmation

If you have not selected Analytic Account / Contract on Sales order then it will create new Contract / Analytic Account for that customer.
Module also support like if you have selected existing Contract/ Analytic Account then it will append Subscription/Contract line into existing contract. (For new subscription product it will append in contract but for existing subscription product it will increase qty in contract.)

Contract from Sale Order Confirmation

We have separated Contract/Subscription lines and Sellable Product lines.
You can find new fields on contract/analytic account as below which will allow you to manage customer contract and recurrning invoice.

- Recurring Period: Invoice creation period.
- Contract Expiration Days: Set contract stage set to "Expires Soon" before end date.
- Date Of Next Invoice: Next invoice will create on this date.
- Order/Invoice Currency: Invoice will create in this currency and this currency is fetch from Sale Order
- Stage: Contract Status (New->Running->Expires Soon->Expired->Locked)
Selling Product On Contract

Using selling product you can have idea for this contract which product originally sold with qty sold and pricing details. And it can be used in future.

Recurring Invoice from Contract

Create Recurring Invoice from Contract using Generate Invoice button on contract form. And Invoice will be created with only contract/warranty/subscription product lines in contract currency.

Case 2 - Existing Contract On Sale Order

If we have selected contract on Sale Order then it will merge/append contract/subcription product lines to contract subscription lines.

Updated Contract/Subcription Lines on Contract

If we have same warranty/contract/subcription line on selected contract then it will increase product quantity otherwise it will create new contract/subscription lines.

Contract Report

Customized report of contract with full details and you can send to you customer. :)

    """,
    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': "http://www.probuse.com",
    'support': 'contact@probuse.com',
    'images': ['static/description/img1.jpeg'],
    'category': 'Website',
    'data':[
        'views/contract_message_template.xml',
        'views/contract_template.xml',
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
