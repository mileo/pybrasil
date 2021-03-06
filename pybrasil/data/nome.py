# -*- coding: utf-8 -*-

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)


MES_JANEIRO = 1
MES_FEVEREIRO = 2
MES_MARCO = 3
MES_ABRIL = 4
MES_MAIO = 5
MES_JUNHO = 6
MES_JULHO = 7
MES_AGOSTO = 8
MES_SETEMBRO = 9
MES_OUTUBRO = 10
MES_NOVEMBRO = 11
MES_DEZEMBRO = 12

MESES = [
    MES_JANEIRO,
    MES_FEVEREIRO,
    MES_MARCO,
    MES_ABRIL,
    MES_MAIO,
    MES_JUNHO,
    MES_JULHO,
    MES_AGOSTO,
    MES_SETEMBRO,
    MES_OUTUBRO,
    MES_NOVEMBRO,
    MES_DEZEMBRO,
]

MES = {
    MES_JANEIRO: 'janeiro',
    MES_FEVEREIRO: 'fevereiro',
    MES_MARCO: 'março',
    MES_ABRIL: 'abril',
    MES_MAIO: 'maio',
    MES_JUNHO: 'junho',
    MES_JULHO: 'julho',
    MES_AGOSTO: 'agosto',
    MES_SETEMBRO: 'setembro',
    MES_OUTUBRO: 'outubro',
    MES_NOVEMBRO: 'novembro',
    MES_DEZEMBRO: 'dezembro',
}

MES_ABREVIADO = {
    MES_JANEIRO: 'jan',
    MES_FEVEREIRO: 'fev',
    MES_MARCO: 'mar',
    MES_ABRIL: 'abr',
    MES_MAIO: 'mai',
    MES_JUNHO: 'jun',
    MES_JULHO: 'jul',
    MES_AGOSTO: 'ago',
    MES_SETEMBRO: 'set',
    MES_OUTUBRO: 'out',
    MES_NOVEMBRO: 'nov',
    MES_DEZEMBRO: 'dez',
}

DIA_SEGUNDA = 0
DIA_TERCA = 1
DIA_QUARTA = 2
DIA_QUINTA = 3
DIA_SEXTA = 4
DIA_SABADO = 5
DIA_DOMINGO = 6

DIAS_DA_SEMANA = [
    DIA_SEGUNDA,
    DIA_TERCA,
    DIA_QUARTA,
    DIA_QUINTA,
    DIA_SEXTA,
    DIA_SABADO,
    DIA_DOMINGO,
]

DIA_DA_SEMANA = {
    DIA_SEGUNDA: 'segunda-feira',
    DIA_TERCA: 'terça-feira',
    DIA_QUARTA: 'quarta-feira',
    DIA_QUINTA: 'quinta-feira',
    DIA_SEXTA: 'sexta-feira',
    DIA_SABADO: 'sábado',
    DIA_DOMINGO: 'domingo',
}

DIA_DA_SEMANA_ABREVIADO = {
    DIA_SEGUNDA: 'seg',
    DIA_TERCA: 'ter',
    DIA_QUARTA: 'qua',
    DIA_QUINTA: 'qui',
    DIA_SEXTA: 'sex',
    DIA_SABADO: 'sáb',
    DIA_DOMINGO: 'dom',
}

MEIO_DIA = 'meio-dia'
MEIA_NOITE = 'meia-noite'
MADRUGADA = 'da madrugada'
MANHA = 'da manhã'
TARDE = 'da tarde'
NOITE = 'da noite'

PERIODO = {
    MEIA_NOITE: [0, 24],
    MADRUGADA: [1, 2, 3, 4, 5],
    MANHA: [6, 7, 8, 9, 10, 11],
    MEIO_DIA: [12],
    TARDE: [13, 14, 15, 16, 17, 18],
    NOITE: [19, 20, 21, 22, 23],
}
