# CarbonCostCode

Repository for testing the carbon cost of codeing related to code used within the MRC-IEU. 
Repository: https://github.com/hw454/GreenAlgorithmsIEU 

# Requirements
## Packages Used

**Green Algorithms** The initial goal was to use the GreenAlgorithms package from https://www.green-algorithms.org/ to calculate the carbon cost from coding. 
However this has installation issues and does not allow for comparing domestic computers.
**Code Carbon** The code carbon package is much more straightforward to use however this is called within a python program. We have therefore written a 
script for calling an R script within python. https://github.com/mlco2/codecarbon  

## Programs to compare: 
\* Record – Number of SNPS/ Statistical Power vs Energy Usage and Carbon cost.  
\*2 different GWAS exposure – GWAS for BMI (Locke ver Yengo). Both two-sample univariable and multivariable analysis. 
\* Running MR with/without proxy look-up? Or using pre-clumped instruments from OpenGWAS versus clumping SNPs locally. 
\* Colocalisation with/without Susie finemapping 
\* Reading in data – packages/functions (data.table, tidyverse, etc), data formats, non-standard formats (comma separated, tab-separated, having to re-do, etc – carbon cost of a bad readme, also importance of reading in first few rows first versus entire file), transposing (R versus Python packages) 
\* Chunk size in pandas 

# Setup
 To calculate the cost of a single program populate a csv named: `method_id.csv`. The name for your csv should be added to the INSERT_FILENAME file. 
 If the method is already in the list match the `method_id` otherwise add a new row. 
 
#### Inside the setup csv populate:
\* method_id (should all be unique) 
\* n_snps (for MRs) 
\* n_rows (for reading data) 
\* n_chunk_size 
\* package (for reading data) 
\* carbon_calculator 

## Calculating your cost.
Using the offline version of the emission tracker from codecarbon track the power usage and run time. 

``
import panda as pd
carbon_dict={method_id:your_id,
              n_snps:your_nsnps,
              n_rows:your_n_rows,
              n_chunk_size: your_chunk
              package:your_package
              carbon_calculator:your_calculator
              cost:power_usage,
              run_time:your_time}
  res_df=pd.Dataframe(carbon_dict)
  res_df.to_csv(results_file_name)
  ``


 

 

 

 
