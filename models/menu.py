response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Licitações'),URL('default','licitacoes')==URL(),URL('default','licitacoes'),[]),
(T('Cadastrar'),URL('default','cadastrar')==URL(),URL('default','cadastrar'),[]),
]

"""(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Anos'),URL('default','anos')==URL(),URL('default','anos'),[]),
(T('Situação'),URL('default','situacao')==URL(),URL('default','situacao'),[]),
(T('Modalidade'),URL('default','modalidade')==URL(),URL('default','modalidade'),[]),
"""
