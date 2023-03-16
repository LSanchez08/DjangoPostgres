# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountAccount(models.Model):
    name = models.CharField(max_length=-1)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=64)
    deprecated = models.BooleanField(blank=True, null=True)
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING)
    internal_type = models.CharField(max_length=-1, blank=True, null=True)
    internal_group = models.CharField(max_length=-1, blank=True, null=True)
    reconcile = models.BooleanField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    group = models.ForeignKey('AccountGroup', models.DO_NOTHING, blank=True, null=True)
    root_id = models.IntegerField(blank=True, null=True)
    is_off_balance = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account'
        unique_together = (('code', 'company'),)


class AccountAccountAccountJournalRel(models.Model):
    account_account = models.OneToOneField(AccountAccount, models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_account_journal_rel'
        unique_together = (('account_account', 'account_journal'),)


class AccountAccountAccountTag(models.Model):
    account_account = models.OneToOneField(AccountAccount, models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey('AccountAccountTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_account_tag'
        unique_together = (('account_account', 'account_account_tag'),)


class AccountAccountTag(models.Model):
    name = models.CharField(max_length=-1)
    applicability = models.CharField(max_length=-1)
    color = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    tax_negate = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    nature = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_tag'


class AccountAccountTagAccountMoveLineRel(models.Model):
    account_move_line = models.OneToOneField('AccountMoveLine', models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tag_account_move_line_rel'
        unique_together = (('account_move_line', 'account_account_tag'),)


class AccountAccountTagAccountTaxRepartitionLineRel(models.Model):
    account_tax_repartition_line = models.OneToOneField('AccountTaxRepartitionLine', models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tag_account_tax_repartition_line_rel'
        unique_together = (('account_tax_repartition_line', 'account_account_tag'),)


class AccountAccountTaxDefaultRel(models.Model):
    account = models.OneToOneField(AccountAccount, models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tax_default_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountTemplate(models.Model):
    name = models.CharField(max_length=-1)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=64)
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING)
    reconcile = models.BooleanField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    nocreate = models.BooleanField(blank=True, null=True)
    chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_template'


class AccountAccountTemplateAccountTag(models.Model):
    account_account_template = models.OneToOneField(AccountAccountTemplate, models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_template_account_tag'
        unique_together = (('account_account_template', 'account_account_tag'),)


class AccountAccountTemplateTaxRel(models.Model):
    account = models.OneToOneField(AccountAccountTemplate, models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_template_tax_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountType(models.Model):
    name = models.CharField(max_length=-1)
    include_initial_balance = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    internal_group = models.CharField(max_length=-1)
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_type'


class AccountAnalyticAccount(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    group = models.ForeignKey('AccountAnalyticGroup', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_account'


class AccountAnalyticDefault(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_stop = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_default'


class AccountAnalyticDefaultAccountAnalyticTagRel(models.Model):
    account_analytic_default = models.OneToOneField(AccountAnalyticDefault, models.DO_NOTHING, primary_key=True)
    account_analytic_tag = models.ForeignKey('AccountAnalyticTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_default_account_analytic_tag_rel'
        unique_together = (('account_analytic_default', 'account_analytic_tag'),)


class AccountAnalyticDistribution(models.Model):
    account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)
    percentage = models.FloatField()
    tag = models.ForeignKey('AccountAnalyticTag', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_distribution'


class AccountAnalyticGroup(models.Model):
    name = models.CharField(max_length=-1)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    complete_name = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_group'


class AccountAnalyticLine(models.Model):
    name = models.CharField(max_length=-1)
    date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    unit_amount = models.FloatField(blank=True, null=True)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(AccountAnalyticGroup, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    general_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey('AccountMoveLine', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    so_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, db_column='so_line', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_line'


class AccountAnalyticLineTagRel(models.Model):
    line = models.OneToOneField(AccountAnalyticLine, models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey('AccountAnalyticTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_line_tag_rel'
        unique_together = (('line', 'tag'),)


class AccountAnalyticTag(models.Model):
    name = models.CharField(max_length=-1)
    color = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    active_analytic_distribution = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag'


class AccountAnalyticTagAccountMoveLineRel(models.Model):
    account_move_line = models.OneToOneField('AccountMoveLine', models.DO_NOTHING, primary_key=True)
    account_analytic_tag = models.ForeignKey(AccountAnalyticTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag_account_move_line_rel'
        unique_together = (('account_move_line', 'account_analytic_tag'),)


class AccountAnalyticTagSaleOrderLineRel(models.Model):
    sale_order_line = models.OneToOneField('SaleOrderLine', models.DO_NOTHING, primary_key=True)
    account_analytic_tag = models.ForeignKey(AccountAnalyticTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag_sale_order_line_rel'
        unique_together = (('sale_order_line', 'account_analytic_tag'),)


class AccountAutomaticEntryWizard(models.Model):
    action = models.CharField(max_length=-1)
    date = models.DateField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    percentage = models.FloatField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    account_type = models.CharField(max_length=-1, blank=True, null=True)
    destination_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_automatic_entry_wizard'


class AccountAutomaticEntryWizardAccountMoveLineRel(models.Model):
    account_automatic_entry_wizard = models.OneToOneField(AccountAutomaticEntryWizard, models.DO_NOTHING, primary_key=True)
    account_move_line = models.ForeignKey('AccountMoveLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_automatic_entry_wizard_account_move_line_rel'
        unique_together = (('account_automatic_entry_wizard', 'account_move_line'),)


class AccountBankStatement(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField()
    date_done = models.DateTimeField(blank=True, null=True)
    balance_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end_real = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=-1)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    total_entry_encoding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    difference = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    cashbox_start = models.ForeignKey('AccountBankStatementCashbox', models.DO_NOTHING, blank=True, null=True)
    cashbox_end = models.ForeignKey('AccountBankStatementCashbox', models.DO_NOTHING, blank=True, null=True)
    previous_statement = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    is_valid_balance_start = models.BooleanField(blank=True, null=True)
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    sequence_prefix = models.CharField(max_length=-1, blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement'


class AccountBankStatementCashbox(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_cashbox'


class AccountBankStatementClosebalance(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_closebalance'


class AccountBankStatementLine(models.Model):
    move = models.ForeignKey('AccountMove', models.DO_NOTHING)
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    account_number = models.CharField(max_length=-1, blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    transaction_type = models.CharField(max_length=-1, blank=True, null=True)
    payment_ref = models.CharField(max_length=-1)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    foreign_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    amount_residual = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    is_reconciled = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_line'


class AccountCashRounding(models.Model):
    name = models.CharField(max_length=-1)
    rounding = models.FloatField()
    strategy = models.CharField(max_length=-1)
    rounding_method = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_cash_rounding'


class AccountCashboxLine(models.Model):
    coin_value = models.DecimalField(max_digits=65535, decimal_places=65535)
    number = models.IntegerField(blank=True, null=True)
    cashbox = models.ForeignKey(AccountBankStatementCashbox, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_cashbox_line'


class AccountChartTemplate(models.Model):
    name = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    code_digits = models.IntegerField()
    visible = models.BooleanField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    use_anglo_saxon = models.BooleanField(blank=True, null=True)
    complete_tax_set = models.BooleanField(blank=True, null=True)
    bank_account_code_prefix = models.CharField(max_length=-1)
    cash_account_code_prefix = models.CharField(max_length=-1)
    transfer_account_code_prefix = models.CharField(max_length=-1)
    income_currency_exchange_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    expense_currency_exchange_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    account_journal_suspense_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    default_cash_difference_income_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    default_cash_difference_expense_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    default_pos_receivable_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_receivable = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_payable = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_expense_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_income_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_expense = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_income = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_stock_account_input_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_stock_account_output_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_stock_valuation_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_tax_payable_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_tax_receivable_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_advance_tax_payment_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_cash_basis_base_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_chart_template'


class AccountCommonJournalReport(models.Model):
    amount_currency = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_common_journal_report'


class AccountCommonJournalReportAccountJournalRel(models.Model):
    account_common_journal_report = models.OneToOneField(AccountCommonJournalReport, models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_journal_report_account_journal_rel'
        unique_together = (('account_common_journal_report', 'account_journal'),)


class AccountCommonReport(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_common_report'


class AccountCommonReportAccountJournalRel(models.Model):
    account_common_report = models.OneToOneField(AccountCommonReport, models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_report_account_journal_rel'
        unique_together = (('account_common_report', 'account_journal'),)


class AccountEdiDocument(models.Model):
    move = models.ForeignKey('AccountMove', models.DO_NOTHING)
    edi_format = models.ForeignKey('AccountEdiFormat', models.DO_NOTHING)
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_edi_document'
        unique_together = (('edi_format', 'move'),)


class AccountEdiFormat(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    code = models.CharField(unique=True, max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_edi_format'


class AccountEdiFormatAccountJournalRel(models.Model):
    account_journal = models.OneToOneField('AccountJournal', models.DO_NOTHING, primary_key=True)
    account_edi_format = models.ForeignKey(AccountEdiFormat, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_edi_format_account_journal_rel'
        unique_together = (('account_journal', 'account_edi_format'),)


class AccountFinancialYearOp(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_financial_year_op'


class AccountFiscalPosition(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    note = models.TextField(blank=True, null=True)
    auto_apply = models.BooleanField(blank=True, null=True)
    vat_required = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING, blank=True, null=True)
    zip_from = models.CharField(max_length=-1, blank=True, null=True)
    zip_to = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position'


class AccountFiscalPositionAccount(models.Model):
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    account_src = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    account_dest = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account'
        unique_together = (('position', 'account_src', 'account_dest'),)


class AccountFiscalPositionAccountTemplate(models.Model):
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING)
    account_src = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    account_dest = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account_template'


class AccountFiscalPositionResCountryStateRel(models.Model):
    account_fiscal_position = models.OneToOneField(AccountFiscalPosition, models.DO_NOTHING, primary_key=True)
    res_country_state = models.ForeignKey('ResCountryState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_res_country_state_rel'
        unique_together = (('account_fiscal_position', 'res_country_state'),)


class AccountFiscalPositionTax(models.Model):
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    tax_src = models.ForeignKey('AccountTax', models.DO_NOTHING)
    tax_dest = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax'
        unique_together = (('position', 'tax_src', 'tax_dest'),)


class AccountFiscalPositionTaxTemplate(models.Model):
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING)
    tax_src = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)
    tax_dest = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax_template'


class AccountFiscalPositionTemplate(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    note = models.TextField(blank=True, null=True)
    auto_apply = models.BooleanField(blank=True, null=True)
    vat_required = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING, blank=True, null=True)
    zip_from = models.CharField(max_length=-1, blank=True, null=True)
    zip_to = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_template'


class AccountFiscalPositionTemplateResCountryStateRel(models.Model):
    account_fiscal_position_template = models.OneToOneField(AccountFiscalPositionTemplate, models.DO_NOTHING, primary_key=True)
    res_country_state = models.ForeignKey('ResCountryState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_template_res_country_state_rel'
        unique_together = (('account_fiscal_position_template', 'res_country_state'),)


class AccountFullReconcile(models.Model):
    name = models.CharField(max_length=-1)
    exchange_move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_full_reconcile'


class AccountGroup(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1)
    code_prefix_start = models.CharField(max_length=-1, blank=True, null=True)
    code_prefix_end = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_group'


class AccountGroupTemplate(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    code_prefix_start = models.CharField(max_length=-1, blank=True, null=True)
    code_prefix_end = models.CharField(max_length=-1, blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_group_template'


class AccountIncoterms(models.Model):
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=3)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_incoterms'


class AccountInvoiceSend(models.Model):
    is_email = models.BooleanField(blank=True, null=True)
    is_print = models.BooleanField(blank=True, null=True)
    printed = models.BooleanField(blank=True, null=True)
    composer = models.ForeignKey('MailComposeMessage', models.DO_NOTHING)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    snailmail_is_letter = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_send'


class AccountInvoiceTransactionRel(models.Model):
    transaction = models.OneToOneField('PaymentTransaction', models.DO_NOTHING, primary_key=True)
    invoice = models.ForeignKey('AccountMove', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_invoice_transaction_rel'
        unique_together = (('transaction', 'invoice'),)


class AccountJournal(models.Model):
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=5)
    active = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    default_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    payment_debit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    payment_credit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    suspense_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    restrict_mode_hash_table = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    invoice_reference_type = models.CharField(max_length=-1)
    invoice_reference_model = models.CharField(max_length=-1)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    refund_sequence = models.BooleanField(blank=True, null=True)
    sequence_override_regex = models.TextField(blank=True, null=True)
    at_least_one_inbound = models.BooleanField(blank=True, null=True)
    at_least_one_outbound = models.BooleanField(blank=True, null=True)
    profit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    loss_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    bank_statements_source = models.CharField(max_length=-1, blank=True, null=True)
    sale_activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True)
    sale_activity_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    sale_activity_note = models.TextField(blank=True, null=True)
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING, blank=True, null=True)
    secure_sequence = models.ForeignKey('IrSequence', models.DO_NOTHING, blank=True, null=True)
    show_on_dashboard = models.BooleanField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal'
        unique_together = (('code', 'name', 'company'),)


class AccountJournalAccountJournalGroupRel(models.Model):
    account_journal_group = models.OneToOneField('AccountJournalGroup', models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_journal_group_rel'
        unique_together = (('account_journal_group', 'account_journal'),)


class AccountJournalAccountPrintJournalRel(models.Model):
    account_print_journal = models.OneToOneField('AccountPrintJournal', models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_print_journal_rel'
        unique_together = (('account_print_journal', 'account_journal'),)


class AccountJournalAccountReconcileModelRel(models.Model):
    account_reconcile_model = models.OneToOneField('AccountReconcileModel', models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_reconcile_model_rel'
        unique_together = (('account_reconcile_model', 'account_journal'),)


class AccountJournalAccountReconcileModelTemplateRel(models.Model):
    account_reconcile_model_template = models.OneToOneField('AccountReconcileModelTemplate', models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_reconcile_model_template_rel'
        unique_together = (('account_reconcile_model_template', 'account_journal'),)


class AccountJournalGroup(models.Model):
    name = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal_group'


class AccountJournalInboundPaymentMethodRel(models.Model):
    journal = models.OneToOneField(AccountJournal, models.DO_NOTHING, primary_key=True)
    inbound_payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING, db_column='inbound_payment_method')

    class Meta:
        managed = False
        db_table = 'account_journal_inbound_payment_method_rel'
        unique_together = (('journal', 'inbound_payment_method'),)


class AccountJournalOutboundPaymentMethodRel(models.Model):
    journal = models.OneToOneField(AccountJournal, models.DO_NOTHING, primary_key=True)
    outbound_payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING, db_column='outbound_payment_method')

    class Meta:
        managed = False
        db_table = 'account_journal_outbound_payment_method_rel'
        unique_together = (('journal', 'outbound_payment_method'),)


class AccountMove(models.Model):
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField()
    ref = models.CharField(max_length=-1, blank=True, null=True)
    narration = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=-1)
    posted_before = models.BooleanField(blank=True, null=True)
    move_type = models.CharField(max_length=-1)
    to_check = models.BooleanField(blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    commercial_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    is_move_sent = models.BooleanField(blank=True, null=True)
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    payment_reference = models.CharField(max_length=-1, blank=True, null=True)
    payment = models.ForeignKey('AccountPayment', models.DO_NOTHING, blank=True, null=True)
    statement_line = models.ForeignKey(AccountBankStatementLine, models.DO_NOTHING, blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_untaxed_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_state = models.CharField(max_length=-1, blank=True, null=True)
    tax_cash_basis_rec = models.ForeignKey('AccountPartialReconcile', models.DO_NOTHING, blank=True, null=True)
    tax_cash_basis_move = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    auto_post = models.BooleanField(blank=True, null=True)
    reversed_entry = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True)
    invoice_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    invoice_date_due = models.DateField(blank=True, null=True)
    invoice_origin = models.CharField(max_length=-1, blank=True, null=True)
    invoice_payment_term = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING, blank=True, null=True)
    invoice_incoterm = models.ForeignKey(AccountIncoterms, models.DO_NOTHING, blank=True, null=True)
    qr_code_method = models.CharField(max_length=-1, blank=True, null=True)
    invoice_source_email = models.CharField(max_length=-1, blank=True, null=True)
    invoice_partner_display_name = models.CharField(max_length=-1, blank=True, null=True)
    invoice_cash_rounding = models.ForeignKey(AccountCashRounding, models.DO_NOTHING, blank=True, null=True)
    secure_sequence_number = models.IntegerField(blank=True, null=True)
    inalterable_hash = models.CharField(max_length=-1, blank=True, null=True)
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    sequence_prefix = models.CharField(max_length=-1, blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    edi_state = models.CharField(max_length=-1, blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    partner_shipping = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    stock_move = models.ForeignKey('StockMove', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move'


class AccountMoveAccountInvoiceSendRel(models.Model):
    account_invoice_send = models.OneToOneField(AccountInvoiceSend, models.DO_NOTHING, primary_key=True)
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_account_invoice_send_rel'
        unique_together = (('account_invoice_send', 'account_move'),)


class AccountMoveAccountResequenceWizardRel(models.Model):
    account_resequence_wizard = models.OneToOneField('AccountResequenceWizard', models.DO_NOTHING, primary_key=True)
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_account_resequence_wizard_rel'
        unique_together = (('account_resequence_wizard', 'account_move'),)


class AccountMoveLine(models.Model):
    move = models.ForeignKey(AccountMove, models.DO_NOTHING)
    move_name = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    parent_state = models.CharField(max_length=-1, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    company_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    account_root_id = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    reconciled = models.BooleanField(blank=True, null=True)
    blocked = models.BooleanField(blank=True, null=True)
    date_maturity = models.DateField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    reconcile_model = models.ForeignKey('AccountReconcileModel', models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey('AccountPayment', models.DO_NOTHING, blank=True, null=True)
    statement_line = models.ForeignKey(AccountBankStatementLine, models.DO_NOTHING, blank=True, null=True)
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING, blank=True, null=True)
    tax_line = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    tax_group = models.ForeignKey('AccountTaxGroup', models.DO_NOTHING, blank=True, null=True)
    tax_base_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tax_exigible = models.BooleanField(blank=True, null=True)
    tax_repartition_line = models.ForeignKey('AccountTaxRepartitionLine', models.DO_NOTHING, blank=True, null=True)
    tax_audit = models.CharField(max_length=-1, blank=True, null=True)
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    full_reconcile = models.ForeignKey(AccountFullReconcile, models.DO_NOTHING, blank=True, null=True)
    matching_number = models.CharField(max_length=-1, blank=True, null=True)
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    display_type = models.CharField(max_length=-1, blank=True, null=True)
    is_rounding_line = models.BooleanField(blank=True, null=True)
    exclude_from_invoice_tab = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    is_anglo_saxon_line = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line'


class AccountMoveLineAccountTaxRel(models.Model):
    account_move_line = models.OneToOneField(AccountMoveLine, models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_line_account_tax_rel'
        unique_together = (('account_move_line', 'account_tax'),)


class AccountMoveReversal(models.Model):
    date_mode = models.CharField(max_length=-1)
    date = models.DateField(blank=True, null=True)
    reason = models.CharField(max_length=-1, blank=True, null=True)
    refund_method = models.CharField(max_length=-1)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_reversal'


class AccountMoveReversalMove(models.Model):
    reversal = models.OneToOneField(AccountMoveReversal, models.DO_NOTHING, primary_key=True)
    move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_reversal_move'
        unique_together = (('reversal', 'move'),)


class AccountMoveReversalNewMove(models.Model):
    reversal = models.OneToOneField(AccountMoveReversal, models.DO_NOTHING, primary_key=True)
    new_move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_reversal_new_move'
        unique_together = (('reversal', 'new_move'),)


class AccountPartialReconcile(models.Model):
    debit_move = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)
    credit_move = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)
    full_reconcile = models.ForeignKey(AccountFullReconcile, models.DO_NOTHING, blank=True, null=True)
    debit_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    credit_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    credit_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    max_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_partial_reconcile'


class AccountPayment(models.Model):
    move = models.ForeignKey(AccountMove, models.DO_NOTHING)
    is_reconciled = models.BooleanField(blank=True, null=True)
    is_matched = models.BooleanField(blank=True, null=True)
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    is_internal_transfer = models.BooleanField(blank=True, null=True)
    payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_type = models.CharField(max_length=-1)
    partner_type = models.CharField(max_length=-1)
    payment_reference = models.CharField(max_length=-1, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    destination_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment_transaction = models.ForeignKey('PaymentTransaction', models.DO_NOTHING, blank=True, null=True)
    payment_token = models.ForeignKey('PaymentToken', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment'


class AccountPaymentAccountBankStatementLineRel(models.Model):
    account_bank_statement_line = models.OneToOneField(AccountBankStatementLine, models.DO_NOTHING, primary_key=True)
    account_payment = models.ForeignKey(AccountPayment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_payment_account_bank_statement_line_rel'
        unique_together = (('account_bank_statement_line', 'account_payment'),)


class AccountPaymentMethod(models.Model):
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1)
    payment_type = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_method'


class AccountPaymentRegister(models.Model):
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    communication = models.CharField(max_length=-1, blank=True, null=True)
    group_payment = models.BooleanField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    payment_type = models.CharField(max_length=-1, blank=True, null=True)
    partner_type = models.CharField(max_length=-1, blank=True, null=True)
    source_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    source_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    source_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    can_edit_wizard = models.BooleanField(blank=True, null=True)
    can_group_payments = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    payment_method = models.ForeignKey(AccountPaymentMethod, models.DO_NOTHING, blank=True, null=True)
    payment_difference_handling = models.CharField(max_length=-1, blank=True, null=True)
    writeoff_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    writeoff_label = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment_token = models.ForeignKey('PaymentToken', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_register'


class AccountPaymentRegisterMoveLineRel(models.Model):
    wizard = models.OneToOneField(AccountPaymentRegister, models.DO_NOTHING, primary_key=True)
    line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_payment_register_move_line_rel'
        unique_together = (('wizard', 'line'),)


class AccountPaymentTerm(models.Model):
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_term'


class AccountPaymentTermLine(models.Model):
    value = models.CharField(max_length=-1)
    value_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days = models.IntegerField()
    day_of_the_month = models.IntegerField(blank=True, null=True)
    option = models.CharField(max_length=-1)
    payment = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_term_line'


class AccountPrintJournal(models.Model):
    sort_selection = models.CharField(max_length=-1)
    amount_currency = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_print_journal'


class AccountReconcileModel(models.Model):
    active = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    rule_type = models.CharField(max_length=-1)
    auto_reconcile = models.BooleanField(blank=True, null=True)
    to_check = models.BooleanField(blank=True, null=True)
    matching_order = models.CharField(max_length=-1)
    match_text_location_label = models.BooleanField(blank=True, null=True)
    match_text_location_note = models.BooleanField(blank=True, null=True)
    match_text_location_reference = models.BooleanField(blank=True, null=True)
    match_nature = models.CharField(max_length=-1)
    match_amount = models.CharField(max_length=-1, blank=True, null=True)
    match_amount_min = models.FloatField(blank=True, null=True)
    match_amount_max = models.FloatField(blank=True, null=True)
    match_label = models.CharField(max_length=-1, blank=True, null=True)
    match_label_param = models.CharField(max_length=-1, blank=True, null=True)
    match_note = models.CharField(max_length=-1, blank=True, null=True)
    match_note_param = models.CharField(max_length=-1, blank=True, null=True)
    match_transaction_type = models.CharField(max_length=-1, blank=True, null=True)
    match_transaction_type_param = models.CharField(max_length=-1, blank=True, null=True)
    match_same_currency = models.BooleanField(blank=True, null=True)
    match_total_amount = models.BooleanField(blank=True, null=True)
    match_total_amount_param = models.FloatField(blank=True, null=True)
    match_partner = models.BooleanField(blank=True, null=True)
    past_months_limit = models.IntegerField(blank=True, null=True)
    decimal_separator = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model'


class AccountReconcileModelAnalyticTagRel(models.Model):
    account_reconcile_model_line = models.OneToOneField('AccountReconcileModelLine', models.DO_NOTHING, primary_key=True)
    account_analytic_tag = models.ForeignKey(AccountAnalyticTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_analytic_tag_rel'
        unique_together = (('account_reconcile_model_line', 'account_analytic_tag'),)


class AccountReconcileModelLine(models.Model):
    model = models.ForeignKey(AccountReconcileModel, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    label = models.CharField(max_length=-1, blank=True, null=True)
    amount_type = models.CharField(max_length=-1)
    force_tax_included = models.BooleanField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    amount_string = models.CharField(max_length=-1)
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line'


class AccountReconcileModelLineAccountTaxRel(models.Model):
    account_reconcile_model_line = models.OneToOneField(AccountReconcileModelLine, models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line_account_tax_rel'
        unique_together = (('account_reconcile_model_line', 'account_tax'),)


class AccountReconcileModelLineTemplate(models.Model):
    model = models.ForeignKey('AccountReconcileModelTemplate', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    label = models.CharField(max_length=-1, blank=True, null=True)
    amount_type = models.CharField(max_length=-1)
    amount_string = models.CharField(max_length=-1, blank=True, null=True)
    force_tax_included = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line_template'


class AccountReconcileModelLineTemplateAccountTaxTemplateRel(models.Model):
    account_reconcile_model_line_template = models.OneToOneField(AccountReconcileModelLineTemplate, models.DO_NOTHING, primary_key=True)
    account_tax_template = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line_template_account_tax_template_rel'
        unique_together = (('account_reconcile_model_line_template', 'account_tax_template'),)


class AccountReconcileModelPartnerMapping(models.Model):
    model = models.ForeignKey(AccountReconcileModel, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    payment_ref_regex = models.CharField(max_length=-1, blank=True, null=True)
    narration_regex = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_partner_mapping'


class AccountReconcileModelResPartnerCategoryRel(models.Model):
    account_reconcile_model = models.OneToOneField(AccountReconcileModel, models.DO_NOTHING, primary_key=True)
    res_partner_category = models.ForeignKey('ResPartnerCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_res_partner_category_rel'
        unique_together = (('account_reconcile_model', 'res_partner_category'),)


class AccountReconcileModelResPartnerRel(models.Model):
    account_reconcile_model = models.OneToOneField(AccountReconcileModel, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_res_partner_rel'
        unique_together = (('account_reconcile_model', 'res_partner'),)


class AccountReconcileModelTemplate(models.Model):
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField()
    rule_type = models.CharField(max_length=-1)
    auto_reconcile = models.BooleanField(blank=True, null=True)
    to_check = models.BooleanField(blank=True, null=True)
    matching_order = models.CharField(max_length=-1, blank=True, null=True)
    match_text_location_label = models.BooleanField(blank=True, null=True)
    match_text_location_note = models.BooleanField(blank=True, null=True)
    match_text_location_reference = models.BooleanField(blank=True, null=True)
    match_nature = models.CharField(max_length=-1)
    match_amount = models.CharField(max_length=-1, blank=True, null=True)
    match_amount_min = models.FloatField(blank=True, null=True)
    match_amount_max = models.FloatField(blank=True, null=True)
    match_label = models.CharField(max_length=-1, blank=True, null=True)
    match_label_param = models.CharField(max_length=-1, blank=True, null=True)
    match_note = models.CharField(max_length=-1, blank=True, null=True)
    match_note_param = models.CharField(max_length=-1, blank=True, null=True)
    match_transaction_type = models.CharField(max_length=-1, blank=True, null=True)
    match_transaction_type_param = models.CharField(max_length=-1, blank=True, null=True)
    match_same_currency = models.BooleanField(blank=True, null=True)
    match_total_amount = models.BooleanField(blank=True, null=True)
    match_total_amount_param = models.FloatField(blank=True, null=True)
    match_partner = models.BooleanField(blank=True, null=True)
    decimal_separator = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_template'


class AccountReconcileModelTemplateResPartnerCategoryRel(models.Model):
    account_reconcile_model_template = models.OneToOneField(AccountReconcileModelTemplate, models.DO_NOTHING, primary_key=True)
    res_partner_category = models.ForeignKey('ResPartnerCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_template_res_partner_category_rel'
        unique_together = (('account_reconcile_model_template', 'res_partner_category'),)


class AccountReconcileModelTemplateResPartnerRel(models.Model):
    account_reconcile_model_template = models.OneToOneField(AccountReconcileModelTemplate, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_template_res_partner_rel'
        unique_together = (('account_reconcile_model_template', 'res_partner'),)


class AccountResequenceWizard(models.Model):
    first_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=-1)
    ordering = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_resequence_wizard'


class AccountSetupBankManualConfig(models.Model):
    res_partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING)
    new_journal_name = models.CharField(max_length=-1)
    num_journals_without_account = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_setup_bank_manual_config'


class AccountTax(models.Model):
    name = models.CharField(max_length=-1)
    type_tax_use = models.CharField(max_length=-1)
    tax_scope = models.CharField(max_length=-1, blank=True, null=True)
    amount_type = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    sequence = models.IntegerField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    description = models.CharField(max_length=-1, blank=True, null=True)
    price_include = models.BooleanField(blank=True, null=True)
    include_base_amount = models.BooleanField(blank=True, null=True)
    analytic = models.BooleanField(blank=True, null=True)
    tax_group = models.ForeignKey('AccountTaxGroup', models.DO_NOTHING)
    tax_exigibility = models.CharField(max_length=-1, blank=True, null=True)
    cash_basis_transition_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    l10n_mx_tax_type = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax'
        unique_together = (('name', 'company', 'type_tax_use', 'tax_scope'),)


class AccountTaxFiliationRel(models.Model):
    parent_tax = models.OneToOneField(AccountTax, models.DO_NOTHING, db_column='parent_tax', primary_key=True)
    child_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, db_column='child_tax')

    class Meta:
        managed = False
        db_table = 'account_tax_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountTaxGroup(models.Model):
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_group'


class AccountTaxRepartitionFinancialTags(models.Model):
    account_tax_repartition_line_template = models.OneToOneField('AccountTaxRepartitionLineTemplate', models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_financial_tags'
        unique_together = (('account_tax_repartition_line_template', 'account_account_tag'),)


class AccountTaxRepartitionLine(models.Model):
    factor_percent = models.FloatField()
    repartition_type = models.CharField(max_length=-1)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    invoice_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, blank=True, null=True)
    refund_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    use_in_tax_closing = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_line'


class AccountTaxRepartitionLineTemplate(models.Model):
    factor_percent = models.FloatField()
    repartition_type = models.CharField(max_length=-1)
    account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    invoice_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True)
    refund_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True)
    use_in_tax_closing = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_line_template'


class AccountTaxRepartitionMinusReportLine(models.Model):
    account_tax_repartition_line_template = models.OneToOneField(AccountTaxRepartitionLineTemplate, models.DO_NOTHING, primary_key=True)
    account_tax_report_line = models.ForeignKey('AccountTaxReportLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_minus_report_line'
        unique_together = (('account_tax_repartition_line_template', 'account_tax_report_line'),)


class AccountTaxRepartitionPlusReportLine(models.Model):
    account_tax_repartition_line_template = models.OneToOneField(AccountTaxRepartitionLineTemplate, models.DO_NOTHING, primary_key=True)
    account_tax_report_line = models.ForeignKey('AccountTaxReportLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_plus_report_line'
        unique_together = (('account_tax_repartition_line_template', 'account_tax_report_line'),)


class AccountTaxReport(models.Model):
    name = models.CharField(max_length=-1)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_report'


class AccountTaxReportLine(models.Model):
    name = models.CharField(max_length=-1)
    report_action = models.ForeignKey('IrActWindow', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    report = models.ForeignKey(AccountTaxReport, models.DO_NOTHING)
    tag_name = models.CharField(max_length=-1, blank=True, null=True)
    code = models.CharField(max_length=-1, blank=True, null=True)
    formula = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_report_line'


class AccountTaxReportLineTagsRel(models.Model):
    account_account_tag = models.OneToOneField(AccountAccountTag, models.DO_NOTHING, primary_key=True)
    account_tax_report_line = models.ForeignKey(AccountTaxReportLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_report_line_tags_rel'
        unique_together = (('account_account_tag', 'account_tax_report_line'),)


class AccountTaxSaleAdvancePaymentInvRel(models.Model):
    sale_advance_payment_inv = models.OneToOneField('SaleAdvancePaymentInv', models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_sale_advance_payment_inv_rel'
        unique_together = (('sale_advance_payment_inv', 'account_tax'),)


class AccountTaxSaleOrderLineRel(models.Model):
    sale_order_line = models.OneToOneField('SaleOrderLine', models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_sale_order_line_rel'
        unique_together = (('sale_order_line', 'account_tax'),)


class AccountTaxTemplate(models.Model):
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    type_tax_use = models.CharField(max_length=-1)
    tax_scope = models.CharField(max_length=-1, blank=True, null=True)
    amount_type = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    description = models.CharField(max_length=-1, blank=True, null=True)
    price_include = models.BooleanField(blank=True, null=True)
    include_base_amount = models.BooleanField(blank=True, null=True)
    analytic = models.BooleanField(blank=True, null=True)
    tax_group = models.ForeignKey(AccountTaxGroup, models.DO_NOTHING, blank=True, null=True)
    tax_exigibility = models.CharField(max_length=-1, blank=True, null=True)
    cash_basis_transition_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    l10n_mx_tax_type = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_template'
        unique_together = (('name', 'type_tax_use', 'tax_scope', 'chart_template'),)


class AccountTaxTemplateFiliationRel(models.Model):
    parent_tax = models.OneToOneField(AccountTaxTemplate, models.DO_NOTHING, db_column='parent_tax', primary_key=True)
    child_tax = models.ForeignKey(AccountTaxTemplate, models.DO_NOTHING, db_column='child_tax')

    class Meta:
        managed = False
        db_table = 'account_tax_template_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountTourUploadBill(models.Model):
    composer = models.ForeignKey('MailComposeMessage', models.DO_NOTHING)
    selection = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tour_upload_bill'


class AccountTourUploadBillEmailConfirm(models.Model):
    email_alias = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tour_upload_bill_email_confirm'


class AccountUnreconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_unreconcile'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthTotpWizard(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    secret = models.CharField(max_length=-1)
    url = models.CharField(max_length=-1, blank=True, null=True)
    qrcode = models.BinaryField(blank=True, null=True)
    code = models.CharField(max_length=7, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_totp_wizard'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BarcodeNomenclature(models.Model):
    name = models.CharField(max_length=32)
    upc_ean_conv = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barcode_nomenclature'


class BarcodeRule(models.Model):
    name = models.CharField(max_length=32)
    barcode_nomenclature = models.ForeignKey(BarcodeNomenclature, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    encoding = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    pattern = models.CharField(max_length=32)
    alias = models.CharField(max_length=32)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barcode_rule'


class BaseDocumentLayout(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    report_layout = models.ForeignKey('ReportLayout', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_document_layout'


class BaseImportImport(models.Model):
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    file = models.BinaryField(blank=True, null=True)
    file_name = models.CharField(max_length=-1, blank=True, null=True)
    file_type = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_import'


class BaseImportMapping(models.Model):
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    column_name = models.CharField(max_length=-1, blank=True, null=True)
    field_name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_mapping'


class BaseImportTestsModelsChar(models.Model):
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char'


class BaseImportTestsModelsCharNoreadonly(models.Model):
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_noreadonly'


class BaseImportTestsModelsCharReadonly(models.Model):
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_readonly'


class BaseImportTestsModelsCharRequired(models.Model):
    value = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_required'


class BaseImportTestsModelsCharStates(models.Model):
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_states'


class BaseImportTestsModelsCharStillreadonly(models.Model):
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_stillreadonly'


class BaseImportTestsModelsComplex(models.Model):
    f = models.FloatField(blank=True, null=True)
    m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c = models.CharField(max_length=-1, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    d = models.DateField(blank=True, null=True)
    dt = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_complex'


class BaseImportTestsModelsFloat(models.Model):
    value = models.FloatField(blank=True, null=True)
    value2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_float'


class BaseImportTestsModelsM2O(models.Model):
    value = models.ForeignKey('BaseImportTestsModelsM2ORelated', models.DO_NOTHING, db_column='value', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o'


class BaseImportTestsModelsM2ORelated(models.Model):
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_related'


class BaseImportTestsModelsM2ORequired(models.Model):
    value = models.ForeignKey('BaseImportTestsModelsM2ORequiredRelated', models.DO_NOTHING, db_column='value')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required'


class BaseImportTestsModelsM2ORequiredRelated(models.Model):
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required_related'


class BaseImportTestsModelsO2M(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m'


class BaseImportTestsModelsO2MChild(models.Model):
    parent = models.ForeignKey(BaseImportTestsModelsO2M, models.DO_NOTHING, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m_child'


class BaseImportTestsModelsPreview(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    somevalue = models.IntegerField()
    othervalue = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_preview'


class BaseLanguageExport(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1)
    format = models.CharField(max_length=-1)
    data = models.BinaryField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_export'


class BaseLanguageImport(models.Model):
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=6)
    data = models.BinaryField()
    filename = models.CharField(max_length=-1)
    overwrite = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_import'


class BaseLanguageInstall(models.Model):
    lang = models.CharField(max_length=-1)
    overwrite = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_install'


class BaseModuleUninstall(models.Model):
    show_all = models.BooleanField(blank=True, null=True)
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_uninstall'


class BaseModuleUpdate(models.Model):
    updated = models.IntegerField(blank=True, null=True)
    added = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_update'


class BaseModuleUpgrade(models.Model):
    module_info = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_upgrade'


class BasePartnerMergeAutomaticWizard(models.Model):
    group_by_email = models.BooleanField(blank=True, null=True)
    group_by_name = models.BooleanField(blank=True, null=True)
    group_by_is_company = models.BooleanField(blank=True, null=True)
    group_by_vat = models.BooleanField(blank=True, null=True)
    group_by_parent_id = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=-1)
    number_group = models.IntegerField(blank=True, null=True)
    current_line = models.ForeignKey('BasePartnerMergeLine', models.DO_NOTHING, blank=True, null=True)
    dst_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    exclude_contact = models.BooleanField(blank=True, null=True)
    exclude_journal_item = models.BooleanField(blank=True, null=True)
    maximum_group = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard'


class BasePartnerMergeAutomaticWizardResPartnerRel(models.Model):
    base_partner_merge_automatic_wizard = models.OneToOneField(BasePartnerMergeAutomaticWizard, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard_res_partner_rel'
        unique_together = (('base_partner_merge_automatic_wizard', 'res_partner'),)


class BasePartnerMergeLine(models.Model):
    wizard = models.ForeignKey(BasePartnerMergeAutomaticWizard, models.DO_NOTHING, blank=True, null=True)
    min_id = models.IntegerField(blank=True, null=True)
    aggr_ids = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_line'


class BaseUpdateTranslations(models.Model):
    lang = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_update_translations'


class BusBus(models.Model):
    channel = models.CharField(max_length=-1, blank=True, null=True)
    message = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_bus'


class BusPresence(models.Model):
    user = models.OneToOneField('ResUsers', models.DO_NOTHING)
    last_poll = models.DateTimeField(blank=True, null=True)
    last_presence = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_presence'


class CalendarAlarm(models.Model):
    name = models.CharField(max_length=-1)
    alarm_type = models.CharField(max_length=-1)
    duration = models.IntegerField()
    interval = models.CharField(max_length=-1)
    duration_minutes = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_alarm'


class CalendarAlarmCalendarEventRel(models.Model):
    calendar_event = models.OneToOneField('CalendarEvent', models.DO_NOTHING, primary_key=True)
    calendar_alarm = models.ForeignKey(CalendarAlarm, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendar_alarm_calendar_event_rel'
        unique_together = (('calendar_event', 'calendar_alarm'),)


class CalendarAttendee(models.Model):
    event = models.ForeignKey('CalendarEvent', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    state = models.CharField(max_length=-1, blank=True, null=True)
    common_name = models.CharField(max_length=-1, blank=True, null=True)
    availability = models.CharField(max_length=-1, blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_attendee'


class CalendarContacts(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_contacts'
        unique_together = (('user', 'partner'),)


class CalendarEvent(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    start = models.DateTimeField()
    stop = models.DateTimeField()
    allday = models.BooleanField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    stop_date = models.DateField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    privacy = models.CharField(max_length=-1)
    location = models.CharField(max_length=-1, blank=True, null=True)
    show_as = models.CharField(max_length=-1)
    res_id = models.IntegerField(blank=True, null=True)
    res_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    res_model_0 = models.CharField(db_column='res_model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    recurrency = models.BooleanField(blank=True, null=True)
    recurrence = models.ForeignKey('CalendarRecurrence', models.DO_NOTHING, blank=True, null=True)
    follow_recurrence = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    opportunity = models.ForeignKey('CrmLead', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event'


class CalendarEventResPartnerRel(models.Model):
    calendar_event = models.OneToOneField(CalendarEvent, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendar_event_res_partner_rel'
        unique_together = (('calendar_event', 'res_partner'),)


class CalendarEventType(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event_type'


class CalendarRecurrence(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    base_event = models.ForeignKey(CalendarEvent, models.DO_NOTHING, blank=True, null=True)
    event_tz = models.CharField(max_length=-1, blank=True, null=True)
    rrule = models.CharField(max_length=-1, blank=True, null=True)
    rrule_type = models.CharField(max_length=-1, blank=True, null=True)
    end_type = models.CharField(max_length=-1, blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    mo = models.BooleanField(blank=True, null=True)
    tu = models.BooleanField(blank=True, null=True)
    we = models.BooleanField(blank=True, null=True)
    th = models.BooleanField(blank=True, null=True)
    fr = models.BooleanField(blank=True, null=True)
    sa = models.BooleanField(blank=True, null=True)
    su = models.BooleanField(blank=True, null=True)
    month_by = models.CharField(max_length=-1, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    weekday = models.CharField(max_length=-1, blank=True, null=True)
    byday = models.CharField(max_length=-1, blank=True, null=True)
    until = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_recurrence'


class CashBoxOut(models.Model):
    name = models.CharField(max_length=-1)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_box_out'


class ChangePasswordUser(models.Model):
    wizard = models.ForeignKey('ChangePasswordWizard', models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    user_login = models.CharField(max_length=-1, blank=True, null=True)
    new_passwd = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_user'


class ChangePasswordWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_wizard'


class ConfirmStockSms(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confirm_stock_sms'


class CrmConvertLeadMassLeadRel(models.Model):
    crm_lead2opportunity_partner_mass = models.OneToOneField('CrmLead2OpportunityPartnerMass', models.DO_NOTHING, primary_key=True)
    crm_lead = models.ForeignKey('CrmLead', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_convert_lead_mass_lead_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'crm_lead'),)


class CrmIapLeadHelpers(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_iap_lead_helpers'


class CrmIapLeadIndustry(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    reveal_id = models.CharField(max_length=-1)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_iap_lead_industry'


class CrmIapLeadIndustryCrmIapLeadMiningRequestRel(models.Model):
    crm_iap_lead_mining_request = models.OneToOneField('CrmIapLeadMiningRequest', models.DO_NOTHING, primary_key=True)
    crm_iap_lead_industry = models.ForeignKey(CrmIapLeadIndustry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_iap_lead_industry_crm_iap_lead_mining_request_rel'
        unique_together = (('crm_iap_lead_mining_request', 'crm_iap_lead_industry'),)


class CrmIapLeadMiningRequest(models.Model):
    name = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    lead_number = models.IntegerField()
    search_type = models.CharField(max_length=-1)
    error = models.TextField(blank=True, null=True)
    lead_type = models.CharField(max_length=-1)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    filter_on_size = models.BooleanField(blank=True, null=True)
    company_size_min = models.IntegerField(blank=True, null=True)
    company_size_max = models.IntegerField(blank=True, null=True)
    contact_number = models.IntegerField(blank=True, null=True)
    contact_filter_type = models.CharField(max_length=-1, blank=True, null=True)
    preferred_role = models.ForeignKey('CrmIapLeadRole', models.DO_NOTHING, blank=True, null=True)
    seniority = models.ForeignKey('CrmIapLeadSeniority', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_iap_lead_mining_request'


class CrmIapLeadMiningRequestCrmIapLeadRoleRel(models.Model):
    crm_iap_lead_mining_request = models.OneToOneField(CrmIapLeadMiningRequest, models.DO_NOTHING, primary_key=True)
    crm_iap_lead_role = models.ForeignKey('CrmIapLeadRole', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_iap_lead_mining_request_crm_iap_lead_role_rel'
        unique_together = (('crm_iap_lead_mining_request', 'crm_iap_lead_role'),)


class CrmIapLeadMiningRequestCrmTagRel(models.Model):
    crm_iap_lead_mining_request = models.OneToOneField(CrmIapLeadMiningRequest, models.DO_NOTHING, primary_key=True)
    crm_tag = models.ForeignKey('CrmTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_iap_lead_mining_request_crm_tag_rel'
        unique_together = (('crm_iap_lead_mining_request', 'crm_tag'),)


class CrmIapLeadMiningRequestResCountryRel(models.Model):
    crm_iap_lead_mining_request = models.OneToOneField(CrmIapLeadMiningRequest, models.DO_NOTHING, primary_key=True)
    res_country = models.ForeignKey('ResCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_iap_lead_mining_request_res_country_rel'
        unique_together = (('crm_iap_lead_mining_request', 'res_country'),)


class CrmIapLeadMiningRequestResCountryStateRel(models.Model):
    crm_iap_lead_mining_request = models.OneToOneField(CrmIapLeadMiningRequest, models.DO_NOTHING, primary_key=True)
    res_country_state = models.ForeignKey('ResCountryState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_iap_lead_mining_request_res_country_state_rel'
        unique_together = (('crm_iap_lead_mining_request', 'res_country_state'),)


class CrmIapLeadRole(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    reveal_id = models.CharField(max_length=-1)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_iap_lead_role'


class CrmIapLeadSeniority(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    reveal_id = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_iap_lead_seniority'


class CrmLead(models.Model):
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    email_normalized = models.CharField(max_length=-1, blank=True, null=True)
    message_bounce = models.IntegerField(blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    phone_sanitized = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    referred = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    stage = models.ForeignKey('CrmStage', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    expected_revenue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prorated_revenue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    recurring_revenue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    recurring_plan = models.ForeignKey('CrmRecurringPlan', models.DO_NOTHING, db_column='recurring_plan', blank=True, null=True)
    recurring_revenue_monthly = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    recurring_revenue_monthly_prorated = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    date_action_last = models.DateTimeField(blank=True, null=True)
    date_open = models.DateTimeField(blank=True, null=True)
    day_open = models.FloatField(blank=True, null=True)
    day_close = models.FloatField(blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    date_conversion = models.DateTimeField(blank=True, null=True)
    date_deadline = models.DateField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    contact_name = models.CharField(max_length=-1, blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    function = models.CharField(max_length=-1, blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, db_column='title', blank=True, null=True)
    email_from = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    mobile = models.CharField(max_length=-1, blank=True, null=True)
    phone_state = models.CharField(max_length=-1, blank=True, null=True)
    email_state = models.CharField(max_length=-1, blank=True, null=True)
    website = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.ForeignKey('ResLang', models.DO_NOTHING, blank=True, null=True)
    street = models.CharField(max_length=-1, blank=True, null=True)
    street2 = models.CharField(max_length=-1, blank=True, null=True)
    zip = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)
    automated_probability = models.FloatField(blank=True, null=True)
    lost_reason = models.ForeignKey('CrmLostReason', models.DO_NOTHING, db_column='lost_reason', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    reveal_id = models.CharField(max_length=-1, blank=True, null=True)
    lead_mining_request = models.ForeignKey(CrmIapLeadMiningRequest, models.DO_NOTHING, blank=True, null=True)
    iap_enrich_done = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead'


class CrmLead2OpportunityPartner(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    action = models.CharField(max_length=-1, blank=True, null=True)
    lead = models.ForeignKey(CrmLead, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    force_assignment = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner'


class CrmLead2OpportunityPartnerMass(models.Model):
    lead = models.ForeignKey(CrmLead, models.DO_NOTHING, blank=True, null=True)
    deduplicate = models.BooleanField(blank=True, null=True)
    action = models.CharField(max_length=-1, blank=True, null=True)
    force_assignment = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner_mass'


class CrmLead2OpportunityPartnerMassResUsersRel(models.Model):
    crm_lead2opportunity_partner_mass = models.OneToOneField(CrmLead2OpportunityPartnerMass, models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner_mass_res_users_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'res_users'),)


class CrmLeadCrmLead2OpportunityPartnerMassRel(models.Model):
    crm_lead2opportunity_partner_mass = models.OneToOneField(CrmLead2OpportunityPartnerMass, models.DO_NOTHING, primary_key=True)
    crm_lead = models.ForeignKey(CrmLead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead_crm_lead2opportunity_partner_mass_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'crm_lead'),)


class CrmLeadCrmLead2OpportunityPartnerRel(models.Model):
    crm_lead2opportunity_partner = models.OneToOneField(CrmLead2OpportunityPartner, models.DO_NOTHING, primary_key=True)
    crm_lead = models.ForeignKey(CrmLead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead_crm_lead2opportunity_partner_rel'
        unique_together = (('crm_lead2opportunity_partner', 'crm_lead'),)


class CrmLeadLost(models.Model):
    lost_reason = models.ForeignKey('CrmLostReason', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead_lost'


class CrmLeadScoringFrequency(models.Model):
    variable = models.CharField(max_length=-1, blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    won_count = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lost_count = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead_scoring_frequency'


class CrmLeadScoringFrequencyField(models.Model):
    field = models.ForeignKey('IrModelFields', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead_scoring_frequency_field'


class CrmLostReason(models.Model):
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lost_reason'


class CrmMergeOpportunity(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_merge_opportunity'


class CrmQuotationPartner(models.Model):
    action = models.CharField(max_length=-1)
    lead = models.ForeignKey(CrmLead, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_quotation_partner'


class CrmRecurringPlan(models.Model):
    name = models.CharField(max_length=-1)
    number_of_months = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_recurring_plan'


class CrmStage(models.Model):
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    is_won = models.BooleanField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    fold = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_stage'


class CrmTag(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_tag'


class CrmTagRel(models.Model):
    lead = models.OneToOneField(CrmLead, models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey(CrmTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_tag_rel'
        unique_together = (('lead', 'tag'),)


class CrmTeam(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    use_quotations = models.BooleanField(blank=True, null=True)
    invoiced_target = models.FloatField(blank=True, null=True)
    use_leads = models.BooleanField(blank=True, null=True)
    use_opportunities = models.BooleanField(blank=True, null=True)
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_team'


class DecimalPrecision(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    digits = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decimal_precision'


class DigestDigest(models.Model):
    name = models.CharField(max_length=-1)
    periodicity = models.CharField(max_length=-1)
    next_run_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    kpi_res_users_connected = models.BooleanField(blank=True, null=True)
    kpi_mail_message_total = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    kpi_account_total_revenue = models.BooleanField(blank=True, null=True)
    kpi_all_sale_total = models.BooleanField(blank=True, null=True)
    kpi_crm_lead_created = models.BooleanField(blank=True, null=True)
    kpi_crm_opportunities_won = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digest_digest'


class DigestDigestResUsersRel(models.Model):
    digest_digest = models.OneToOneField(DigestDigest, models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'digest_digest_res_users_rel'
        unique_together = (('digest_digest', 'res_users'),)


class DigestTip(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    tip_description = models.TextField(blank=True, null=True)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digest_tip'


class DigestTipResUsersRel(models.Model):
    digest_tip = models.OneToOneField(DigestTip, models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'digest_tip_res_users_rel'
        unique_together = (('digest_tip', 'res_users'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmailTemplateAttachmentRel(models.Model):
    email_template = models.OneToOneField('MailTemplate', models.DO_NOTHING, primary_key=True)
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_attachment_rel'
        unique_together = (('email_template', 'attachment'),)


class FetchmailServer(models.Model):
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    server = models.CharField(max_length=-1, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    server_type = models.CharField(max_length=-1)
    is_ssl = models.BooleanField(blank=True, null=True)
    attach = models.BooleanField(blank=True, null=True)
    original = models.BooleanField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=-1, blank=True, null=True)
    password = models.CharField(max_length=-1, blank=True, null=True)
    object = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    configuration = models.TextField(blank=True, null=True)
    script = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fetchmail_server'


class IapAccount(models.Model):
    service_name = models.CharField(max_length=-1, blank=True, null=True)
    account_token = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iap_account'


class IapAccountResCompanyRel(models.Model):
    iap_account = models.OneToOneField(IapAccount, models.DO_NOTHING, primary_key=True)
    res_company = models.ForeignKey('ResCompany', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iap_account_res_company_rel'
        unique_together = (('iap_account', 'res_company'),)


class IrActClient(models.Model):
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=-1)
    binding_view_types = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=-1)
    target = models.CharField(max_length=-1, blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    context = models.CharField(max_length=-1)
    params_store = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_client'


class IrActReportXml(models.Model):
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=-1)
    binding_view_types = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=-1)
    report_type = models.CharField(max_length=-1)
    report_name = models.CharField(max_length=-1)
    report_file = models.CharField(max_length=-1, blank=True, null=True)
    multi = models.BooleanField(blank=True, null=True)
    paperformat = models.ForeignKey('ReportPaperformat', models.DO_NOTHING, blank=True, null=True)
    print_report_name = models.CharField(max_length=-1, blank=True, null=True)
    attachment_use = models.BooleanField(blank=True, null=True)
    attachment = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_report_xml'


class IrActServer(models.Model):
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=-1)
    binding_view_types = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING)
    model_name = models.CharField(max_length=-1, blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    crud_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    link_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)
    activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True)
    activity_summary = models.CharField(max_length=-1, blank=True, null=True)
    activity_note = models.TextField(blank=True, null=True)
    activity_date_deadline_range = models.IntegerField(blank=True, null=True)
    activity_date_deadline_range_type = models.CharField(max_length=-1, blank=True, null=True)
    activity_user_type = models.CharField(max_length=-1)
    activity_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    activity_user_field_name = models.CharField(max_length=-1, blank=True, null=True)
    sms_template = models.ForeignKey('SmsTemplate', models.DO_NOTHING, blank=True, null=True)
    sms_mass_keep_log = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_server'


class IrActServerGroupRel(models.Model):
    act = models.OneToOneField(IrActServer, models.DO_NOTHING, primary_key=True)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_server_group_rel'
        unique_together = (('act', 'gid'),)


class IrActServerMailChannelRel(models.Model):
    ir_act_server = models.OneToOneField(IrActServer, models.DO_NOTHING, primary_key=True)
    mail_channel = models.ForeignKey('MailChannel', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_act_server_mail_channel_rel'
        unique_together = (('ir_act_server', 'mail_channel'),)


class IrActServerResPartnerRel(models.Model):
    ir_act_server = models.OneToOneField(IrActServer, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_act_server_res_partner_rel'
        unique_together = (('ir_act_server', 'res_partner'),)


class IrActUrl(models.Model):
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=-1)
    binding_view_types = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    url = models.TextField()
    target = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_act_url'


class IrActWindow(models.Model):
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=-1)
    binding_view_types = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    domain = models.CharField(max_length=-1, blank=True, null=True)
    context = models.CharField(max_length=-1)
    res_id = models.IntegerField(blank=True, null=True)
    res_model = models.CharField(max_length=-1)
    target = models.CharField(max_length=-1, blank=True, null=True)
    view_mode = models.CharField(max_length=-1)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
    search_view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    filter = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_window'


class IrActWindowGroupRel(models.Model):
    act = models.OneToOneField(IrActWindow, models.DO_NOTHING, primary_key=True)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_window_group_rel'
        unique_together = (('act', 'gid'),)


class IrActWindowView(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    view_mode = models.CharField(max_length=-1)
    act_window = models.ForeignKey(IrActWindow, models.DO_NOTHING, blank=True, null=True)
    multi = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_window_view'
        unique_together = (('act_window', 'view_mode'),)


class IrActions(models.Model):
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=-1)
    binding_view_types = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_actions'


class IrActionsTodo(models.Model):
    action_id = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_actions_todo'


class IrAttachment(models.Model):
    name = models.CharField(max_length=-1)
    description = models.TextField(blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    res_field = models.CharField(max_length=-1, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=-1)
    url = models.CharField(max_length=1024, blank=True, null=True)
    public = models.BooleanField(blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    db_datas = models.BinaryField(blank=True, null=True)
    store_fname = models.CharField(max_length=-1, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=40, blank=True, null=True)
    mimetype = models.CharField(max_length=-1, blank=True, null=True)
    index_content = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    original = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_attachment'


class IrConfigParameter(models.Model):
    key = models.CharField(unique=True, max_length=-1)
    value = models.TextField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_config_parameter'


class IrCron(models.Model):
    ir_actions_server = models.ForeignKey(IrActServer, models.DO_NOTHING)
    cron_name = models.CharField(max_length=-1, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    active = models.BooleanField(blank=True, null=True)
    interval_number = models.IntegerField(blank=True, null=True)
    interval_type = models.CharField(max_length=-1, blank=True, null=True)
    numbercall = models.IntegerField(blank=True, null=True)
    doall = models.BooleanField(blank=True, null=True)
    nextcall = models.DateTimeField()
    lastcall = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_cron'


class IrDefault(models.Model):
    field = models.ForeignKey('IrModelFields', models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    condition = models.CharField(max_length=-1, blank=True, null=True)
    json_value = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_default'


class IrDemo(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_demo'


class IrDemoFailure(models.Model):
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING)
    error = models.CharField(max_length=-1, blank=True, null=True)
    wizard = models.ForeignKey('IrDemoFailureWizard', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_demo_failure'


class IrDemoFailureWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_demo_failure_wizard'


class IrExports(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    resource = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports'


class IrExportsLine(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    export = models.ForeignKey(IrExports, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports_line'


class IrFilters(models.Model):
    name = models.CharField(max_length=-1)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    domain = models.TextField()
    context = models.TextField()
    sort = models.TextField()
    model_id = models.CharField(max_length=-1)
    is_default = models.BooleanField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'ir_filters'
        unique_together = (('name', 'model_id', 'user', 'action_id'),)


class IrLogging(models.Model):
    create_uid = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    dbname = models.CharField(max_length=-1, blank=True, null=True)
    level = models.CharField(max_length=-1, blank=True, null=True)
    message = models.TextField()
    path = models.CharField(max_length=-1)
    func = models.CharField(max_length=-1)
    line = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_logging'


class IrMailServer(models.Model):
    name = models.CharField(max_length=-1)
    smtp_host = models.CharField(max_length=-1)
    smtp_port = models.IntegerField()
    smtp_user = models.CharField(max_length=-1, blank=True, null=True)
    smtp_pass = models.CharField(max_length=-1, blank=True, null=True)
    smtp_encryption = models.CharField(max_length=-1)
    smtp_debug = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_mail_server'


class IrModel(models.Model):
    name = models.CharField(max_length=-1)
    model = models.CharField(unique=True, max_length=-1)
    order = models.CharField(max_length=-1)
    info = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    transient = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    is_mail_thread = models.BooleanField(blank=True, null=True)
    is_mail_activity = models.BooleanField(blank=True, null=True)
    is_mail_blacklist = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model'


class IrModelAccess(models.Model):
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    model = models.ForeignKey(IrModel, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True)
    perm_read = models.BooleanField(blank=True, null=True)
    perm_write = models.BooleanField(blank=True, null=True)
    perm_create = models.BooleanField(blank=True, null=True)
    perm_unlink = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_access'


class IrModelConstraint(models.Model):
    name = models.CharField(max_length=-1)
    definition = models.CharField(max_length=-1, blank=True, null=True)
    message = models.CharField(max_length=-1, blank=True, null=True)
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='model')
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_column='module')
    type = models.CharField(max_length=1)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_constraint'
        unique_together = (('name', 'module'),)


class IrModelData(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    noupdate = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    module = models.CharField(max_length=-1)
    model = models.CharField(max_length=-1)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_data'
        unique_together = (('module', 'name'),)


class IrModelFields(models.Model):
    name = models.CharField(max_length=-1)
    complete_name = models.CharField(max_length=-1, blank=True, null=True)
    model = models.CharField(max_length=-1)
    relation = models.CharField(max_length=-1, blank=True, null=True)
    relation_field = models.CharField(max_length=-1, blank=True, null=True)
    relation_field_0 = models.ForeignKey('self', models.DO_NOTHING, db_column='relation_field_id', blank=True, null=True)  # Field renamed because of name conflict.
    model_0 = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='model_id')  # Field renamed because of name conflict.
    field_description = models.CharField(max_length=-1)
    help = models.TextField(blank=True, null=True)
    ttype = models.CharField(max_length=-1)
    copied = models.BooleanField(blank=True, null=True)
    related = models.CharField(max_length=-1, blank=True, null=True)
    related_field = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    required = models.BooleanField(blank=True, null=True)
    readonly = models.BooleanField(blank=True, null=True)
    index = models.BooleanField(blank=True, null=True)
    translate = models.BooleanField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=-1)
    on_delete = models.CharField(max_length=-1, blank=True, null=True)
    domain = models.CharField(max_length=-1, blank=True, null=True)
    group_expand = models.BooleanField(blank=True, null=True)
    selectable = models.BooleanField(blank=True, null=True)
    relation_table = models.CharField(max_length=-1, blank=True, null=True)
    column1 = models.CharField(max_length=-1, blank=True, null=True)
    column2 = models.CharField(max_length=-1, blank=True, null=True)
    compute = models.TextField(blank=True, null=True)
    depends = models.CharField(max_length=-1, blank=True, null=True)
    store = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    tracking = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_fields'
        unique_together = (('model', 'name'),)


class IrModelFieldsGroupRel(models.Model):
    field = models.OneToOneField(IrModelFields, models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_model_fields_group_rel'
        unique_together = (('field', 'group'),)


class IrModelFieldsSelection(models.Model):
    field = models.ForeignKey(IrModelFields, models.DO_NOTHING)
    value = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_fields_selection'
        unique_together = (('field', 'value'),)


class IrModelRelation(models.Model):
    name = models.CharField(max_length=-1)
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='model')
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_column='module')
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_relation'


class IrModuleCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)
    exclusive = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_category'


class IrModuleModule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    website = models.CharField(max_length=-1, blank=True, null=True)
    summary = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    author = models.CharField(max_length=-1, blank=True, null=True)
    icon = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=16, blank=True, null=True)
    latest_version = models.CharField(max_length=-1, blank=True, null=True)
    shortdesc = models.CharField(max_length=-1, blank=True, null=True)
    category = models.ForeignKey(IrModuleCategory, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    application = models.BooleanField(blank=True, null=True)
    demo = models.BooleanField(blank=True, null=True)
    web = models.BooleanField(blank=True, null=True)
    license = models.CharField(max_length=32, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    auto_install = models.BooleanField(blank=True, null=True)
    to_buy = models.BooleanField(blank=True, null=True)
    maintainer = models.CharField(max_length=-1, blank=True, null=True)
    contributors = models.TextField(blank=True, null=True)
    published_version = models.CharField(max_length=-1, blank=True, null=True)
    url = models.CharField(max_length=-1, blank=True, null=True)
    menus_by_module = models.TextField(blank=True, null=True)
    reports_by_module = models.TextField(blank=True, null=True)
    views_by_module = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module'


class IrModuleModuleDependency(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, blank=True, null=True)
    auto_install_required = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module_dependency'


class IrModuleModuleExclusion(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module_exclusion'


class IrProperty(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    res_id = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    fields = models.ForeignKey(IrModelFields, models.DO_NOTHING)
    value_float = models.FloatField(blank=True, null=True)
    value_integer = models.IntegerField(blank=True, null=True)
    value_text = models.TextField(blank=True, null=True)
    value_binary = models.BinaryField(blank=True, null=True)
    value_reference = models.CharField(max_length=-1, blank=True, null=True)
    value_datetime = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'ir_property'


class IrRule(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    model = models.ForeignKey(IrModel, models.DO_NOTHING)
    domain_force = models.TextField(blank=True, null=True)
    perm_read = models.BooleanField(blank=True, null=True)
    perm_write = models.BooleanField(blank=True, null=True)
    perm_create = models.BooleanField(blank=True, null=True)
    perm_unlink = models.BooleanField(blank=True, null=True)
    global_field = models.BooleanField(db_column='global', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_rule'


class IrSequence(models.Model):
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1, blank=True, null=True)
    implementation = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    prefix = models.CharField(max_length=-1, blank=True, null=True)
    suffix = models.CharField(max_length=-1, blank=True, null=True)
    number_next = models.IntegerField()
    number_increment = models.IntegerField()
    padding = models.IntegerField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    use_date_range = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_sequence'


class IrSequenceDateRange(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()
    sequence = models.ForeignKey(IrSequence, models.DO_NOTHING)
    number_next = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_sequence_date_range'


class IrServerObjectLines(models.Model):
    server = models.ForeignKey(IrActServer, models.DO_NOTHING, blank=True, null=True)
    col1 = models.ForeignKey(IrModelFields, models.DO_NOTHING, db_column='col1')
    value = models.TextField()
    evaluation_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_server_object_lines'


class IrTranslation(models.Model):
    name = models.CharField(max_length=-1)
    res_id = models.IntegerField(blank=True, null=True)
    lang = models.ForeignKey('ResLang', models.DO_NOTHING, db_column='lang', blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    src = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    module = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'ir_translation'
        unique_together = (('type', 'lang'), ('type', 'lang', 'name', 'res_id'), ('type', 'name', 'lang', 'res_id'),)


class IrUiMenu(models.Model):
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    web_icon = models.CharField(max_length=-1, blank=True, null=True)
    action = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_menu'


class IrUiMenuGroupRel(models.Model):
    menu = models.OneToOneField(IrUiMenu, models.DO_NOTHING, primary_key=True)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_ui_menu_group_rel'
        unique_together = (('menu', 'gid'),)


class IrUiView(models.Model):
    name = models.CharField(max_length=-1)
    model = models.CharField(max_length=-1, blank=True, null=True)
    key = models.CharField(max_length=-1, blank=True, null=True)
    priority = models.IntegerField()
    type = models.CharField(max_length=-1, blank=True, null=True)
    arch_db = models.TextField(blank=True, null=True)
    arch_fs = models.CharField(max_length=-1, blank=True, null=True)
    arch_updated = models.BooleanField(blank=True, null=True)
    arch_prev = models.TextField(blank=True, null=True)
    inherit = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    field_parent = models.CharField(max_length=-1, blank=True, null=True)
    mode = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    customize_show = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_view'


class IrUiViewCustom(models.Model):
    ref = models.ForeignKey(IrUiView, models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    arch = models.TextField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_view_custom'


class IrUiViewGroupRel(models.Model):
    view = models.OneToOneField(IrUiView, models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_ui_view_group_rel'
        unique_together = (('view', 'group'),)


class JournalAccountControlRel(models.Model):
    journal = models.OneToOneField(AccountJournal, models.DO_NOTHING, primary_key=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'journal_account_control_rel'
        unique_together = (('journal', 'account'),)


class JournalAccountTypeControlRel(models.Model):
    journal = models.OneToOneField(AccountJournal, models.DO_NOTHING, primary_key=True)
    type = models.ForeignKey(AccountAccountType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'journal_account_type_control_rel'
        unique_together = (('journal', 'type'),)


class MailActivity(models.Model):
    res_model = models.ForeignKey(IrModel, models.DO_NOTHING)
    res_model_0 = models.CharField(db_column='res_model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    res_id = models.IntegerField()
    res_name = models.CharField(max_length=-1, blank=True, null=True)
    activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True)
    summary = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    date_deadline = models.DateField()
    automated = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    request_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    recommended_activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True)
    previous_activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    calendar_event = models.ForeignKey(CalendarEvent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_activity'


class MailActivityRel(models.Model):
    activity = models.OneToOneField('MailActivityType', models.DO_NOTHING, primary_key=True)
    recommended = models.ForeignKey('MailActivityType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_activity_rel'
        unique_together = (('activity', 'recommended'),)


class MailActivityType(models.Model):
    name = models.CharField(max_length=-1)
    summary = models.CharField(max_length=-1, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    delay_count = models.IntegerField(blank=True, null=True)
    delay_unit = models.CharField(max_length=-1)
    delay_from = models.CharField(max_length=-1)
    icon = models.CharField(max_length=-1, blank=True, null=True)
    decoration_type = models.CharField(max_length=-1, blank=True, null=True)
    res_model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)
    default_next_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    force_next = models.BooleanField(blank=True, null=True)
    category = models.CharField(max_length=-1, blank=True, null=True)
    default_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    default_description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_activity_type'


class MailActivityTypeMailTemplateRel(models.Model):
    mail_activity_type = models.OneToOneField(MailActivityType, models.DO_NOTHING, primary_key=True)
    mail_template = models.ForeignKey('MailTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_activity_type_mail_template_rel'
        unique_together = (('mail_activity_type', 'mail_template'),)


class MailAlias(models.Model):
    alias_name = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    alias_model = models.ForeignKey(IrModel, models.DO_NOTHING)
    alias_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    alias_defaults = models.TextField()
    alias_force_thread_id = models.IntegerField(blank=True, null=True)
    alias_parent_model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)
    alias_parent_thread_id = models.IntegerField(blank=True, null=True)
    alias_contact = models.CharField(max_length=-1)
    alias_bounced_content = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_alias'


class MailBlacklist(models.Model):
    email = models.CharField(unique=True, max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_blacklist'


class MailBlacklistRemove(models.Model):
    email = models.CharField(max_length=-1)
    reason = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_blacklist_remove'


class MailChannel(models.Model):
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    channel_type = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)
    email_send = models.BooleanField(blank=True, null=True)
    public = models.CharField(max_length=-1)
    group_public = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True)
    moderation = models.BooleanField(blank=True, null=True)
    moderation_notify = models.BooleanField(blank=True, null=True)
    moderation_notify_msg = models.TextField(blank=True, null=True)
    moderation_guidelines = models.BooleanField(blank=True, null=True)
    moderation_guidelines_msg = models.TextField(blank=True, null=True)
    alias = models.ForeignKey(MailAlias, models.DO_NOTHING)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel'


class MailChannelMailWizardInviteRel(models.Model):
    mail_wizard_invite = models.OneToOneField('MailWizardInvite', models.DO_NOTHING, primary_key=True)
    mail_channel = models.ForeignKey(MailChannel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_channel_mail_wizard_invite_rel'
        unique_together = (('mail_wizard_invite', 'mail_channel'),)


class MailChannelModeratorRel(models.Model):
    mail_channel = models.OneToOneField(MailChannel, models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_channel_moderator_rel'
        unique_together = (('mail_channel', 'res_users'),)


class MailChannelPartner(models.Model):
    custom_channel_name = models.CharField(max_length=-1, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    channel = models.ForeignKey(MailChannel, models.DO_NOTHING, blank=True, null=True)
    fetched_message = models.ForeignKey('MailMessage', models.DO_NOTHING, blank=True, null=True)
    seen_message = models.ForeignKey('MailMessage', models.DO_NOTHING, blank=True, null=True)
    fold_state = models.CharField(max_length=-1, blank=True, null=True)
    is_minimized = models.BooleanField(blank=True, null=True)
    is_pinned = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel_partner'


class MailChannelResGroupsRel(models.Model):
    mail_channel = models.OneToOneField(MailChannel, models.DO_NOTHING, primary_key=True)
    res_groups = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_channel_res_groups_rel'
        unique_together = (('mail_channel', 'res_groups'),)


class MailComposeMessage(models.Model):
    subject = models.CharField(max_length=-1, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('MailMessage', models.DO_NOTHING, blank=True, null=True)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)
    layout = models.CharField(max_length=-1, blank=True, null=True)
    add_sign = models.BooleanField(blank=True, null=True)
    email_from = models.CharField(max_length=-1, blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    composition_mode = models.CharField(max_length=-1, blank=True, null=True)
    model = models.CharField(max_length=-1, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    record_name = models.CharField(max_length=-1, blank=True, null=True)
    use_active_domain = models.BooleanField(blank=True, null=True)
    active_domain = models.TextField(blank=True, null=True)
    message_type = models.CharField(max_length=-1)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, blank=True, null=True)
    mail_activity_type = models.ForeignKey(MailActivityType, models.DO_NOTHING, blank=True, null=True)
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    no_auto_thread = models.BooleanField(blank=True, null=True)
    is_log = models.BooleanField(blank=True, null=True)
    notify = models.BooleanField(blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    auto_delete_message = models.BooleanField(blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_compose_message'


class MailComposeMessageIrAttachmentsRel(models.Model):
    wizard = models.OneToOneField(MailComposeMessage, models.DO_NOTHING, primary_key=True)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_ir_attachments_rel'
        unique_together = (('wizard', 'attachment'),)


class MailComposeMessageResPartnerRel(models.Model):
    wizard = models.OneToOneField(MailComposeMessage, models.DO_NOTHING, primary_key=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_res_partner_rel'
        unique_together = (('wizard', 'partner'),)


class MailFollowers(models.Model):
    res_model = models.CharField(max_length=-1)
    res_id = models.IntegerField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    channel = models.ForeignKey(MailChannel, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_followers'
        unique_together = (('res_model', 'res_id', 'channel'), ('res_model', 'res_id', 'partner'),)


class MailFollowersMailMessageSubtypeRel(models.Model):
    mail_followers = models.OneToOneField(MailFollowers, models.DO_NOTHING, primary_key=True)
    mail_message_subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_followers_mail_message_subtype_rel'
        unique_together = (('mail_followers', 'mail_message_subtype'),)


class MailMail(models.Model):
    mail_message = models.ForeignKey('MailMessage', models.DO_NOTHING)
    body_html = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    notification = models.BooleanField(blank=True, null=True)
    email_to = models.TextField(blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    scheduled_date = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    fetchmail_server = models.ForeignKey(FetchmailServer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mail'


class MailMailResPartnerRel(models.Model):
    mail_mail = models.OneToOneField(MailMail, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_mail_res_partner_rel'
        unique_together = (('mail_mail', 'res_partner'),)


class MailMessage(models.Model):
    subject = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    model = models.CharField(max_length=-1, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    record_name = models.CharField(max_length=-1, blank=True, null=True)
    message_type = models.CharField(max_length=-1)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, blank=True, null=True)
    mail_activity_type = models.ForeignKey(MailActivityType, models.DO_NOTHING, blank=True, null=True)
    is_internal = models.BooleanField(blank=True, null=True)
    email_from = models.CharField(max_length=-1, blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    no_auto_thread = models.BooleanField(blank=True, null=True)
    message_id = models.CharField(max_length=-1, blank=True, null=True)
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    moderation_status = models.CharField(max_length=-1, blank=True, null=True)
    moderator = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    email_layout_xmlid = models.CharField(max_length=-1, blank=True, null=True)
    add_sign = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message'


class MailMessageMailChannelRel(models.Model):
    mail_message = models.OneToOneField(MailMessage, models.DO_NOTHING, primary_key=True)
    mail_channel = models.ForeignKey(MailChannel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_mail_channel_rel'
        unique_together = (('mail_message', 'mail_channel'),)


class MailMessageResPartnerNeedactionRel(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    mail = models.ForeignKey(MailMail, models.DO_NOTHING, blank=True, null=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    notification_type = models.CharField(max_length=-1)
    notification_status = models.CharField(max_length=-1, blank=True, null=True)
    is_read = models.BooleanField(blank=True, null=True)
    read_date = models.DateTimeField(blank=True, null=True)
    failure_type = models.CharField(max_length=-1, blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    sms = models.ForeignKey('SmsSms', models.DO_NOTHING, blank=True, null=True)
    sms_number = models.CharField(max_length=-1, blank=True, null=True)
    letter = models.ForeignKey('SnailmailLetter', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_needaction_rel'


class MailMessageResPartnerNeedactionRelMailResendMessageRel(models.Model):
    mail_resend_message = models.OneToOneField('MailResendMessage', models.DO_NOTHING, primary_key=True)
    mail_message_res_partner_needaction_rel = models.ForeignKey(MailMessageResPartnerNeedactionRel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_needaction_rel_mail_resend_message_rel'
        unique_together = (('mail_resend_message', 'mail_message_res_partner_needaction_rel'),)


class MailMessageResPartnerRel(models.Model):
    mail_message = models.OneToOneField(MailMessage, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageResPartnerStarredRel(models.Model):
    mail_message = models.OneToOneField(MailMessage, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_starred_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageSubtype(models.Model):
    name = models.CharField(max_length=-1)
    description = models.TextField(blank=True, null=True)
    internal = models.BooleanField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    relation_field = models.CharField(max_length=-1, blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    default = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    hidden = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message_subtype'


class MailModeration(models.Model):
    email = models.CharField(max_length=-1)
    status = models.CharField(max_length=-1)
    channel = models.ForeignKey(MailChannel, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_moderation'
        unique_together = (('email', 'channel'),)


class MailResendCancel(models.Model):
    model = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_resend_cancel'


class MailResendMessage(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_resend_message'


class MailResendPartner(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    resend = models.BooleanField(blank=True, null=True)
    resend_wizard = models.ForeignKey(MailResendMessage, models.DO_NOTHING, blank=True, null=True)
    message = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_resend_partner'


class MailShortcode(models.Model):
    source = models.CharField(max_length=-1)
    substitution = models.TextField()
    description = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_shortcode'


class MailTemplate(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    subject = models.CharField(max_length=-1, blank=True, null=True)
    email_from = models.CharField(max_length=-1, blank=True, null=True)
    use_default_to = models.BooleanField(blank=True, null=True)
    email_to = models.CharField(max_length=-1, blank=True, null=True)
    partner_to = models.CharField(max_length=-1, blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    report_name = models.CharField(max_length=-1, blank=True, null=True)
    report_template = models.ForeignKey(IrActReportXml, models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    scheduled_date = models.CharField(max_length=-1, blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    ref_ir_act_window = models.ForeignKey(IrActWindow, models.DO_NOTHING, db_column='ref_ir_act_window', blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_template'


class MailTemplatePreview(models.Model):
    mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING)
    resource_ref = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    error_msg = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_template_preview'


class MailTrackingValue(models.Model):
    field = models.ForeignKey(IrModelFields, models.DO_NOTHING, db_column='field')
    field_desc = models.CharField(max_length=-1)
    field_type = models.CharField(max_length=-1, blank=True, null=True)
    old_value_integer = models.IntegerField(blank=True, null=True)
    old_value_float = models.FloatField(blank=True, null=True)
    old_value_monetary = models.FloatField(blank=True, null=True)
    old_value_char = models.CharField(max_length=-1, blank=True, null=True)
    old_value_text = models.TextField(blank=True, null=True)
    old_value_datetime = models.DateTimeField(blank=True, null=True)
    new_value_integer = models.IntegerField(blank=True, null=True)
    new_value_float = models.FloatField(blank=True, null=True)
    new_value_monetary = models.FloatField(blank=True, null=True)
    new_value_char = models.CharField(max_length=-1, blank=True, null=True)
    new_value_text = models.TextField(blank=True, null=True)
    new_value_datetime = models.DateTimeField(blank=True, null=True)
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    tracking_sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_tracking_value'


class MailWizardInvite(models.Model):
    res_model = models.CharField(max_length=-1)
    res_id = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    send_mail = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite'


class MailWizardInviteResPartnerRel(models.Model):
    mail_wizard_invite = models.OneToOneField(MailWizardInvite, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite_res_partner_rel'
        unique_together = (('mail_wizard_invite', 'res_partner'),)


class MeetingCategoryRel(models.Model):
    event = models.OneToOneField(CalendarEvent, models.DO_NOTHING, primary_key=True)
    type = models.ForeignKey(CalendarEventType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'meeting_category_rel'
        unique_together = (('event', 'type'),)


class MergeOpportunityRel(models.Model):
    merge = models.OneToOneField(CrmMergeOpportunity, models.DO_NOTHING, primary_key=True)
    opportunity = models.ForeignKey(CrmLead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'merge_opportunity_rel'
        unique_together = (('merge', 'opportunity'),)


class MessageAttachmentRel(models.Model):
    message = models.OneToOneField(MailMessage, models.DO_NOTHING, primary_key=True)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'message_attachment_rel'
        unique_together = (('message', 'attachment'),)


class PaymentAcquirer(models.Model):
    name = models.CharField(max_length=-1)
    color = models.IntegerField(blank=True, null=True)
    display_as = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    provider = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    view_template = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    registration_view_template = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1)
    capture_manually = models.BooleanField(blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    check_validity = models.BooleanField(blank=True, null=True)
    pre_msg = models.TextField(blank=True, null=True)
    auth_msg = models.TextField(blank=True, null=True)
    pending_msg = models.TextField(blank=True, null=True)
    done_msg = models.TextField(blank=True, null=True)
    cancel_msg = models.TextField(blank=True, null=True)
    save_token = models.CharField(max_length=-1, blank=True, null=True)
    fees_active = models.BooleanField(blank=True, null=True)
    fees_dom_fixed = models.FloatField(blank=True, null=True)
    fees_dom_var = models.FloatField(blank=True, null=True)
    fees_int_fixed = models.FloatField(blank=True, null=True)
    fees_int_var = models.FloatField(blank=True, null=True)
    qr_code = models.BooleanField(blank=True, null=True)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, blank=True, null=True)
    module_state = models.CharField(max_length=-1, blank=True, null=True)
    payment_flow = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    so_reference_type = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_acquirer'


class PaymentAcquirerOnboardingWizard(models.Model):
    payment_method = models.CharField(max_length=-1, blank=True, null=True)
    paypal_user_type = models.CharField(max_length=-1, blank=True, null=True)
    paypal_email_account = models.CharField(max_length=-1, blank=True, null=True)
    paypal_seller_account = models.CharField(max_length=-1, blank=True, null=True)
    paypal_pdt_token = models.CharField(max_length=-1, blank=True, null=True)
    stripe_secret_key = models.CharField(max_length=-1, blank=True, null=True)
    stripe_publishable_key = models.CharField(max_length=-1, blank=True, null=True)
    manual_name = models.CharField(max_length=-1, blank=True, null=True)
    journal_name = models.CharField(max_length=-1, blank=True, null=True)
    acc_number = models.CharField(max_length=-1, blank=True, null=True)
    manual_post_msg = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_acquirer_onboarding_wizard'


class PaymentAcquirerPaymentIconRel(models.Model):
    payment_acquirer = models.OneToOneField(PaymentAcquirer, models.DO_NOTHING, primary_key=True)
    payment_icon = models.ForeignKey('PaymentIcon', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_acquirer_payment_icon_rel'
        unique_together = (('payment_acquirer', 'payment_icon'),)


class PaymentCountryRel(models.Model):
    payment = models.OneToOneField(PaymentAcquirer, models.DO_NOTHING, primary_key=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_country_rel'
        unique_together = (('payment', 'country'),)


class PaymentIcon(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_icon'


class PaymentLinkWizard(models.Model):
    res_model = models.CharField(max_length=-1)
    res_id = models.IntegerField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    amount_max = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_link_wizard'


class PaymentToken(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    acquirer = models.ForeignKey(PaymentAcquirer, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    acquirer_ref = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    verified = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_token'


class PaymentTransaction(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    acquirer = models.ForeignKey(PaymentAcquirer, models.DO_NOTHING)
    type = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    state_message = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    fees = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    reference = models.CharField(unique=True, max_length=-1)
    acquirer_reference = models.CharField(max_length=-1, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    partner_lang = models.CharField(max_length=-1, blank=True, null=True)
    partner_email = models.CharField(max_length=-1, blank=True, null=True)
    partner_zip = models.CharField(max_length=-1, blank=True, null=True)
    partner_address = models.CharField(max_length=-1, blank=True, null=True)
    partner_city = models.CharField(max_length=-1, blank=True, null=True)
    partner_country = models.ForeignKey('ResCountry', models.DO_NOTHING)
    partner_phone = models.CharField(max_length=-1, blank=True, null=True)
    html_3ds = models.CharField(max_length=-1, blank=True, null=True)
    callback_model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)
    callback_res_id = models.IntegerField(blank=True, null=True)
    callback_method = models.CharField(max_length=-1, blank=True, null=True)
    callback_hash = models.CharField(max_length=-1, blank=True, null=True)
    return_url = models.CharField(max_length=-1, blank=True, null=True)
    is_processed = models.BooleanField(blank=True, null=True)
    payment_token = models.ForeignKey(PaymentToken, models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey(AccountPayment, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_transaction'


class PhoneBlacklist(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    number = models.CharField(unique=True, max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone_blacklist'


class PhoneBlacklistRemove(models.Model):
    phone = models.CharField(max_length=-1)
    reason = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone_blacklist_remove'


class PortalShare(models.Model):
    res_model = models.CharField(max_length=-1)
    res_id = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_share'


class PortalShareResPartnerRel(models.Model):
    portal_share = models.OneToOneField(PortalShare, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portal_share_res_partner_rel'
        unique_together = (('portal_share', 'res_partner'),)


class PortalWizard(models.Model):
    welcome_message = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_wizard'


class PortalWizardUser(models.Model):
    wizard = models.ForeignKey(PortalWizard, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    email = models.CharField(max_length=-1, blank=True, null=True)
    in_portal = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_wizard_user'


class ProcurementGroup(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    move_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_group'


class ProductAttrExclusionValueIdsRel(models.Model):
    product_template_attribute_exclusion = models.OneToOneField('ProductTemplateAttributeExclusion', models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attr_exclusion_value_ids_rel'
        unique_together = (('product_template_attribute_exclusion', 'product_template_attribute_value'),)


class ProductAttribute(models.Model):
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    create_variant = models.CharField(max_length=-1)
    display_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute'


class ProductAttributeCustomValue(models.Model):
    custom_product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING)
    custom_value = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_order_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_custom_value'
        unique_together = (('custom_product_template_attribute_value', 'sale_order_line'),)


class ProductAttributeProductTemplateRel(models.Model):
    product_attribute = models.OneToOneField(ProductAttribute, models.DO_NOTHING, primary_key=True)
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_product_template_rel'
        unique_together = (('product_attribute', 'product_template'),)


class ProductAttributeValue(models.Model):
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING)
    is_custom = models.BooleanField(blank=True, null=True)
    html_color = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute_value'
        unique_together = (('name', 'attribute'),)


class ProductAttributeValueProductTemplateAttributeLineRel(models.Model):
    product_attribute_value = models.OneToOneField(ProductAttributeValue, models.DO_NOTHING, primary_key=True)
    product_template_attribute_line = models.ForeignKey('ProductTemplateAttributeLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_value_product_template_attribute_line_rel'
        unique_together = (('product_attribute_value', 'product_template_attribute_line'),)


class ProductCategory(models.Model):
    name = models.CharField(max_length=-1)
    complete_name = models.CharField(max_length=-1, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    removal_strategy = models.ForeignKey('ProductRemoval', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductPackaging(models.Model):
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    barcode = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_packaging'


class ProductPricelist(models.Model):
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    discount_policy = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pricelist'


class ProductPricelistItem(models.Model):
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    min_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    applied_on = models.CharField(max_length=-1)
    base = models.CharField(max_length=-1)
    base_pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING, blank=True, null=True)
    pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING)
    price_surcharge = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_round = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_min_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_max_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    compute_price = models.CharField(max_length=-1)
    fixed_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    percent_price = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pricelist_item'


class ProductProduct(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    default_code = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    barcode = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    combination_indices = models.CharField(max_length=-1, blank=True, null=True)
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    can_image_variant_1024_be_zoomed = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_product'
        unique_together = (('product_tmpl', 'combination_indices'),)


class ProductProductStockInventoryRel(models.Model):
    stock_inventory = models.OneToOneField('StockInventory', models.DO_NOTHING, primary_key=True)
    product_product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_product_stock_inventory_rel'
        unique_together = (('stock_inventory', 'product_product'),)


class ProductRemoval(models.Model):
    name = models.CharField(max_length=-1)
    method = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_removal'


class ProductReplenish(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    product_has_variants = models.BooleanField()
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    quantity = models.FloatField()
    date_planned = models.DateTimeField()
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_replenish'


class ProductReplenishStockLocationRouteRel(models.Model):
    product_replenish = models.OneToOneField(ProductReplenish, models.DO_NOTHING, primary_key=True)
    stock_location_route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_replenish_stock_location_route_rel'
        unique_together = (('product_replenish', 'stock_location_route'),)


class ProductSupplierTaxesRel(models.Model):
    prod = models.OneToOneField('ProductTemplate', models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_supplier_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductSupplierinfo(models.Model):
    name = models.ForeignKey('ResPartner', models.DO_NOTHING, db_column='name')
    product_name = models.CharField(max_length=-1, blank=True, null=True)
    product_code = models.CharField(max_length=-1, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    min_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, blank=True, null=True)
    delay = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_supplierinfo'


class ProductTaxesRel(models.Model):
    prod = models.OneToOneField('ProductTemplate', models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductTemplate(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_purchase = models.TextField(blank=True, null=True)
    description_sale = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING)
    list_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sale_ok = models.BooleanField(blank=True, null=True)
    purchase_ok = models.BooleanField(blank=True, null=True)
    uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    uom_po = models.ForeignKey('UomUom', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    default_code = models.CharField(max_length=-1, blank=True, null=True)
    can_image_1024_be_zoomed = models.BooleanField(blank=True, null=True)
    has_configurable_attributes = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    service_type = models.CharField(max_length=-1, blank=True, null=True)
    sale_line_warn = models.CharField(max_length=-1)
    sale_line_warn_msg = models.TextField(blank=True, null=True)
    expense_policy = models.CharField(max_length=-1, blank=True, null=True)
    invoice_policy = models.CharField(max_length=-1, blank=True, null=True)
    sale_delay = models.FloatField(blank=True, null=True)
    tracking = models.CharField(max_length=-1)
    description_picking = models.TextField(blank=True, null=True)
    description_pickingout = models.TextField(blank=True, null=True)
    description_pickingin = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template'


class ProductTemplateAttributeExclusion(models.Model):
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING, blank=True, null=True)
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_exclusion'


class ProductTemplateAttributeLine(models.Model):
    active = models.BooleanField(blank=True, null=True)
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING)
    attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_line'


class ProductTemplateAttributeValue(models.Model):
    ptav_active = models.BooleanField(blank=True, null=True)
    product_attribute_value = models.ForeignKey(ProductAttributeValue, models.DO_NOTHING)
    attribute_line = models.ForeignKey(ProductTemplateAttributeLine, models.DO_NOTHING)
    price_extra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING, blank=True, null=True)
    attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_value'
        unique_together = (('attribute_line', 'product_attribute_value'),)


class ProductTemplateAttributeValueSaleOrderLineRel(models.Model):
    sale_order_line = models.OneToOneField('SaleOrderLine', models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey(ProductTemplateAttributeValue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_value_sale_order_line_rel'
        unique_together = (('sale_order_line', 'product_template_attribute_value'),)


class ProductVariantCombination(models.Model):
    product_product = models.OneToOneField(ProductProduct, models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey(ProductTemplateAttributeValue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_variant_combination'
        unique_together = (('product_product', 'product_template_attribute_value'),)


class RelModulesLangexport(models.Model):
    wiz = models.OneToOneField(BaseLanguageExport, models.DO_NOTHING, primary_key=True)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rel_modules_langexport'
        unique_together = (('wiz', 'module'),)


class RelServerActions(models.Model):
    server = models.OneToOneField(IrActServer, models.DO_NOTHING, primary_key=True)
    action = models.ForeignKey(IrActServer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rel_server_actions'
        unique_together = (('server', 'action'),)


class ReportLayout(models.Model):
    view = models.ForeignKey(IrUiView, models.DO_NOTHING)
    image = models.CharField(max_length=-1, blank=True, null=True)
    pdf = models.CharField(max_length=-1, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_layout'


class ReportPaperformat(models.Model):
    name = models.CharField(max_length=-1)
    default = models.BooleanField(blank=True, null=True)
    format = models.CharField(max_length=-1, blank=True, null=True)
    margin_top = models.FloatField(blank=True, null=True)
    margin_bottom = models.FloatField(blank=True, null=True)
    margin_left = models.FloatField(blank=True, null=True)
    margin_right = models.FloatField(blank=True, null=True)
    page_height = models.IntegerField(blank=True, null=True)
    page_width = models.IntegerField(blank=True, null=True)
    orientation = models.CharField(max_length=-1, blank=True, null=True)
    header_line = models.BooleanField(blank=True, null=True)
    header_spacing = models.IntegerField(blank=True, null=True)
    dpi = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_paperformat'


class ResBank(models.Model):
    name = models.CharField(max_length=-1)
    street = models.CharField(max_length=-1, blank=True, null=True)
    street2 = models.CharField(max_length=-1, blank=True, null=True)
    zip = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, db_column='state', blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, db_column='country', blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    bic = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    l10n_mx_edi_code = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_bank'


class ResCompany(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    report_header = models.TextField(blank=True, null=True)
    report_footer = models.TextField(blank=True, null=True)
    logo_web = models.BinaryField(blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    company_registry = models.CharField(max_length=-1, blank=True, null=True)
    paperformat = models.ForeignKey(ReportPaperformat, models.DO_NOTHING, blank=True, null=True)
    external_report_layout = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    base_onboarding_company_state = models.CharField(max_length=-1, blank=True, null=True)
    font = models.CharField(max_length=-1, blank=True, null=True)
    primary_color = models.CharField(max_length=-1, blank=True, null=True)
    secondary_color = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True)
    partner_gid = models.IntegerField(blank=True, null=True)
    snailmail_color = models.BooleanField(blank=True, null=True)
    snailmail_cover = models.BooleanField(blank=True, null=True)
    snailmail_duplex = models.BooleanField(blank=True, null=True)
    fiscalyear_last_day = models.IntegerField()
    fiscalyear_last_month = models.CharField(max_length=-1)
    period_lock_date = models.DateField(blank=True, null=True)
    fiscalyear_lock_date = models.DateField(blank=True, null=True)
    tax_lock_date = models.DateField(blank=True, null=True)
    transfer_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    expects_chart_of_accounts = models.BooleanField(blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING, blank=True, null=True)
    bank_account_code_prefix = models.CharField(max_length=-1, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=-1, blank=True, null=True)
    default_cash_difference_income_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    default_cash_difference_expense_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    account_journal_suspense_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    transfer_account_code_prefix = models.CharField(max_length=-1, blank=True, null=True)
    account_sale_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, blank=True, null=True)
    account_purchase_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, blank=True, null=True)
    tax_calculation_rounding_method = models.CharField(max_length=-1, blank=True, null=True)
    currency_exchange_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    income_currency_exchange_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    expense_currency_exchange_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    anglo_saxon_accounting = models.BooleanField(blank=True, null=True)
    property_stock_account_input_categ = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    property_stock_account_output_categ = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    property_stock_valuation_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    tax_exigibility = models.BooleanField(blank=True, null=True)
    account_tax_fiscal_country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    incoterm = models.ForeignKey(AccountIncoterms, models.DO_NOTHING, blank=True, null=True)
    qr_code = models.BooleanField(blank=True, null=True)
    invoice_is_email = models.BooleanField(blank=True, null=True)
    invoice_is_print = models.BooleanField(blank=True, null=True)
    account_opening_move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True)
    account_opening_date = models.DateField()
    account_setup_bank_data_state = models.CharField(max_length=-1, blank=True, null=True)
    account_setup_fy_data_state = models.CharField(max_length=-1, blank=True, null=True)
    account_setup_coa_state = models.CharField(max_length=-1, blank=True, null=True)
    account_onboarding_invoice_layout_state = models.CharField(max_length=-1, blank=True, null=True)
    account_onboarding_create_invoice_state = models.CharField(max_length=-1, blank=True, null=True)
    account_onboarding_sale_tax_state = models.CharField(max_length=-1, blank=True, null=True)
    account_invoice_onboarding_state = models.CharField(max_length=-1, blank=True, null=True)
    account_dashboard_onboarding_state = models.CharField(max_length=-1, blank=True, null=True)
    invoice_terms = models.TextField(blank=True, null=True)
    account_setup_bill_state = models.CharField(max_length=-1, blank=True, null=True)
    account_default_pos_receivable_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    expense_accrual_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    revenue_accrual_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    automatic_entry_default_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    tax_cash_basis_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    account_cash_basis_base_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    payment_acquirer_onboarding_state = models.CharField(max_length=-1, blank=True, null=True)
    payment_onboarding_payment_method = models.CharField(max_length=-1, blank=True, null=True)
    invoice_is_snailmail = models.BooleanField(blank=True, null=True)
    portal_confirmation_sign = models.BooleanField(blank=True, null=True)
    portal_confirmation_pay = models.BooleanField(blank=True, null=True)
    quotation_validity_days = models.IntegerField(blank=True, null=True)
    sale_quotation_onboarding_state = models.CharField(max_length=-1, blank=True, null=True)
    sale_onboarding_order_confirmation_state = models.CharField(max_length=-1, blank=True, null=True)
    sale_onboarding_sample_quotation_state = models.CharField(max_length=-1, blank=True, null=True)
    sale_onboarding_payment_method = models.CharField(max_length=-1, blank=True, null=True)
    sale_order_template = models.ForeignKey('SaleOrderTemplate', models.DO_NOTHING, blank=True, null=True)
    vat_check_vies = models.BooleanField(blank=True, null=True)
    nomenclature = models.ForeignKey(BarcodeNomenclature, models.DO_NOTHING, blank=True, null=True)
    internal_transit_location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    stock_move_email_validation = models.BooleanField(blank=True, null=True)
    stock_mail_confirmation_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    stock_move_sms_validation = models.BooleanField(blank=True, null=True)
    stock_sms_confirmation_template = models.ForeignKey('SmsTemplate', models.DO_NOTHING, blank=True, null=True)
    has_received_warning_stock_sms = models.BooleanField(blank=True, null=True)
    security_lead = models.FloatField()

    class Meta:
        managed = False
        db_table = 'res_company'


class ResCompanyUsersRel(models.Model):
    cid = models.OneToOneField(ResCompany, models.DO_NOTHING, db_column='cid', primary_key=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_company_users_rel'
        unique_together = (('cid', 'user'),)


class ResConfig(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config'


class ResConfigInstaller(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config_installer'


class ResConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    user_default_rights = models.BooleanField(blank=True, null=True)
    external_email_server_default = models.BooleanField(blank=True, null=True)
    module_base_import = models.BooleanField(blank=True, null=True)
    module_google_calendar = models.BooleanField(blank=True, null=True)
    module_microsoft_calendar = models.BooleanField(blank=True, null=True)
    module_google_drive = models.BooleanField(blank=True, null=True)
    module_google_spreadsheet = models.BooleanField(blank=True, null=True)
    module_auth_oauth = models.BooleanField(blank=True, null=True)
    module_auth_ldap = models.BooleanField(blank=True, null=True)
    module_base_gengo = models.BooleanField(blank=True, null=True)
    module_account_inter_company_rules = models.BooleanField(blank=True, null=True)
    module_pad = models.BooleanField(blank=True, null=True)
    module_voip = models.BooleanField(blank=True, null=True)
    module_web_unsplash = models.BooleanField(blank=True, null=True)
    module_partner_autocomplete = models.BooleanField(blank=True, null=True)
    module_base_geolocalize = models.BooleanField(blank=True, null=True)
    module_google_recaptcha = models.BooleanField(blank=True, null=True)
    group_multi_currency = models.BooleanField(blank=True, null=True)
    show_effect = models.BooleanField(blank=True, null=True)
    fail_counter = models.IntegerField(blank=True, null=True)
    alias_domain = models.CharField(max_length=-1, blank=True, null=True)
    unsplash_access_key = models.CharField(max_length=-1, blank=True, null=True)
    auth_signup_reset_password = models.BooleanField(blank=True, null=True)
    auth_signup_uninvited = models.CharField(max_length=-1, blank=True, null=True)
    auth_signup_template_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    group_discount_per_so_line = models.BooleanField(blank=True, null=True)
    group_uom = models.BooleanField(blank=True, null=True)
    group_product_variant = models.BooleanField(blank=True, null=True)
    module_sale_product_configurator = models.BooleanField(blank=True, null=True)
    module_sale_product_matrix = models.BooleanField(blank=True, null=True)
    group_stock_packaging = models.BooleanField(blank=True, null=True)
    group_product_pricelist = models.BooleanField(blank=True, null=True)
    group_sale_pricelist = models.BooleanField(blank=True, null=True)
    product_pricelist_setting = models.CharField(max_length=-1, blank=True, null=True)
    product_weight_in_lbs = models.CharField(max_length=-1, blank=True, null=True)
    product_volume_volume_in_cubic_feet = models.CharField(max_length=-1, blank=True, null=True)
    digest_emails = models.BooleanField(blank=True, null=True)
    digest = models.ForeignKey(DigestDigest, models.DO_NOTHING, blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING, blank=True, null=True)
    module_account_accountant = models.BooleanField(blank=True, null=True)
    group_analytic_accounting = models.BooleanField(blank=True, null=True)
    group_analytic_tags = models.BooleanField(blank=True, null=True)
    group_warning_account = models.BooleanField(blank=True, null=True)
    group_cash_rounding = models.BooleanField(blank=True, null=True)
    group_show_line_subtotals_tax_excluded = models.BooleanField(blank=True, null=True)
    group_show_line_subtotals_tax_included = models.BooleanField(blank=True, null=True)
    group_show_sale_receipts = models.BooleanField(blank=True, null=True)
    group_show_purchase_receipts = models.BooleanField(blank=True, null=True)
    show_line_subtotals_tax_selection = models.CharField(max_length=-1)
    module_account_budget = models.BooleanField(blank=True, null=True)
    module_account_payment = models.BooleanField(blank=True, null=True)
    module_account_reports = models.BooleanField(blank=True, null=True)
    module_account_check_printing = models.BooleanField(blank=True, null=True)
    module_account_batch_payment = models.BooleanField(blank=True, null=True)
    module_account_sepa = models.BooleanField(blank=True, null=True)
    module_account_sepa_direct_debit = models.BooleanField(blank=True, null=True)
    module_account_plaid = models.BooleanField(blank=True, null=True)
    module_account_yodlee = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_qif = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_ofx = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_csv = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_camt = models.BooleanField(blank=True, null=True)
    module_currency_rate_live = models.BooleanField(blank=True, null=True)
    module_account_intrastat = models.BooleanField(blank=True, null=True)
    module_product_margin = models.BooleanField(blank=True, null=True)
    module_l10n_eu_service = models.BooleanField(blank=True, null=True)
    module_account_taxcloud = models.BooleanField(blank=True, null=True)
    module_account_invoice_extract = models.BooleanField(blank=True, null=True)
    module_snailmail_account = models.BooleanField(blank=True, null=True)
    use_invoice_terms = models.BooleanField(blank=True, null=True)
    group_auto_done_setting = models.BooleanField(blank=True, null=True)
    module_sale_margin = models.BooleanField(blank=True, null=True)
    use_quotation_validity_days = models.BooleanField(blank=True, null=True)
    group_warning_sale = models.BooleanField(blank=True, null=True)
    group_sale_delivery_address = models.BooleanField(blank=True, null=True)
    group_proforma_sales = models.BooleanField(blank=True, null=True)
    default_invoice_policy = models.CharField(max_length=-1, blank=True, null=True)
    deposit_default_product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    module_delivery = models.BooleanField(blank=True, null=True)
    module_delivery_dhl = models.BooleanField(blank=True, null=True)
    module_delivery_fedex = models.BooleanField(blank=True, null=True)
    module_delivery_ups = models.BooleanField(blank=True, null=True)
    module_delivery_usps = models.BooleanField(blank=True, null=True)
    module_delivery_bpost = models.BooleanField(blank=True, null=True)
    module_delivery_easypost = models.BooleanField(blank=True, null=True)
    module_product_email_template = models.BooleanField(blank=True, null=True)
    module_sale_coupon = models.BooleanField(blank=True, null=True)
    module_sale_amazon = models.BooleanField(blank=True, null=True)
    automatic_invoice = models.BooleanField(blank=True, null=True)
    template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    confirmation_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    group_sale_order_template = models.BooleanField(blank=True, null=True)
    module_sale_quotation_builder = models.BooleanField(blank=True, null=True)
    module_l10n_mx_edi = models.BooleanField(blank=True, null=True)
    crm_alias_prefix = models.CharField(max_length=-1, blank=True, null=True)
    generate_lead_from_alias = models.BooleanField(blank=True, null=True)
    group_use_lead = models.BooleanField(blank=True, null=True)
    group_use_recurring_revenues = models.BooleanField(blank=True, null=True)
    module_crm_iap_lead = models.BooleanField(blank=True, null=True)
    module_crm_iap_lead_website = models.BooleanField(blank=True, null=True)
    module_crm_iap_lead_enrich = models.BooleanField(blank=True, null=True)
    module_mail_client_extension = models.BooleanField(blank=True, null=True)
    lead_enrich_auto = models.CharField(max_length=-1, blank=True, null=True)
    lead_mining_in_pipeline = models.BooleanField(blank=True, null=True)
    predictive_lead_scoring_start_date_str = models.CharField(max_length=-1, blank=True, null=True)
    predictive_lead_scoring_fields_str = models.CharField(max_length=-1, blank=True, null=True)
    module_procurement_jit = models.CharField(max_length=-1, blank=True, null=True)
    module_product_expiry = models.BooleanField(blank=True, null=True)
    group_stock_production_lot = models.BooleanField(blank=True, null=True)
    group_lot_on_delivery_slip = models.BooleanField(blank=True, null=True)
    group_stock_tracking_lot = models.BooleanField(blank=True, null=True)
    group_stock_tracking_owner = models.BooleanField(blank=True, null=True)
    group_stock_adv_location = models.BooleanField(blank=True, null=True)
    group_warning_stock = models.BooleanField(blank=True, null=True)
    group_stock_sign_delivery = models.BooleanField(blank=True, null=True)
    module_stock_picking_batch = models.BooleanField(blank=True, null=True)
    module_stock_barcode = models.BooleanField(blank=True, null=True)
    module_stock_sms = models.BooleanField(blank=True, null=True)
    group_stock_multi_locations = models.BooleanField(blank=True, null=True)
    module_stock_landed_costs = models.BooleanField(blank=True, null=True)
    group_display_incoterm = models.BooleanField(blank=True, null=True)
    group_lot_on_invoice = models.BooleanField(blank=True, null=True)
    use_security_lead = models.BooleanField(blank=True, null=True)
    default_picking_policy = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'res_config_settings'


class ResCountry(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    code = models.CharField(unique=True, max_length=2, blank=True, null=True)
    address_format = models.TextField(blank=True, null=True)
    address_view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    phone_code = models.IntegerField(blank=True, null=True)
    name_position = models.CharField(max_length=-1, blank=True, null=True)
    vat_label = models.CharField(max_length=-1, blank=True, null=True)
    state_required = models.BooleanField(blank=True, null=True)
    zip_required = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country'


class ResCountryGroup(models.Model):
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_group'


class ResCountryGroupPricelistRel(models.Model):
    pricelist = models.OneToOneField(ProductPricelist, models.DO_NOTHING, primary_key=True)
    res_country_group = models.ForeignKey(ResCountryGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_country_group_pricelist_rel'
        unique_together = (('pricelist', 'res_country_group'),)


class ResCountryResCountryGroupRel(models.Model):
    res_country = models.OneToOneField(ResCountry, models.DO_NOTHING, primary_key=True)
    res_country_group = models.ForeignKey(ResCountryGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_country_res_country_group_rel'
        unique_together = (('res_country', 'res_country_group'),)


class ResCountryState(models.Model):
    country = models.ForeignKey(ResCountry, models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_state'
        unique_together = (('country', 'code'),)


class ResCurrency(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    symbol = models.CharField(max_length=-1)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    decimal_places = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    position = models.CharField(max_length=-1, blank=True, null=True)
    currency_unit_label = models.CharField(max_length=-1, blank=True, null=True)
    currency_subunit_label = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency'


class ResCurrencyRate(models.Model):
    name = models.DateField()
    rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency_rate'
        unique_together = (('name', 'currency', 'company'),)


class ResGroups(models.Model):
    name = models.CharField(max_length=-1)
    comment = models.TextField(blank=True, null=True)
    category = models.ForeignKey(IrModuleCategory, models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    share = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_groups'
        unique_together = (('category', 'name'),)


class ResGroupsImpliedRel(models.Model):
    gid = models.OneToOneField(ResGroups, models.DO_NOTHING, db_column='gid', primary_key=True)
    hid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='hid')

    class Meta:
        managed = False
        db_table = 'res_groups_implied_rel'
        unique_together = (('gid', 'hid'),)


class ResGroupsReportRel(models.Model):
    uid = models.OneToOneField(IrActReportXml, models.DO_NOTHING, db_column='uid', primary_key=True)
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'res_groups_report_rel'
        unique_together = (('uid', 'gid'),)


class ResGroupsUsersRel(models.Model):
    gid = models.OneToOneField(ResGroups, models.DO_NOTHING, db_column='gid', primary_key=True)
    uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'res_groups_users_rel'
        unique_together = (('gid', 'uid'),)


class ResLang(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    code = models.CharField(unique=True, max_length=-1)
    iso_code = models.CharField(max_length=-1, blank=True, null=True)
    url_code = models.CharField(unique=True, max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    direction = models.CharField(max_length=-1)
    date_format = models.CharField(max_length=-1)
    time_format = models.CharField(max_length=-1)
    week_start = models.CharField(max_length=-1)
    grouping = models.CharField(max_length=-1)
    decimal_point = models.CharField(max_length=-1)
    thousands_sep = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_lang'


class ResPartner(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, db_column='title', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    tz = models.CharField(max_length=-1, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    vat = models.CharField(max_length=-1, blank=True, null=True)
    website = models.CharField(max_length=-1, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    credit_limit = models.FloatField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    employee = models.BooleanField(blank=True, null=True)
    function = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    street = models.CharField(max_length=-1, blank=True, null=True)
    street2 = models.CharField(max_length=-1, blank=True, null=True)
    zip = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    state = models.ForeignKey(ResCountryState, models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, blank=True, null=True)
    partner_latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner_longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    mobile = models.CharField(max_length=-1, blank=True, null=True)
    is_company = models.BooleanField(blank=True, null=True)
    industry = models.ForeignKey('ResPartnerIndustry', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    partner_share = models.BooleanField(blank=True, null=True)
    commercial_partner = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    commercial_company_name = models.CharField(max_length=-1, blank=True, null=True)
    company_name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    email_normalized = models.CharField(max_length=-1, blank=True, null=True)
    message_bounce = models.IntegerField(blank=True, null=True)
    signup_token = models.CharField(max_length=-1, blank=True, null=True)
    signup_type = models.CharField(max_length=-1, blank=True, null=True)
    signup_expiration = models.DateTimeField(blank=True, null=True)
    team = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True)
    partner_gid = models.IntegerField(blank=True, null=True)
    additional_info = models.CharField(max_length=-1, blank=True, null=True)
    phone_sanitized = models.CharField(max_length=-1, blank=True, null=True)
    debit_limit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    last_time_entries_checked = models.DateTimeField(blank=True, null=True)
    invoice_warn = models.CharField(max_length=-1, blank=True, null=True)
    invoice_warn_msg = models.TextField(blank=True, null=True)
    supplier_rank = models.IntegerField(blank=True, null=True)
    customer_rank = models.IntegerField(blank=True, null=True)
    sale_warn = models.CharField(max_length=-1, blank=True, null=True)
    sale_warn_msg = models.TextField(blank=True, null=True)
    calendar_last_notif_ack = models.DateTimeField(blank=True, null=True)
    picking_warn = models.CharField(max_length=-1, blank=True, null=True)
    picking_warn_msg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner'


class ResPartnerAutocompleteSync(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    synched = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_autocomplete_sync'


class ResPartnerBank(models.Model):
    active = models.BooleanField(blank=True, null=True)
    acc_number = models.CharField(max_length=-1)
    sanitized_acc_number = models.CharField(max_length=-1, blank=True, null=True)
    acc_holder_name = models.CharField(max_length=-1, blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    bank = models.ForeignKey(ResBank, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    l10n_mx_edi_clabe = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_bank'
        unique_together = (('sanitized_acc_number', 'company'),)


class ResPartnerCategory(models.Model):
    name = models.CharField(max_length=-1)
    color = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_category'


class ResPartnerIndustry(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    full_name = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_industry'


class ResPartnerResPartnerCategoryRel(models.Model):
    category = models.OneToOneField(ResPartnerCategory, models.DO_NOTHING, primary_key=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_partner_res_partner_category_rel'
        unique_together = (('category', 'partner'),)


class ResPartnerTitle(models.Model):
    name = models.CharField(max_length=-1)
    shortcut = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_title'


class ResUsers(models.Model):
    active = models.BooleanField(blank=True, null=True)
    login = models.CharField(unique=True, max_length=-1)
    password = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    share = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    totp_secret = models.CharField(max_length=-1, blank=True, null=True)
    notification_type = models.CharField(max_length=-1)
    odoobot_state = models.CharField(max_length=-1, blank=True, null=True)
    odoobot_failed = models.BooleanField(blank=True, null=True)
    sale_team = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True)
    target_sales_won = models.IntegerField(blank=True, null=True)
    target_sales_done = models.IntegerField(blank=True, null=True)
    target_sales_invoiced = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users'


class ResUsersApikeys(models.Model):
    name = models.CharField(max_length=-1)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING)
    scope = models.CharField(max_length=-1, blank=True, null=True)
    index = models.CharField(max_length=8, blank=True, null=True)
    key = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_apikeys'


class ResUsersApikeysDescription(models.Model):
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_apikeys_description'


class ResUsersIdentitycheck(models.Model):
    request = models.CharField(max_length=-1, blank=True, null=True)
    password = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_identitycheck'


class ResUsersLog(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_log'


class ResetViewArchWizard(models.Model):
    view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    reset_mode = models.CharField(max_length=-1)
    compare_view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reset_view_arch_wizard'


class ResourceCalendar(models.Model):
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    hours_per_day = models.FloatField(blank=True, null=True)
    tz = models.CharField(max_length=-1)
    two_weeks_calendar = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar'


class ResourceCalendarAttendance(models.Model):
    name = models.CharField(max_length=-1)
    dayofweek = models.CharField(max_length=-1)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    hour_from = models.FloatField()
    hour_to = models.FloatField()
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING)
    day_period = models.CharField(max_length=-1)
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING, blank=True, null=True)
    week_type = models.CharField(max_length=-1, blank=True, null=True)
    display_type = models.CharField(max_length=-1, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar_attendance'


class ResourceCalendarLeaves(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING, blank=True, null=True)
    time_type = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar_leaves'


class ResourceResource(models.Model):
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    resource_type = models.CharField(max_length=-1)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    time_efficiency = models.FloatField()
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING)
    tz = models.CharField(max_length=-1)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_resource'


class ResourceTest(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    resource = models.ForeignKey(ResourceResource, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    resource_calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_test'


class RuleGroupRel(models.Model):
    rule_group = models.OneToOneField(IrRule, models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey(ResGroups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rule_group_rel'
        unique_together = (('rule_group', 'group'),)


class SaleAdvancePaymentInv(models.Model):
    advance_payment_method = models.CharField(max_length=-1)
    deduct_down_payments = models.BooleanField(blank=True, null=True)
    has_down_payments = models.BooleanField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True)
    fixed_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    deposit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_advance_payment_inv'


class SaleOrder(models.Model):
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    client_order_ref = models.CharField(max_length=-1, blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    date_order = models.DateTimeField()
    validity_date = models.DateField(blank=True, null=True)
    require_signature = models.BooleanField(blank=True, null=True)
    require_payment = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    partner_invoice = models.ForeignKey(ResPartner, models.DO_NOTHING)
    partner_shipping = models.ForeignKey(ResPartner, models.DO_NOTHING)
    pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True)
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    invoice_status = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_term = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING, blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    team = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True)
    signed_by = models.CharField(max_length=-1, blank=True, null=True)
    signed_on = models.DateTimeField(blank=True, null=True)
    commitment_date = models.DateTimeField(blank=True, null=True)
    show_update_pricelist = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_order_template = models.ForeignKey('SaleOrderTemplate', models.DO_NOTHING, blank=True, null=True)
    opportunity = models.ForeignKey(CrmLead, models.DO_NOTHING, blank=True, null=True)
    incoterm = models.ForeignKey(AccountIncoterms, models.DO_NOTHING, db_column='incoterm', blank=True, null=True)
    picking_policy = models.CharField(max_length=-1)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)
    procurement_group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order'


class SaleOrderCancel(models.Model):
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_cancel'


class SaleOrderLine(models.Model):
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING)
    name = models.TextField()
    sequence = models.IntegerField(blank=True, null=True)
    invoice_status = models.CharField(max_length=-1, blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_tax = models.FloatField(blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_reduce = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_reduce_taxinc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_reduce_taxexcl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_column='product_uom', blank=True, null=True)
    qty_delivered_method = models.CharField(max_length=-1, blank=True, null=True)
    qty_delivered = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_delivered_manual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    untaxed_amount_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    untaxed_amount_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    salesman = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    order_partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    is_expense = models.BooleanField(blank=True, null=True)
    is_downpayment = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    customer_lead = models.FloatField()
    display_type = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING, db_column='product_packaging', blank=True, null=True)
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_line'


class SaleOrderLineInvoiceRel(models.Model):
    invoice_line = models.OneToOneField(AccountMoveLine, models.DO_NOTHING, primary_key=True)
    order_line = models.ForeignKey(SaleOrderLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_line_invoice_rel'
        unique_together = (('invoice_line', 'order_line'),)


class SaleOrderOption(models.Model):
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING, blank=True, null=True)
    line = models.ForeignKey(SaleOrderLine, models.DO_NOTHING, blank=True, null=True)
    name = models.TextField()
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_option'


class SaleOrderTagRel(models.Model):
    order = models.OneToOneField(SaleOrder, models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey(CrmTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_tag_rel'
        unique_together = (('order', 'tag'),)


class SaleOrderTemplate(models.Model):
    name = models.CharField(max_length=-1)
    note = models.TextField(blank=True, null=True)
    number_of_days = models.IntegerField(blank=True, null=True)
    require_signature = models.BooleanField(blank=True, null=True)
    require_payment = models.BooleanField(blank=True, null=True)
    mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_template'


class SaleOrderTemplateLine(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    sale_order_template = models.ForeignKey(SaleOrderTemplate, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    name = models.TextField()
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True)
    display_type = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_template_line'


class SaleOrderTemplateOption(models.Model):
    sale_order_template = models.ForeignKey(SaleOrderTemplate, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    name = models.TextField()
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_template_option'


class SaleOrderTransactionRel(models.Model):
    sale_order = models.OneToOneField(SaleOrder, models.DO_NOTHING, primary_key=True)
    transaction = models.ForeignKey(PaymentTransaction, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_transaction_rel'
        unique_together = (('sale_order', 'transaction'),)


class SalePaymentAcquirerOnboardingWizard(models.Model):
    paypal_user_type = models.CharField(max_length=-1, blank=True, null=True)
    paypal_email_account = models.CharField(max_length=-1, blank=True, null=True)
    paypal_seller_account = models.CharField(max_length=-1, blank=True, null=True)
    paypal_pdt_token = models.CharField(max_length=-1, blank=True, null=True)
    stripe_secret_key = models.CharField(max_length=-1, blank=True, null=True)
    stripe_publishable_key = models.CharField(max_length=-1, blank=True, null=True)
    manual_name = models.CharField(max_length=-1, blank=True, null=True)
    journal_name = models.CharField(max_length=-1, blank=True, null=True)
    acc_number = models.CharField(max_length=-1, blank=True, null=True)
    manual_post_msg = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_payment_acquirer_onboarding_wizard'


class SmsCancel(models.Model):
    model = models.CharField(max_length=-1)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_cancel'


class SmsComposer(models.Model):
    composition_mode = models.CharField(max_length=-1)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    res_ids = models.CharField(max_length=-1, blank=True, null=True)
    use_active_domain = models.BooleanField(blank=True, null=True)
    active_domain = models.TextField(blank=True, null=True)
    mass_keep_log = models.BooleanField(blank=True, null=True)
    mass_force_send = models.BooleanField(blank=True, null=True)
    mass_use_blacklist = models.BooleanField(blank=True, null=True)
    recipient_single_number_itf = models.CharField(max_length=-1, blank=True, null=True)
    number_field_name = models.CharField(max_length=-1, blank=True, null=True)
    numbers = models.CharField(max_length=-1, blank=True, null=True)
    template = models.ForeignKey('SmsTemplate', models.DO_NOTHING, blank=True, null=True)
    body = models.TextField()
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_composer'


class SmsResend(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_resend'


class SmsResendRecipient(models.Model):
    sms_resend = models.ForeignKey(SmsResend, models.DO_NOTHING)
    notification = models.ForeignKey(MailMessageResPartnerNeedactionRel, models.DO_NOTHING)
    resend = models.BooleanField(blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    sms_number = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_resend_recipient'


class SmsSms(models.Model):
    number = models.CharField(max_length=-1, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1)
    error_code = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_sms'


class SmsTemplate(models.Model):
    lang = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    model = models.ForeignKey(IrModel, models.DO_NOTHING)
    model_0 = models.CharField(db_column='model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    body = models.CharField(max_length=-1)
    sidebar_action = models.ForeignKey(IrActWindow, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_template'


class SmsTemplatePreview(models.Model):
    sms_template = models.ForeignKey(SmsTemplate, models.DO_NOTHING)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    resource_ref = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_template_preview'


class SnailmailConfirmInvoice(models.Model):
    model_name = models.CharField(max_length=-1, blank=True, null=True)
    invoice_send = models.ForeignKey(AccountInvoiceSend, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_confirm_invoice'


class SnailmailLetter(models.Model):
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    model = models.CharField(max_length=-1)
    res_id = models.IntegerField()
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    report_template = models.ForeignKey(IrActReportXml, models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    color = models.BooleanField(blank=True, null=True)
    cover = models.BooleanField(blank=True, null=True)
    duplex = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=-1)
    error_code = models.CharField(max_length=-1, blank=True, null=True)
    info_msg = models.CharField(max_length=-1, blank=True, null=True)
    message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True)
    street = models.CharField(max_length=-1, blank=True, null=True)
    street2 = models.CharField(max_length=-1, blank=True, null=True)
    zip = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    state_0 = models.ForeignKey(ResCountryState, models.DO_NOTHING, db_column='state_id', blank=True, null=True)  # Field renamed because of name conflict.
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_letter'


class SnailmailLetterCancel(models.Model):
    model = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_letter_cancel'


class SnailmailLetterFormatError(models.Model):
    message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True)
    snailmail_cover = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_letter_format_error'


class SnailmailLetterMissingRequiredFields(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    letter = models.ForeignKey(SnailmailLetter, models.DO_NOTHING, blank=True, null=True)
    street = models.CharField(max_length=-1, blank=True, null=True)
    street2 = models.CharField(max_length=-1, blank=True, null=True)
    zip = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    state = models.ForeignKey(ResCountryState, models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_letter_missing_required_fields'


class StockAssignSerial(models.Model):
    move = models.ForeignKey('StockMove', models.DO_NOTHING)
    next_serial_number = models.CharField(max_length=-1)
    next_serial_count = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_assign_serial'


class StockBackorderConfirmation(models.Model):
    show_transfers = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_backorder_confirmation'


class StockBackorderConfirmationLine(models.Model):
    backorder_confirmation = models.ForeignKey(StockBackorderConfirmation, models.DO_NOTHING, blank=True, null=True)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    to_backorder = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_backorder_confirmation_line'


class StockChangeProductQty(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING)
    new_quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_change_product_qty'


class StockImmediateTransfer(models.Model):
    show_transfers = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_immediate_transfer'


class StockImmediateTransferLine(models.Model):
    immediate_transfer = models.ForeignKey(StockImmediateTransfer, models.DO_NOTHING)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING)
    to_immediate = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_immediate_transfer_line'


class StockInventory(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    date = models.DateTimeField()
    state = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    start_empty = models.BooleanField(blank=True, null=True)
    prefill_counted_quantity = models.CharField(max_length=-1, blank=True, null=True)
    exhausted = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_inventory'


class StockInventoryLine(models.Model):
    is_editable = models.BooleanField(blank=True, null=True)
    inventory = models.ForeignKey(StockInventory, models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    prod_lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    theoretical_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inventory_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_inventory_line'


class StockInventoryStockLocationRel(models.Model):
    stock_inventory = models.OneToOneField(StockInventory, models.DO_NOTHING, primary_key=True)
    stock_location = models.ForeignKey('StockLocation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_inventory_stock_location_rel'
        unique_together = (('stock_inventory', 'stock_location'),)


class StockLocation(models.Model):
    name = models.CharField(max_length=-1)
    complete_name = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    usage = models.CharField(max_length=-1)
    location = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    posx = models.IntegerField(blank=True, null=True)
    posy = models.IntegerField(blank=True, null=True)
    posz = models.IntegerField(blank=True, null=True)
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    scrap_location = models.BooleanField(blank=True, null=True)
    return_location = models.BooleanField(blank=True, null=True)
    removal_strategy = models.ForeignKey(ProductRemoval, models.DO_NOTHING, blank=True, null=True)
    barcode = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    valuation_in_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    valuation_out_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_location'
        unique_together = (('barcode', 'company'),)


class StockLocationRoute(models.Model):
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    product_selectable = models.BooleanField(blank=True, null=True)
    product_categ_selectable = models.BooleanField(blank=True, null=True)
    warehouse_selectable = models.BooleanField(blank=True, null=True)
    supplied_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    supplier_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_selectable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_location_route'


class StockLocationRouteCateg(models.Model):
    route = models.OneToOneField(StockLocationRoute, models.DO_NOTHING, primary_key=True)
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_location_route_categ'
        unique_together = (('route', 'categ'),)


class StockLocationRouteMove(models.Model):
    move = models.OneToOneField('StockMove', models.DO_NOTHING, primary_key=True)
    route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_location_route_move'
        unique_together = (('move', 'route'),)


class StockLocationRouteStockRulesReportRel(models.Model):
    stock_rules_report = models.OneToOneField('StockRulesReport', models.DO_NOTHING, primary_key=True)
    stock_location_route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_location_route_stock_rules_report_rel'
        unique_together = (('stock_rules_report', 'stock_location_route'),)


class StockMove(models.Model):
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField()
    date_deadline = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    description_picking = models.TextField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_column='product_uom')
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    price_unit = models.FloatField(blank=True, null=True)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    procure_method = models.CharField(max_length=-1)
    scrapped = models.BooleanField(blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    rule = models.ForeignKey('StockRule', models.DO_NOTHING, blank=True, null=True)
    propagate_cancel = models.BooleanField(blank=True, null=True)
    delay_alert_date = models.DateTimeField(blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    inventory = models.ForeignKey(StockInventory, models.DO_NOTHING, blank=True, null=True)
    origin_returned_move = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    restrict_partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    additional = models.BooleanField(blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    package_level = models.ForeignKey('StockPackageLevel', models.DO_NOTHING, blank=True, null=True)
    next_serial = models.CharField(max_length=-1, blank=True, null=True)
    next_serial_count = models.IntegerField(blank=True, null=True)
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    to_refund = models.BooleanField(blank=True, null=True)
    sale_line = models.ForeignKey(SaleOrderLine, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_move'


class StockMoveLine(models.Model):
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    qty_done = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    package_level = models.ForeignKey('StockPackageLevel', models.DO_NOTHING, blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    lot_name = models.CharField(max_length=-1, blank=True, null=True)
    result_package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField()
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    state = models.CharField(max_length=-1, blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    description_picking = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_move_line'


class StockMoveLineConsumeRel(models.Model):
    consume_line = models.OneToOneField(StockMoveLine, models.DO_NOTHING, primary_key=True)
    produce_line = models.ForeignKey(StockMoveLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_move_line_consume_rel'
        unique_together = (('consume_line', 'produce_line'),)


class StockMoveMoveRel(models.Model):
    move_orig = models.OneToOneField(StockMove, models.DO_NOTHING, primary_key=True)
    move_dest = models.ForeignKey(StockMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_move_move_rel'
        unique_together = (('move_orig', 'move_dest'),)


class StockOrderpointSnooze(models.Model):
    predefined_date = models.CharField(max_length=-1, blank=True, null=True)
    snoozed_until = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_orderpoint_snooze'


class StockOrderpointSnoozeStockWarehouseOrderpointRel(models.Model):
    stock_orderpoint_snooze = models.OneToOneField(StockOrderpointSnooze, models.DO_NOTHING, primary_key=True)
    stock_warehouse_orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_orderpoint_snooze_stock_warehouse_orderpoint_rel'
        unique_together = (('stock_orderpoint_snooze', 'stock_warehouse_orderpoint'),)


class StockPackageDestination(models.Model):
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_package_destination'


class StockPackageLevel(models.Model):
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_package_level'


class StockPicking(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    backorder = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    move_type = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1, blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
    date_deadline = models.DateTimeField(blank=True, null=True)
    has_deadline_issue = models.BooleanField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    printed = models.BooleanField(blank=True, null=True)
    is_locked = models.BooleanField(blank=True, null=True)
    immediate_transfer = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale = models.ForeignKey(SaleOrder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking'
        unique_together = (('name', 'company'),)


class StockPickingBackorderRel(models.Model):
    stock_backorder_confirmation = models.OneToOneField(StockBackorderConfirmation, models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey(StockPicking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_picking_backorder_rel'
        unique_together = (('stock_backorder_confirmation', 'stock_picking'),)


class StockPickingSmsRel(models.Model):
    confirm_stock_sms = models.OneToOneField(ConfirmStockSms, models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey(StockPicking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_picking_sms_rel'
        unique_together = (('confirm_stock_sms', 'stock_picking'),)


class StockPickingTransferRel(models.Model):
    stock_immediate_transfer = models.OneToOneField(StockImmediateTransfer, models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey(StockPicking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_picking_transfer_rel'
        unique_together = (('stock_immediate_transfer', 'stock_picking'),)


class StockPickingType(models.Model):
    name = models.CharField(max_length=-1)
    color = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    sequence_0 = models.ForeignKey(IrSequence, models.DO_NOTHING, db_column='sequence_id', blank=True, null=True)  # Field renamed because of name conflict.
    sequence_code = models.CharField(max_length=-1)
    default_location_src = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    default_location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=-1)
    return_picking_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    show_entire_packs = models.BooleanField(blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    use_create_lots = models.BooleanField(blank=True, null=True)
    use_existing_lots = models.BooleanField(blank=True, null=True)
    show_operations = models.BooleanField(blank=True, null=True)
    show_reserved = models.BooleanField(blank=True, null=True)
    barcode = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking_type'


class StockProductionLot(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_production_lot'


class StockPutawayRule(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    location_in = models.ForeignKey(StockLocation, models.DO_NOTHING)
    location_out = models.ForeignKey(StockLocation, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_putaway_rule'


class StockQuant(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    lot = models.ForeignKey(StockProductionLot, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    reserved_quantity = models.FloatField()
    in_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quant'


class StockQuantPackage(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quant_package'


class StockQuantityHistory(models.Model):
    inventory_datetime = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quantity_history'


class StockReturnPicking(models.Model):
    picking = models.ForeignKey(StockPicking, models.DO_NOTHING, blank=True, null=True)
    move_dest_exists = models.BooleanField(blank=True, null=True)
    original_location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    parent_location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_return_picking'


class StockReturnPickingLine(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    wizard = models.ForeignKey(StockReturnPicking, models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    to_refund = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_return_picking_line'


class StockRouteProduct(models.Model):
    route = models.OneToOneField(StockLocationRoute, models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey(ProductTemplate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_product'
        unique_together = (('route', 'product'),)


class StockRouteWarehouse(models.Model):
    route = models.OneToOneField(StockLocationRoute, models.DO_NOTHING, primary_key=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_warehouse'
        unique_together = (('route', 'warehouse'),)


class StockRule(models.Model):
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    group_propagation_option = models.CharField(max_length=-1, blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    action = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    location_src = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING)
    procure_method = models.CharField(max_length=-1)
    route_sequence = models.IntegerField(blank=True, null=True)
    picking_type = models.ForeignKey(StockPickingType, models.DO_NOTHING)
    delay = models.IntegerField(blank=True, null=True)
    partner_address = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    propagate_cancel = models.BooleanField(blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    propagate_warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    auto = models.CharField(max_length=-1)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_rule'


class StockRulesReport(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING)
    product_has_variants = models.BooleanField()
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_rules_report'


class StockRulesReportStockWarehouseRel(models.Model):
    stock_rules_report = models.OneToOneField(StockRulesReport, models.DO_NOTHING, primary_key=True)
    stock_warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_rules_report_stock_warehouse_rel'
        unique_together = (('stock_rules_report', 'stock_warehouse'),)


class StockSchedulerCompute(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_scheduler_compute'


class StockScrap(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    lot = models.ForeignKey(StockProductionLot, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey(StockQuantPackage, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True)
    picking = models.ForeignKey(StockPicking, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    scrap_location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    scrap_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    state = models.CharField(max_length=-1, blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_scrap'


class StockTraceabilityReport(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_traceability_report'


class StockTrackConfirmation(models.Model):
    inventory = models.ForeignKey(StockInventory, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_track_confirmation'


class StockTrackLine(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    tracking = models.CharField(max_length=-1, blank=True, null=True)
    wizard = models.ForeignKey(StockTrackConfirmation, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_track_line'


class StockValuationLayer(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unit_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    remaining_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    remaining_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    stock_valuation_layer = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    stock_move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True)
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_valuation_layer'


class StockValuationLayerRevaluation(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    added_value = models.DecimalField(max_digits=65535, decimal_places=65535)
    reason = models.CharField(max_length=-1, blank=True, null=True)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_valuation_layer_revaluation'


class StockWarehouse(models.Model):
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    view_location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    lot_stock = models.ForeignKey(StockLocation, models.DO_NOTHING)
    code = models.CharField(max_length=5)
    reception_steps = models.CharField(max_length=-1)
    delivery_steps = models.CharField(max_length=-1)
    wh_input_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    wh_qc_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    wh_output_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    wh_pack_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    mto_pull = models.ForeignKey(StockRule, models.DO_NOTHING, blank=True, null=True)
    pick_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    pack_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    out_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    in_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    int_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    crossdock_route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING, blank=True, null=True)
    reception_route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING, blank=True, null=True)
    delivery_route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_warehouse'
        unique_together = (('code', 'company'), ('name', 'company'),)


class StockWarehouseOrderpoint(models.Model):
    name = models.CharField(max_length=-1)
    trigger = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    snoozed_until = models.DateField(blank=True, null=True)
    warehouse = models.ForeignKey(StockWarehouse, models.DO_NOTHING)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    product_min_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_max_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    qty_multiple = models.DecimalField(max_digits=65535, decimal_places=65535)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING, blank=True, null=True)
    qty_to_order = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_warehouse_orderpoint'


class StockWarnInsufficientQtyScrap(models.Model):
    scrap = models.ForeignKey(StockScrap, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    quantity = models.FloatField()
    product_uom_name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_warn_insufficient_qty_scrap'


class StockWhResupplyTable(models.Model):
    supplied_wh = models.OneToOneField(StockWarehouse, models.DO_NOTHING, primary_key=True)
    supplier_wh = models.ForeignKey(StockWarehouse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_wh_resupply_table'
        unique_together = (('supplied_wh', 'supplier_wh'),)


class TaxAdjustmentsWizard(models.Model):
    reason = models.CharField(max_length=-1)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    date = models.DateField()
    debit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    credit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    adjustment_type = models.CharField(max_length=-1)
    tax_report_line = models.ForeignKey(AccountTaxReportLine, models.DO_NOTHING)
    company_currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_adjustments_wizard'


class TeamFavoriteUserRel(models.Model):
    team = models.OneToOneField(CrmTeam, models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_favorite_user_rel'
        unique_together = (('team', 'user'),)


class UomCategory(models.Model):
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uom_category'


class UomUom(models.Model):
    name = models.CharField(max_length=-1)
    category = models.ForeignKey(UomCategory, models.DO_NOTHING)
    factor = models.DecimalField(max_digits=65535, decimal_places=65535)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535)
    active = models.BooleanField(blank=True, null=True)
    uom_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uom_uom'


class UtmCampaign(models.Model):
    name = models.CharField(max_length=-1)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING)
    stage = models.ForeignKey('UtmStage', models.DO_NOTHING)
    is_website = models.BooleanField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_campaign'


class UtmMedium(models.Model):
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_medium'


class UtmSource(models.Model):
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_source'


class UtmStage(models.Model):
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_stage'


class UtmTag(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_tag'


class UtmTagRel(models.Model):
    tag = models.OneToOneField(UtmCampaign, models.DO_NOTHING, primary_key=True)
    campaign = models.ForeignKey(UtmTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'utm_tag_rel'
        unique_together = (('tag', 'campaign'),)


class ValidateAccountMove(models.Model):
    force_post = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validate_account_move'


class WebEditorConverterTest(models.Model):
    char = models.CharField(max_length=-1, blank=True, null=True)
    integer = models.IntegerField(blank=True, null=True)
    float = models.FloatField(blank=True, null=True)
    numeric = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    many2one = models.ForeignKey('WebEditorConverterTestSub', models.DO_NOTHING, db_column='many2one', blank=True, null=True)
    binary = models.BinaryField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    selection_str = models.CharField(max_length=-1, blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test'


class WebEditorConverterTestSub(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test_sub'


class WebTourTour(models.Model):
    name = models.CharField(max_length=-1)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_tour_tour'


class WizardIrModelMenuCreate(models.Model):
    menu = models.ForeignKey(IrUiMenu, models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wizard_ir_model_menu_create'
