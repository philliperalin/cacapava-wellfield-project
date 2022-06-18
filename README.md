# cacapava-wellfield-project
Implementation of a wellfield in Caçapava, SP, Brazil.

## :construction: Work In Progress :construction: <img src="https://github.com/philliperalin/philliperalin/blob/main/assets/git-pikachu.gif" width="85">

---

## Objective 
* Implementation of a wellfield with its constructive parameters in the municipality of Caçapava to meet the demand of a possible abrupt population growth of 20 thousand people.
* Define the best area to construct the wellfield.

---

[``` ./data/ ```](data/) folder contain the data used in this project:
* [```dados-daee.csv```](data/dados-daee.csv) well data from [DAEE](http://www.aplicacoes.daee.sp.gov.br/usosrec/Daeewebpoco.html)
* [```dados-siagas.csv```](data/dados-siagas.csv) well data from [SIAGAS](http://siagasweb.cprm.gov.br/layout/)
* [```IRITANI-data.csv```](data/IRITANI-data.csv) well data from [Iritani, 1999](https://www.teses.usp.br/teses/disponiveis/44/44133/tde-16082013-125326/pt-br.php)

[```./transmissivity/```](transmissivity/) folder contain the files to estimate the transmissivity from the available data:
* [```T-estimation.py```](transmissivity/T-estimation.py) transmissivity estimates using [welltestpy](https://geostat-framework.readthedocs.io/projects/welltestpy/en/stable/) :construction: (Work in progress) :construction:
* [```Sc-T.ipynb```](transmissivity/Sc_T.ipynb) transmissivity estimates using empirical method that relates transmissivity and specific capacity

---

## References
IRITANI, M. A., 1999. Modelação Matemática Tridimensional para a Proteção das Captações de Água Subterrânea [doi:10.11606/T.44.1999.tde-16082013-125326]. São Paulo : Instituto de Geociências, Universidade de São Paulo. Tese de Doutorado em Recursos Minerais e Hidrogeologia. [acesso 2022-06-17].