### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_modalidade',
    Field('f_tipo', type='string',
          label=T('Tipo')),
    auth.signature,
    format='%(f_tipo)s',
    migrate=settings.migrate)

db.define_table('t_modalidade_archive',db.t_modalidade,Field('current_record','reference t_modalidade',readable=False,writable=False))

########################################
db.define_table('t_anos',
    Field('f_ano', type='string',
          label=T('Ano')),
    auth.signature,
    format='%(f_ano)s',
    migrate=settings.migrate)

db.define_table('t_anos_archive',db.t_anos,Field('current_record','reference t_anos',readable=False,writable=False))

########################################
db.define_table('t_situacao',
    Field('f_tipo', type='string',
          label=T('Tipo')),
    auth.signature,
    format='%(f_tipo)s',
    migrate=settings.migrate)

db.define_table('t_situacao_archive',db.t_situacao,Field('current_record','reference t_situacao',readable=False,writable=False))

########################################
db.define_table('t_licitacoes',
    Field('f_n_procedimento', type='string',
          label=T('Nº do Procedimento')),
    Field('f_modalidade', type='reference t_modalidade',
          label=T('Modalidade')),
    Field('f_anos', type='reference t_anos',
          label=T('Ano')),
    Field('f_situacao', type='reference t_situacao',
          label=T('Situação')),
    Field('f_concluido', 'boolean',
          label=T('Concluído?')),
    auth.signature,
    format='%(f_n_procedimento)s',
    migrate=settings.migrate)

db.define_table('t_licitacoes_archive',db.t_licitacoes,Field('current_record','reference t_licitacoes',readable=False,writable=False))
