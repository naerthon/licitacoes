# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def cadastrar():
    form = SQLFORM(db.t_licitacoes,onupdate=auth.archive)
    if form.process().accepted:
        session.flash = 'Formulário aceito!'
        redirect(URL('cadastrar'))
    elif form.errors:
         response.flash = 'Erros no formulário!'
    else:
         response.flash = 'Preencha o formulário!'
    return dict(form=form)

def get_header_labels(table=None):
    headers = {}
    for field in db[table].fields:
        headers[table+'.'+field] = db[table][field].label
    return headers
"""

@auth.requires_login()
def licitacoes():
    rows = SQLTABLE(
        db(db.t_licitacoes.id).select(db.t_licitacoes.f_n_procedimento,
        db.t_licitacoes.f_modalidade),
        headers = get_header_labels('t_licitacoes')
    )
    return dict(rows=rows)
"""
@auth.requires_login()
def licitacoes():
    rows = SQLTABLE(db().select(db.t_licitacoes.f_n_procedimento, db.t_licitacoes.f_anos,db.t_licitacoes.f_modalidade,db.t_licitacoes.f_situacao,db.t_licitacoes.f_concluido, orderby=db.t_licitacoes.f_modalidade),
        headers = get_header_labels('t_licitacoes'),
        _width='100%',
        _class='table table-hover',
        _id='div',
    )
    return dict(rows=rows)

@auth.requires_login()
def anos():
    form = SQLFORM.grid(db.t_anos,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def situacao():
    form = SQLFORM.grid(db.t_situacao,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def modalidade():
    form = SQLFORM.grid(db.t_modalidade,onupdate=auth.archive)
    return locals()

