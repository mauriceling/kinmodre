# KinModRe (Repository of Whole Cell Kinetic Models)

### List of Whole Cell Kinetic Models Developed by My Group
Each of themese models have a [data package](https://github.com/mauriceling/kinmodre/tree/main/data_packages), which generally contains (i) an Excel file containing details of the model, (ii) a model specification file (.modelspec) of the model written in AdvanceSyn Model format, (iii) a Python file (.py), which is the simulatable model, generated from the model specification file, (iv) an Excel file containing the simulation results, and (v) published paper of the model (if any). The model specification file (.modelspec) is replicated in [asm](https://github.com/mauriceling/kinmodre/tree/main/asm) folder; and the generated Python file is replicated in [odescripts](https://github.com/mauriceling/kinmodre/tree/main/odescripts) folder.

More details on each model; number of metabolites, enzymes, and reactions; are listed in [List of Kinetic Models.xlsx](https://github.com/mauriceling/kinmodre/blob/main/List%20of%20Kinetic%20Models.xlsx) file.

1. UniKin1 (2020) on Generic Central Metabolism [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/UniKin1-A-Universal,-Non-Species-Specific-Whole-Cell-Kinetic-Model)]
1. ecoJC20 (2021) on _Escherichia coli_ [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/Adaptation-of-Whole-Cell-Kinetic-Model-Template%2C-UniKin1%2C-to-Escherichia-coli-Whole-Cell-Kinetic-Model%2C-ecoJC20)]
1. pbmKZJ23 (2024) on _Stutzerimonas balearica_ DSM 6083 [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/Ab-Initio-Whole-Cell-Kinetic-Model-of-Stutzerimonas-balearica-DSM-6083-%28pbmKZJ23%29)]
1. bbfMA24 (2025) on _Bifidobacterium bifidum_ BGN4 [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/Ab-Initio-Whole-Cell-Kinetic-Model-of-Bifidobacterium-bifidum-BGN4-%28bbfMA24%29)]
1. lacAS24 (2025) on _Lactobacillus acidophilus_ NCFM [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/Ab-Initio-Whole-Cell-Kinetic-Model-of-Lactobacillus-acidophilus-NCFM-%28lacAS24%29)]
1. lfeTS24 (2025) on _Limosilactobacillus fermentum_ EFEL6800 [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/Ab-Initio-Whole-Cell-Kinetic-Model-of-Limosilactobacillus-fermentum-EFEL6800-%28lfeTS24%29)]
1. ebeTBSW25 (2025) on _Escherichia coli_ BL21 [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/Ab-Initio-Whole-Cell-Kinetic-Models-of-Escherichia-coli-BL21-%28ebeTBSW25%29-and-MG1655-%28ecoMAL25%29)]
1. ecoMAL25 (2025) on _Escherichia coli_ MG1655 [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/Ab-Initio-Whole-Cell-Kinetic-Models-of-Escherichia-coli-BL21-%28ebeTBSW25%29-and-MG1655-%28ecoMAL25%29)]
1. yliYKY24 (2025) on _Yarrowia lipolytica_ CLIB122 [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/Ab-Initio-Whole-Cell-Kinetic-Model-of-Yarrowia-lipolytica-CLIB122-%28yliYKY24%29)]
1. bshSM25 (2025) on _Bacillus subtilis_ 6051-HGW [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/Four-Ab-Initio-Whole-Cell-Kinetic-Models-of-Bacillus-subtilis-168-%28bsuLL25%29-6051-HGW-%28bshSM25%29%2C-N33-%28bsuN33SS25%29%2C-FUA2231-%28bsuGR25%29)]
1. bsuN33SS25 (2025) on _Bacillus subtilis_ N33 [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/Four-Ab-Initio-Whole-Cell-Kinetic-Models-of-Bacillus-subtilis-168-%28bsuLL25%29-6051-HGW-%28bshSM25%29%2C-N33-%28bsuN33SS25%29%2C-FUA2231-%28bsuGR25%29)]
1. bsuGR25 (2025) on _Bacillus subtilis_ FUA2231 [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/Four-Ab-Initio-Whole-Cell-Kinetic-Models-of-Bacillus-subtilis-168-%28bsuLL25%29-6051-HGW-%28bshSM25%29%2C-N33-%28bsuN33SS25%29%2C-FUA2231-%28bsuGR25%29)]
1. bsuLL25 (2025) on _Bacillus subtilis_ 168 [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/Four-Ab-Initio-Whole-Cell-Kinetic-Models-of-Bacillus-subtilis-168-%28bsuLL25%29-6051-HGW-%28bshSM25%29%2C-N33-%28bsuN33SS25%29%2C-FUA2231-%28bsuGR25%29)]
1. UniKin2 (2025) on Pan-Reactome [[publication](https://github.com/mauriceling/mauriceling.github.io/wiki/UniKin2-%E2%80%93-A-Universal%2C-Pan-Reactome-Kinetic-Model)]
1. ddsAAR26

### List of Whole Cell Kinetic Models Converted from Genome-Scale Models (GSMs)
As these Kinetic Models were converted from their respective GSMs using [Amir-Hamzah et al. (2022)](https://github.com/mauriceling/mauriceling.github.io/wiki/Kinetic-Models-with-Default-Enzyme-Kinetics-from-Genome-scale-Models), there are only model specification files (.modelspec) in the [asm](https://github.com/mauriceling/kinmodre/tree/main/asm) folder - there is no equivalent data package. However, the source GSMs are in [GSM](https://github.com/mauriceling/kinmodre/tree/main/GSM) folder. Hence, the model specification file and GSM will have the same name; for example, the iAF1260.xml [GSM](https://github.com/mauriceling/kinmodre/tree/main/GSM) folder is the source GSM that was converted into iAF1260.modelspec in [asm](https://github.com/mauriceling/kinmodre/tree/main/asm) folder.

More details on each model are listed in [List of GSM-Converted Kinetic Models]([List of GSM-Converted Kinetic Models.xlsx](https://github.com/mauriceling/kinmodre/blob/main/List%20of%20GSM-Converted%20Kinetic%20Models.xlsx) file.

1. e_coli_core [Source: BiGG]
1. iAF1260 [Source: BiGG]
1. Recon3D [Source: BiGG]

[BiGG] Norsigian et al. 2020. BiGG Models 2020: multi-strain genome-scale models and expansion across the phylogenetic tree. Nucleic Acids Research 48(D1):D402–D406. https://doi.org/10.1093/nar/gkz1054
