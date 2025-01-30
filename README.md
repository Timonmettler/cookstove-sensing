<!-- badges: start -->
[![](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
<!-- badges: end -->

<h1> Sensing improved cookstoves to estimate CO2 emission reduction </h1>

<b>Contributors</b>  
- Timon Mettler <a href="https://orcid.org/XXXX-XXXX-XXXX-XXXX">
<img alt="ORCID logo" src="https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png" width="16" height="16" /> XXXX-XXXX-XXXX-XXXX
</a> *author, developer*  
- Jakub Tkaczuk <a href="https://orcid.org/0000-0001-7997-9423">
<img alt="ORCID logo" src="https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png" width="16" height="16" /> 0000-0001-7997-9423
</a> *supervisor, developer, maintainer*  
- Elizabeth Tilley <a href="https://orcid.org/0000-0002-2095-9724">
<img alt="ORCID logo" src="https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png" width="16" height="16" /> 0000-0002-2095-9724
</a> *supervisor*  

<p align="middle"> 
<img src="img/ETH_GHE_logo_negative.svg" width=600>
<br><br>
This repository compliments the openly-accessible bachelor's thesis, available on the<br \>  
<a href="">ETH Research Collection</a>.
</p>

# Background

This repository compliments the bachelor's thesis on developing the sensor system for estimating the emission reduction though improved cookstove usage. Hardware created within this project lays the foundations for establishing accurate and easy to operate hardware for obtaining carbon certificates under Paris Agreement. The thesis presents the design and implementation of a system for data collection and evaluation of the environmental impact of improved cookstoves compared to traditional models. The resulting system is open-source, reliable, and cost-effective. It uses Raspberry Pi Pico to collect data from a thermocouple and a scale to measure the runtime and wood consumption of cookstoves. Designed for deployment in remote areas lacking electricity and Wi-Fi connectivity, the system operates using solar panels and transmits sensor data to a cloud-based server via a cellular connection. By providing precise and reliable data, the system enhances the accuracy of emissions calculations associated with cookstoves. The work presented in the thesis and this repository serves as a comprehensive guide for creating a robust, cost-efficient, and remotely deployable data logging solution, contributing to the accurate assessment of CO2 emissions savings and supporting climate change mitigation efforts.

# Hardware

Hardware used in the project:
- Microcontroller (Raspberry Pi Pico) serves as the central processing unit to manage data acquisition and transmission.
- Micro SD card module and micro SD card allows storing the sensor data locally.
- SIM7670E Cellular modem enables reliable data transmission over cellular networks.
- Load cells and the HX711 load cell amplifier measure the weight of wood consumed by the cookstove.
- K-type thermocouple and AD8495 thermocouple amplifier measure cookstove temperature.
- PCF8523 Real-Time Clock provides accurate timestamps for collected data.
- Waveshare solar power management module (D) ensures continuous power supply by managing the batteries and solar panels.
- Three 18650 Li-ion batteries are selected for their energy density and reusability.
- Two 10 W, 12 V solar panels supply energy to charge the batteries in remote environments.
- LM3940 voltage regulator regulates the voltage from 5 V to 3.3 V to ensure safe operation.
- TRU COMPONENTS KST 220 enclosure provides a protective casing for the hardware.

| name                                        | source                                                | approximate price [CHF] |
| ------------------------------------------- | ----------------------------------------------------- | ----------------------- |
| Raspberry Pi Pico                           | [Pi-Shop](https://www.pi-shop.ch/raspberry-pi-pico-2) | 7.90                    |
| Micro SD card module                        |                                                       |                         |
| Micro SD card                               |                                                       |                         |
| SIM7670E module                             |                                                       |                         |
| Three load cells                            |                                                       |                         |
| HX711 load cell amplifier                   |                                                       |                         |
| K-type thermocouple                         |                                                       |                         |
| AD8495 thermocouple amplifier               |                                                       |                         |
| PCF8523 Real-Time Clock                     |                                                       |                         |
| Waveshare solar power management module (D) |                                                       |                         |
| Three 18650 Li-ion batteries                |                                                       |                         | 
| Two 10 W, 12 V solar panels                 |                                                       |                         |
| LM3940 voltage regulator                    |                                                       |                         |
| TRU COMPONENTS KST 220 enclosure            |                                                       |                         |
| **TOTAL**                                   |                                                       |                         |

The dataflow between the hardware components is schematically represented below.

![](img/subsystems.png)

# Software

The `main.py` script follows the workflow presented on the figure below.

![](img/software_diagram.png)

# Wiring diagram

The wiring diagram presents electrical connections between hardware.

![](img/wiring_diagramm.png)

# License

Both the thesis, published on the [ETH Research Collection]() and the underlying data, published in this repository are licensed under [Creative Commons Attribution 4.0 International](https://github.com/Global-Health-Engineering/cookstove-sensing/blob/main/LICENSE.md).
