# Cacapava Wellfield Project
Implementation of a wellfield in Caçapava, SP, Brazil. This project is a final assessment of a undergraduate class named: Water and monitoring wells for groundwater

This project was designed and carried out with the collaboration of:
* Cleilson Lopes
* Matheus Lima

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

[```./groundwater_recharge/```](groudwater_recharge/) folder contain the workflow file used to estimate the groundwater recharge in Caçapava-SP. Here was used the Thornthwaite-Mather Procedure (Thornthwaite and Mather, 1957). The groundwater recharge map are [here](results/recharge.png)

[```./reports/```](reports/) folder contain the reports of progress presented in the class.

[```./results/```](results/) folder contain the maps produced to delimite and define the wellfield.

[```./transmissivity/```](transmissivity/) folder contain the files to estimate the transmissivity from the available data:
* [```T-estimation.py```](transmissivity/T-estimation.py) transmissivity estimates using [welltestpy](https://geostat-framework.readthedocs.io/projects/welltestpy/en/stable/) :construction: (Work in progress) :construction:
* [```Sc-T.ipynb```](transmissivity/Sc_T.ipynb) transmissivity estimates using empirical method that relates transmissivity and specific capacity (Mace, 2000)

---

## References
Allen RG, Pereira LS, Raes D, Smith M (1998). Crop evapotranspiration: guidelines for computing crop water requirements. Irrigation and Drainage Paper 56, FAO, Rome.

IRITANI, M. A., 1999. Modelação Matemática Tridimensional para a Proteção das Captações de Água Subterrânea [doi:10.11606/T.44.1999.tde-16082013-125326](https://www.teses.usp.br/teses/disponiveis/44/44133/tde-16082013-125326/pt-br.php). São Paulo : Instituto de Geociências, Universidade de São Paulo. Tese de Doutorado em Recursos Minerais e Hidrogeologia. [acesso 2022-06-17].

MACE, R., 2000. Estimating transmissivity using specific-capacity data. Conference: Proceedings of the Ogallala Aquifer Symposium-2000

Saxton, K. E., & Rawls, W. J. (2006). Soil water characteristic estimates by texture and organic matter for hydrologic solutions. Soil science society of America Journal, 70(5), 1569-1578.

Thornthwaite, C. W., & Mather, J. R. (1957). Instructions and tables for computing potential evapotranspiration and the water balance. Publ. Climatol., 10(3).
