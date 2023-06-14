import subprocess
import pandas as pd
import codecarbon as cc

tracker = cc.OfflineEmissionsTracker(country_iso_code="GB")
rfilenames=pd.read_csv('RFilenames.csv')
c_calculator= "Code_Carbon"
col_names=['method_id','n_snps','n_rows','package','cost','run_time','carbon_calculator']
ResultsDF=pd.DataFrame(columns=col_names)
for fname,inputs in rfilenames:
    m_df = pd.read_csv(fname+'MethodDetails.csv')
    m_id = m_df.method_id 
    n_snps = m_df.n_snps
    n_r = m_df.n_rows
    pack = m_df.package
    with cc.OfflineEmissionsTracker() as tracker:
        subprocess.call (["/usr/bin/Rscript", inputs, fname])
        row_dict={'method_id':m_id,
                  'n_snps':n_snps,
                  'n_rows':n_r,
                  'package': pack,
                  'cost':tracker.power_usage, #FIXME
                  'run_time':tracker.run_time, #FIXME
                  'carbon_calculator':c_calculator}
        single_df=pd.DataFrame(row_dict)
        Results_df=pd.concat([single_df,Results_df])
