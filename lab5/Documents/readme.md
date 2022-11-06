# Laboratorium 5 - TIER protocol i tidy data

Original data tb.csv is available in /OriginalData folder. It's also copied to /AnalysisData with name changed to tb_org.


The data from tb.csv has been sorted and cumulated in script Command.py - the more interesting columns weer chosen and cumulated. The inforamtions about age have been abandoned as to make the table more readable. 
The whole script is in /CommandFiles/Command.py

Data after analysis is available in:
- /AnalysisData/tb_ana.csv - file contains chosen info from tb_org.csv. Only information about yearly new cases per country, divided by sex:
  - iso2 - string, country name coded in ISO alpha 2.
  - year - int, a year in which the data was taken.
  - new_sp - int, all new cases 
  - m_cases - int, male new cases
  - f_cases - int, female new cases

- /AnalysisData/tb_org.csv - file contains information from tb.csv. Headers of file are:
  - iso2 - string, country name coded in ISO alpha 2.
  - year - int, a year in which the data was taken.
  - new_sp - int, all new cases 
  - 20 headers coded with new_sp_{f/m}age - int, new cases divided by age and sex
